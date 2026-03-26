import fakeredis
from fastapi.testclient import TestClient

import web.app as web_app
from web.app import app


def test_chat_reaproveita_historico_da_sessao(mem, monkeypatch):
    captured_contexts = []

    def fake_process(message, context=None):
        captured_contexts.append(context or {})
        return f"eco:{message}"

    monkeypatch.setattr(web_app.orchestrator, "process", fake_process)
    monkeypatch.setattr(web_app.focus_guard, "start_guard", lambda: None)
    monkeypatch.setattr(web_app.focus_guard, "stop_guard", lambda: None)
    monkeypatch.setattr(web_app.focus_guard, "is_running", lambda: False)

    web_app.memory._redis_client = fakeredis.FakeRedis(decode_responses=True)

    with TestClient(app) as client:
        first = client.post("/chat", data={"message": "primeira pergunta"})
        second = client.post("/chat", data={"message": "segunda pergunta"})

    assert first.status_code == 200
    assert second.status_code == 200
    assert captured_contexts[0]["chat_history"] == []
    assert captured_contexts[1]["chat_history"] == [
        {"role": "user", "content": "primeira pergunta"},
        {"role": "assistant", "content": "eco:primeira pergunta"},
    ]


def test_audit_page_exibe_eventos_alertas_handoffs_e_logs(mem, monkeypatch, tmp_path):
    monkeypatch.setattr(web_app.focus_guard, "start_guard", lambda: None)
    monkeypatch.setattr(web_app.focus_guard, "stop_guard", lambda: None)
    monkeypatch.setattr(web_app.focus_guard, "is_running", lambda: False)

    log_file = tmp_path / "agent_system.log"
    log_file.write_text("linha 1\nlinha 2 do log\n", encoding="utf-8")
    monkeypatch.setattr(web_app, "LOG_FILE", str(log_file))

    fake = fakeredis.FakeRedis(decode_responses=True)
    web_app.memory._redis_client = fake
    web_app.memory.create_alert("deviation_moderate", "Atraso detectado")
    web_app.memory.create_audit_event(
        event_type="auto_reschedule",
        title="Bloco reagendado",
        details="09:00-10:00 → 11:00-12:00",
        agent="focus_guard",
    )
    web_app.memory.log_handoff("orchestrator", "scheduler", "get_today_schedule")

    with TestClient(app) as client:
        response = client.get("/audit")

    assert response.status_code == 200
    assert "Bloco reagendado" in response.text
    assert "Atraso detectado" in response.text
    assert "orchestrator → scheduler" in response.text
    assert "linha 2 do log" in response.text
