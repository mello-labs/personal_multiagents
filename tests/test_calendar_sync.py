import pytest
from datetime import datetime
from agents import calendar_sync

# =============================================================================
# Mocks e Utilitários de Teste
# =============================================================================


class MockEvents:
    def __init__(self, items=None, error=None):
        self.items = items or []
        self.error = error
        self.last_call_kwargs = {}

    def list(self, **kwargs):
        self.last_call_kwargs = kwargs
        return self

    def insert(self, **kwargs):
        self.last_call_kwargs = kwargs
        return self

    def execute(self):
        if self.error:
            raise self.error
        return {"items": self.items, "id": "new-event-id"}


class MockService:
    def __init__(self, items=None, error=None):
        self._events = MockEvents(items, error)

    def events(self):
        return self._events


@pytest.fixture
def mock_calendar_service(monkeypatch):
    """Fixture para mockar o serviço do Google Calendar."""

    def _setup_mock(items=None, error=None):
        service = MockService(items, error)
        monkeypatch.setattr(calendar_sync, "_get_service", lambda: service)
        return service

    return _setup_mock


# =============================================================================
# Testes de Normalização e Parsing
# =============================================================================


def test_normalize_date_range_swaps():
    """Testa se _normalize_date_range inverte se a data fim for anterior."""
    start, end = calendar_sync._normalize_date_range("2026-03-22", "2026-03-20")
    assert start.isoformat() == "2026-03-20"
    assert end.isoformat() == "2026-03-22"


def test_parse_event_time_fixed_time():
    """Testa o parsing de horário fixo (dateTime)."""
    event = {"dateTime": "2026-03-20T09:30:00Z"}
    assert calendar_sync._parse_event_time(event) == "09:30"


def test_parse_event_time_all_day():
    """Testa o parsing de evento de dia inteiro (date)."""
    event = {"date": "2026-03-20"}
    assert calendar_sync._parse_event_time(event) == "00:00"


# =============================================================================
# Testes de Importação (Google -> Notion/Memory)
# =============================================================================


def test_fetch_events_range_mapping(mock_calendar_service):
    """Testa se fetch_events_range mapeia corretamente os campos do Google."""
    items = [
        {
            "id": "abc-123",
            "summary": "Reunião de Alinhamento",
            "start": {"dateTime": "2026-05-10T10:00:00Z"},
            "end": {"dateTime": "2026-05-10T11:00:00Z"},
            "location": "Google Meet",
            "description": "Discussão sobre o projeto.",
        }
    ]
    mock_calendar_service(items)

    events = calendar_sync.fetch_events_range("2026-05-10", "2026-05-10")

    assert len(events) == 1
    ev = events[0]
    assert ev["google_event_id"] == "abc-123"
    assert ev["title"] == "Reunião de Alinhamento"
    assert ev["time_slot"] == "10:00-11:00"
    assert ev["location"] == "Google Meet"
    assert ev["all_day"] is False


def test_import_skips_duplicates_from_notion(mem, mock_calendar_service, monkeypatch):
    """
    Testa integração: Notion já tem um bloco, Google tem o mesmo + um novo.
    Deve importar apenas o novo do Google.
    """
    # 1. Simula bloco vindo do Notion (já em memória)
    mem.create_agenda_block(
        block_date="2026-05-10",
        time_slot="09:00-10:00",
        task_title="Foco Profundo (Notion)"
    )

    # 2. Mocka Google Calendar com um duplicado e um novo
    google_events = [
        # Duplicado (mesma data, hora e título ignorando o sufixo de origem se houver,
        # mas aqui usaremos títulos exatos para o teste de chave composite)
        {
            "id": "g1",
            "summary": "Foco Profundo (Notion)",
            "start": {"dateTime": "2026-05-10T09:00:00Z"},
            "end": {"dateTime": "2026-05-10T10:00:00Z"},
        },
        # Novo
        {
            "id": "g2",
            "summary": "Café com Time",
            "start": {"dateTime": "2026-05-10T11:00:00Z"},
            "end": {"dateTime": "2026-05-10T11:30:00Z"},
        }
    ]
    mock_calendar_service(google_events)

    # Mocka memory no agente (embora ele use core.memory globalmente,
    # no caso de teste unitário garantimos que aponta para o mem da fixture)
    monkeypatch.setattr(calendar_sync, "memory", mem)
    monkeypatch.setattr(calendar_sync.notifier, "info", lambda *a, **k: None)
    monkeypatch.setattr(calendar_sync.notifier, "success", lambda *a, **k: None)

    imported_count = calendar_sync.import_events_range_as_blocks("2026-05-10", "2026-05-10")

    assert imported_count == 1
    blocks = mem.get_agenda_for_date("2026-05-10")
    titles = {b["task_title"] for b in blocks}
    assert "Foco Profundo (Notion)" in titles
    assert "Café com Time" in titles


# =============================================================================
# Testes de Exportação (Notion/Memory -> Google)
# =============================================================================


def test_export_block_to_calendar_success(mock_calendar_service, monkeypatch):
    """Testa se a exportação de um bloco gera a chamada correta para o Google."""
    service = mock_calendar_service()
    monkeypatch.setattr(calendar_sync.notifier, "success", lambda *a, **k: None)

    event_id = calendar_sync.export_block_to_calendar(
        block_date="2026-05-10",
        time_slot="14:00-15:00",
        task_title="Reunião de Teste",
        description="Teste de exportação"
    )

    assert event_id == "new-event-id"
    last_call = service._events.last_call_kwargs
    body = last_call["body"]
    assert body["summary"] == "Reunião de Teste"
    assert "2026-05-10T14:00:00" in body["start"]["dateTime"]
    assert "2026-05-10T15:00:00" in body["end"]["dateTime"]


def test_export_block_invalid_timeslot(mock_calendar_service, monkeypatch):
    """Testa flag de erro para time_slot mal formado."""
    mock_calendar_service()  # Previne que tente carregar credenciais reais
    monkeypatch.setattr(calendar_sync.notifier, "warning", lambda *a, **k: None)

    event_id = calendar_sync.export_block_to_calendar(
        block_date="2026-05-10",
        time_slot="14:00",  # Sem hífen
        task_title="Erro"
    )
    assert event_id is None


# =============================================================================
# Testes de Resiliência
# =============================================================================


def test_fetch_events_handles_api_error(mock_calendar_service, monkeypatch):
    """Testa se o agente lida graciosamente com erros da API do Google."""
    mock_calendar_service(error=Exception("API Down"))
    monkeypatch.setattr(calendar_sync.notifier, "error", lambda *a, **k: None)

    events = calendar_sync.fetch_events_range("2026-03-20", "2026-03-20")
    assert events == []
