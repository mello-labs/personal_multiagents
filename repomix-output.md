This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose

This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format

The content is organized as follows:

1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines

- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes

- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure

```text
.devcontainer/
  devcontainer.json
.github/
  dependabot.yml
agents/
  __init__.py
  calendar_sync.py
  ecosystem_monitor.py
  focus_guard.py
  life_guard.py
  notion_sync.py
  orchestrator.py
  persona_manager.py
  retrospective.py
  scheduler.py
  validator.py
config/
  alert_thresholds.yml
  ecosystem.yml
core/
  __init__.py
  memory.py
  notifier.py
  openai_utils.py
  sanity_client.py
docs/
  arquitetura/
    SANITY_SCHEMA.md
    SCHEMA_SIGNAL_DECISION.md
  assets/
    multiagentes-banner.svg
  auditoria/
    AUDITORIA_AGENTES.md
  ecossistema/
    ECOSSISTEMA_NEO_PROTOCOL.md
    ECOSSISTEMAS_ORGS.md
    GUIAS_REFERENCIA.md
  governanca/
    CONTRATO_AGENTES.md
    MATRIZ_GOVERNANCA_AGENTES.md
    PLANO_SOBERANIA_SANITY.md
    POLITICA_PRECEDENCIA_NOTION.md
  operacao/
    MANUAL_DEV.md
    MANUAL_USUARIO.md
    redis-weekly-check.md
  planejamento/
    NEXTSTEPS.md
    SPRINT_ECOSSISTEMA.md
    SPRINT_VIDA.md
  GUIAS_REFERENCIA.json
  INDEX.md
  SISTEMA_REGISTRY.json
personas/
  architect.json
  coordinator.json
  taylor.json
sanity/
  schemaTypes/
    agenda_block.js
    agent_config.js
    area.js
    decision.js
    focus_session.js
    index.js
    intervention_script.js
    llm_prompt.js
    persona.js
    project.js
    public_artifact.js
    signal.js
    source.js
    task.js
  static/
    .gitkeep
  .gitignore
  eslint.config.mjs
  package.json
  README.md
  sanity.cli.js
  sanity.config.js
scripts/
  com.multiagentes.docker-maintenance.plist.template
  docker_maintenance.sh
  install_docker_maintenance_launchd.sh
  install_launchd.sh
web/
  static/
    favicon.ico
    icon-192.png
    icon-512.png
    manifest.json
    sw.js
  templates/
    partials/
      agenda.html
      block_row.html
      chat_message.html
      status.html
      task_row.html
      tasks.html
    agenda.html
    audit.html
    base.html
    chat_page.html
    ecosystem_page.html
    index.html
    tasks_page.html
  __init__.py
  app.py
.env.example
.gitignore
AGENTS.md
config.py
Dockerfile
favicon.ico
focus_guard_service.py
main.py
Makefile
Procfile
railway.json
README.md
requirements.txt
ROADMAP.md
```

# Files

## File: .devcontainer/devcontainer.json
````json
{
  "name": "Multiagentes · Dev",

  "build": {
    "context": "..",
    "dockerfile": "../Dockerfile"
  },

  "forwardPorts": [8000],
  "portsAttributes": {
    "8000": { "label": "Web UI", "onAutoForward": "openBrowser" }
  },

  "postCreateCommand": "pip install --no-cache-dir -r requirements.txt && mkdir -p logs reports",

  "remoteEnv": {
    "PYTHONPATH": "/workspaces/mypersonal_multiagents",
    "PYTHONUNBUFFERED": "1",
    "WEB_HOST": "0.0.0.0",
    "WEB_PORT": "8000",
    "PATH": "${containerEnv:PATH}"
  },

  "remoteUser": "appuser",
  "shutdownAction": "stopContainer",

  "customizations": {
    "vscode": {
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "python.terminal.activateEnvironment": false,
        "editor.formatOnSave": true
      },
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.debugpy",
        "eamodio.gitlens",
        "donjayamanne.githistory",
        "ms-azuretools.vscode-containers",
        "usernamehw.errorlens",
        "oderwat.indent-rainbow"
      ]
    }
  }
}
````

## File: .github/dependabot.yml
````yaml
# To get started with Dependabot version updates, you'll need to specify which
# package ecosystems to update and where the package manifests are located.
# Please see the documentation for more information:
# https://docs.github.com/github/administering-a-repository/configuration-options-for-dependency-updates
# https://containers.dev/guide/dependabot

version: 2
updates:
 - package-ecosystem: "devcontainers"
   directory: "/"
   schedule:
     interval: weekly
````

## File: agents/__init__.py
````python
# agents/__init__.py
# Pacote de agentes especialistas.
# Importações lazy para evitar circular imports — importe diretamente nos módulos:
#   from agents import notion_sync
#   from agents import scheduler
#   etc.

__all__ = [
    "calendar_sync",
    "focus_guard",
    "life_guard",
    "notion_sync",
    "orchestrator",
    "persona_manager",
    "retrospective",
    "scheduler",
    "validator",
]
````

## File: agents/calendar_sync.py
````python
# =============================================================================
# agents/calendar_sync.py — Agente de integração com Google Calendar
# =============================================================================
# Importa eventos do Google Calendar como blocos de agenda.
# Exporta blocos criados pelo Scheduler de volta ao calendário.
#
# Setup:
#   1. Crie um projeto no Google Cloud Console
#   2. Ative a Google Calendar API
#   3. Baixe credentials.json e coloque na raiz do projeto
#   4. Execute: python main.py calendar-auth
#      → Abre o browser para OAuth e salva token.json
#
# Variáveis de ambiente:
#   GOOGLE_CREDENTIALS_FILE  = caminho para credentials.json  (padrão: ./credentials.json)
#   GOOGLE_TOKEN_FILE        = caminho para token.json        (padrão: ./token.json)
#   GOOGLE_CALENDAR_ID       = ID do calendário               (padrão: primary)

import os
import sys
from datetime import date, datetime, timedelta
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import (
    GOOGLE_CALENDAR_ID,
    GOOGLE_CREDENTIALS_FILE,
    GOOGLE_TOKEN_FILE,
)
from core import memory, notifier

AGENT_NAME = "calendar_sync"

# Escopos necessários
SCOPES = ["https://www.googleapis.com/auth/calendar"]


# ---------------------------------------------------------------------------
# Autenticação OAuth
# ---------------------------------------------------------------------------


def _get_service():
    """
    Retorna o serviço autenticado da Google Calendar API.
    Requer google-api-python-client e google-auth-oauthlib instalados.
    """
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError:
        raise RuntimeError(
            "Instale as dependências: pip install google-api-python-client google-auth-oauthlib"
        )

    creds = None

    # Carrega token salvo
    if os.path.exists(GOOGLE_TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(GOOGLE_TOKEN_FILE, SCOPES)

    # Renova ou inicia fluxo OAuth
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(GOOGLE_CREDENTIALS_FILE):
                raise RuntimeError(
                    f"Arquivo de credenciais não encontrado: {GOOGLE_CREDENTIALS_FILE}\n"
                    "Baixe o credentials.json do Google Cloud Console."
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                GOOGLE_CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Salva token para próximas execuções com permissões restritas (600)
        fd = os.open(GOOGLE_TOKEN_FILE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w") as f:
            f.write(creds.to_json())

    return build("calendar", "v3", credentials=creds)


def authorize() -> bool:
    """Inicia o fluxo de autorização OAuth. Retorna True se bem-sucedido."""
    try:
        _get_service()
        notifier.success("Google Calendar autorizado com sucesso!", AGENT_NAME)
        return True
    except Exception as e:
        notifier.error(f"Erro na autorização: {e}", AGENT_NAME)
        return False


def is_authorized() -> bool:
    """Verifica se já existe um token válido."""
    return os.path.exists(GOOGLE_TOKEN_FILE)


# ---------------------------------------------------------------------------
# Leitura de eventos
# ---------------------------------------------------------------------------


def _parse_event_time(event_time: dict) -> Optional[str]:
    """Extrai string de horário de um evento (dateTime ou date)."""
    if "dateTime" in event_time:
        dt = datetime.fromisoformat(event_time["dateTime"])
        return dt.strftime("%H:%M")
    elif "date" in event_time:
        return "00:00"
    return None


def fetch_today_events() -> list[dict]:
    """
    Busca eventos do calendário de hoje.
    Retorna lista normalizada com time_slot, title, all_day, event_id.
    """
    today = date.today().isoformat()
    return fetch_events_range(today, today)


def fetch_events_range(start_date: str, end_date: str) -> list[dict]:
    """Busca eventos do Google Calendar em um intervalo de datas."""
    try:
        service = _get_service()
    except Exception as e:
        notifier.warning(
            f"Não foi possível conectar ao Google Calendar: {e}", AGENT_NAME
        )
        return []

    start_dt, end_dt = _normalize_date_range(start_date, end_date)
    time_min = datetime.combine(start_dt, datetime.min.time()).isoformat() + "Z"
    time_max = (
        datetime.combine(end_dt + timedelta(days=1), datetime.min.time()).isoformat()
        + "Z"
    )

    try:
        result = (
            service.events()
            .list(
                calendarId=GOOGLE_CALENDAR_ID,
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
    except Exception as e:
        notifier.error(f"Erro ao buscar eventos: {e}", AGENT_NAME)
        return []

    events = []
    for ev in result.get("items", []):
        start_raw = ev.get("start", {})
        start = _parse_event_time(ev.get("start", {}))
        end = _parse_event_time(ev.get("end", {}))
        time_slot = (
            f"{start}-{end}" if start and end and start != end else (start or "")
        )
        all_day = "dateTime" not in start_raw
        event_date = ""
        if "dateTime" in start_raw:
            event_date = datetime.fromisoformat(start_raw["dateTime"]).strftime(
                "%Y-%m-%d"
            )
        elif "date" in start_raw:
            event_date = start_raw["date"]

        events.append(
            {
                "google_event_id": ev["id"],
                "title": ev.get("summary", "Sem título"),
                "date": event_date,
                "time_slot": time_slot,
                "all_day": all_day,
                "location": ev.get("location", ""),
                "description": ev.get("description", ""),
            }
        )

    notifier.info(
        f"Google Calendar: {len(events)} evento(s) entre {start_dt.isoformat()} e {end_dt.isoformat()}.",
        AGENT_NAME,
    )
    return events


def fetch_week_events(days_ahead: int = 7) -> list[dict]:
    """Busca eventos dos próximos N dias."""
    start_date = datetime.now().date().isoformat()
    end_date = (datetime.now().date() + timedelta(days=days_ahead)).isoformat()
    return fetch_events_range(start_date, end_date)


def _normalize_date_range(start_date: str, end_date: str) -> tuple[date, date]:
    start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()
    if end_dt < start_dt:
        start_dt, end_dt = end_dt, start_dt
    return start_dt, end_dt


# ---------------------------------------------------------------------------
# Importar eventos como blocos de agenda
# ---------------------------------------------------------------------------


def import_today_as_blocks(skip_all_day: bool = True) -> int:
    """
    Importa eventos de hoje do Google Calendar como blocos de agenda local.
    Evita duplicatas verificando se já existe um bloco com o mesmo time_slot + título.
    Retorna número de blocos criados.
    """
    today = date.today().isoformat()
    return import_events_range_as_blocks(today, today, skip_all_day=skip_all_day)


def import_events_range_as_blocks(
    start_date: str,
    end_date: str,
    skip_all_day: bool = True,
) -> int:
    """Importa eventos do Google Calendar para blocos locais em um intervalo."""
    events = fetch_events_range(start_date, end_date)
    if not events:
        return 0

    existing_blocks = memory.list_agenda_between(
        start_date, end_date, include_rescheduled=True
    )
    existing_keys = {
        (b.get("block_date", ""), b.get("time_slot", ""), b.get("task_title", ""))
        for b in existing_blocks
    }

    created = 0
    for ev in events:
        if skip_all_day and ev.get("all_day"):
            continue

        key = (ev.get("date", ""), ev["time_slot"], ev["title"])
        if key in existing_keys:
            continue  # Já existe

        memory.create_agenda_block(
            block_date=ev.get("date") or start_date,
            time_slot=ev["time_slot"],
            task_title=ev["title"],
        )
        existing_keys.add(key)
        created += 1
        notifier.info(
            f"Bloco importado: {ev.get('date', '?')} {ev['time_slot']} — {ev['title']}",
            AGENT_NAME,
        )

    if created:
        notifier.success(
            f"{created} evento(s) do Google Calendar importados entre {start_date} e {end_date}.",
            AGENT_NAME,
        )
    else:
        notifier.info("Nenhum evento novo para importar.", AGENT_NAME)

    return created


# ---------------------------------------------------------------------------
# Exportar blocos para o Google Calendar
# ---------------------------------------------------------------------------


def export_block_to_calendar(
    block_date: str,
    time_slot: str,
    task_title: str,
    description: str = "",
) -> Optional[str]:
    """
    Cria um evento no Google Calendar para um bloco de agenda.
    Retorna o Google Event ID ou None em caso de erro.
    """
    try:
        service = _get_service()
    except Exception as e:
        notifier.warning(f"Não foi possível exportar para o Calendar: {e}", AGENT_NAME)
        return None

    # Parseia o time_slot (formato "HH:MM-HH:MM")
    if "-" not in time_slot:
        notifier.warning(f"Formato de time_slot inválido: {time_slot}", AGENT_NAME)
        return None

    start_str, end_str = time_slot.split("-", 1)
    start_dt = datetime.fromisoformat(f"{block_date}T{start_str.strip()}:00")
    end_dt = datetime.fromisoformat(f"{block_date}T{end_str.strip()}:00")

    # Ajuste de fuso (usa o fuso local via isoformat)
    try:
        import tzlocal  # type: ignore

        local_tz = tzlocal.get_localzone()
        start_dt = start_dt.replace(tzinfo=local_tz)
        end_dt = end_dt.replace(tzinfo=local_tz)
        tz_str = str(local_tz)
    except ImportError:
        tz_str = "America/Sao_Paulo"
        notifier.warning(
            "tzlocal não disponível — usando America/Sao_Paulo como fallback de timezone.",
            AGENT_NAME,
        )

    event_body = {
        "summary": task_title,
        "description": description or "Criado pelo Multiagentes",
        "start": {"dateTime": start_dt.isoformat(), "timeZone": tz_str},
        "end": {"dateTime": end_dt.isoformat(), "timeZone": tz_str},
    }

    try:
        created = (
            service.events()
            .insert(calendarId=GOOGLE_CALENDAR_ID, body=event_body)
            .execute()
        )
        event_id = created["id"]
        notifier.success(
            f"Evento criado no Calendar: '{task_title}' ({time_slot})", AGENT_NAME
        )
        return event_id
    except Exception as e:
        notifier.error(f"Erro ao criar evento: {e}", AGENT_NAME)
        return None


# ---------------------------------------------------------------------------
# Handoff entry point
# ---------------------------------------------------------------------------


def handle_handoff(payload: dict) -> dict:
    action = payload.get("action", "")
    notifier.agent_event(f"Recebendo handoff: action='{action}'", AGENT_NAME)
    handoff_id = memory.log_handoff("orchestrator", AGENT_NAME, action, payload)

    try:
        result: dict = {}

        if action == "import_today":
            skip_all_day = payload.get("skip_all_day", True)
            count = import_today_as_blocks(skip_all_day=skip_all_day)
            result = {"imported": count, "message": f"{count} evento(s) importados."}

        elif action == "fetch_today":
            events = fetch_today_events()
            result = {"events": events, "count": len(events)}

        elif action == "fetch_week":
            days = payload.get("days_ahead", 7)
            events = fetch_week_events(days_ahead=days)
            result = {"events": events, "count": len(events)}

        elif action == "fetch_range":
            events = fetch_events_range(payload["start_date"], payload["end_date"])
            result = {"events": events, "count": len(events)}

        elif action == "import_range":
            count = import_events_range_as_blocks(
                payload["start_date"],
                payload["end_date"],
                skip_all_day=payload.get("skip_all_day", True),
            )
            result = {"imported": count, "message": f"{count} evento(s) importado(s)."}

        elif action == "export_block":
            event_id = export_block_to_calendar(
                block_date=payload["block_date"],
                time_slot=payload["time_slot"],
                task_title=payload["task_title"],
                description=payload.get("description", ""),
            )
            result = {"event_id": event_id, "exported": event_id is not None}

        elif action == "status":
            result = {
                "authorized": is_authorized(),
                "calendar_id": GOOGLE_CALENDAR_ID,
                "credentials_file": GOOGLE_CREDENTIALS_FILE,
                "token_file": GOOGLE_TOKEN_FILE,
            }

        else:
            raise ValueError(f"Ação desconhecida: '{action}'")

        memory.update_handoff_result(handoff_id, result, "success")
        return {"status": "success", "result": result}

    except Exception as exc:
        error_msg = str(exc)
        notifier.error(f"Erro no handoff '{action}': {error_msg}", AGENT_NAME)
        memory.update_handoff_result(handoff_id, {"error": error_msg}, "error")
        return {"status": "error", "result": {"error": error_msg}}
````

## File: agents/ecosystem_monitor.py
````python
"""
agents/ecosystem_monitor.py — Fase 1: Órbita externa do kernel

Observa o ecossistema externo de NEØ MELLØ e produz sinais acionáveis:
  - GitHub: atividade por org, repos estagnados, issues abertas
  - Railway: health check de serviços via HTTP
  - On-chain: NEOFLW via DexScreener

Saídas:
  - health_check()   → dict com status de cada camada
  - daily_report()   → string formatada para leitura humana
  - run()            → executa tudo e persiste no Redis

Não faz:
  - alterar agenda íntima automaticamente
  - publicar nada diretamente
  - chamar focus_guard ou life_guard
"""

from __future__ import annotations

import os
import time
import json
import datetime
import requests
import redis
from typing import Any

from core import memory, notifier

AGENT_NAME = "ecosystem_monitor"

# ─── Configuração ────────────────────────────────────────────────────────────

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
RAILWAY_TOKEN = os.getenv("RAILWAY_TOKEN", "")
RAILWAY_WORKSPACE_ID = os.getenv("RAILWAY_WORKSPACE_ID", "")

GITHUB_ORGS = [
    "NEO-PROTOCOL",
    "NEO-FlowOFF",
    "flowpay-system",
    "neo-smart-factory",
    "FluxxDAO",
    "wodxpro",
]

# Repos prioritários para monitorar dentro de cada org
PRIORITY_REPOS = {
    "NEO-PROTOCOL": [
        "neobot",
        "neo-dashboard",
        "neo-mello-eth",
        "mio-system",
        "neoflw-base-landing",
    ],
    "NEO-FlowOFF": [
        "neo-control-plane",
        "neo-content-dashboard",
        "neo-content-accounts-api",
    ],
    "flowpay-system": ["flowpay-api", "flowpay-app"],
    "neo-smart-factory": ["smart-core", "smart-nft", "smart-cli"],
    "FluxxDAO": ["fluxx-backend", "fluxx-landing"],
    "wodxpro": ["wod-protocol", "wod-eth", "wod-x-pro"],
}

# Serviços Railway: nome → URL de health check
RAILWAY_SERVICES: dict[str, dict[str, str]] = {
    "neo-dashboard": {
        "url": "https://mypersonal-multiagents.up.railway.app/health",
        "priority": "P0",
    },
    "neo-mello-eth": {
        "url": "https://neomelloeth.up.railway.app/",
        "priority": "P0",
    },
    "neo-mello-eth-redis": {
        "url": "https://redis-neomello.up.railway.app/",
        "priority": "P0",
    },
    "mio-system": {
        "url": "https://mio-system-production.up.railway.app/health",
        "priority": "P1",
    },
    "neo-nexus": {
        "url": "https://neo-nexus-production.up.railway.app/health",
        "priority": "P1",
    },
    "neobot": {
        "url": "https://neobot-production.up.railway.app/health",
        "priority": "P0",
    },
}

# NEOFLW on Base
NEOFLW_CONTRACT = "0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B"
NEOFLW_CHAIN = "base"

# Thresholds
STALE_HOURS = 72  # repo sem push → sinalizar
ISSUE_WARN = 20  # issues abertas → warn
PRICE_DROP_PCT = 15  # queda de preço → alert
LIQUIDITY_MIN = 1000  # liquidez mínima USD
VOLUME_MIN = 500  # volume 24h mínimo USD

# Redis TTL
REDIS_TTL_SECONDS = 86400  # 24h


# ─── Helpers HTTP ──────────────────


def _get(
    url: str, headers: dict | None = None, timeout: int = 8
) -> dict | None:
    try:
        resp = requests.get(url, headers=headers or {}, timeout=timeout)
        if resp.ok:
            try:
                return resp.json()
            except ValueError:
                return {"_raw_status": resp.status_code, "_ok": True}
        return {"_error": resp.status_code}
    except requests.exceptions.RequestException as exc:
        return {"_exception": str(exc)}


def _github_headers() -> dict:
    h = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        h["Authorization"] = f"token {GITHUB_TOKEN}"
    return h


# ─── GitHub ──────────────────────────────────────────────────────────────────


def _hours_since(iso_str: str | None) -> float | None:
    if not iso_str:
        return None
    try:
        dt = datetime.datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        now = datetime.datetime.now(datetime.timezone.utc)
        return (now - dt).total_seconds() / 3600
    except (ValueError, TypeError):
        return None


def check_github() -> dict:
    """Verifica atividade GitHub em todas as orgs."""
    result: dict[str, Any] = {}
    headers = _github_headers()

    for org in GITHUB_ORGS:
        org_result: dict[str, Any] = {
            "status": "ok",
            "repos_active_24h": 0,
            "repos_stale": [],
            "open_issues": 0,
            "repos": {},
        }

        # Busca repos da org
        repos_data = _get(
            f"https://api.github.com/orgs/{org}/repos?per_page=30&sort=pushed",
            headers=headers,
        )

        if (
            not repos_data
            or "_error" in repos_data
            or "_exception" in repos_data
        ):
            org_result["status"] = "error"
            org_result["error"] = str(repos_data)
            result[org] = org_result
            continue

        if not isinstance(repos_data, list):
            org_result["status"] = "error"
            result[org] = org_result
            continue

        for repo in repos_data:
            name = repo.get("name", "")
            pushed = repo.get("pushed_at")
            issues = repo.get("open_issues_count", 0)
            hours = _hours_since(pushed)

            org_result["open_issues"] += issues

            repo_info = {
                "pushed_at": pushed,
                "hours_since_push": round(hours, 1) if hours is not None else None,
                "open_issues": issues,
                "stale": (hours is not None and hours > STALE_HOURS),
                "priority": name in PRIORITY_REPOS.get(org, []),
            }
            org_result["repos"][name] = repo_info

            if hours is not None and hours <= 24:
                org_result["repos_active_24h"] += 1

            if (
                hours is not None
                and hours > STALE_HOURS
                and name in PRIORITY_REPOS.get(org, [])
            ):
                org_result["repos_stale"].append(name)

        if org_result["repos_stale"]:
            org_result["status"] = "warn"
        if org_result["open_issues"] >= ISSUE_WARN:
            org_result["status"] = "warn"

        result[org] = org_result

    return result


# ─── Railway ─────────────────────────────────────────────────────────────────


def check_railway() -> dict:
    """Verifica saúde dos serviços Railway via HTTP health check."""
    result: dict[str, Any] = {}

    for service, cfg in RAILWAY_SERVICES.items():
        url = cfg["url"]
        priority = cfg.get("priority", "P2")
        start = time.time()

        try:
            resp = requests.get(url, timeout=8, allow_redirects=True)
            elapsed_ms = round((time.time() - start) * 1000)
            status_code = resp.status_code

            if status_code == 200:
                status = "ok"
                try:
                    body = resp.json()
                    svc_status = body.get("status", "ok")
                    if str(svc_status).lower() not in (
                        "ok",
                        "up",
                        "healthy",
                        "true",
                    ):
                        status = "warn"
                except ValueError:
                    pass
            elif status_code in (301, 302, 307, 308):
                status = "ok"  # redirect = vivo
            elif status_code == 404:
                status = "warn"  # existe mas endpoint não encontrado
            elif status_code >= 500:
                status = "fail"
            else:
                status = "warn"

            result[service] = {
                "status": status,
                "http_code": status_code,
                "response_ms": elapsed_ms,
                "priority": priority,
                "url": url,
            }

        except requests.exceptions.Timeout:
            result[service] = {
                "status": "fail",
                "error": "timeout",
                "priority": priority,
                "url": url,
            }
        except Exception as exc:
            result[service] = {
                "status": "fail",
                "error": str(exc),
                "priority": priority,
                "url": url,
            }

    return result


# ─── On-chain / DexScreener ───────────────────────────────────────────────────


def check_onchain() -> dict:
    """Verifica NEOFLW via DexScreener."""
    result: dict[str, Any] = {
        "NEOFLW": {
            "status": "unknown",
            "contract": NEOFLW_CONTRACT,
            "chain": NEOFLW_CHAIN,
        }
    }

    # Tenta endpoint de pairs por contrato
    data = _get(
        f"https://api.dexscreener.com/latest/dex/tokens/{NEOFLW_CONTRACT}",
        timeout=10,
    )

    pairs = None
    if data and isinstance(data.get("pairs"), list) and data["pairs"]:
        pairs = data["pairs"]
    else:
        # Tenta endpoint alternativo
        data2 = _get(
            f"https://api.dexscreener.com/token-pairs/v1/{NEOFLW_CHAIN}/{NEOFLW_CONTRACT}",
            timeout=10,
        )
        if data2 and isinstance(data2, list) and data2:
            pairs = data2

    if not pairs:
        result["NEOFLW"]["status"] = "no_data"
        result["NEOFLW"][
            "note"
        ] = "Token sem liquidez ativa ou não indexado no DexScreener"
        return result

    # Usa o par com maior liquidez
    pairs_sorted = sorted(
        pairs,
        key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0),
        reverse=True,
    )
    pair = pairs_sorted[0]

    price_usd = pair.get("priceUsd")
    liquidity_usd = pair.get("liquidity", {}).get("usd", 0) or 0
    volume_24h = pair.get("volume", {}).get("h24", 0) or 0
    price_change_24h = pair.get("priceChange", {}).get("h24", 0) or 0
    dex_id = pair.get("dexId", "")
    pair_address = pair.get("pairAddress", "")

    # Avaliar status
    status = "ok"
    alerts = []

    if float(liquidity_usd) < LIQUIDITY_MIN:
        status = "warn"
        alerts.append(f"liquidez baixa: ${liquidity_usd:.0f}")

    if float(volume_24h) < VOLUME_MIN:
        alerts.append(f"volume 24h baixo: ${volume_24h:.0f}")

    if float(price_change_24h) <= -PRICE_DROP_PCT:
        status = "fail"
        alerts.append(f"queda de preço 24h: {price_change_24h:.1f}%")

    result["NEOFLW"] = {
        "status": status,
        "price_usd": price_usd,
        "liquidity_usd": round(float(liquidity_usd), 2),
        "volume_24h_usd": round(float(volume_24h), 2),
        "price_change_24h_pct": round(float(price_change_24h), 2),
        "dex": dex_id,
        "pair_address": pair_address,
        "contract": NEOFLW_CONTRACT,
        "chain": NEOFLW_CHAIN,
        "alerts": alerts,
    }

    return result


# ─── Health Check ─────────────────────────────────────────────────────────────


def health_check() -> dict:
    """Executa health check completo do ecossistema."""
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    notifier.info("Iniciando health check do ecossistema...", AGENT_NAME)

    github = check_github()
    railway = check_railway()
    onchain = check_onchain()

    # Contagens de status
    gh_orgs_total = len(github)
    gh_orgs_warn = sum(1 for v in github.values() if v.get("status") != "ok")
    gh_repos_active = sum(v.get("repos_active_24h", 0) for v in github.values())
    gh_stale = [r for v in github.values() for r in v.get("repos_stale", [])]

    rw_total = len(railway)
    rw_ok = sum(1 for v in railway.values() if v.get("status") == "ok")
    rw_warn = sum(1 for v in railway.values() if v.get("status") == "warn")
    rw_fail = sum(1 for v in railway.values() if v.get("status") == "fail")

    # Status global
    global_status = "ok"
    if rw_fail > 0 or gh_orgs_warn > 0:
        global_status = "warn"
    if rw_fail >= 2:
        global_status = "fail"
    if any(
        railway.get(s, {}).get("status") == "fail"
        for s in ["neo-dashboard", "neo-mello-eth"]
    ):
        global_status = "fail"

    result = {
        "timestamp": now,
        "status": global_status,
        "summary": {
            "github": {
                "orgs_total": gh_orgs_total,
                "orgs_warn": gh_orgs_warn,
                "repos_active_24h": gh_repos_active,
                "repos_stale_priority": gh_stale,
            },
            "railway": {
                "services_total": rw_total,
                "services_ok": rw_ok,
                "services_warn": rw_warn,
                "services_fail": rw_fail,
            },
            "onchain": {
                "NEOFLW": onchain.get("NEOFLW", {}).get("status", "unknown"),
            },
        },
        "github": github,
        "railway": railway,
        "onchain": onchain,
    }

    # Persiste no Redis
    try:
        memory.set_state("ecosystem:health_check:latest", result)
        memory.set_state(f"ecosystem:health_check:{now[:10]}", result)
    except requests.exceptions.RequestException as exc:
        notifier.warning(
            f"Falha ao persistir health check no Redis: {exc}", AGENT_NAME
        )

    notifier.info(
        f"Health check concluído: {global_status.upper()} "
        f"| Railway {rw_ok}/{rw_total} ok "
        f"| GitHub {gh_repos_active} repos ativos 24h",
        AGENT_NAME,
    )

    return result


# ─── Daily Report ─────────────────────────────────────────────────────────────


def _status_icon(status: str) -> str:
    return {
        "ok": "OK  ",
        "warn": "WARN",
        "fail": "FAIL",
        "unknown": "???",
        "no_data": "----",
    }.get(status, "????")


def daily_report(data: dict | None = None) -> str:
    """Gera relatório diário legível. Usa dados do health_check se não fornecidos."""
    if data is None:
        # Tenta carregar do Redis
        try:
            r = memory.get_redis()
            raw = r.get("ecosystem:health_check:latest")
            if raw:
                data = json.loads(raw)
        except (redis.RedisError, json.JSONDecodeError):
            pass

    if data is None:
        data = health_check()

    today = data.get("timestamp", "")[:10]
    summary = data.get("summary", {})
    github = data.get("github", {})
    railway = data.get("railway", {})
    onchain = data.get("onchain", {})
    global_status = data.get("status", "?")

    lines: list[str] = []
    lines.append(f"NEØ Ecosystem — {today}")
    lines.append(f"{_status_icon(global_status)} Status global")
    lines.append("")

    # GitHub
    gh_s = summary.get("github", {})
    lines.append("GitHub")
    lines.append(f"  {gh_s.get('repos_active_24h', 0)} repos ativos (24h)")
    stale = gh_s.get("repos_stale_priority", [])
    if stale:
        lines.append(f"  WARN repos prioritários estagnados: {', '.join(stale)}")
    # Por org
    for org, info in github.items():
        active = info.get("repos_active_24h", 0)
        issues = info.get("open_issues", 0)
        status = info.get("status", "ok")
        icon = _status_icon(status)
        lines.append(f"  {icon} {org}: {active} ativos / {issues} issues abertas")

    lines.append("")

    # Railway
    rw_s = summary.get("railway", {})
    lines.append("Infra (Railway)")
    lines.append(
        f"  {rw_s.get('services_ok', 0)}/{rw_s.get('services_total', 0)} serviços ok"
    )
    for svc, info in railway.items():
        status = info.get("status", "?")
        icon = _status_icon(status)
        code = info.get("http_code", info.get("error", "?"))
        ms = info.get("response_ms", "")
        ms_str = f" ({ms}ms)" if ms else ""
        prio = info.get("priority", "")
        lines.append(f"  {icon} {svc} [{prio}]: {code}{ms_str}")

    lines.append("")

    # On-chain
    neoflw = onchain.get("NEOFLW", {})
    neoflw_status = neoflw.get("status", "unknown")
    lines.append("On-chain")
    if neoflw_status == "no_data":
        lines.append("  ---- NEOFLW: sem dados no Coingecko")
    else:
        price = neoflw.get("price_usd", "?")
        vol = neoflw.get("volume_24h_usd", "?")
        liq = neoflw.get("liquidity_usd", "?")
        chg = neoflw.get("price_change_24h_pct", "?")
        icon = _status_icon(neoflw_status)
        lines.append(
            f"  {icon} NEOFLW: ${price} | vol: ${vol} | liq: ${liq} | Δ: {chg}%"
        )
        for alert in neoflw.get("alerts", []):
            lines.append(f"       ⚠ {alert}")

    lines.append("")

    # Ações sugeridas
    actions: list[str] = []

    fail_svcs = [s for s, v in railway.items() if v.get("status") == "fail"]
    warn_svcs = [s for s, v in railway.items() if v.get("status") == "warn"]
    if fail_svcs:
        msg = f"verificar serviço(s) com falha: {', '.join(fail_svcs)}"
        actions.append(msg)
    if warn_svcs:
        actions.append(f"investigar: {', '.join(warn_svcs)}")
    if stale:
        actions.append(f"revisar repos estagnados: {', '.join(stale)}")
    if neoflw.get("alerts"):
        actions.append("monitorar NEOFLW — alertas ativos")

    if actions:
        lines.append("Ação sugerida")
        for a in actions:
            lines.append(f"  - {a}")
    else:
        lines.append("Sem ações urgentes.")

    report = "\n".join(lines)

    # Persiste relatório no Redis
    try:
        memory.set_state("ecosystem:daily_report:latest", report)
        memory.set_state(f"ecosystem:daily_report:{today}", report)
    except Exception as exc:
        notifier.warning(
            f"Falha ao persistir relatório no Redis: {exc}", AGENT_NAME
        )

    return report


# ─── Entry point ───────────────────────


def run() -> str:
    """Executa health check completo e devolve relatório."""
    data = health_check()
    report = daily_report(data)

    # Alerta imediato apenas para eventos graves
    rw = data.get("railway", {})
    p0_fail = [
        s
        for s, v in rw.items()
        if v.get("status") == "fail" and v.get("priority") == "P0"
    ]
    if p0_fail:
        msg = f"[ECOSYSTEM] Serviço P0 com falha: {', '.join(p0_fail)}"
        notifier.mac_push("NEO Ecosystem FAIL", msg, sound=True)

    return report
````

## File: agents/focus_guard.py
````python
# =============================================================================
# agents/focus_guard.py — Agente guardião do foco
# =============================================================================
# Roda em background thread e periodicamente:
#   1. Verifica se há uma sessão de foco ativa
#   2. Compara o que foi planejado vs. o que foi feito
#   3. Emite alertas/cobranças no terminal
#   4. Registra desvios no banco de dados
#
# O loop principal usa a lib `schedule` para disparos periódicos.
# A thread roda como daemon e é parada por um Event.

import json
import os
import sys
import threading
import time
from datetime import date, datetime
from typing import Optional

import schedule

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import notion_sync as _notion_sync
from agents import scheduler as _scheduler
from config import (
    FOCUS_CHECK_INTERVAL_MINUTES,
    NOTION_SYNC_INTERVAL_MINUTES,
)
from core import memory, notifier, sanity_client
from core.openai_utils import chat_completions

AGENT_NAME = "focus_guard"

# Níveis de escalada por tempo de sessão
ESCALATION_LEVELS = [
    {
        "minutes": 30,
        "channel": "mac",
        "sound": False,
        "msg": "30 min em {task}. Planejado: {planned}min.",
    },
    {
        "minutes": 60,
        "channel": "mac",
        "sound": True,
        "msg": "1 hora em {task}. Hora de checar.",
    },
    {
        "minutes": 120,
        "channel": "mac+alexa",
        "sound": True,
        "msg": "2 horas em {task}. Para agora.",
    },
    {
        "minutes": 240,
        "channel": "mac+alexa",
        "sound": True,
        "msg": "4 horas. Sai do computador por 10 minutos.",
    },
]

# Estado interno do Focus Guard
_state_key = "focus_guard_state"
_stop_event = threading.Event()
_guard_thread: Optional[threading.Thread] = None


# Prompt para análise de desvio via LLM
_DEVIATION_PROMPT_FALLBACK = """Você é o Focus Guard, um agente que monitora o progresso de tarefas pessoais.
Analise os dados fornecidos e determine:
1. Se o usuário está dentro do plano (on-track) ou desviou
2. Se houve desvio, qual a gravidade (leve/moderado/grave)
3. Uma mensagem de cobrança/encorajamento adequada (seja direto, mas empático)

Retorne JSON com:
{
  "on_track": true/false,
  "deviation_level": "none" | "light" | "moderate" | "severe",
  "message": "sua mensagem aqui",
  "recommendation": "ação recomendada"
}
"""


def _get_deviation_prompt() -> str:
    return sanity_client.get_prompt(
        "focus_guard", "deviation", _DEVIATION_PROMPT_FALLBACK
    )


def _get_runtime_environment() -> str:
    return "local" if sys.platform == "darwin" else "server"


def _get_intervention_levels() -> list[dict]:
    scripts = sanity_client.get_intervention_scripts(AGENT_NAME)
    current_env = _get_runtime_environment()
    levels = []
    for script in scripts:
        scope = script.get("environment_scope", "all")
        if scope not in {"all", current_env}:
            continue
        levels.append(
            {
                "minutes": script.get("trigger_minutes"),
                "channel": script.get("channel", "log_only"),
                "sound": script.get("sound", False),
                "msg": script.get("message", ""),
                "title": script.get("title", "NEO Focus Guard"),
            }
        )

    levels = [level for level in levels if isinstance(level.get("minutes"), int)]
    return levels or ESCALATION_LEVELS


# ---------------------------------------------------------------------------
# Análise de progresso
# ---------------------------------------------------------------------------


def analyze_progress() -> dict:
    """
    Compara agenda planejada vs. realidade atual.
    Retorna análise estruturada do progresso.
    """
    today_blocks = memory.get_today_agenda()
    active_session = memory.get_active_focus_session()
    now = datetime.now()
    current_time_str = now.strftime("%H:%M")

    # Blocos que já deveriam ter passado (time_slot de início ≤ agora)
    overdue_blocks = []
    current_block = None
    upcoming_blocks = []

    for block in today_blocks:
        slot = block.get("time_slot", "")
        if "-" in slot:
            try:
                start_str = slot.split("-")[0].strip()
                end_str = slot.split("-")[1].strip()
                start_t = datetime.strptime(
                    f"{date.today()} {start_str}", "%Y-%m-%d %H:%M"
                )
                end_t = datetime.strptime(f"{date.today()} {end_str}", "%Y-%m-%d %H:%M")

                if end_t < now and not block.get("completed"):
                    overdue_blocks.append(block)
                elif start_t <= now <= end_t:
                    current_block = block
                elif start_t > now:
                    upcoming_blocks.append(block)
            except ValueError:
                pass

    load = {
        "total": len(today_blocks),
        "completed": sum(1 for b in today_blocks if b.get("completed")),
        "overdue": len(overdue_blocks),
        "current": current_block,
        "upcoming": len(upcoming_blocks),
    }

    # Calcula on-track básico (sem LLM)
    on_track = len(overdue_blocks) == 0

    return {
        "timestamp": now.isoformat(),
        "current_time": current_time_str,
        "on_track": on_track,
        "load": load,
        "overdue_blocks": overdue_blocks,
        "current_block": current_block,
        "upcoming_blocks_count": len(upcoming_blocks),
        "active_focus_session": active_session,
    }


def analyze_with_llm(progress: dict) -> dict:
    """
    Usa o GPT-4o-mini para gerar análise e mensagem personalizada de cobrança.
    Retorna dict com on_track, deviation_level, message, recommendation.
    """
    progress_str = json.dumps(progress, ensure_ascii=False, indent=2, default=str)

    try:
        response = chat_completions(
            messages=[
                {"role": "system", "content": _get_deviation_prompt()},
                {"role": "user", "content": f"Dados de progresso:\n{progress_str}"},
            ],
            temperature=0.6,
            response_format={"type": "json_object"},
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        notifier.error(f"Erro na análise LLM: {e}", AGENT_NAME)
        # Fallback: análise básica sem LLM
        if progress.get("on_track"):
            return {
                "on_track": True,
                "deviation_level": "none",
                "message": "Você está no caminho certo! Continue focado.",
                "recommendation": "Mantenha o ritmo atual.",
            }
        else:
            overdue = progress.get("load", {}).get("overdue", 0)
            return {
                "on_track": False,
                "deviation_level": "moderate" if overdue <= 2 else "severe",
                "message": f"Atenção! {overdue} bloco(s) da agenda não foram concluídos. Hora de volcar o foco!",
                "recommendation": "Revise a agenda e retome a próxima tarefa pendente.",
            }


# ---------------------------------------------------------------------------
# Escalada por tempo de sessão
# ---------------------------------------------------------------------------


def _check_escalation(
    session_minutes: int, task_title: str, planned_minutes: int
) -> None:
    """Dispara notificação no canal certo baseado no tempo de sessão."""
    today = datetime.now().date()
    for level in _get_intervention_levels():
        state_key = f"escalation:{today}:{task_title}:{level['minutes']}"
        if memory.get_state(state_key):
            continue
        if session_minutes >= level["minutes"]:
            msg = level["msg"].format(task=task_title, planned=planned_minutes)
            if "mac" in level["channel"]:
                notifier.mac_push(
                    level.get("title", "NEO Focus Guard"), msg, sound=level["sound"]
                )
            if "alexa" in level["channel"]:
                notifier.alexa_announce(msg)
            memory.set_state(state_key, "sent")
            break  # só um nível por check


# ---------------------------------------------------------------------------
# Loop de verificação periódica
# ---------------------------------------------------------------------------


def _auto_reschedule_overdue_blocks(progress: dict) -> list[dict]:
    actions = []
    overdue_blocks = progress.get("overdue_blocks", [])
    if not overdue_blocks:
        return actions

    for block in overdue_blocks:
        result = _scheduler.auto_reschedule_block(
            block_id=block["id"],
            reason="Bloco vencido detectado no check periódico do Focus Guard.",
        )
        status = result.get("status")
        if status not in {"created", "linked"}:
            continue

        details = f"{block.get('time_slot')} → {result.get('new_block_date')} {result.get('new_time_slot')}"
        if status == "linked":
            details = (
                f"{block.get('time_slot')} → bloco existente #{result.get('rescheduled_to_block_id')} "
                f"em {result.get('new_block_date')} {result.get('new_time_slot')}"
            )

        memory.create_audit_event(
            event_type="auto_reschedule",
            title=f"Bloco reagendado: {block.get('task_title', 'Sem título')}",
            details=details,
            level="warning",
            agent=AGENT_NAME,
            payload=result,
            related_id=str(block["id"]),
        )
        actions.append(result)

    return actions


def _run_focus_check(
    progress: Optional[dict] = None,
    analysis: Optional[dict] = None,
) -> dict:
    """Executado pelo scheduler a cada intervalo configurado.

    Aceita `progress` e `analysis` pré-computados para evitar chamadas LLM
    duplicadas quando invocado a partir de `force_check`.
    Retorna dict com progress e analysis para uso pelo chamador.
    """
    notifier.focus_alert("═══ CHECK-IN DO FOCUS GUARD ═══", AGENT_NAME)

    if progress is None:
        progress = analyze_progress()
    if analysis is None:
        analysis = analyze_with_llm(progress)
    rescheduled_actions = _auto_reschedule_overdue_blocks(progress)

    # Salva estado atual
    memory.set_state(
        _state_key,
        {
            "last_check": datetime.now().isoformat(),
            "on_track": analysis.get("on_track", True),
            "deviation_level": analysis.get("deviation_level", "none"),
        },
    )
    memory.create_audit_event(
        event_type="focus_check",
        title="Check periódico do Focus Guard",
        details=(
            f"on_track={analysis.get('on_track', True)} | "
            f"desvio={analysis.get('deviation_level', 'none')} | "
            f"atrasados={progress.get('load', {}).get('overdue', 0)} | "
            f"reagendados={len(rescheduled_actions)}"
        ),
        level="warning" if not analysis.get("on_track", True) else "info",
        agent=AGENT_NAME,
        payload={
            "progress": progress,
            "analysis": analysis,
            "rescheduled_actions": rescheduled_actions,
        },
    )

    # Exibe resumo
    load = progress.get("load", {})
    notifier.info(
        f"Agenda hoje: {load.get('completed', 0)}/{load.get('total', 0)} blocos concluídos "
        f"| {load.get('overdue', 0)} atrasado(s)",
        AGENT_NAME,
    )

    # Sessão de foco ativa
    active = progress.get("active_focus_session")
    if active:
        started = active.get("started_at", "")
        notifier.info(
            f"Sessão ativa: '{active.get('task_title')}' desde {started[:16]}",
            AGENT_NAME,
        )
        try:
            started_dt = datetime.fromisoformat(started)
            session_minutes = int((datetime.now() - started_dt).total_seconds() / 60)
            _check_escalation(
                session_minutes=session_minutes,
                task_title=active.get("task_title", "?"),
                planned_minutes=active.get("planned_minutes", 25),
            )
        except Exception:
            pass

    # Mensagem de análise
    deviation = analysis.get("deviation_level", "none")
    message = analysis.get("message", "")
    recommendation = analysis.get("recommendation", "")

    if deviation == "none":
        notifier.success(f"✅ {message}", AGENT_NAME)
    elif deviation == "light":
        notifier.warning(f"⚡ {message}", AGENT_NAME)
    elif deviation == "moderate":
        notifier.warning(f"🚨 {message}", AGENT_NAME)
        if recommendation:
            notifier.warning(f"   → {recommendation}", AGENT_NAME)
    else:  # severe
        notifier.error(f"🔥 {message}", AGENT_NAME)
        if recommendation:
            notifier.error(f"   → {recommendation}", AGENT_NAME)

    # Registra alerta no banco se houver desvio
    if not analysis.get("on_track", True):
        alert_type = f"deviation_{deviation}"
        full_msg = message
        if recommendation:
            full_msg += f" | Recomendação: {recommendation}"
        alert_id = memory.create_alert(alert_type, full_msg)
        memory.create_audit_event(
            event_type="alert_created",
            title=f"Alerta gerado: {alert_type}",
            details=full_msg,
            level="warning" if deviation != "severe" else "error",
            agent=AGENT_NAME,
            related_id=str(alert_id),
        )

    # Blocos atrasados
    overdue = progress.get("overdue_blocks", [])
    if overdue:
        notifier.warning("Blocos atrasados:", AGENT_NAME)
        for b in overdue:
            notifier.warning(
                f"  • {b.get('time_slot', '?')} — {b.get('task_title', '?')}",
                AGENT_NAME,
            )

    if rescheduled_actions:
        notifier.warning("Reagendamentos automáticos:", AGENT_NAME)
        for action in rescheduled_actions:
            notifier.warning(
                f"  • bloco {action.get('original_block_id')} → "
                f"{action.get('new_block_date')} {action.get('new_time_slot')}",
                AGENT_NAME,
            )

    # Life Guard — rotinas pessoais
    try:
        from agents import life_guard as _life_guard

        _life_guard.run_all_checks()
    except Exception as e:
        notifier.warning(f"Life Guard check ignorado: {e}", AGENT_NAME)

    notifier.separator()
    return {"progress": progress, "analysis": analysis}


def _run_differential_sync() -> None:
    """Callback do scheduler para sync diferencial periódico."""
    try:
        count = _notion_sync.sync_differential()
        if count:
            notifier.info(f"Auto-sync: {count} tarefa(s) sincronizada(s).", AGENT_NAME)
    except Exception as e:
        notifier.warning(f"Erro no auto-sync diferencial: {e}", AGENT_NAME)


def _background_loop() -> None:
    """Thread principal do Focus Guard — roda o scheduler.run_pending() em loop."""
    # Lê configuração do Sanity; cai nos valores de env/config.py se indisponível
    cfg = sanity_client.get_agent_config(AGENT_NAME) or {}
    if not cfg.get("enabled", True):
        notifier.warning(
            "Focus Guard desabilitado via Sanity (agent_config.enabled=false). Encerrando loop.",
            AGENT_NAME,
        )
        return
    interval = int(cfg.get("check_interval_minutes") or FOCUS_CHECK_INTERVAL_MINUTES)
    if interval != FOCUS_CHECK_INTERVAL_MINUTES:
        notifier.info(
            f"Intervalo de check lido do Sanity: {interval} min (env={FOCUS_CHECK_INTERVAL_MINUTES}).",
            AGENT_NAME,
        )

    # Configura o job periódico de check de foco
    schedule.every(interval).minutes.do(_run_focus_check)

    # Configura sync diferencial periódico
    schedule.every(NOTION_SYNC_INTERVAL_MINUTES).minutes.do(_run_differential_sync)

    # Executa uma verificação imediata ao iniciar (protegida contra falha de Redis)
    try:
        _run_focus_check()
    except Exception as e:
        notifier.warning(
            f"Check inicial ignorado (Redis indisponível?): {e}", AGENT_NAME
        )

    while not _stop_event.is_set():
        try:
            schedule.run_pending()
        except Exception as e:
            notifier.warning(f"Erro no scheduler (ignorado): {e}", AGENT_NAME)
        time.sleep(30)  # Polling a cada 30 segundos

    notifier.info("Focus Guard encerrado.", AGENT_NAME)


# ---------------------------------------------------------------------------
# API pública — start/stop da thread de background
# ---------------------------------------------------------------------------


def start_guard() -> None:
    """Inicia o Focus Guard em background thread (daemon)."""
    global _guard_thread
    if _guard_thread and _guard_thread.is_alive():
        notifier.warning("Focus Guard já está rodando.", AGENT_NAME)
        return

    _stop_event.clear()
    _guard_thread = threading.Thread(
        target=_background_loop,
        name="FocusGuardThread",
        daemon=True,
    )
    _guard_thread.start()
    notifier.success(
        f"Focus Guard em background (check a cada {FOCUS_CHECK_INTERVAL_MINUTES} min).",
        AGENT_NAME,
    )


def stop_guard() -> None:
    """Para o Focus Guard."""
    _stop_event.set()
    schedule.clear()
    notifier.info("Focus Guard parado.", AGENT_NAME)


def is_running() -> bool:
    """Verifica se o Focus Guard está ativo."""
    return _guard_thread is not None and _guard_thread.is_alive()


def force_check() -> dict:
    """Força uma verificação imediata (chamável pelo Orchestrator).

    Computa progress e analysis uma única vez e repassa para _run_focus_check,
    evitando chamadas LLM duplicadas.
    """
    notifier.agent_event("Verificação forçada pelo Orchestrator.", AGENT_NAME)
    progress = analyze_progress()
    analysis = analyze_with_llm(progress)
    return _run_focus_check(progress=progress, analysis=analysis)


# ---------------------------------------------------------------------------
# Gestão de sessões de foco (Pomodoro-style)
# ---------------------------------------------------------------------------


def start_focus_session(task_id: int, task_title: str, minutes: int = 25) -> dict:
    """Inicia uma sessão de foco rastreada."""
    # Encerra sessão anterior se existir
    active = memory.get_active_focus_session()
    if active:
        memory.end_focus_session(active["id"], status="abandoned")
        notifier.warning(
            f"Sessão anterior '{active['task_title']}' encerrada (abandonada).",
            AGENT_NAME,
        )

    session_id = memory.start_focus_session(task_id, task_title, minutes)
    notifier.focus_alert(
        f"🎯 Sessão de foco iniciada: '{task_title}' ({minutes} minutos)", AGENT_NAME
    )
    memory.set_state("current_focus_task", {"task_id": task_id, "title": task_title})

    return {
        "session_id": session_id,
        "task_title": task_title,
        "planned_minutes": minutes,
    }


def end_focus_session(status: str = "completed", notes: str = "") -> dict:
    """Encerra a sessão de foco ativa."""
    active = memory.get_active_focus_session()
    if not active:
        notifier.warning("Nenhuma sessão de foco ativa.", AGENT_NAME)
        return {"message": "Nenhuma sessão ativa."}

    memory.end_focus_session(active["id"], status, notes or None)
    memory.set_state("current_focus_task", None)

    emoji = "✅" if status == "completed" else "⚠️"
    notifier.success(
        f"{emoji} Sessão encerrada: '{active['task_title']}' ({status})", AGENT_NAME
    )
    return {
        "session_id": active["id"],
        "status": status,
        "task_title": active["task_title"],
    }


# ---------------------------------------------------------------------------
# Handoff entry point — chamado pelo Orchestrator
# ---------------------------------------------------------------------------


def handle_handoff(payload: dict) -> dict:
    """
    Ponto de entrada para handoffs do Orchestrator.
    """
    action = payload.get("action", "")
    notifier.agent_event(f"Recebendo handoff: action='{action}'", AGENT_NAME)

    handoff_id = memory.log_handoff("orchestrator", AGENT_NAME, action, payload)

    try:
        result: dict = {}

        if action == "start_guard":
            start_guard()
            result = {"message": "Focus Guard iniciado.", "running": True}

        elif action == "stop_guard":
            stop_guard()
            result = {"message": "Focus Guard parado.", "running": False}

        elif action == "force_check":
            check = force_check()
            result = check

        elif action == "start_session":
            session = start_focus_session(
                task_id=payload["task_id"],
                task_title=payload["task_title"],
                minutes=payload.get("minutes", 25),
            )
            result = session

        elif action == "end_session":
            session = end_focus_session(
                status=payload.get("status", "completed"),
                notes=payload.get("notes", ""),
            )
            result = session

        elif action == "status":
            state = memory.get_state(_state_key, {})
            active = memory.get_active_focus_session()
            result = {
                "running": is_running(),
                "last_check": state.get("last_check"),
                "on_track": state.get("on_track", True),
                "deviation_level": state.get("deviation_level", "none"),
                "active_session": active,
            }

        elif action == "get_alerts":
            alerts = memory.get_pending_alerts()
            result = {"alerts": alerts, "count": len(alerts)}

        else:
            raise ValueError(f"Ação desconhecida: '{action}'")

        memory.update_handoff_result(handoff_id, result, "success")
        return {"status": "success", "result": result}

    except Exception as exc:
        error_msg = str(exc)
        notifier.error(f"Erro no handoff '{action}': {error_msg}", AGENT_NAME)
        memory.update_handoff_result(handoff_id, {"error": error_msg}, "error")
        return {"status": "error", "result": {"error": error_msg}}
````

## File: agents/life_guard.py
````python
"""
agents/life_guard.py — Guardião de rotinas pessoais

Monitora e notifica sobre:
- Hidratação (a cada 90 min durante horário ativo)
- Exercício físico (check diário às 7h)
- Higiene (check às 10h)
- Refeições (almoço 12h30, jantar 19h30)
- Finanças (alertas de vencimento próximo)

Não julga. Apenas registra e lembra.
"""

import json
import os
import sys
from datetime import date, datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import memory, notifier, sanity_client

AGENT_NAME = "life_guard"

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

DAILY_ROUTINES = [
    {
        "id": "exercise",
        "name": "Exercício",
        "check_at": "07:00",
        "message": "Você se exercitou hoje?",
        "channel": "mac",
        "sound": False,
    },
    {
        "id": "shower",
        "name": "Banho",
        "check_at": "10:00",
        "message": "Hora do banho.",
        "channel": "mac",
        "sound": False,
    },
    {
        "id": "lunch",
        "name": "Almoco",
        "check_at": "12:30",
        "message": "Parar para almocar.",
        "channel": "mac+alexa",
        "sound": False,
    },
    {
        "id": "dinner",
        "name": "Jantar",
        "check_at": "19:30",
        "message": "Parar para jantar.",
        "channel": "mac",
        "sound": False,
    },
]

WATER_INTERVAL_MINUTES = int(os.getenv("LIFE_GUARD_WATER_INTERVAL", "90"))
ACTIVE_HOUR_START = int(os.getenv("LIFE_GUARD_ACTIVE_HOUR_START", "8"))
ACTIVE_HOUR_END = int(os.getenv("LIFE_GUARD_ACTIVE_HOUR_END", "22"))


# ---------------------------------------------------------------------------
# Despacho de notificações
# ---------------------------------------------------------------------------


def _dispatch(message: str, channel: str, sound: bool) -> None:
    if "mac" in channel:
        notifier.mac_push("NEO Life Guard", message, sound=sound)
    if "alexa" in channel:
        notifier.alexa_announce(message)
    notifier.info(f"[life_guard] {message}", AGENT_NAME)


# ---------------------------------------------------------------------------
# Rotinas diárias
# ---------------------------------------------------------------------------


def check_daily_routines() -> list:
    """Verifica rotinas diárias e dispara lembretes."""
    now = datetime.now()
    today = date.today().isoformat()
    triggered = []

    for routine in DAILY_ROUTINES:
        state_key = f"life_guard:{today}:{routine['id']}"
        if memory.get_state(state_key):
            continue  # já enviado hoje

        h, m = map(int, routine["check_at"].split(":"))
        scheduled_dt = now.replace(hour=h, minute=m, second=0, microsecond=0)

        # janela de 30 minutos após o horário programado
        if scheduled_dt <= now <= scheduled_dt + timedelta(minutes=30):
            _dispatch(
                routine["message"], routine["channel"], routine.get("sound", False)
            )
            memory.set_state(state_key, "sent")
            triggered.append(routine["id"])

    return triggered


# ---------------------------------------------------------------------------
# Hidratação
# ---------------------------------------------------------------------------


def check_hydration() -> bool:
    """Lembra de beber água a cada 90 minutos no horário ativo."""
    now = datetime.now()
    if not (ACTIVE_HOUR_START <= now.hour < ACTIVE_HOUR_END):
        return False

    state_key = "life_guard:water:last_sent"
    last_sent_iso = memory.get_state(state_key)

    if last_sent_iso:
        try:
            last_sent = datetime.fromisoformat(last_sent_iso)
            if (now - last_sent).total_seconds() < WATER_INTERVAL_MINUTES * 60:
                return False
        except Exception:
            pass

    _dispatch("Beber agua.", "mac", sound=False)
    memory.set_state(state_key, now.isoformat())
    return True


# ---------------------------------------------------------------------------
# Finanças
# ---------------------------------------------------------------------------


def check_finances() -> list:
    """
    Verifica pagamentos próximos do vencimento.
    Formato esperado em life_guard:finances (JSON):
    [{"name": "Cartao XP", "due_day": 15, "amount": 1200.00}]
    """
    today = date.today()
    finances_raw = memory.get_state("life_guard:finances")
    if not finances_raw:
        return []

    try:
        finances = json.loads(finances_raw)
    except Exception:
        return []

    alerts = []
    for item in finances:
        due_day = item.get("due_day", 0)
        days_until = (due_day - today.day) % 30  # aproximação mensal

        if 0 <= days_until <= 3:
            state_key = f"life_guard:finance:{today.year}-{today.month}:{item['name']}"
            if memory.get_state(state_key):
                continue
            msg = f"{item['name']}: vence em {days_until}d - R$ {item['amount']:.2f}"
            _dispatch(msg, "mac", sound=True)
            memory.set_state(state_key, "sent")
            alerts.append(item)

    return alerts


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def run_all_checks() -> dict:
    """Entry point para o loop de background."""
    if not sanity_client.is_agent_enabled(AGENT_NAME, default=True):
        notifier.info(
            "Life Guard desabilitado via Sanity (agent_config.enabled=false).",
            AGENT_NAME,
        )
        return {"routines": [], "hydration": {}, "finances": []}
    return {
        "routines": check_daily_routines(),
        "hydration": check_hydration(),
        "finances": check_finances(),
    }


# ---------------------------------------------------------------------------
# Ações manuais
# ---------------------------------------------------------------------------


def add_finance(name: str, due_day: int, amount: float) -> dict:
    """Adiciona ou atualiza um item de finanças pessoais."""
    finances_raw = memory.get_state("life_guard:finances") or "[]"
    try:
        finances = json.loads(finances_raw)
    except Exception:
        finances = []
    finances = [f for f in finances if f["name"] != name]
    finances.append({"name": name, "due_day": due_day, "amount": amount})
    memory.set_state("life_guard:finances", json.dumps(finances))
    return {"status": "ok", "item": name}


def confirm_routine(routine_id: str) -> dict:
    """Marca rotina como feita (ex: 'já me exercitei')."""
    today = date.today().isoformat()
    memory.set_state(f"life_guard:{today}:{routine_id}", "sent")
    memory.set_state(f"life_guard:{today}:{routine_id}:done", "true")
    return {"status": "confirmed", "routine": routine_id}


# ---------------------------------------------------------------------------
# Handoff entry point
# ---------------------------------------------------------------------------


def handle_handoff(payload: dict) -> dict:
    action = payload.get("action")
    if action == "add_finance":
        return add_finance(payload["name"], payload["due_day"], payload["amount"])
    if action == "confirm_routine":
        return confirm_routine(payload["routine_id"])
    if action == "check":
        return run_all_checks()
    return {"error": f"unknown action: {action}"}
````

## File: agents/notion_sync.py
````python
# =============================================================================
# agents/notion_sync.py — Agente de sincronização com o Notion
# =============================================================================
# Usa a Notion REST API diretamente (requests + token).
# Responsável por criar/atualizar páginas nos databases "Tarefas" e "Agenda Diária".
#
# Databases esperados no Notion:
#   Tarefas:
#     - Nome          (title)
#     - Status        (select): "A fazer" | "Em progresso" | "Concluído"
#     - Prioridade    (select): "Alta" | "Média" | "Baixa"
#     - Horário previsto (rich_text)
#     - Horário real     (rich_text)
#
#   Agenda Diária:
#     - Data          (date)
#     - Bloco horário (rich_text)
#     - Tarefa vinculada (relation → Tarefas)
#     - Concluído     (checkbox)

import os
import sys
from datetime import date, datetime, timedelta
from typing import Any, Optional

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import (
    NOTION_AGENDA_DB_ID,
    NOTION_API_BASE,
    NOTION_API_VERSION,
    NOTION_TASKS_DB_ID,
    NOTION_TOKEN,
)
from core import memory, notifier

AGENT_NAME = "notion_sync"


# ---------------------------------------------------------------------------
# Cliente HTTP base
# ---------------------------------------------------------------------------


def _headers() -> dict:
    """Retorna os headers padrão para chamadas à Notion API."""
    return {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_API_VERSION,
    }


class _NotionRateLimitError(RuntimeError):
    """Levantada em 429 ou 5xx — elegível para retry automático."""


@retry(
    retry=retry_if_exception_type(_NotionRateLimitError),
    wait=wait_exponential(multiplier=1, min=1, max=30),
    stop=stop_after_attempt(4),
    reraise=True,
)
def _request(method: str, endpoint: str, data: Optional[dict] = None) -> dict:
    """
    Faz uma requisição à Notion API.
    Faz retry automático em 429 (rate limit) e 5xx com backoff exponencial (1s→2s→4s→30s).
    Levanta RuntimeError em caso de falha não-recuperável.
    """
    url = f"{NOTION_API_BASE}/{endpoint.lstrip('/')}"
    response = requests.request(method, url, headers=_headers(), json=data, timeout=15)

    if response.status_code == 429 or response.status_code >= 500:
        raise _NotionRateLimitError(
            f"Notion API erro {response.status_code} em {method} {endpoint}: {response.text[:200]}"
        )

    if not response.ok:
        raise RuntimeError(
            f"Notion API erro {response.status_code} em {method} {endpoint}: {response.text[:500]}"
        )

    return response.json()


# ---------------------------------------------------------------------------
# Helpers para construir propriedades Notion
# ---------------------------------------------------------------------------


def _prop_title(text: str) -> dict:
    return {"title": [{"text": {"content": text}}]}


def _prop_select(value: str) -> dict:
    return {"select": {"name": value}}


def _prop_rich_text(text: str) -> dict:
    return {"rich_text": [{"text": {"content": text}}]}


def _prop_date(date_str: str) -> dict:
    """date_str pode ser YYYY-MM-DD ou ISO datetime."""
    return {"date": {"start": date_str}}


def _prop_checkbox(checked: bool) -> dict:
    return {"checkbox": checked}


def _prop_relation(page_id: str) -> dict:
    return {"relation": [{"id": page_id}]}


# ---------------------------------------------------------------------------
# Operações em Tarefas
# ---------------------------------------------------------------------------


def create_notion_task(
    title: str,
    status: str = "A fazer",
    priority: str = "Média",
    scheduled_time: Optional[str] = None,
    actual_time: Optional[str] = None,
) -> str:
    """
    Cria uma nova página no database Tarefas do Notion.
    Retorna o ID da página criada.
    """
    if not NOTION_TOKEN or not NOTION_TASKS_DB_ID:
        notifier.warning(
            "Notion não configurado — tarefa não sincronizada.", AGENT_NAME
        )
        return ""

    properties: dict[str, Any] = {
        "Nome": _prop_title(title),
        "Status": _prop_select(status),
        "Prioridade": _prop_select(priority),
    }
    if scheduled_time:
        properties["Horário previsto"] = _prop_rich_text(scheduled_time)
    if actual_time:
        properties["Horário real"] = _prop_rich_text(actual_time)

    payload = {
        "parent": {"database_id": NOTION_TASKS_DB_ID},
        "properties": properties,
    }

    result = _request("POST", "pages", payload)
    page_id = result["id"]
    notifier.success(
        f"Tarefa criada no Notion: '{title}' (ID: {page_id[:8]}...)", AGENT_NAME
    )
    return page_id


def update_notion_task_status(
    notion_page_id: str,
    status: str,
    actual_time: Optional[str] = None,
) -> None:
    """Atualiza o status (e horário real) de uma tarefa no Notion."""
    if not NOTION_TOKEN or not notion_page_id:
        return

    properties: dict[str, Any] = {"Status": _prop_select(status)}
    if actual_time:
        properties["Horário real"] = _prop_rich_text(actual_time)

    _request("PATCH", f"pages/{notion_page_id}", {"properties": properties})
    notifier.info(
        f"Status atualizado no Notion → {status} (página {notion_page_id[:8]}...)",
        AGENT_NAME,
    )


def fetch_notion_tasks(filter_status: Optional[str] = None) -> list[dict]:
    """
    Lê todas as tarefas do Notion (com filtro opcional por status).
    Retorna lista de dicts com campos normalizados.
    """
    if not NOTION_TOKEN or not NOTION_TASKS_DB_ID:
        notifier.warning(
            "Notion não configurado — leitura de tarefas impossível.", AGENT_NAME
        )
        return []

    payload: dict[str, Any] = {"page_size": 100}
    if filter_status:
        payload["filter"] = {
            "property": "Status",
            "select": {"equals": filter_status},
        }

    result = _request("POST", f"databases/{NOTION_TASKS_DB_ID}/query", payload)
    tasks = []
    for page in result.get("results", []):
        props = page.get("properties", {})
        task = {
            "notion_page_id": page["id"],
            "title": _extract_title(props.get("Nome")),
            "status": _extract_select(props.get("Status")),
            "priority": _extract_select(props.get("Prioridade")),
            "scheduled_time": _extract_rich_text(props.get("Horário previsto")),
            "actual_time": _extract_rich_text(props.get("Horário real")),
        }
        tasks.append(task)

    notifier.info(f"Lidas {len(tasks)} tarefas do Notion.", AGENT_NAME)
    return tasks


# ---------------------------------------------------------------------------
# Operações na Agenda Diária
# ---------------------------------------------------------------------------


def create_notion_agenda_block(
    block_date: str,
    time_slot: str,
    task_title: str,
    notion_task_page_id: Optional[str] = None,
    completed: bool = False,
) -> str:
    """
    Cria um bloco na Agenda Diária do Notion.
    Retorna o ID da página criada.
    """
    if not NOTION_TOKEN or not NOTION_AGENDA_DB_ID:
        notifier.warning(
            "Notion não configurado — bloco de agenda não criado.", AGENT_NAME
        )
        return ""

    properties: dict[str, Any] = {
        "Data": _prop_date(block_date),
        "Bloco horário": _prop_rich_text(f"{time_slot} — {task_title}"),
        "Concluído": _prop_checkbox(completed),
    }

    # Se temos o ID da tarefa no Notion, criamos a relação
    if notion_task_page_id:
        properties["Tarefa vinculada"] = _prop_relation(notion_task_page_id)

    payload = {
        "parent": {"database_id": NOTION_AGENDA_DB_ID},
        "properties": properties,
    }

    result = _request("POST", "pages", payload)
    page_id = result["id"]
    notifier.success(
        f"Bloco de agenda criado: {block_date} {time_slot} → '{task_title}'", AGENT_NAME
    )
    return page_id


def mark_notion_agenda_block_done(notion_page_id: str, completed: bool = True) -> None:
    """Marca um bloco de agenda como concluído no Notion."""
    if not NOTION_TOKEN or not notion_page_id:
        return
    _request(
        "PATCH",
        f"pages/{notion_page_id}",
        {"properties": {"Concluído": _prop_checkbox(completed)}},
    )
    notifier.info(
        f"Bloco de agenda {'concluído' if completed else 'reaberto'} no Notion.",
        AGENT_NAME,
    )


def fetch_today_agenda_from_notion() -> list[dict]:
    """Lê os blocos de hoje da Agenda Diária no Notion."""
    today = date.today().isoformat()
    return fetch_agenda_range_from_notion(today, today)


def fetch_agenda_range_from_notion(start_date: str, end_date: str) -> list[dict]:
    """Lê blocos da Agenda Diária do Notion em um intervalo de datas."""
    if not NOTION_TOKEN or not NOTION_AGENDA_DB_ID:
        return []

    start_dt, end_dt = _normalize_date_range(start_date, end_date)
    payload = {
        "page_size": 100,
        "filter": {
            "and": [
                {"property": "Data", "date": {"on_or_after": start_dt}},
                {"property": "Data", "date": {"on_or_before": end_dt}},
            ]
        },
        "sorts": [
            {"property": "Data", "direction": "ascending"},
            {"property": "Bloco horário", "direction": "ascending"},
        ],
    }

    result = _request("POST", f"databases/{NOTION_AGENDA_DB_ID}/query", payload)
    blocks = []
    for page in result.get("results", []):
        props = page.get("properties", {})
        block_text = _extract_rich_text(props.get("Bloco horário"))
        time_slot, task_title = _split_agenda_block_text(block_text)
        blocks.append(
            {
                "notion_page_id": page["id"],
                "date": _extract_date(props.get("Data")),
                "time_slot": time_slot,
                "task_title": task_title,
                "completed": _extract_checkbox(props.get("Concluído")),
                "raw_block": block_text,
            }
        )

    return blocks


# ---------------------------------------------------------------------------
# Sincronização bidirecional
# ---------------------------------------------------------------------------


def sync_tasks_to_local() -> int:
    """
    Puxa tarefas do Notion e insere/atualiza no banco local.
    Retorna quantas tarefas foram sincronizadas.
    """
    notion_tasks = fetch_notion_tasks()
    count = 0
    for nt in notion_tasks:
        # Verifica se já existe localmente pela page_id
        existing = None
        all_local = memory.list_all_tasks()
        for lt in all_local:
            if lt.get("notion_page_id") == nt["notion_page_id"]:
                existing = lt
                break

        if not existing:
            task_id = memory.create_task(
                title=nt["title"] or "Sem título",
                priority=nt["priority"] or "Média",
                scheduled_time=nt["scheduled_time"],
                notion_page_id=nt["notion_page_id"],
            )
            if nt["status"]:
                memory.update_task_status(task_id, nt["status"])
            count += 1
            _maybe_create_agenda_block(task_id, nt)
        else:
            memory.update_task(
                existing["id"],
                title=nt["title"] or existing.get("title") or "Sem título",
                priority=nt["priority"] or existing.get("priority") or "Média",
                scheduled_time=nt.get("scheduled_time"),
                actual_time=nt.get("actual_time"),
                notion_page_id=nt.get("notion_page_id")
                or existing.get("notion_page_id"),
            )
            if nt.get("status"):
                memory.update_task_status(
                    existing["id"],
                    nt["status"],
                    nt.get("actual_time") or None,
                )
            # Tarefa já existe — garante bloco de agenda se tiver horário
            _maybe_create_agenda_block(existing["id"], nt)

    # Reconciliação: remove do Redis tarefas que já não existem no Notion
    notion_ids = {
        nt["notion_page_id"] for nt in notion_tasks if nt.get("notion_page_id")
    }
    removed = 0
    for lt in memory.list_all_tasks():
        local_notion_id = lt.get("notion_page_id") or ""
        title = lt.get("title") or ""
        # Caso 1: tem notion_page_id mas sumiu do Notion → órfã real
        orphan = local_notion_id and local_notion_id not in notion_ids
        # Caso 2: notion_page_id vazio + título sentinela → foi criada com título vazio no Notion
        sentinel = not local_notion_id and title in ("Sem título", "")
        if orphan or sentinel:
            memory.delete_task(lt["id"])
            removed += 1
            reason = (
                "não existe mais no Notion"
                if orphan
                else "notion_page_id vazio e título inválido"
            )
            notifier.info(
                f"Tarefa removida do Redis ({reason}): id={lt['id']} title='{title}'",
                AGENT_NAME,
            )

    notifier.success(
        f"Sincronização concluída: {count} nova(s), {removed} removida(s).", AGENT_NAME
    )
    return count


def _maybe_create_agenda_block(task_id: int, nt: dict) -> None:
    """Cria bloco de agenda hoje para tarefa com scheduled_time, sem duplicar."""
    from datetime import date as _date

    scheduled_time = (nt.get("scheduled_time") or "").strip()
    status = nt.get("status") or "A fazer"
    if not scheduled_time or status == "Concluído":
        return

    today = _date.today().isoformat()
    # Evita duplicata: verifica se já existe bloco com esse task_id hoje
    existing_blocks = memory.get_today_agenda()
    for b in existing_blocks:
        if str(b.get("task_id")) == str(task_id):
            return  # Já tem bloco para essa tarefa hoje

    # Normaliza o horário para "HH:MM-HH:MM"
    time_slot = _normalize_time_slot(scheduled_time)

    memory.create_agenda_block(
        block_date=today,
        time_slot=time_slot,
        task_title=nt.get("title") or "Sem título",
        task_id=task_id,
        notion_page_id=nt.get("notion_page_id"),
    )


def sync_agenda_range_to_local(start_date: str, end_date: str) -> int:
    """Importa blocos da Agenda Diária do Notion para o banco local."""
    blocks = fetch_agenda_range_from_notion(start_date, end_date)
    if not blocks:
        return 0

    local_blocks = memory.list_agenda_between(
        start_date, end_date, include_rescheduled=True
    )
    existing_keys = {
        (
            block.get("block_date"),
            block.get("time_slot"),
            (block.get("task_title") or "").strip().lower(),
        )
        for block in local_blocks
    }

    created = 0
    for block in blocks:
        block_date = block.get("date") or start_date
        task_title = block.get("task_title") or "Sem título"
        key = (block_date, block.get("time_slot"), task_title.strip().lower())
        if not block.get("time_slot") or key in existing_keys:
            continue

        memory.create_agenda_block(
            block_date=block_date,
            time_slot=block["time_slot"],
            task_title=task_title,
            notion_page_id=block.get("notion_page_id"),
        )
        existing_keys.add(key)
        created += 1

    if created:
        notifier.success(
            f"Agenda Notion: {created} bloco(s) importado(s) entre {start_date} e {end_date}.",
            AGENT_NAME,
        )
    return created


def sync_local_task_to_notion(task_id: int) -> Optional[str]:
    """
    Envia uma tarefa local para o Notion (cria ou atualiza).
    Retorna o notion_page_id.
    """
    task = memory.get_task(task_id)
    if not task:
        notifier.error(f"Tarefa {task_id} não encontrada.", AGENT_NAME)
        return None

    if task.get("notion_page_id"):
        # Atualiza
        update_notion_task_status(
            task["notion_page_id"],
            task["status"],
            task.get("actual_time"),
        )
        return task["notion_page_id"]
    else:
        # Cria
        page_id = create_notion_task(
            title=task["title"],
            status=task["status"],
            priority=task["priority"],
            scheduled_time=task.get("scheduled_time"),
            actual_time=task.get("actual_time"),
        )
        if page_id:
            memory.update_task_notion_id(task_id, page_id)
        return page_id


# ---------------------------------------------------------------------------
# Helpers de extração de propriedades Notion
# ---------------------------------------------------------------------------


def _extract_title(prop: Optional[dict]) -> str:
    if not prop:
        return ""
    items = prop.get("title", [])
    return "".join(t.get("plain_text", "") for t in items)


def _extract_select(prop: Optional[dict]) -> str:
    if not prop:
        return ""
    sel = prop.get("select")
    return sel.get("name", "") if sel else ""


def _extract_rich_text(prop: Optional[dict]) -> str:
    if not prop:
        return ""
    items = prop.get("rich_text", [])
    return "".join(t.get("plain_text", "") for t in items)


def _extract_date(prop: Optional[dict]) -> str:
    if not prop:
        return ""
    d = prop.get("date")
    return d.get("start", "") if d else ""


def _extract_checkbox(prop: Optional[dict]) -> bool:
    if not prop:
        return False
    return bool(prop.get("checkbox", False))


def _normalize_time_slot(value: str) -> str:
    raw = value.strip()
    if not raw:
        return ""
    if "-" in raw:
        start_str, end_str = [part.strip() for part in raw.split("-", 1)]
        return f"{start_str}-{end_str}"
    try:
        start_dt = datetime.strptime(raw, "%H:%M")
        end_dt = start_dt + timedelta(hours=1)
        return f"{start_dt.strftime('%H:%M')}-{end_dt.strftime('%H:%M')}"
    except ValueError:
        return raw


def _split_agenda_block_text(raw_text: str) -> tuple[str, str]:
    if "—" in raw_text:
        left, right = raw_text.split("—", 1)
        return left.strip(), right.strip() or "Sem título"
    return raw_text.strip(), "Sem título"


def _normalize_date_range(start_date: str, end_date: str) -> tuple[str, str]:
    start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()
    if end_dt < start_dt:
        start_dt, end_dt = end_dt, start_dt
    return start_dt.isoformat(), end_dt.isoformat()


# ---------------------------------------------------------------------------
# Sincronização diferencial
# ---------------------------------------------------------------------------


def fetch_tasks_modified_since(last_sync_iso: str) -> list[dict]:
    """Puxa apenas tarefas modificadas após last_sync_iso (polling diferencial)."""
    if not NOTION_TOKEN or not NOTION_TASKS_DB_ID:
        return []

    payload: dict[str, Any] = {
        "page_size": 100,
        "filter": {
            "timestamp": "last_edited_time",
            "last_edited_time": {"after": last_sync_iso},
        },
    }

    result = _request("POST", f"databases/{NOTION_TASKS_DB_ID}/query", payload)
    tasks = []
    for page in result.get("results", []):
        props = page.get("properties", {})
        task = {
            "notion_page_id": page["id"],
            "title": _extract_title(props.get("Nome")),
            "status": _extract_select(props.get("Status")),
            "priority": _extract_select(props.get("Prioridade")),
            "scheduled_time": _extract_rich_text(props.get("Horário previsto")),
            "actual_time": _extract_rich_text(props.get("Horário real")),
            "last_edited_time": page.get("last_edited_time", ""),
        }
        tasks.append(task)

    notifier.info(
        f"Sync diferencial: {len(tasks)} tarefa(s) modificada(s) desde {last_sync_iso[:16]}.",
        AGENT_NAME,
    )
    return tasks


def sync_differential() -> int:
    """
    Sincronização diferencial: importa do Notion apenas o que mudou desde
    o último sync. Guarda/lê o timestamp em system_state['notion_last_sync_ts'].
    Retorna número de tarefas criadas/atualizadas.
    """
    last_sync = memory.get_state("notion_last_sync_ts")

    if not last_sync:
        notifier.info("Primeira sync — executando full sync.", AGENT_NAME)
        count = sync_tasks_to_local()
    else:
        modified = fetch_tasks_modified_since(last_sync)
        count = 0
        all_local = memory.list_all_tasks()
        local_by_notion_id = {
            lt["notion_page_id"]: lt for lt in all_local if lt.get("notion_page_id")
        }

        for nt in modified:
            existing = local_by_notion_id.get(nt["notion_page_id"])
            if existing:
                if nt["status"] and existing["status"] != nt["status"]:
                    memory.update_task_status(existing["id"], nt["status"])
                    count += 1
                _maybe_create_agenda_block(existing["id"], nt)
            else:
                task_id = memory.create_task(
                    title=nt["title"] or "Sem título",
                    priority=nt["priority"] or "Média",
                    scheduled_time=nt["scheduled_time"],
                    notion_page_id=nt["notion_page_id"],
                )
                if nt["status"]:
                    memory.update_task_status(task_id, nt["status"])
                count += 1
                _maybe_create_agenda_block(task_id, nt)

    memory.set_state("notion_last_sync_ts", datetime.now().isoformat())
    if count:
        notifier.success(
            f"Sync diferencial: {count} tarefa(s) processada(s).", AGENT_NAME
        )
    return count


# ---------------------------------------------------------------------------
# Handoff entry point — chamado pelo Orchestrator
# ---------------------------------------------------------------------------


class HandoffPayload:
    """Estrutura de handoff padronizada para este agente."""

    @staticmethod
    def create_task(
        title: str, priority: str = "Média", scheduled_time: str = ""
    ) -> dict:
        return {
            "action": "create_task",
            "title": title,
            "priority": priority,
            "scheduled_time": scheduled_time,
        }

    @staticmethod
    def update_status(task_id: int, status: str) -> dict:
        return {"action": "update_status", "task_id": task_id, "status": status}

    @staticmethod
    def sync_from_notion() -> dict:
        return {"action": "sync_from_notion"}

    @staticmethod
    def get_today_agenda() -> dict:
        return {"action": "get_today_agenda"}


def handle_handoff(payload: dict) -> dict:
    """
    Ponto de entrada para handoffs do Orchestrator.
    Retorna dict com 'status' e 'result'.
    """
    action = payload.get("action", "")
    notifier.agent_event(f"Recebendo handoff: action='{action}'", AGENT_NAME)

    handoff_id = memory.log_handoff("orchestrator", AGENT_NAME, action, payload)

    try:
        result = {}

        if action == "create_task":
            page_id = create_notion_task(
                title=payload["title"],
                priority=payload.get("priority", "Média"),
                scheduled_time=payload.get("scheduled_time", ""),
            )
            result = {
                "notion_page_id": page_id,
                "message": f"Tarefa '{payload['title']}' criada.",
            }

        elif action == "update_status":
            task = memory.get_task(payload["task_id"])
            if task and task.get("notion_page_id"):
                update_notion_task_status(task["notion_page_id"], payload["status"])
            result = {"message": f"Status atualizado para '{payload['status']}'."}

        elif action == "sync_from_notion":
            count = sync_tasks_to_local()
            result = {"synced": count, "message": f"{count} tarefa(s) importada(s)."}

        elif action == "get_today_agenda":
            blocks = fetch_today_agenda_from_notion()
            local_blocks = memory.get_today_agenda()
            result = {
                "notion_blocks": blocks,
                "local_blocks": local_blocks,
                "total": len(blocks) or len(local_blocks),
            }

        elif action == "sync_agenda_range":
            start_date, end_date = _normalize_date_range(
                payload["start_date"],
                payload["end_date"],
            )
            count = sync_agenda_range_to_local(start_date, end_date)
            result = {
                "synced": count,
                "message": f"{count} bloco(s) de agenda importado(s).",
                "start_date": start_date,
                "end_date": end_date,
            }

        elif action == "sync_differential":
            count = sync_differential()
            result = {
                "synced": count,
                "message": f"{count} tarefa(s) atualizada(s) pelo sync diferencial.",
            }

        else:
            raise ValueError(f"Ação desconhecida: '{action}'")

        memory.update_handoff_result(handoff_id, result, "success")
        return {"status": "success", "result": result}

    except Exception as exc:
        error_msg = str(exc)
        notifier.error(f"Erro no handoff '{action}': {error_msg}", AGENT_NAME)
        memory.update_handoff_result(handoff_id, {"error": error_msg}, "error")
        return {"status": "error", "result": {"error": error_msg}}
````

## File: agents/orchestrator.py
````python
# =============================================================================
# agents/orchestrator.py — Agente orquestrador central
# =============================================================================
# Recebe input do usuário (texto livre), decide qual agente acionar,
# delega via handoffs e consolida as respostas em linguagem natural.
#
# Fluxo de handoff:
#   Usuário → Orchestrator → [Scheduler | FocusGuard | NotionSync | Validator]
#                                      ↓
#                          Resposta consolidada → Usuário
#
# O Orchestrator usa o GPT-4o-mini como "roteador inteligente": o LLM decide
# qual combinação de agentes acionar e em que ordem.

import json
import os
import re
import sys
from datetime import datetime
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa os agentes especialistas
from agents import (
    calendar_sync,
    focus_guard,
    notion_sync,
    retrospective,
    scheduler,
    validator,
)
from agents.persona_manager import (
    get_direct_prompt,
    get_persona,
    get_synthesis_prompt,
    get_system_prompt,
    get_temperature,
)
from core import memory, notifier, sanity_client
from core.openai_utils import chat_completions

AGENT_NAME = "orchestrator"


# ---------------------------------------------------------------------------
# Descrição dos agentes disponíveis (para o LLM do Orchestrator)
# ---------------------------------------------------------------------------

AGENTS_REGISTRY = {
    "scheduler": {
        "description": "Gerencia blocos de tempo, agenda diária, priorização de tarefas.",
        "actions": [
            "get_today_schedule",
            "add_block",
            "complete_block",
            "suggest_agenda",
            "get_prioritized_tasks",
        ],
    },
    "focus_guard": {
        "description": "Monitora foco, gerencia sessões Pomodoro, emite alertas de desvio.",
        "actions": [
            "start_guard",
            "stop_guard",
            "force_check",
            "start_session",
            "end_session",
            "status",
            "get_alerts",
        ],
    },
    "notion_sync": {
        "description": "Cria/atualiza tarefas e agenda no Notion via API REST.",
        "actions": [
            "create_task",
            "update_status",
            "sync_from_notion",
            "get_today_agenda",
        ],
    },
    "validator": {
        "description": "Valida cruzando evidências se uma tarefa foi realmente concluída.",
        "actions": [
            "validate_task",
            "validate_all",
            "get_evidence",
        ],
    },
    "retrospective": {
        "description": "Gera relatório de retrospectiva semanal com métricas e insights.",
        "actions": ["run", "metrics_only"],
    },
    "calendar_sync": {
        "description": "Integra Google Calendar como capacidade opcional de agenda — importa eventos e exporta blocos quando ativado.",
        "actions": [
            "import_today",
            "fetch_today",
            "fetch_week",
            "export_block",
            "status",
        ],
    },
}


# Prompt do Orchestrator para roteamento de intenções
_ROUTING_PROMPT_FALLBACK = f"""Você é o Orchestrator de um sistema de gestão pessoal com múltiplos agentes.
Dado um input do usuário, determine:
1. Qual(is) agente(s) acionar
2. Qual ação executar em cada agente
3. Os parâmetros necessários para cada ação

Agentes disponíveis:
{json.dumps(AGENTS_REGISTRY, ensure_ascii=False, indent=2)}

Retorne um JSON com:
{{
  "intent": "descrição breve da intenção do usuário",
  "handoffs": [
    {{
      "agent": "nome_do_agente",
      "payload": {{
        "action": "nome_da_ação",
        ... outros parâmetros ...
      }}
    }}
  ],
  "requires_user_input": false,
  "clarification_question": null
}}

Regras importantes:
- Se precisar de mais informações, defina requires_user_input=true e clarification_question
- Para criar tarefas, sempre envie para notion_sync E scheduler
- Para marcar tarefa como concluída, sempre passe pelo validator ANTES de confirmar
- Para verificar agenda, combine scheduler + notion_sync
- Se o usuário perguntar sobre foco/progresso, acione o focus_guard
- Se o usuário perguntar sobre atraso, alertas, avisos, notificações ou status do sistema, consulte os agentes.
- Não responda diretamente sobre estado operacional se você não consultou dados reais.
- Quando múltiplos agentes são necessários, ordene-os pela lógica de execução
- Se nenhum agente for necessário, retorne handoffs vazio e responda diretamente
"""


# Prompt base para síntese — será composto com a persona ativa
_SYNTHESIS_BASE = """Você é o Orchestrator de um sistema de gestão pessoal.
Baseado nos resultados dos agentes especialistas, forneça uma resposta clara,
concisa e útil ao usuário.

Nunca invente tarefas, alertas, horários ou estados do sistema. Só mencione itens que
apareçam explicitamente nos resultados recebidos. Se faltar dado, diga que não foi possível
confirmar.
Não mencione detalhes técnicos internos (IDs de banco, payloads JSON, etc.)."""

_DIRECT_BASE = """Você é um assistente de gestão pessoal.
Nunca afirme estado do sistema, tarefas, alertas ou agenda sem dados explícitos no contexto.
Se a pergunta depender do estado do sistema e ele não estiver disponível, diga que precisa verificar."""

# Mantém compatibilidade — usados como fallback
SYNTHESIS_PROMPT = _SYNTHESIS_BASE
DIRECT_RESPONSE_PROMPT = _DIRECT_BASE


def _get_routing_prompt() -> str:
    return sanity_client.get_prompt("orchestrator", "routing", _ROUTING_PROMPT_FALLBACK)


def _build_synthesis_prompt(persona_id: Optional[str] = None) -> str:
    """Compõe o prompt de síntese com a persona ativa."""
    base_prompt = sanity_client.get_prompt("orchestrator", "synthesis", _SYNTHESIS_BASE)
    persona_override = get_synthesis_prompt(persona_id)
    if persona_override:
        return f"{base_prompt}\n\nEstilo de resposta:\n{persona_override}"
    return base_prompt


def _build_direct_prompt(persona_id: Optional[str] = None) -> str:
    """Compõe o prompt de resposta direta com a persona ativa."""
    base_prompt = sanity_client.get_prompt("orchestrator", "direct", _DIRECT_BASE)
    persona_override = get_direct_prompt(persona_id)
    if persona_override:
        return f"{base_prompt}\n\nEstilo de resposta:\n{persona_override}"
    return base_prompt


def _context_history_text(context: Optional[dict]) -> str:
    if not context:
        return ""

    history = context.get("chat_history", [])
    if not isinstance(history, list):
        return ""

    lines = []
    for item in history[-6:]:
        if not isinstance(item, dict):
            continue
        role = item.get("role", "user")
        content = str(item.get("content", "")).strip()
        if not content:
            continue
        label = "Usuário" if role == "user" else "Assistente"
        lines.append(f"{label}: {content}")
    return "\n".join(lines)


def _build_rule_based_route(
    user_input: str, context: Optional[dict] = None
) -> Optional[dict]:
    history_text = _context_history_text(context)
    combined = f"{history_text}\nUsuário: {user_input}".lower()

    mentions_delay = bool(re.search(r"\batras\w*", combined))
    mentions_alert = any(
        term in combined
        for term in (
            "alerta",
            "alertas",
            "aviso",
            "avisado",
            "notificação",
            "notificações",
        )
    )
    mentions_focus = any(
        term in combined for term in ("foco", "desvio", "on track", "fora do plano")
    )
    asks_status = any(
        term in combined
        for term in (
            "como está",
            "qual é o status",
            "status atual",
            "situação",
            "meu sistema",
        )
    )
    asks_next_step = any(
        term in combined
        for term in ("o que fazer", "como devo agir", "me ajude", "indique o que fazer")
    )
    asks_capability = any(
        term in combined
        for term in (
            "o que voce consegue",
            "o que você consegue",
            "o que pode fazer",
            "o que voce pode fazer",
            "capaz de fazer",
            "seus limites",
            "suas capacidades",
            "node infiltrado",
            "nó infiltrado",
        )
    )
    mentions_deploy = any(
        term in combined
        for term in (
            "railway",
            "deploy",
            "deployado",
            "produção",
            "producao",
            "codigo deployado",
            "código deployado",
        )
    )

    if asks_capability and (mentions_deploy or "sistema" in combined):
        return {
            "intent": "capabilities_runtime",
            "handoffs": [],
            "requires_user_input": False,
            "clarification_question": None,
        }

    if (
        mentions_delay
        or (mentions_alert and (asks_status or asks_next_step))
        or (mentions_focus and asks_status)
    ):
        return {
            "intent": "verificar atrasos, alertas e foco atual",
            "handoffs": [
                {"agent": "focus_guard", "payload": {"action": "force_check"}},
                {"agent": "focus_guard", "payload": {"action": "get_alerts"}},
                {"agent": "scheduler", "payload": {"action": "get_prioritized_tasks"}},
            ],
            "requires_user_input": False,
            "clarification_question": None,
        }

    if asks_status and any(
        term in combined for term in ("agenda", "tarefas", "tarefa", "foco", "sistema")
    ):
        return {
            "intent": "status operacional do sistema",
            "handoffs": [
                {"agent": "focus_guard", "payload": {"action": "status"}},
                {"agent": "focus_guard", "payload": {"action": "get_alerts"}},
                {"agent": "scheduler", "payload": {"action": "get_today_schedule"}},
                {"agent": "scheduler", "payload": {"action": "get_prioritized_tasks"}},
            ],
            "requires_user_input": False,
            "clarification_question": None,
        }

    return None


def _result_for(handoff_results: list[dict], agent: str, action: str) -> dict:
    for item in handoff_results:
        if item.get("agent") == agent and item.get("action") == action:
            return item.get("result", {}) or {}
    return {}


def _format_focus_response(handoff_results: list[dict]) -> Optional[str]:
    force_check = _result_for(handoff_results, "focus_guard", "force_check")
    focus_status = _result_for(handoff_results, "focus_guard", "status")
    alerts_result = _result_for(handoff_results, "focus_guard", "get_alerts")
    tasks_result = _result_for(handoff_results, "scheduler", "get_prioritized_tasks")
    schedule_result = _result_for(handoff_results, "scheduler", "get_today_schedule")

    if not any(
        (force_check, focus_status, alerts_result, tasks_result, schedule_result)
    ):
        return None

    alerts = alerts_result.get("alerts", [])
    prioritized_tasks = tasks_result.get("tasks", [])
    blocks = schedule_result.get("blocks", [])

    lines: list[str] = []

    if force_check:
        progress = force_check.get("progress", {})
        load = progress.get("load", {})
        overdue_blocks = progress.get("overdue_blocks", [])
        analysis = force_check.get("analysis", {})
        overdue_count = load.get("overdue", len(overdue_blocks))

        if overdue_count:
            lines.append(f"Encontrei {overdue_count} bloco(s) atrasado(s) no sistema.")
            for block in overdue_blocks[:3]:
                lines.append(
                    f"{block.get('time_slot', '?')} | {block.get('task_title', 'Sem título')}"
                )
        else:
            lines.append("Não encontrei bloco atrasado neste instante.")

        if alerts:
            latest = alerts[0]
            lines.append(f"Há {len(alerts)} alerta(s) pendente(s).")
            if latest.get("message"):
                lines.append(f"Último alerta: {latest['message']}")
        else:
            lines.append("Não há alertas pendentes registrados.")

        if analysis.get("recommendation"):
            lines.append(f"Ação recomendada: {analysis['recommendation']}")
        elif overdue_blocks:
            first = overdue_blocks[0]
            lines.append(
                f"Ação recomendada: retome '{first.get('task_title', 'a tarefa atrasada')}' agora ou reprograme esse bloco antes de puxar outra frente."
            )
    else:
        running = focus_status.get("running")
        on_track = focus_status.get("on_track")
        if running is not None:
            lines.append(
                f"Focus Guard: {'ativo' if running else 'desligado'} | "
                f"{'no plano' if on_track else 'com desvio'}"
            )
        if alerts:
            lines.append(f"Alertas pendentes: {len(alerts)}.")
        else:
            lines.append("Alertas pendentes: 0.")

        if blocks:
            completed = sum(1 for block in blocks if block.get("completed"))
            lines.append(
                f"Agenda de hoje: {completed}/{len(blocks)} blocos concluídos."
            )

    if prioritized_tasks:
        top = prioritized_tasks[0]
        label = top.get("title", "Sem título")
        priority = top.get("priority", "Média")
        status = top.get("status", "A fazer")
        lines.append(f"Prioridade operacional agora: '{label}' [{priority}, {status}].")

    return "\n".join(lines)


def _runtime_capabilities_response(context: Optional[dict] = None) -> str:
    """Resposta determinística para perguntas sobre capacidade do runtime."""
    summary = {}
    if context and isinstance(context.get("system_summary"), dict):
        summary = context["system_summary"]
    tasks = summary.get("tasks", {})
    agenda = summary.get("agenda_today", {})
    alerts = summary.get("alerts", {})

    return (
        "Sim. Aqui no chat voce fala com o runtime deployado desta aplicacao.\n"
        "Eu consigo operar o sistema pelos agentes: status de foco, alertas, agenda, tarefas, sync e validacoes.\n"
        f"Snapshot agora: tarefas {tasks.get('total', 0)} | agenda {agenda.get('completed', 0)}/{agenda.get('total_blocks', 0)} blocos | alertas {alerts.get('pending', 0)}.\n"
        "Limites reais: nao tenho shell do servidor por este chat, nao rodo git/comandos de infra e nao publico nada externo sem gate."
    )


def _is_parrot_reply(user_input: str, reply: str) -> bool:
    """Evita respostas que apenas repetem a mensagem do usuário."""
    norm_user = re.sub(r"\W+", "", user_input or "", flags=re.UNICODE).lower()
    norm_reply = re.sub(r"\W+", "", reply or "", flags=re.UNICODE).lower()
    if not norm_user or not norm_reply:
        return False
    return norm_reply == norm_user or norm_reply.startswith(norm_user)


# ---------------------------------------------------------------------------
# Roteamento de intenção via LLM
# ---------------------------------------------------------------------------


def route_intent(user_input: str, context: Optional[dict] = None) -> dict:
    """
    Analisa o input do usuário e decide quais agentes acionar.

    Returns:
        Dict com 'intent', 'handoffs', 'requires_user_input', 'clarification_question'
    """
    rule_based = _build_rule_based_route(user_input, context)
    if rule_based:
        notifier.agent_event(
            f"Intent heurística: '{rule_based.get('intent', '?')}' | "
            f"Handoffs: {[h['agent'] for h in rule_based.get('handoffs', [])]}",
            AGENT_NAME,
        )
        return rule_based

    # Contexto adicional para o LLM (estado atual do sistema)
    system_context = {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "focus_guard_running": focus_guard.is_running(),
        "active_focus_session": memory.get_active_focus_session(),
        "pending_tasks_count": len(memory.get_tasks_by_status("A fazer")),
        "in_progress_tasks_count": len(memory.get_tasks_by_status("Em progresso")),
    }

    if context:
        system_context.update(context)

    messages = [
        {"role": "system", "content": _get_routing_prompt()},
        {
            "role": "user",
            "content": f"""Contexto do sistema:
{json.dumps(system_context, ensure_ascii=False, indent=2, default=str)}

Input do usuário: "{user_input}"

Retorne o JSON de roteamento.""",
        },
    ]

    try:
        response = chat_completions(
            messages=messages,
            temperature=0.2,
            response_format={"type": "json_object"},
        )
        routing = json.loads(response.choices[0].message.content)
        notifier.agent_event(
            f"Intent: '{routing.get('intent', '?')}' | "
            f"Handoffs: {[h['agent'] for h in routing.get('handoffs', [])]}",
            AGENT_NAME,
        )
        return routing
    except Exception as e:
        notifier.error(f"Erro no roteamento: {e}", AGENT_NAME)
        return {
            "intent": "unknown",
            "handoffs": [],
            "requires_user_input": True,
            "clarification_question": "Não entendi sua solicitação. Pode reformular?",
        }


# ---------------------------------------------------------------------------
# Execução de handoffs
# ---------------------------------------------------------------------------

_AGENT_HANDLERS = {
    "scheduler": scheduler.handle_handoff,
    "focus_guard": focus_guard.handle_handoff,
    "notion_sync": notion_sync.handle_handoff,
    "validator": validator.handle_handoff,
    "retrospective": retrospective.handle_handoff,
    "calendar_sync": calendar_sync.handle_handoff,
}


def execute_handoffs(handoffs: list[dict]) -> list[dict]:
    """
    Executa a lista de handoffs em sequência.
    Cada handoff pode referenciar resultados de handoffs anteriores.

    Returns:
        Lista de resultados com agent, action, status, result.
    """
    results = []
    accumulated_context: dict = {}

    for handoff in handoffs:
        agent_name = handoff.get("agent", "")
        payload = handoff.get("payload", {})

        handler = _AGENT_HANDLERS.get(agent_name)
        if not handler:
            notifier.error(f"Agente '{agent_name}' não encontrado.", AGENT_NAME)
            results.append(
                {
                    "agent": agent_name,
                    "action": payload.get("action", "?"),
                    "status": "error",
                    "result": {"error": f"Agente '{agent_name}' não registrado."},
                }
            )
            continue

        notifier.agent_event(
            f"Delegando para {agent_name}.{payload.get('action', '?')}...", AGENT_NAME
        )

        # Injeta contexto acumulado (resultados anteriores podem ser necessários)
        if accumulated_context:
            payload["_context"] = accumulated_context

        response = handler(payload)
        results.append(
            {
                "agent": agent_name,
                "action": payload.get("action", "?"),
                "status": response.get("status", "unknown"),
                "result": response.get("result", {}),
            }
        )

        # Acumula contexto para handoffs subsequentes
        accumulated_context[agent_name] = response.get("result", {})

    return results


# ---------------------------------------------------------------------------
# Síntese da resposta final
# ---------------------------------------------------------------------------


def synthesize_response(
    user_input: str,
    intent: str,
    handoff_results: list[dict],
    context: Optional[dict] = None,
    persona_id: Optional[str] = None,
) -> str:
    """
    Usa o GPT-GPT-4o-mini para sintetizar os resultados dos agentes em resposta natural.
    """
    fast_path = _format_focus_response(handoff_results)
    if fast_path:
        return fast_path

    results_str = json.dumps(handoff_results, ensure_ascii=False, indent=2, default=str)
    history_text = _context_history_text(context)
    history_block = f"Histórico recente:\n{history_text}\n\n" if history_text else ""

    synthesis_prompt = _build_synthesis_prompt(persona_id)
    persona_system = get_system_prompt(persona_id)
    if persona_system:
        synthesis_prompt = f"{synthesis_prompt}\n\nPersonalidade:\n{persona_system}"

    messages = [
        {"role": "system", "content": synthesis_prompt},
        {
            "role": "user",
            "content": f"""{history_block}Input original do usuário: "{user_input}"
Intenção detectada: {intent}

Resultados dos agentes especialistas:
{results_str}

Forneça uma resposta útil e clara ao usuário.""",
        },
    ]

    try:
        response = chat_completions(
            messages=messages,
            temperature=get_temperature(persona_id, "synthesis"),
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        notifier.error(f"Erro na síntese: {e}", AGENT_NAME)
        # Fallback: lista resultados diretamente
        lines = ["Resultado das ações executadas:"]
        for r in handoff_results:
            status_emoji = "✅" if r["status"] == "success" else "❌"
            lines.append(f"{status_emoji} {r['agent']}.{r['action']}: {r['status']}")
            if r["status"] == "error":
                lines.append(f"   Erro: {r['result'].get('error', '?')}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Pipeline principal do Orchestrator
# ---------------------------------------------------------------------------


def process(
    user_input: str,
    context: Optional[dict] = None,
    persona_id: Optional[str] = None,
) -> str:
    """
    Pipeline completo: input → roteamento → execução → síntese → resposta.

    Args:
        user_input: Comando/pergunta do usuário em linguagem natural.
        context:    Contexto extra opcional (ex: conversa anterior).
        persona_id: ID da persona ativa (None = persona padrão).

    Returns:
        Resposta final em texto para exibir ao usuário.
    """
    notifier.separator(f"ORCHESTRATOR")
    persona = get_persona(persona_id)
    persona_label = persona.get("short_name", "default") if persona else "default"
    notifier.agent_event(
        f'[{persona_label}] Input: "{user_input[:80]}{"..." if len(user_input) > 80 else ""}"',
        AGENT_NAME,
    )

    # 1. Rotear intenção
    routing = route_intent(user_input, context)

    # 2. Verificar se precisa de mais informações
    if routing.get("requires_user_input"):
        question = routing.get(
            "clarification_question", "Pode detalhar sua solicitação?"
        )
        notifier.warning(f"Preciso de mais informações: {question}", AGENT_NAME)
        return f"❓ {question}"

    # 3. Executar handoffs
    handoffs = routing.get("handoffs", [])
    if not handoffs:
        if routing.get("intent") == "capabilities_runtime":
            return _runtime_capabilities_response(context)
        notifier.info("Nenhum agente necessário — respondendo diretamente.", AGENT_NAME)
        return _direct_response(user_input, context, persona_id)

    results = execute_handoffs(handoffs)

    # 4. Sintetizar resposta
    response = synthesize_response(
        user_input=user_input,
        intent=routing.get("intent", ""),
        handoff_results=results,
        context=context,
        persona_id=persona_id,
    )

    notifier.separator()
    return response


def _direct_response(
    user_input: str,
    context: Optional[dict] = None,
    persona_id: Optional[str] = None,
) -> str:
    """Resposta direta do Orchestrator para perguntas simples sem agentes."""
    history_text = _context_history_text(context)
    history_block = f"Histórico recente:\n{history_text}\n\n" if history_text else ""

    direct_prompt = _build_direct_prompt(persona_id)
    persona_system = get_system_prompt(persona_id)
    if persona_system:
        direct_prompt = f"{direct_prompt}\n\nPersonalidade:\n{persona_system}"

    try:
        response = chat_completions(
            messages=[
                {
                    "role": "system",
                    "content": direct_prompt,
                },
                {
                    "role": "user",
                    "content": f"{history_block}Pergunta atual: {user_input}",
                },
            ],
            temperature=get_temperature(persona_id, "direct"),
        )
        content = response.choices[0].message.content.strip()
        if _is_parrot_reply(user_input, content):
            return (
                "Entendi seu ponto. Se quiser, eu te respondo de forma objetiva em uma destas frentes: "
                "status do sistema, foco/alertas, agenda/tarefas ou capacidade do deploy."
            )
        return content
    except Exception as e:
        return f"Desculpe, ocorreu um erro: {e}"


# ---------------------------------------------------------------------------
# Comandos rápidos do Orchestrator (shortcuts)
# ---------------------------------------------------------------------------


def quick_status() -> str:
    """Gera um status rápido completo do sistema."""
    return process("Qual é o status atual da minha agenda e foco hoje?")


def quick_add_task(title: str, priority: str = "Média", time_slot: str = "") -> str:
    """Atalho para adicionar uma tarefa rapidamente."""
    msg = f"Adicionar tarefa: '{title}', prioridade {priority}"
    if time_slot:
        msg += f", horário {time_slot}"
    return process(msg)


def quick_complete_task(task_id: int) -> str:
    """Atalho para marcar uma tarefa como concluída (com validação)."""
    return process(f"Marcar tarefa {task_id} como concluída")


def quick_start_focus(task_id: int, task_title: str, minutes: int = 25) -> str:
    """Atalho para iniciar uma sessão de foco."""
    return process(
        f"Iniciar sessão de foco na tarefa {task_id} ({task_title}) por {minutes} minutos"
    )


def get_system_summary() -> dict:
    """Retorna um resumo completo do estado do sistema (sem LLM)."""
    all_tasks = memory.list_all_tasks()
    today_agenda = memory.get_today_agenda()
    active_session = memory.get_active_focus_session()
    pending_alerts = memory.get_pending_alerts()
    focus_state = memory.get_state("focus_guard_state", {})

    return {
        "tasks": {
            "total": len(all_tasks),
            "a_fazer": sum(1 for t in all_tasks if t["status"] == "A fazer"),
            "em_progresso": sum(1 for t in all_tasks if t["status"] == "Em progresso"),
            "concluido": sum(1 for t in all_tasks if t["status"] == "Concluído"),
        },
        "agenda_today": {
            "total_blocks": len(today_agenda),
            "completed": sum(1 for b in today_agenda if b.get("completed")),
        },
        "focus": {
            "guard_running": focus_guard.is_running(),
            "active_session": active_session,
            "last_check": focus_state.get("last_check"),
            "on_track": focus_state.get("on_track", True),
        },
        "alerts": {
            "pending": len(pending_alerts),
        },
    }
````

## File: agents/persona_manager.py
````python
# =============================================================================
# agents/persona_manager.py — Gerenciador de identidades/personas
# =============================================================================
# Carrega personas de personas/*.json e fornece a persona ativa para o
# orchestrator compor prompts dinamicamente.
#
# Uso:
#   from agents.persona_manager import get_persona, list_personas, set_active_persona

import json
import os
import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import memory, notifier, sanity_client

_PERSONAS_DIR = Path(__file__).parent.parent / "personas"
_DEFAULT_PERSONA_ID = "coordinator"

# Cache em memória
_personas: dict[str, dict] = {}
_active_persona_id: str = _DEFAULT_PERSONA_ID


def _normalize_persona(source: dict, fallback_id: str) -> dict:
    persona_id = (
        source.get("id")
        or source.get("persona_id", {}).get("current")
        or source.get("persona_id")
        or fallback_id
    )
    params = source.get("parameters") or {}
    if not params:
        params = {
            "temperature_routing": source.get("temperature_routing", 0.2),
            "temperature_synthesis": source.get("temperature_synthesis", 0.5),
            "temperature_direct": source.get("temperature_direct", 0.7),
        }

    return {
        "id": persona_id,
        "name": source.get("name", fallback_id),
        "short_name": source.get("short_name", source.get("name", fallback_id)[:6]),
        "icon": source.get("icon", "●"),
        "description": source.get("description", ""),
        "tone": source.get("tone", "neutral"),
        "language": source.get("language", "pt-BR"),
        "system_prompt": source.get("system_prompt", ""),
        "synthesis_prompt_override": source.get("synthesis_prompt_override", ""),
        "direct_prompt_override": source.get("direct_prompt_override", ""),
        "preferred_model": source.get("preferred_model", ""),
        "role": source.get("role", ""),
        "parameters": params,
        "active": source.get("active", True),
    }


def _load_personas_from_disk() -> dict[str, dict]:
    personas: dict[str, dict] = {}
    if not _PERSONAS_DIR.exists():
        return personas
    for filepath in sorted(_PERSONAS_DIR.glob("*.json")):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                persona = json.load(f)
            pid = persona.get("id", filepath.stem)
            personas[pid] = _normalize_persona(persona, pid)
        except (json.JSONDecodeError, OSError) as e:
            notifier.error(f"Erro ao carregar {filepath.name}: {e}", "persona_manager")
    return personas


def _load_personas_from_sanity() -> dict[str, dict]:
    personas: dict[str, dict] = {}
    for item in sanity_client.get_all_personas():
        if not isinstance(item, dict):
            continue
        pid = (
            item.get("persona_id", {}).get("current")
            or item.get("persona_id")
            or item.get("id")
            or item.get("_id")
        )
        if not pid:
            continue
        personas[pid] = _normalize_persona(item, pid)
    return personas


def _load_personas() -> None:
    """Carrega personas com Sanity como fonte primária e disco como fallback."""
    global _personas
    disk_personas = _load_personas_from_disk()
    sanity_personas = _load_personas_from_sanity()
    merged = dict(disk_personas)
    merged.update(sanity_personas)
    _personas.clear()
    _personas.update(merged)
    global _active_persona_id
    # Restaura a persona ativa do Redis (sobrevive a restarts do servidor)
    try:
        saved = memory.get_state("active_persona_id")
        if saved and saved in _personas:
            _active_persona_id = saved
    except Exception:
        pass
    if _active_persona_id not in _personas:
        _active_persona_id = (
            _DEFAULT_PERSONA_ID
            if _DEFAULT_PERSONA_ID in _personas
            else next(iter(_personas), _DEFAULT_PERSONA_ID)
        )


def _ensure_loaded() -> None:
    if not _personas:
        _load_personas()


def reload_personas() -> None:
    """Força recarga das personas do Sanity e do disco."""
    sanity_client.invalidate_cache()
    _load_personas()


def list_personas() -> list[dict]:
    """Retorna lista resumida de todas as personas disponíveis."""
    _ensure_loaded()
    return [
        {
            "id": p["id"],
            "name": p["name"],
            "short_name": p.get("short_name", p["name"][:6]),
            "icon": p.get("icon", "●"),
            "description": p.get("description", ""),
            "tone": p.get("tone", "neutral"),
        }
        for p in _personas.values()
    ]


def get_persona(persona_id: Optional[str] = None) -> dict:
    """Retorna a persona completa pelo ID, ou a persona ativa."""
    _ensure_loaded()
    pid = persona_id or _active_persona_id
    persona = _personas.get(pid)
    if not persona:
        # Fallback para a default
        persona = _personas.get(_DEFAULT_PERSONA_ID, {})
    return persona


def get_active_persona_id() -> str:
    """Retorna o ID da persona ativa globalmente."""
    return _active_persona_id


def set_active_persona(persona_id: str) -> bool:
    """Define a persona ativa. Persiste no Redis para sobreviver a restarts."""
    global _active_persona_id
    _ensure_loaded()
    if persona_id in _personas:
        _active_persona_id = persona_id
        try:
            memory.set_state("active_persona_id", persona_id)
        except Exception:
            pass  # nunca falha por Redis indisponível
        return True
    return False


def get_system_prompt(persona_id: Optional[str] = None) -> str:
    """Retorna o system prompt da persona."""
    persona = get_persona(persona_id)
    return persona.get("system_prompt", "")


def get_synthesis_prompt(persona_id: Optional[str] = None) -> str:
    """Retorna o prompt de síntese customizado ou o padrão."""
    persona = get_persona(persona_id)
    return persona.get("synthesis_prompt_override", "")


def get_direct_prompt(persona_id: Optional[str] = None) -> str:
    """Retorna o prompt de resposta direta customizado."""
    persona = get_persona(persona_id)
    return persona.get("direct_prompt_override", "")


def get_temperature(persona_id: Optional[str] = None, phase: str = "direct") -> float:
    """Retorna a temperature para uma fase específica (routing, synthesis, direct)."""
    persona = get_persona(persona_id)
    params = persona.get("parameters", {})
    key = f"temperature_{phase}"
    defaults = {
        "temperature_routing": 0.2,
        "temperature_synthesis": 0.5,
        "temperature_direct": 0.7,
    }
    return params.get(key, defaults.get(key, 0.5))
````

## File: agents/retrospective.py
````python
# =============================================================================
# agents/retrospective.py — Agente de Retrospectiva Semanal
# =============================================================================
# Analisa a semana, calcula métricas e gera relatório via LLM.
# Opcionalmente cria página no Notion com os resultados.

import json
import sys
import os
from datetime import datetime, timedelta
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import notion_sync as _notion_sync
from config import NOTION_RETROSPECTIVE_PAGE_ID
from core import memory, notifier, sanity_client
from core.openai_utils import chat_completions

AGENT_NAME = "retrospective"

_RETROSPECTIVE_PROMPT_FALLBACK = """Você é um coach de produtividade pessoal.
Analise os dados da semana e gere uma retrospectiva clara com:

1. **Resumo Executivo** — 2-3 frases sobre a semana
2. **Pontos Positivos** — o que funcionou bem (bullet points)
3. **Pontos de Atenção** — o que pode melhorar (bullet points)
4. **Padrões Identificados** — insights sobre comportamento e produtividade
5. **Recomendações para a Próxima Semana** — 3-5 ações concretas

Seja direto, honesto e encorajador. Baseie-se apenas nos dados fornecidos.
Responda em markdown formatado."""


def _get_retrospective_prompt() -> str:
    return sanity_client.get_prompt(
        "retrospective",
        "retrospective",
        _RETROSPECTIVE_PROMPT_FALLBACK,
    )


# ---------------------------------------------------------------------------
# Coleta de dados
# ---------------------------------------------------------------------------


def _get_week_start() -> str:
    """Retorna ISO datetime de 7 dias atrás."""
    return (datetime.now() - timedelta(days=7)).isoformat()


def collect_week_data() -> dict:
    """Coleta todos os dados relevantes da semana."""
    since = _get_week_start()

    # Sessões de foco
    sessions = memory.get_sessions_since(since)
    total_focus_min = sum(s.get("actual_minutes") or 0 for s in sessions)
    completed_sessions = [s for s in sessions if s.get("status") == "completed"]
    abandoned_sessions = [s for s in sessions if s.get("status") == "abandoned"]

    # Tarefas
    all_tasks = memory.list_all_tasks()
    completed_tasks = memory.get_completed_tasks_since(since)
    pending_tasks = [t for t in all_tasks if t["status"] == "A fazer"]
    in_progress_tasks = [t for t in all_tasks if t["status"] == "Em progresso"]

    # Handoffs (atividade dos agentes)
    handoffs = memory.get_handoffs_since(since)
    handoffs_by_agent: dict = {}
    for h in handoffs:
        ag = h.get("target_agent", "unknown")
        handoffs_by_agent[ag] = handoffs_by_agent.get(ag, 0) + 1

    # Taxa de conclusão
    total_tasks_worked = len(completed_tasks) + len(in_progress_tasks)
    completion_rate = (
        round(len(completed_tasks) / total_tasks_worked * 100, 1)
        if total_tasks_worked > 0
        else 0.0
    )

    # Tempo médio por sessão
    avg_session_min = (
        round(total_focus_min / len(completed_sessions), 1)
        if completed_sessions
        else 0.0
    )

    return {
        "period": {
            "start": since[:10],
            "end": datetime.now().strftime("%Y-%m-%d"),
        },
        "metrics": {
            "total_focus_minutes": total_focus_min,
            "total_focus_hours": round(total_focus_min / 60, 1),
            "sessions_completed": len(completed_sessions),
            "sessions_abandoned": len(abandoned_sessions),
            "avg_session_minutes": avg_session_min,
            "tasks_completed": len(completed_tasks),
            "tasks_pending": len(pending_tasks),
            "tasks_in_progress": len(in_progress_tasks),
            "completion_rate_pct": completion_rate,
            "agent_activity": handoffs_by_agent,
        },
        "completed_tasks": [
            {"title": t["title"], "priority": t.get("priority", "Média")}
            for t in completed_tasks[:20]  # limita para não estourar o contexto LLM
        ],
        "focus_sessions": [
            {
                "task": s.get("task_title", "?"),
                "minutes": s.get("actual_minutes", 0),
                "status": s.get("status"),
                "date": (s.get("started_at") or "")[:10],
            }
            for s in sessions[:30]
        ],
    }


# ---------------------------------------------------------------------------
# Geração do relatório via LLM
# ---------------------------------------------------------------------------


def generate_report(data: dict) -> str:
    """Gera o relatório markdown via GPT-4o-mini."""
    data_str = json.dumps(data, ensure_ascii=False, indent=2, default=str)

    try:
        response = chat_completions(
            messages=[
                {"role": "system", "content": _get_retrospective_prompt()},
                {
                    "role": "user",
                    "content": f"Dados da semana:\n\n{data_str}\n\nGere a retrospectiva.",
                },
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        notifier.error(f"Erro ao gerar relatório: {e}", AGENT_NAME)
        m = data["metrics"]
        return f"""# Retrospectiva {data["period"]["start"]} → {data["period"]["end"]}

## Métricas
- Foco total: {m["total_focus_hours"]}h ({m["total_focus_minutes"]} min)
- Sessões concluídas: {m["sessions_completed"]}
- Sessões abandonadas: {m["sessions_abandoned"]}
- Tarefas concluídas: {m["tasks_completed"]}
- Taxa de conclusão: {m["completion_rate_pct"]}%

*(Relatório gerado sem LLM — erro: {e})*"""


# ---------------------------------------------------------------------------
# Criação de página no Notion
# ---------------------------------------------------------------------------


def _markdown_to_notion_blocks(text: str) -> list[dict]:
    """Converte markdown simples em blocos Notion."""
    blocks = []
    for line in text.split("\n"):
        line_stripped = line.strip()
        if not line_stripped:
            blocks.append(
                {"object": "block", "type": "paragraph", "paragraph": {"rich_text": []}}
            )
        elif line_stripped.startswith("# "):
            blocks.append(
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": [
                            {"type": "text", "text": {"content": line_stripped[2:]}}
                        ]
                    },
                }
            )
        elif line_stripped.startswith("## "):
            blocks.append(
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [
                            {"type": "text", "text": {"content": line_stripped[3:]}}
                        ]
                    },
                }
            )
        elif line_stripped.startswith("### "):
            blocks.append(
                {
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {
                        "rich_text": [
                            {"type": "text", "text": {"content": line_stripped[4:]}}
                        ]
                    },
                }
            )
        elif line_stripped.startswith("- ") or line_stripped.startswith("* "):
            blocks.append(
                {
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {
                        "rich_text": [
                            {"type": "text", "text": {"content": line_stripped[2:]}}
                        ]
                    },
                }
            )
        elif line_stripped.startswith("**") and line_stripped.endswith("**"):
            blocks.append(
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": line_stripped.strip("*")},
                                "annotations": {"bold": True},
                            }
                        ]
                    },
                }
            )
        else:
            # Paragraph — strip inline markdown markers simply
            clean = line_stripped.replace("**", "").replace("*", "").replace("`", "")
            blocks.append(
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": clean}}]
                    },
                }
            )
    return blocks[:100]  # Notion limita children por request


def create_notion_retrospective_page(title: str, content_md: str) -> Optional[str]:
    """Cria uma página de retrospectiva no Notion. Retorna o page_id ou None."""
    if not NOTION_RETROSPECTIVE_PAGE_ID:
        notifier.warning(
            "NOTION_RETROSPECTIVE_PAGE_ID não configurado — página não criada.",
            AGENT_NAME,
        )
        return None

    blocks = _markdown_to_notion_blocks(content_md)
    payload = {
        "parent": {"page_id": NOTION_RETROSPECTIVE_PAGE_ID},
        "properties": {"title": {"title": [{"text": {"content": title}}]}},
        "children": blocks,
    }

    try:
        result = _notion_sync._request("POST", "pages", data=payload)
        page_id = result["id"]
        notifier.success(
            f"Retrospectiva criada no Notion: {page_id[:8]}...", AGENT_NAME
        )
        return page_id
    except Exception as e:
        notifier.error(f"Erro ao criar página no Notion: {e}", AGENT_NAME)
        return None


# ---------------------------------------------------------------------------
# Salva relatório localmente
# ---------------------------------------------------------------------------


def save_report_locally(title: str, content: str) -> str:
    """Salva o relatório como .md na pasta reports/."""
    from pathlib import Path
    from config import BASE_DIR

    reports_dir = Path(BASE_DIR) / "reports"
    reports_dir.mkdir(exist_ok=True)

    filename = f"{title.replace(' ', '_').replace('/', '-')}.md"
    filepath = reports_dir / filename
    filepath.write_text(content, encoding="utf-8")
    notifier.success(f"Relatório salvo em: {filepath}", AGENT_NAME)
    return str(filepath)


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------


def run_retrospective(push_to_notion: bool = True) -> dict:
    """
    Executa o pipeline completo de retrospectiva.
    Retorna dict com métricas, relatório e localização do arquivo.
    """
    notifier.separator("RETROSPECTIVA SEMANAL")
    notifier.info("Coletando dados da semana...", AGENT_NAME)

    data = collect_week_data()
    m = data["metrics"]

    # Exibe métricas no terminal
    notifier.info(
        f"Foco: {m['total_focus_hours']}h | Sessões: {m['sessions_completed']} concluídas "
        f"| Tarefas: {m['tasks_completed']} concluídas ({m['completion_rate_pct']}%)",
        AGENT_NAME,
    )

    notifier.info("Gerando relatório via LLM...", AGENT_NAME)
    report_md = generate_report(data)

    period = data["period"]
    title = f"Retrospectiva {period['start']} → {period['end']}"

    # Salva localmente sempre
    local_path = save_report_locally(title, report_md)

    # Envia ao Notion se solicitado
    notion_page_id = None
    if push_to_notion:
        notion_page_id = create_notion_retrospective_page(title, report_md)

    result = {
        "title": title,
        "period": period,
        "metrics": m,
        "local_path": local_path,
        "notion_page_id": notion_page_id,
        "report_preview": report_md[:500] + "..."
        if len(report_md) > 500
        else report_md,
    }

    notifier.separator()
    return result


# ---------------------------------------------------------------------------
# Handoff entry point
# ---------------------------------------------------------------------------


def handle_handoff(payload: dict) -> dict:
    action = payload.get("action", "")
    notifier.agent_event(f"Recebendo handoff: action='{action}'", AGENT_NAME)
    handoff_id = memory.log_handoff("orchestrator", AGENT_NAME, action, payload)

    try:
        result: dict = {}

        if action == "run":
            push = payload.get("push_to_notion", True)
            result = run_retrospective(push_to_notion=push)

        elif action == "metrics_only":
            data = collect_week_data()
            result = data["metrics"]

        else:
            raise ValueError(f"Ação desconhecida: '{action}'")

        memory.update_handoff_result(handoff_id, result, "success")
        return {"status": "success", "result": result}

    except Exception as exc:
        error_msg = str(exc)
        notifier.error(f"Erro no handoff '{action}': {error_msg}", AGENT_NAME)
        memory.update_handoff_result(handoff_id, {"error": error_msg}, "error")
        return {"status": "error", "result": {"error": error_msg}}
````

## File: agents/scheduler.py
````python
# =============================================================================
# agents/scheduler.py — Agente de gerenciamento de horários e blocos de tempo
# =============================================================================
# Responsável por:
#   - Criar e gerenciar blocos de agenda no dia
#   - Priorizar tarefas por urgência/horário
#   - Sugerir reorganizações de agenda via LLM
#   - Sincronizar com o Notion Sync Agent

import json
import os
import sys
from datetime import date, datetime, time, timedelta
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import memory, notifier, sanity_client
from core.openai_utils import chat_completions

AGENT_NAME = "scheduler"

# Prompt de sistema para o LLM do Scheduler
_SYSTEM_PROMPT_FALLBACK = """Você é o Scheduler Agent de um sistema de gestão pessoal.
Sua função é gerenciar blocos de tempo e priorizar tarefas.

Ao receber uma lista de tarefas, você deve:
1. Ordenar por prioridade (Alta > Média > Baixa) e urgência de horário
2. Sugerir blocos de tempo realistas (mínimo 25 minutos por tarefa)
3. Incluir pausas entre blocos longos (≥90 min → sugerir pausa de 15 min)
4. Alertar sobre conflitos de horário ou agenda sobrecarregada
5. Respeitar os horários já agendados

Responda sempre em JSON estruturado com o campo "schedule" (lista de blocos)
e "warnings" (lista de avisos). Exemplo de bloco:
{
  "time_slot": "09:00-10:00",
  "task_title": "Revisar PRs",
  "priority": "Alta",
  "notes": "Começar pelo PR #42"
}
"""


def _get_system_prompt() -> str:
    return sanity_client.get_prompt("scheduler", "scheduling", _SYSTEM_PROMPT_FALLBACK)


# ---------------------------------------------------------------------------
# Lógica de agendamento local (sem LLM)
# ---------------------------------------------------------------------------


def get_today_schedule() -> list[dict]:
    """Retorna o cronograma de hoje do banco local, ordenado por horário."""
    return memory.get_today_agenda()


def _parse_slot_range(
    block_date: str, time_slot: str
) -> Optional[tuple[datetime, datetime]]:
    if "-" not in time_slot:
        return None
    try:
        start_str, end_str = [part.strip() for part in time_slot.split("-", 1)]
        start_dt = datetime.strptime(f"{block_date} {start_str}", "%Y-%m-%d %H:%M")
        end_dt = datetime.strptime(f"{block_date} {end_str}", "%Y-%m-%d %H:%M")
        if end_dt <= start_dt:
            return None
        return start_dt, end_dt
    except ValueError:
        return None


def _format_slot(start_dt: datetime, duration_minutes: int) -> str:
    end_dt = start_dt + timedelta(minutes=duration_minutes)
    return f"{start_dt.strftime('%H:%M')}-{end_dt.strftime('%H:%M')}"


def _round_up_to_quarter(dt: datetime) -> datetime:
    base = dt.replace(second=0, microsecond=0)
    remainder = base.minute % 15
    if remainder == 0 and base.second == 0 and base.microsecond == 0:
        return base
    return base + timedelta(minutes=(15 - remainder))


def _find_same_task_future_block(
    blocks: list[dict],
    task_id: Optional[int],
    task_title: str,
    start_after: datetime,
    exclude_block_id: int,
) -> Optional[dict]:
    normalized_title = task_title.strip().lower()
    for block in blocks:
        if (
            block.get("id") == exclude_block_id
            or block.get("completed")
            or block.get("rescheduled")
        ):
            continue
        block_range = _parse_slot_range(
            block.get("block_date", date.today().isoformat()),
            block.get("time_slot", ""),
        )
        if not block_range:
            continue
        block_start, _ = block_range
        if block_start < start_after:
            continue
        same_task_id = task_id is not None and str(block.get("task_id")) == str(task_id)
        same_title = (block.get("task_title") or "").strip().lower() == normalized_title
        if same_task_id or same_title:
            return block
    return None


def _find_available_start(
    block_date: str,
    duration_minutes: int,
    blocks: list[dict],
    start_after: datetime,
    exclude_block_ids: set[int],
) -> datetime:
    day_start = datetime.combine(
        datetime.strptime(block_date, "%Y-%m-%d").date(), time(9, 0)
    )
    candidate = max(_round_up_to_quarter(start_after), day_start)

    intervals = []
    for block in blocks:
        if block.get("id") in exclude_block_ids:
            continue
        block_range = _parse_slot_range(
            block.get("block_date", block_date), block.get("time_slot", "")
        )
        if not block_range:
            continue
        start_dt, end_dt = block_range
        intervals.append((start_dt, end_dt))

    intervals.sort(key=lambda item: item[0])

    for start_dt, end_dt in intervals:
        if end_dt <= candidate:
            continue
        if candidate + timedelta(minutes=duration_minutes) <= start_dt:
            return candidate
        if candidate < end_dt:
            candidate = _round_up_to_quarter(end_dt)

    return candidate


def find_next_available_slot(
    duration_minutes: int,
    start_after: Optional[datetime] = None,
    max_days_ahead: int = 3,
) -> tuple[str, str]:
    reference = start_after or datetime.now()

    for offset in range(max_days_ahead + 1):
        target_date = (reference.date() + timedelta(days=offset)).isoformat()
        day_start = (
            reference
            if offset == 0
            else datetime.combine(reference.date() + timedelta(days=offset), time(9, 0))
        )
        blocks = memory.get_agenda_for_date(target_date)
        start_dt = _find_available_start(
            target_date,
            duration_minutes,
            blocks,
            day_start,
            exclude_block_ids=set(),
        )
        if start_dt.date().isoformat() == target_date:
            return target_date, _format_slot(start_dt, duration_minutes)

    fallback_date = reference.date().isoformat()
    return fallback_date, _format_slot(
        _round_up_to_quarter(reference), duration_minutes
    )


def add_schedule_block(
    time_slot: str,
    task_title: str,
    task_id: Optional[int] = None,
    block_date: Optional[str] = None,
) -> int:
    """
    Adiciona um bloco de agenda no banco local.

    Args:
        time_slot:   Ex: "09:00-10:00"
        task_title:  Nome da tarefa
        task_id:     ID local da tarefa (opcional)
        block_date:  Data no formato YYYY-MM-DD (padrão: hoje)

    Returns:
        ID do bloco criado.
    """
    target_date = block_date or date.today().isoformat()
    block_id = memory.create_agenda_block(
        block_date=target_date,
        time_slot=time_slot,
        task_title=task_title,
        task_id=task_id,
    )
    notifier.success(
        f"Bloco adicionado: {target_date} {time_slot} → '{task_title}'", AGENT_NAME
    )
    return block_id


def complete_block(block_id: int) -> None:
    """Marca um bloco de agenda como concluído."""
    memory.mark_block_completed(block_id, True)
    notifier.success(f"Bloco {block_id} marcado como concluído.", AGENT_NAME)


def auto_reschedule_block(
    block_id: int,
    reason: str = "Bloco atrasado detectado pelo Focus Guard.",
    reference_time: Optional[datetime] = None,
    max_reschedules: int = 3,
) -> dict:
    block = memory.get_block(block_id)
    if not block:
        return {"status": "missing", "reason": "Bloco não encontrado."}
    if block.get("completed"):
        return {"status": "skipped", "reason": "Bloco já concluído."}
    if block.get("rescheduled"):
        return {"status": "skipped", "reason": "Bloco já foi reagendado."}
    if int(block.get("reschedule_count") or 0) >= max_reschedules:
        return {"status": "skipped", "reason": "Limite de reagendamentos atingido."}

    block_date = block.get("block_date") or date.today().isoformat()
    block_range = _parse_slot_range(block_date, block.get("time_slot", ""))
    if not block_range:
        return {"status": "skipped", "reason": "Time slot inválido."}

    start_dt, end_dt = block_range
    _params = sanity_client.get_agent_parameters(AGENT_NAME)
    _min_block = int(_params.get("minimum_block_minutes") or 25)
    duration_minutes = max(int((end_dt - start_dt).total_seconds() / 60), _min_block)
    now_dt = reference_time or datetime.now()
    same_day_blocks = memory.get_agenda_for_date(block_date)

    existing = _find_same_task_future_block(
        same_day_blocks,
        block.get("task_id"),
        block.get("task_title", ""),
        start_after=now_dt,
        exclude_block_id=block_id,
    )
    if existing:
        memory.update_block(
            block_id,
            rescheduled=True,
            rescheduled_to_block_id=existing["id"],
        )
        return {
            "status": "linked",
            "original_block_id": block_id,
            "rescheduled_to_block_id": existing["id"],
            "new_time_slot": existing.get("time_slot"),
            "new_block_date": existing.get("block_date"),
            "reason": "Já existia um bloco futuro para esta tarefa.",
        }

    target_date, new_time_slot = find_next_available_slot(
        duration_minutes,
        start_after=max(now_dt, end_dt),
    )
    new_block_id = memory.create_agenda_block(
        block_date=target_date,
        time_slot=new_time_slot,
        task_title=block.get("task_title", "Sem título"),
        task_id=block.get("task_id"),
        notion_page_id=block.get("notion_page_id"),
        source_block_id=block.get("source_block_id") or block_id,
        created_by="auto_reschedule",
        reschedule_count=int(block.get("reschedule_count") or 0) + 1,
    )
    memory.update_block(
        block_id,
        rescheduled=True,
        rescheduled_to_block_id=new_block_id,
    )

    notifier.warning(
        f"Bloco {block_id} reagendado automaticamente para {target_date} {new_time_slot}.",
        AGENT_NAME,
    )
    return {
        "status": "created",
        "original_block_id": block_id,
        "rescheduled_to_block_id": new_block_id,
        "old_time_slot": block.get("time_slot"),
        "new_time_slot": new_time_slot,
        "new_block_date": target_date,
        "duration_minutes": duration_minutes,
        "reason": reason,
    }


def get_prioritized_tasks() -> list[dict]:
    """
    Retorna tarefas pendentes/em progresso ordenadas por:
    1. Prioridade (Alta > Média > Baixa)
    2. Horário agendado (mais cedo primeiro)
    """
    priority_order = {"Alta": 0, "Média": 1, "Baixa": 2}

    pending = memory.get_tasks_by_status("A fazer")
    in_progress = memory.get_tasks_by_status("Em progresso")
    all_tasks = in_progress + pending

    def sort_key(t: dict):
        p = priority_order.get(t.get("priority", "Média"), 1)
        sched = t.get("scheduled_time") or "99:99"
        return (p, sched)

    return sorted(all_tasks, key=sort_key)


def detect_schedule_conflicts() -> list[str]:
    """
    Detecta conflitos básicos na agenda de hoje:
    - Blocos com mesmo horário de início
    - Tarefas sem bloco associado (órfãs)
    """
    blocks = get_today_schedule()
    conflicts = []

    # Checar duplicidade de time_slot
    seen_slots: dict[str, list] = {}
    for b in blocks:
        slot = b.get("time_slot", "")
        start = slot.split("-")[0].strip() if "-" in slot else slot
        seen_slots.setdefault(start, []).append(b.get("task_title", "?"))

    for start_time, tasks in seen_slots.items():
        if len(tasks) > 1:
            conflicts.append(f"Conflito em {start_time}: {', '.join(tasks)}")

    return conflicts


def calculate_schedule_load(blocks: Optional[list] = None) -> dict:
    """
    Calcula a carga total da agenda:
    - Total de blocos
    - Minutos agendados
    - Percentual de conclusão
    """
    if blocks is None:
        blocks = get_today_schedule()

    total = len(blocks)
    done = sum(1 for b in blocks if b.get("completed"))

    # Calcula minutos agendados somando duração dos blocos
    total_minutes = 0
    for b in blocks:
        slot = b.get("time_slot", "")
        if "-" in slot:
            try:
                parts = slot.split("-")
                start = datetime.strptime(parts[0].strip(), "%H:%M")
                end = datetime.strptime(parts[1].strip(), "%H:%M")
                total_minutes += int((end - start).total_seconds() / 60)
            except ValueError:
                pass

    pct = round((done / total) * 100) if total > 0 else 0

    return {
        "total_blocks": total,
        "completed_blocks": done,
        "pending_blocks": total - done,
        "total_minutes": total_minutes,
        "completion_percent": pct,
    }


# ---------------------------------------------------------------------------
# Sugestão de agenda via LLM
# ---------------------------------------------------------------------------


def suggest_agenda_with_llm(
    tasks: Optional[list[dict]] = None,
    context: str = "",
) -> dict:
    """
    Usa o GPT-4o para sugerir uma agenda otimizada para o dia.

    Args:
        tasks:    Lista de tarefas (pega as pendentes se None)
        context:  Contexto adicional (ex: "só tenho 3h disponíveis hoje")

    Returns:
        Dict com "schedule" (lista de blocos sugeridos) e "warnings".
    """
    if tasks is None:
        tasks = get_prioritized_tasks()

    if not tasks:
        return {"schedule": [], "warnings": ["Nenhuma tarefa pendente encontrada."]}

    # Formata tarefas para o prompt
    tasks_str = json.dumps(
        [
            {
                "title": t.get("title"),
                "priority": t.get("priority"),
                "scheduled_time": t.get("scheduled_time", ""),
                "status": t.get("status"),
            }
            for t in tasks
        ],
        ensure_ascii=False,
        indent=2,
    )

    current_time = datetime.now().strftime("%H:%M")
    user_message = f"""
Hora atual: {current_time}
Data: {date.today().isoformat()}

Tarefas a agendar:
{tasks_str}

{f"Contexto adicional: {context}" if context else ""}

Por favor, crie uma agenda otimizada para hoje. Retorne JSON puro (sem markdown).
"""

    try:
        response = chat_completions(
            messages=[
                {"role": "system", "content": _get_system_prompt()},
                {"role": "user", "content": user_message},
            ],
            temperature=0.3,
            response_format={"type": "json_object"},
        )
        result = json.loads(response.choices[0].message.content)
        notifier.success("Agenda sugerida pelo LLM gerada com sucesso.", AGENT_NAME)
        return result
    except Exception as e:
        notifier.error(f"Erro ao gerar sugestão de agenda: {e}", AGENT_NAME)
        return {"schedule": [], "warnings": [str(e)]}


def apply_llm_suggestion(suggestion: dict, auto_sync_notion: bool = False) -> list[int]:
    """
    Aplica a sugestão de agenda do LLM ao banco local.
    Retorna lista de IDs de blocos criados.
    """
    created_ids = []
    schedule = suggestion.get("schedule", [])

    for block in schedule:
        time_slot = block.get("time_slot", "")
        task_title = block.get("task_title", "")
        if not time_slot or not task_title:
            continue

        # Tenta encontrar tarefa local correspondente pelo título
        all_tasks = memory.list_all_tasks()
        matched_task = next(
            (t for t in all_tasks if t["title"].lower() == task_title.lower()), None
        )
        task_id = matched_task["id"] if matched_task else None

        block_id = add_schedule_block(
            time_slot=time_slot,
            task_title=task_title,
            task_id=task_id,
        )
        created_ids.append(block_id)

    warnings = suggestion.get("warnings", [])
    for w in warnings:
        notifier.warning(w, AGENT_NAME)

    notifier.success(f"{len(created_ids)} bloco(s) de agenda criados.", AGENT_NAME)
    return created_ids


# ---------------------------------------------------------------------------
# Handoff entry point — chamado pelo Orchestrator
# ---------------------------------------------------------------------------


def handle_handoff(payload: dict) -> dict:
    """
    Ponto de entrada para handoffs do Orchestrator.
    Retorna dict com 'status' e 'result'.
    """
    action = payload.get("action", "")
    notifier.agent_event(f"Recebendo handoff: action='{action}'", AGENT_NAME)

    handoff_id = memory.log_handoff("orchestrator", AGENT_NAME, action, payload)

    try:
        result: dict = {}

        if action == "get_today_schedule":
            blocks = get_today_schedule()
            load = calculate_schedule_load(blocks)
            conflicts = detect_schedule_conflicts()
            result = {
                "blocks": blocks,
                "load": load,
                "conflicts": conflicts,
            }

        elif action == "add_block":
            block_id = add_schedule_block(
                time_slot=payload["time_slot"],
                task_title=payload["task_title"],
                task_id=payload.get("task_id"),
                block_date=payload.get("block_date"),
            )
            result = {"block_id": block_id, "message": "Bloco adicionado."}

        elif action == "complete_block":
            complete_block(payload["block_id"])
            result = {"message": "Bloco marcado como concluído."}

        elif action == "suggest_agenda":
            suggestion = suggest_agenda_with_llm(context=payload.get("context", ""))
            if payload.get("apply", False):
                ids = apply_llm_suggestion(suggestion)
                result = {"suggestion": suggestion, "applied_blocks": ids}
            else:
                result = {"suggestion": suggestion}

        elif action == "get_prioritized_tasks":
            tasks = get_prioritized_tasks()
            result = {"tasks": tasks, "count": len(tasks)}

        elif action == "auto_reschedule_block":
            result = auto_reschedule_block(
                block_id=payload["block_id"],
                reason=payload.get(
                    "reason", "Bloco atrasado detectado automaticamente."
                ),
            )

        else:
            raise ValueError(f"Ação desconhecida: '{action}'")

        memory.update_handoff_result(handoff_id, result, "success")
        return {"status": "success", "result": result}

    except Exception as exc:
        error_msg = str(exc)
        notifier.error(f"Erro no handoff '{action}': {error_msg}", AGENT_NAME)
        memory.update_handoff_result(handoff_id, {"error": error_msg}, "error")
        return {"status": "error", "result": {"error": error_msg}}
````

## File: agents/validator.py
````python
# =============================================================================
# agents/validator.py — Agente de validação cruzada entre agentes
# =============================================================================
# Responsável por:
#   - Confirmar se uma tarefa foi REALMENTE concluída (não apenas marcada)
#   - Cruzar dados do banco local com o Notion
#   - Pedir confirmação ao usuário quando necessário
#   - Emitir veredicto final (validated / rejected / pending_confirmation)
#
# Este agente atua como "auditor" — é chamado antes de marcar definitivamente
# uma tarefa como concluída.

import json
import os
import sys
from datetime import datetime
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import notion_sync as _notion_sync
from core import memory, notifier, sanity_client
from core.openai_utils import chat_completions

AGENT_NAME = "validator"

# Prompt do Validator para análise de conclusão via LLM
_VALIDATOR_PROMPT_FALLBACK = """Você é o Validator Agent de um sistema de gestão pessoal.
Sua função é determinar se uma tarefa foi genuinamente concluída.

Avalie os dados fornecidos e retorne um veredicto em JSON:
{
  "verdict": "validated" | "rejected" | "pending_confirmation",
  "confidence": 0.0 a 1.0,
  "reasons": ["motivo 1", "motivo 2"],
  "questions": ["pergunta para o usuário se precisar de confirmação"],
  "recommendation": "ação recomendada"
}

Critérios para "validated":
  - Tarefa marcada como concluída no banco local E no Notion
  - Horário real de conclusão registrado
  - Sessão de foco correspondente encerrada como 'completed'
  - Conteúdo da tarefa compatível com o esperado

Critérios para "rejected":
  - Marcada como concluída mas sem horário real
  - Dados inconsistentes entre local e Notion
  - Sessão de foco abandonada ou nunca iniciada

Critérios para "pending_confirmation":
  - Dados parcialmente consistentes — precisa de confirmação do usuário
  - Tarefa marcada manualmente sem sessão de foco associada
"""


def _get_validator_prompt() -> str:
    return sanity_client.get_prompt(
        "validator", "validation", _VALIDATOR_PROMPT_FALLBACK
    )


# ---------------------------------------------------------------------------
# Coleta de evidências de conclusão
# ---------------------------------------------------------------------------


def gather_evidence(task_id: int) -> dict:
    """
    Coleta todas as evidências disponíveis sobre conclusão de uma tarefa.
    Cruza dados do banco local, sessões de foco e estado do Notion.
    """
    task = memory.get_task(task_id)
    if not task:
        return {"error": f"Tarefa {task_id} não encontrada no banco local."}

    focus_sessions = memory.get_focus_sessions_for_task(task_id)
    agenda_blocks = memory.get_agenda_blocks_for_task(task_id)

    # Informações do Notion (se disponível)
    notion_data = None
    if task.get("notion_page_id"):
        try:
            notion_tasks = _notion_sync.fetch_notion_tasks()
            notion_data = next(
                (
                    nt
                    for nt in notion_tasks
                    if nt["notion_page_id"] == task["notion_page_id"]
                ),
                None,
            )
        except Exception as e:
            notion_data = {"error": str(e)}

    return {
        "task": task,
        "focus_sessions": focus_sessions,
        "agenda_blocks": agenda_blocks,
        "notion_data": notion_data,
        "evidence_collected_at": datetime.now().isoformat(),
    }


def check_data_consistency(evidence: dict) -> dict:
    """
    Verifica consistência dos dados sem LLM.
    Retorna flags de consistência.
    """
    task = evidence.get("task", {})
    sessions = evidence.get("focus_sessions", [])
    blocks = evidence.get("agenda_blocks", [])
    notion = evidence.get("notion_data")

    flags = {
        "local_status_is_done": task.get("status") == "Concluído",
        "has_actual_time": bool(task.get("actual_time")),
        "has_completed_session": any(s.get("status") == "completed" for s in sessions),
        "has_any_session": len(sessions) > 0,
        "block_completed": any(b.get("completed") for b in blocks),
        "notion_synced": notion is not None and "error" not in str(notion),
        "notion_status_matches": (
            notion is not None and notion.get("status") == task.get("status")
            if notion and "error" not in str(notion)
            else None
        ),
    }

    # Score de consistência (0-100)
    score = 0
    if flags["local_status_is_done"]:
        score += 30
    if flags["has_actual_time"]:
        score += 20
    if flags["has_completed_session"]:
        score += 25
    if flags["block_completed"]:
        score += 15
    if flags["notion_status_matches"]:
        score += 10

    flags["consistency_score"] = score
    return flags


# ---------------------------------------------------------------------------
# Validação via LLM
# ---------------------------------------------------------------------------


def validate_with_llm(evidence: dict, flags: dict) -> dict:
    """
    Usa o GPT-4o-mini para analisar as evidências e emitir veredicto.
    """
    data = {
        "task": evidence.get("task"),
        "consistency_flags": flags,
        "sessions_summary": [
            {
                "status": s.get("status"),
                "planned_minutes": s.get("planned_minutes"),
                "actual_minutes": s.get("actual_minutes"),
            }
            for s in evidence.get("focus_sessions", [])
        ],
        "agenda_blocks_summary": [
            {"time_slot": b.get("time_slot"), "completed": b.get("completed")}
            for b in evidence.get("agenda_blocks", [])
        ],
        "notion_data": evidence.get("notion_data"),
    }

    prompt = f"""Evidências coletadas sobre a tarefa:
{json.dumps(data, ensure_ascii=False, indent=2, default=str)}

Emita seu veredicto em JSON puro (sem markdown).
"""

    try:
        response = chat_completions(
            messages=[
                {"role": "system", "content": _get_validator_prompt()},
                {"role": "user", "content": prompt},
            ],
            temperature=0.1,  # Baixa temperatura: queremos análise determinística
            response_format={"type": "json_object"},
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        notifier.error(f"Erro no LLM do Validator: {e}", AGENT_NAME)
        # Fallback baseado nos flags
        score = flags.get("consistency_score", 0)
        if score >= 70:
            return {
                "verdict": "validated",
                "confidence": score / 100,
                "reasons": ["Dados consistentes entre local, sessões e agenda."],
                "questions": [],
                "recommendation": "Tarefa pode ser confirmada como concluída.",
            }
        elif score >= 40:
            return {
                "verdict": "pending_confirmation",
                "confidence": score / 100,
                "reasons": ["Dados parcialmente consistentes."],
                "questions": ["Você confirma que a tarefa foi realmente concluída?"],
                "recommendation": "Solicite confirmação ao usuário.",
            }
        else:
            return {
                "verdict": "rejected",
                "confidence": (100 - score) / 100,
                "reasons": [
                    "Dados insuficientes ou inconsistentes para validar conclusão."
                ],
                "questions": [],
                "recommendation": "Verifique se a tarefa foi realmente concluída antes de marcá-la.",
            }


# ---------------------------------------------------------------------------
# Ação após validação
# ---------------------------------------------------------------------------


def apply_verdict(task_id: int, verdict: dict) -> dict:
    """
    Aplica o veredicto do Validator:
    - 'validated':              Confirma status no banco e Notion
    - 'rejected':               Reverte status para 'Em progresso'
    - 'pending_confirmation':   Aguarda input do usuário
    """
    v = verdict.get("verdict", "pending_confirmation")
    task = memory.get_task(task_id)

    if v == "validated":
        # Confirma como concluído com timestamp
        actual_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        memory.update_task_status(task_id, "Concluído", actual_time)

        # Atualiza Notion se vinculado
        if task and task.get("notion_page_id"):
            try:
                _notion_sync.update_notion_task_status(
                    task["notion_page_id"], "Concluído", actual_time
                )
            except Exception as e:
                notifier.warning(f"Não foi possível atualizar Notion: {e}", AGENT_NAME)

        notifier.success(
            f"✅ Tarefa '{task.get('title', task_id)}' VALIDADA como concluída!",
            AGENT_NAME,
        )

    elif v == "rejected":
        memory.update_task_status(task_id, "Em progresso")
        notifier.warning(
            f"❌ Tarefa '{task.get('title', task_id)}' REJEITADA — revertida para 'Em progresso'.",
            AGENT_NAME,
        )

    else:  # pending_confirmation
        questions = verdict.get("questions", [])
        notifier.warning(
            f"⏳ Tarefa '{task.get('title', task_id)}' aguarda CONFIRMAÇÃO.", AGENT_NAME
        )
        if questions:
            notifier.info("Perguntas para confirmação:", AGENT_NAME)
            for q in questions:
                notifier.info(f"  → {q}", AGENT_NAME)

    return {"applied": True, "verdict": v, "task_id": task_id}


def validate_task(task_id: int, force_confirm: bool = False) -> dict:
    """
    Pipeline completo de validação de uma tarefa.

    Args:
        task_id:       ID local da tarefa
        force_confirm: Se True, aceita pending_confirmation como validated

    Returns:
        Dict com evidence, flags, verdict, e resultado da aplicação.
    """
    notifier.agent_event(f"Iniciando validação da tarefa {task_id}...", AGENT_NAME)

    evidence = gather_evidence(task_id)
    if "error" in evidence:
        return {"status": "error", "message": evidence["error"]}

    flags = check_data_consistency(evidence)
    notifier.info(
        f"Score de consistência: {flags.get('consistency_score', 0)}/100", AGENT_NAME
    )

    verdict = validate_with_llm(evidence, flags)
    notifier.info(
        f"Veredicto LLM: {verdict.get('verdict')} "
        f"(confiança: {verdict.get('confidence', 0):.0%})",
        AGENT_NAME,
    )

    # Se force_confirm e pending → trata como validated
    if force_confirm and verdict.get("verdict") == "pending_confirmation":
        verdict["verdict"] = "validated"
        verdict["reasons"].append("Confirmação forçada pelo usuário.")

    applied = apply_verdict(task_id, verdict)

    return {
        "task_id": task_id,
        "evidence_summary": {
            "local_status": evidence["task"].get("status"),
            "sessions_count": len(evidence.get("focus_sessions", [])),
            "blocks_count": len(evidence.get("agenda_blocks", [])),
        },
        "flags": flags,
        "verdict": verdict,
        "applied": applied,
    }


def validate_all_completed() -> list[dict]:
    """Valida todas as tarefas marcadas como 'Concluído' no banco local."""
    completed = memory.get_tasks_by_status("Concluído")
    results = []
    for task in completed:
        result = validate_task(task["id"])
        results.append(result)
    notifier.success(f"{len(results)} tarefa(s) validada(s).", AGENT_NAME)
    return results


# ---------------------------------------------------------------------------
# Handoff entry point — chamado pelo Orchestrator
# ---------------------------------------------------------------------------


def handle_handoff(payload: dict) -> dict:
    """
    Ponto de entrada para handoffs do Orchestrator.
    """
    action = payload.get("action", "")
    notifier.agent_event(f"Recebendo handoff: action='{action}'", AGENT_NAME)

    handoff_id = memory.log_handoff("orchestrator", AGENT_NAME, action, payload)

    try:
        result: dict = {}

        if action == "validate_task":
            validation = validate_task(
                task_id=payload["task_id"],
                force_confirm=payload.get("force_confirm", False),
            )
            result = validation

        elif action == "validate_all":
            validations = validate_all_completed()
            result = {
                "validations": validations,
                "total": len(validations),
                "validated": sum(
                    1
                    for v in validations
                    if v.get("verdict", {}).get("verdict") == "validated"
                ),
            }

        elif action == "get_evidence":
            evidence = gather_evidence(payload["task_id"])
            flags = check_data_consistency(evidence)
            result = {"evidence": evidence, "flags": flags}

        else:
            raise ValueError(f"Ação desconhecida: '{action}'")

        memory.update_handoff_result(handoff_id, result, "success")
        return {"status": "success", "result": result}

    except Exception as exc:
        error_msg = str(exc)
        notifier.error(f"Erro no handoff '{action}': {error_msg}", AGENT_NAME)
        memory.update_handoff_result(handoff_id, {"error": error_msg}, "error")
        return {"status": "error", "result": {"error": error_msg}}
````

## File: config/alert_thresholds.yml
````yaml
version: 1
description: Alert thresholds for external ecosystem monitoring

github:
  no_activity_hours_active_repo: 72
  issue_backlog_warn_count: 20

railway:
  service_down_minutes: 5
  deployment_failure_consecutive: 2

vercel:
  deployment_failure_consecutive: 2
  no_deploy_days_warn: 28

cloudflare:
  http_5xx_warn_count: 5
  http_5xx_fail_count: 20

onchain:
  neoflw_price_drop_pct: 15
  neoflw_liquidity_usd_min: 1000
  neoflw_volume_24h_usd_min: 500

reporting:
  push_only_for_severity:
    - fail
    - critical
  daily_report_default_delivery: pull
````

## File: config/ecosystem.yml
````yaml
version: 1
description: External ecosystem monitor configuration

runtime:
  report_mode: pull_first
  health_check_interval_minutes: 30
  daily_report_hour_local: "20:00"
  redis_signal_ttl_hours: 24

github:
  enabled: true
  orgs:
    - NEO-PROTOCOL
    - NEO-FlowOFF
    - flowpay-system
    - neo-smart-factory
    - FluxxDAO
    - wodxpro
  repos_per_org_limit: 15
  commit_window_hours: 24
  staleness_threshold_hours: 72

railway:
  enabled: true
  environments:
    - production

vercel:
  enabled: false
  projects: []

cloudflare:
  enabled: false
  zones: []

onchain:
  enabled: true
  assets:
    - name: NEOFLW
      provider: dexscreener
      chain: base
      contract: "0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B"

publish:
  allow_public_artifacts: false
  require_human_review: true
````

## File: core/__init__.py
````python
# core/__init__.py
# Pacote de infraestrutura do sistema.
# Use importações diretas nos módulos:
#   from core import memory
#   from core import notifier

__all__ = ["memory", "notifier"]
````

## File: core/memory.py
````python
# =============================================================================
# core/memory.py — Estado compartilhado entre agentes via Redis
# =============================================================================
# Substitui o SQLite por Redis para persistência durável no Railway.
# Mantém a mesma API pública — nenhum outro módulo precisa mudar.
#
# Estrutura de chaves Redis:
#   task:{id}                  HASH com todos os campos da tarefa
#   tasks:all                  ZSET  scored por created_at (unix ts)
#   tasks:notion:{notion_id}   STRING → task_id
#   tasks:next_id              COUNTER
#
#   block:{id}                 HASH
#   blocks:date:{YYYY-MM-DD}   ZSET scored por minutos do time_slot
#   blocks:next_id             COUNTER
#
#   session:{id}               HASH
#   sessions:all               ZSET scored por started_at
#   session:active             STRING → session_id (se houver sessão ativa)
#   sessions:next_id           COUNTER
#
#   handoff:{id}               HASH
#   handoffs:all               ZSET scored por created_at
#   handoffs:next_id           COUNTER
#
#   state:{key}                STRING (JSON)
#
#   alert:{id}                 HASH
#   alerts:pending             ZSET scored por created_at
#   alerts:all                 ZSET scored por created_at
#   alerts:next_id             COUNTER
#
#   audit:{id}                 HASH
#   audit:events               ZSET scored por created_at
#   audit:next_id              COUNTER

import json
import subprocess
import sys
import threading
import time
from datetime import date, datetime, timedelta, timezone
from typing import Any, Optional

import redis as redis_lib

from config import REDIS_URL

# ---------------------------------------------------------------------------
# Conexão singleton (lazy) com auto-start de redis-server local
# ---------------------------------------------------------------------------

_redis_client: Optional[redis_lib.Redis] = None
_lock = threading.Lock()

# Só tenta auto-start no macOS com URL local (nunca em container Railway/Docker)
_IS_LOCAL = any(h in REDIS_URL for h in ("localhost", "127.0.0.1"))
_IS_MACOS = sys.platform == "darwin"
_CAN_AUTOSTART = _IS_LOCAL and _IS_MACOS


def _start_local_redis() -> None:
    """Tenta iniciar redis-server local via brew (somente macOS)."""
    try:
        subprocess.Popen(
            ["redis-server", "--daemonize", "yes", "--loglevel", "warning"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        time.sleep(0.8)
    except FileNotFoundError:
        raise RuntimeError(
            "Redis não encontrado. Instale com:\n"
            "  brew install redis\n"
            "Ou suba via Docker:\n"
            "  make redis-up"
        )


def _r() -> redis_lib.Redis:
    global _redis_client
    if _redis_client is None:
        client = redis_lib.from_url(
            REDIS_URL, decode_responses=True, socket_connect_timeout=2
        )
        try:
            client.ping()
            print(f"[Memory] Redis conectado: {REDIS_URL}")
        except (
            redis_lib.exceptions.ConnectionError,
            redis_lib.exceptions.TimeoutError,
        ):
            if _CAN_AUTOSTART:
                print("[Memory] Redis offline — tentando iniciar redis-server local...")
                _start_local_redis()
                client = redis_lib.from_url(REDIS_URL, decode_responses=True)
                client.ping()  # levanta exceção se ainda falhar
            else:
                raise redis_lib.exceptions.ConnectionError(
                    f"Não foi possível conectar ao Redis ({REDIS_URL}). "
                    "Verifique se REDIS_URL está configurado corretamente no Railway."
                )
        _redis_client = client
    return _redis_client


# ---------------------------------------------------------------------------
# Helpers internos
# ---------------------------------------------------------------------------


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def _ts(dt_str: Optional[str] = None) -> float:
    """Converte string ISO para unix timestamp (score do ZSET)."""
    if dt_str is None:
        return datetime.now(timezone.utc).timestamp()
    try:
        return datetime.fromisoformat(dt_str).timestamp()
    except Exception:
        return datetime.now(timezone.utc).timestamp()


def _ts_from_timeslot(time_slot: str) -> float:
    """'09:00-10:00' → 540.0  (minutos desde meia-noite, para sort)."""
    try:
        t = time_slot.split("-")[0].strip()
        h, m = t.split(":")
        return float(int(h) * 60 + int(m))
    except Exception:
        return 0.0


def _next_id(counter_key: str) -> int:
    return _r().incr(counter_key)


def _to_dict(data: dict, int_fields: list[str] | None = None) -> dict:
    """Limpa strings vazias e converte campos numéricos."""
    result = {}
    for k, v in data.items():
        result[k] = v if v != "" else None
    if int_fields:
        for f in int_fields:
            if result.get(f) is not None:
                try:
                    result[f] = int(result[f])
                except (ValueError, TypeError):
                    pass
    return result


# =============================================================================
# INIT
# =============================================================================


def init_db() -> None:
    """Verifica conexão Redis. Substitui o init_db() do SQLite."""
    try:
        _r()
    except Exception as e:
        print(
            f"[Memory] AVISO: Redis indisponível ({e}). Tentativas serão feitas sob demanda."
        )
        # Não levanta exceção — o app sobe; falha nas operações reais se Redis não estiver acessível


def get_redis() -> redis_lib.Redis:
    """Retorna o cliente Redis bruto para operações nativas específicas."""
    return _r()


# =============================================================================
# TASKS
# =============================================================================


def create_task(
    title: str,
    priority: str = "Média",
    scheduled_time: Optional[str] = None,
    notes: Optional[str] = None,
    notion_page_id: Optional[str] = None,
) -> int:
    with _lock:
        task_id = _next_id("tasks:next_id")
        now = _now()
        data = {
            "id": str(task_id),
            "title": title,
            "priority": priority,
            "status": "A fazer",
            "scheduled_time": scheduled_time or "",
            "actual_time": "",
            "notes": notes or "",
            "notion_page_id": notion_page_id or "",
            "created_at": now,
            "updated_at": now,
        }
        r = _r()
        r.hset(f"task:{task_id}", mapping=data)
        r.zadd("tasks:all", {str(task_id): _ts(now)})
        if notion_page_id:
            r.set(f"tasks:notion:{notion_page_id}", task_id)
        return task_id


def update_task_status(
    task_id: int, status: str, actual_time: Optional[str] = None
) -> None:
    r = _r()
    key = f"task:{task_id}"
    r.hset(key, "status", status)
    r.hset(key, "updated_at", _now())
    if actual_time:
        r.hset(key, "actual_time", actual_time)


def update_task(task_id: int, **fields: Any) -> None:
    """Atualiza campos arbitrários de uma tarefa existente."""
    r = _r()
    mapping = {}
    notion_page_id = None
    old_notion_page_id = None
    task_key = f"task:{task_id}"

    if "notion_page_id" in fields:
        old_notion_page_id = r.hget(task_key, "notion_page_id")

    for key, value in fields.items():
        if key == "id":
            continue
        if key == "notion_page_id":
            notion_page_id = value
        if value is None:
            mapping[key] = ""
        else:
            mapping[key] = str(value)

    if not mapping:
        return

    mapping["updated_at"] = _now()
    r.hset(task_key, mapping=mapping)
    if "notion_page_id" in fields and old_notion_page_id:
        if old_notion_page_id != mapping.get("notion_page_id", ""):
            r.delete(f"tasks:notion:{old_notion_page_id}")
    if notion_page_id:
        r.set(f"tasks:notion:{notion_page_id}", task_id)
    elif "notion_page_id" in fields and old_notion_page_id:
        r.delete(f"tasks:notion:{old_notion_page_id}")


def get_task(task_id: int) -> Optional[dict]:
    data = _r().hgetall(f"task:{task_id}")
    if not data:
        return None
    data["id"] = int(task_id)
    return _to_dict(data, int_fields=["id"])


def get_tasks_by_status(status: str) -> list[dict]:
    r = _r()
    task_ids = r.zrange("tasks:all", 0, -1)
    tasks = []
    for tid in task_ids:
        data = r.hgetall(f"task:{tid}")
        if data and data.get("status") == status:
            data["id"] = int(tid)
            tasks.append(_to_dict(data, int_fields=["id"]))
    tasks.sort(key=lambda t: t.get("scheduled_time") or "")
    return tasks


def get_today_tasks() -> list[dict]:
    today = date.today().isoformat()
    return [
        t for t in list_all_tasks() if (t.get("scheduled_time") or "").startswith(today)
    ]


def list_all_tasks() -> list[dict]:
    r = _r()
    task_ids = r.zrevrange("tasks:all", 0, -1)  # mais recentes primeiro
    tasks = []
    for tid in task_ids:
        data = r.hgetall(f"task:{tid}")
        if data:
            data["id"] = int(tid)
            tasks.append(_to_dict(data, int_fields=["id"]))
    return tasks


def update_task_notion_id(task_id: int, notion_page_id: str) -> None:
    r = _r()
    r.hset(f"task:{task_id}", "notion_page_id", notion_page_id)
    r.hset(f"task:{task_id}", "updated_at", _now())
    r.set(f"tasks:notion:{notion_page_id}", task_id)


def delete_task(task_id: int) -> None:
    """Remove uma tarefa do Redis (hash + índices tasks:all e tasks:notion)."""
    with _lock:
        r = _r()
        task_key = f"task:{task_id}"
        notion_page_id = r.hget(task_key, "notion_page_id")
        r.delete(task_key)
        r.zrem("tasks:all", str(task_id))
        if notion_page_id:
            r.delete(f"tasks:notion:{notion_page_id}")


# =============================================================================
# AGENDA BLOCKS
# =============================================================================


def create_agenda_block(
    block_date: str,
    time_slot: str,
    task_title: str,
    task_id: Optional[int] = None,
    notion_page_id: Optional[str] = None,
    source_block_id: Optional[int] = None,
    created_by: str = "manual",
    reschedule_count: int = 0,
) -> int:
    with _lock:
        block_id = _next_id("blocks:next_id")
        now = _now()
        data = {
            "id": str(block_id),
            "block_date": block_date,
            "time_slot": time_slot,
            "task_id": str(task_id) if task_id is not None else "",
            "task_title": task_title,
            "notion_page_id": notion_page_id or "",
            "completed": "0",
            "rescheduled": "0",
            "rescheduled_to_block_id": "",
            "source_block_id": str(source_block_id)
            if source_block_id is not None
            else "",
            "created_by": created_by,
            "reschedule_count": str(reschedule_count),
            "created_at": now,
            "updated_at": now,
        }
        r = _r()
        r.hset(f"block:{block_id}", mapping=data)
        r.zadd(
            f"blocks:date:{block_date}", {str(block_id): _ts_from_timeslot(time_slot)}
        )
        if task_id is not None:
            r.zadd(
                f"blocks:task:{task_id}", {str(block_id): _ts_from_timeslot(time_slot)}
            )
        if notion_page_id:
            r.set(f"blocks:notion:{notion_page_id}", block_id)
        return block_id


def get_today_agenda(include_rescheduled: bool = False) -> list[dict]:
    return get_agenda_for_date(
        date.today().isoformat(), include_rescheduled=include_rescheduled
    )


def get_agenda_for_date(
    block_date: str, include_rescheduled: bool = False
) -> list[dict]:
    r = _r()
    block_ids = r.zrange(f"blocks:date:{block_date}", 0, -1)
    blocks = []
    for bid in block_ids:
        data = r.hgetall(f"block:{bid}")
        if data:
            if not include_rescheduled and data.get("rescheduled", "0") == "1":
                continue
            data["id"] = int(bid)
            blocks.append(
                _to_dict(
                    data,
                    int_fields=[
                        "id",
                        "task_id",
                        "completed",
                        "rescheduled",
                        "rescheduled_to_block_id",
                        "source_block_id",
                        "reschedule_count",
                    ],
                )
            )
    return blocks


def list_agenda_between(
    start_date: str,
    end_date: str,
    include_rescheduled: bool = False,
) -> list[dict]:
    try:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        return []

    if end_dt < start_dt:
        start_dt, end_dt = end_dt, start_dt

    blocks = []
    cursor = start_dt
    while cursor <= end_dt:
        blocks.extend(
            get_agenda_for_date(
                cursor.isoformat(), include_rescheduled=include_rescheduled
            )
        )
        cursor += timedelta(days=1)
    return blocks


def get_block(block_id: int) -> Optional[dict]:
    data = _r().hgetall(f"block:{block_id}")
    if not data:
        return None
    data["id"] = int(block_id)
    return _to_dict(
        data,
        int_fields=[
            "id",
            "task_id",
            "completed",
            "rescheduled",
            "rescheduled_to_block_id",
            "source_block_id",
            "reschedule_count",
        ],
    )


def update_block(block_id: int, **fields: Any) -> None:
    r = _r()
    mapping = {}
    for key, value in fields.items():
        if value is None:
            mapping[key] = ""
        elif isinstance(value, bool):
            mapping[key] = "1" if value else "0"
        else:
            mapping[key] = str(value)
    mapping["updated_at"] = _now()
    r.hset(f"block:{block_id}", mapping=mapping)


def mark_block_completed(block_id: int, completed: bool = True) -> None:
    update_block(block_id, completed=completed)


# =============================================================================
# FOCUS SESSIONS
# =============================================================================


def start_focus_session(
    task_id: int, task_title: str, planned_minutes: int = 25
) -> int:
    with _lock:
        session_id = _next_id("sessions:next_id")
        now = _now()
        data = {
            "id": str(session_id),
            "task_id": str(task_id),
            "task_title": task_title,
            "started_at": now,
            "ended_at": "",
            "planned_minutes": str(planned_minutes),
            "actual_minutes": "",
            "status": "active",
            "notes": "",
        }
        r = _r()
        r.hset(f"session:{session_id}", mapping=data)
        r.zadd("sessions:all", {str(session_id): _ts(now)})
        r.zadd(f"sessions:task:{task_id}", {str(session_id): _ts(now)})
        r.set("session:active", session_id)
        return session_id


def end_focus_session(
    session_id: int, status: str = "completed", notes: Optional[str] = None
) -> None:
    r = _r()
    now = _now()
    session = r.hgetall(f"session:{session_id}")

    actual_minutes = ""
    if session.get("started_at"):
        try:
            started = datetime.fromisoformat(session["started_at"])
            ended = datetime.fromisoformat(now)
            actual_minutes = str(int((ended - started).total_seconds() / 60))
        except Exception:
            pass

    r.hset(
        f"session:{session_id}",
        mapping={
            "ended_at": now,
            "status": status,
            "actual_minutes": actual_minutes,
            "notes": notes or session.get("notes", ""),
        },
    )

    active = r.get("session:active")
    if active and int(active) == session_id:
        r.delete("session:active")


def get_active_focus_session() -> Optional[dict]:
    r = _r()
    active_id = r.get("session:active")
    if not active_id:
        return None
    data = r.hgetall(f"session:{active_id}")
    if data and data.get("status") == "active":
        data["id"] = int(active_id)
        return _to_dict(data, int_fields=["id"])
    # Sessão expirou ou foi finalizada; limpa ponteiro
    r.delete("session:active")
    return None


def get_focus_sessions_for_task(task_id: int) -> list[dict]:
    """Retorna todas as sessões de foco associadas a uma tarefa específica."""
    r = _r()
    session_ids = r.zrange(f"sessions:task:{task_id}", 0, -1)
    sessions = []
    for sid in session_ids:
        data = r.hgetall(f"session:{sid}")
        if data:
            data["id"] = int(sid)
            sessions.append(_to_dict(data, int_fields=["id"]))
    return sessions


def get_agenda_blocks_for_task(task_id: int) -> list[dict]:
    """Retorna todos os blocos de agenda associados a uma tarefa específica."""
    r = _r()
    block_ids = r.zrange(f"blocks:task:{task_id}", 0, -1)
    blocks = []
    for bid in block_ids:
        data = r.hgetall(f"block:{bid}")
        if data:
            data["id"] = int(bid)
            blocks.append(
                _to_dict(
                    data,
                    int_fields=[
                        "id",
                        "task_id",
                        "completed",
                        "rescheduled",
                        "rescheduled_to_block_id",
                        "source_block_id",
                        "reschedule_count",
                    ],
                )
            )
    return blocks


def get_agenda_blocks_for_tasks(task_ids: list[int]) -> dict[int, list[dict]]:
    """Retorna blocos por tarefa em lote para reduzir round-trips ao Redis."""
    if not task_ids:
        return {}

    r = _r()
    pipe = r.pipeline()
    for task_id in task_ids:
        pipe.zrange(f"blocks:task:{task_id}", 0, -1)
    block_id_lists = pipe.execute()

    seen = set()
    unique_block_ids = []
    for block_ids in block_id_lists:
        for bid in block_ids:
            if bid not in seen:
                seen.add(bid)
                unique_block_ids.append(bid)

    block_data_map = {}
    if unique_block_ids:
        pipe = r.pipeline()
        for bid in unique_block_ids:
            pipe.hgetall(f"block:{bid}")
        raw_blocks = pipe.execute()
        for bid, data in zip(unique_block_ids, raw_blocks):
            if not data:
                continue
            data["id"] = int(bid)
            block_data_map[bid] = _to_dict(
                data,
                int_fields=[
                    "id",
                    "task_id",
                    "completed",
                    "rescheduled",
                    "rescheduled_to_block_id",
                    "source_block_id",
                    "reschedule_count",
                ],
            )

    blocks_by_task: dict[int, list[dict]] = {}
    for task_id, block_ids in zip(task_ids, block_id_lists):
        blocks_by_task[task_id] = [
            block_data_map[bid] for bid in block_ids if bid in block_data_map
        ]
    return blocks_by_task


# =============================================================================
# AGENT HANDOFFS (auditoria)
# =============================================================================


def log_handoff(
    source_agent: str,
    target_agent: str,
    action: str,
    payload: Any = None,
    result: Any = None,
    status: str = "pending",
) -> int:
    with _lock:
        handoff_id = _next_id("handoffs:next_id")
        now = _now()
        data = {
            "id": str(handoff_id),
            "source_agent": source_agent,
            "target_agent": target_agent,
            "action": action,
            "payload": json.dumps(payload) if payload is not None else "",
            "result": json.dumps(result) if result is not None else "",
            "status": status,
            "created_at": now,
        }
        r = _r()
        r.hset(f"handoff:{handoff_id}", mapping=data)
        r.zadd("handoffs:all", {str(handoff_id): _ts(now)})
        return handoff_id


def update_handoff_result(
    handoff_id: int, result: Any, status: str = "success"
) -> None:
    _r().hset(
        f"handoff:{handoff_id}",
        mapping={
            "result": json.dumps(result),
            "status": status,
        },
    )


# =============================================================================
# SYSTEM STATE (chave-valor)
# =============================================================================


def set_state(key: str, value: Any) -> None:
    _r().set(f"state:{key}", json.dumps(value))


def get_state(key: str, default: Any = None) -> Any:
    val = _r().get(f"state:{key}")
    if val is None:
        return default
    try:
        return json.loads(val)
    except Exception:
        return val


# =============================================================================
# ALERTS
# =============================================================================


def create_alert(alert_type: str, message: str) -> int:
    with _lock:
        alert_id = _next_id("alerts:next_id")
        now = _now()
        data = {
            "id": str(alert_id),
            "alert_type": alert_type,
            "message": message,
            "acknowledged": "0",
            "created_at": now,
        }
        r = _r()
        r.hset(f"alert:{alert_id}", mapping=data)
        r.zadd("alerts:pending", {str(alert_id): _ts(now)})
        r.zadd("alerts:all", {str(alert_id): _ts(now)})
        return alert_id


def get_pending_alerts() -> list[dict]:
    r = _r()
    alert_ids = r.zrevrange("alerts:pending", 0, -1)
    alerts = []
    for aid in alert_ids:
        data = r.hgetall(f"alert:{aid}")
        if data and data.get("acknowledged", "0") == "0":
            data["id"] = int(aid)
            alerts.append(_to_dict(data, int_fields=["id", "acknowledged"]))
    return alerts


def list_alerts(limit: int = 50, include_acknowledged: bool = True) -> list[dict]:
    r = _r()
    alert_ids = r.zrevrange("alerts:all", 0, max(limit - 1, 0))
    alerts = []
    for aid in alert_ids:
        data = r.hgetall(f"alert:{aid}")
        if not data:
            continue
        if not include_acknowledged and data.get("acknowledged", "0") != "0":
            continue
        data["id"] = int(aid)
        alerts.append(_to_dict(data, int_fields=["id", "acknowledged"]))
    return alerts


def acknowledge_alert(alert_id: int) -> None:
    r = _r()
    r.hset(f"alert:{alert_id}", "acknowledged", "1")
    r.zrem("alerts:pending", str(alert_id))


# =============================================================================
# AUDIT EVENTS
# =============================================================================


def create_audit_event(
    event_type: str,
    title: str,
    details: str = "",
    level: str = "info",
    agent: str = "system",
    payload: Any = None,
    related_id: Optional[str] = None,
) -> int:
    with _lock:
        event_id = _next_id("audit:next_id")
        now = _now()
        data = {
            "id": str(event_id),
            "event_type": event_type,
            "title": title,
            "details": details,
            "level": level,
            "agent": agent,
            "payload": json.dumps(payload, ensure_ascii=False)
            if payload is not None
            else "",
            "related_id": related_id or "",
            "created_at": now,
        }
        r = _r()
        r.hset(f"audit:{event_id}", mapping=data)
        r.zadd("audit:events", {str(event_id): _ts(now)})
        return event_id


def list_audit_events(limit: int = 50, event_type: Optional[str] = None) -> list[dict]:
    r = _r()
    event_ids = r.zrevrange("audit:events", 0, max(limit - 1, 0))
    events = []
    for eid in event_ids:
        data = r.hgetall(f"audit:{eid}")
        if not data:
            continue
        if event_type and data.get("event_type") != event_type:
            continue
        data["id"] = int(eid)
        events.append(_to_dict(data, int_fields=["id"]))
    return events


# =============================================================================
# RETROSPECTIVE QUERIES
# =============================================================================


def get_sessions_since(since_iso: str) -> list[dict]:
    r = _r()
    since_ts = _ts(since_iso)
    session_ids = r.zrangebyscore("sessions:all", since_ts, "+inf")
    sessions = []
    for sid in session_ids:
        data = r.hgetall(f"session:{sid}")
        if data:
            data["id"] = int(sid)
            sessions.append(_to_dict(data, int_fields=["id"]))
    return sessions


def get_completed_tasks_since(since_iso: str) -> list[dict]:
    return [
        t
        for t in list_all_tasks()
        if t.get("status") == "Concluído" and (t.get("updated_at") or "") >= since_iso
    ]


def get_handoffs_since(since_iso: str) -> list[dict]:
    r = _r()
    since_ts = _ts(since_iso)
    handoff_ids = r.zrangebyscore("handoffs:all", since_ts, "+inf")
    handoffs = []
    for hid in handoff_ids:
        data = r.hgetall(f"handoff:{hid}")
        if data:
            data["id"] = int(hid)
            handoffs.append(_to_dict(data, int_fields=["id"]))
    return handoffs


def list_recent_handoffs(limit: int = 50) -> list[dict]:
    r = _r()
    handoff_ids = r.zrevrange("handoffs:all", 0, max(limit - 1, 0))
    handoffs = []
    for hid in handoff_ids:
        data = r.hgetall(f"handoff:{hid}")
        if data:
            data["id"] = int(hid)
            handoffs.append(_to_dict(data, int_fields=["id"]))
    return handoffs
````

## File: core/notifier.py
````python
# =============================================================================
# core/notifier.py — Sistema de notificações e alertas
# =============================================================================
# Exibe mensagens coloridas no terminal e persiste tudo em arquivo de log.
# Os agentes chamam as funções deste módulo para comunicar eventos.


import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from enum import Enum

from config import LOG_FILE, LOG_LEVEL


# ---------------------------------------------------------------------------
# Cores ANSI para terminal (Linux/macOS; desative no Windows antigo)
# ---------------------------------------------------------------------------
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    GRAY = "\033[90m"


_IS_RAILWAY = bool(
    os.getenv("RAILWAY_ENVIRONMENT")
    or os.getenv("RAILWAY_PROJECT_ID")
    or os.getenv("RAILWAY_SERVICE_ID")
)
_FORCE_COLOR = os.getenv("FORCE_COLOR", "").lower() in {"1", "true", "yes"}
_NO_COLOR = os.getenv("NO_COLOR") is not None
_USE_COLOR = _FORCE_COLOR or (
    sys.stdout.isatty() and not _NO_COLOR and not _IS_RAILWAY
)


# ---------------------------------------------------------------------------
# Configuração do logger Python padrão
# ---------------------------------------------------------------------------


def _setup_logger() -> logging.Logger:
    log_path = Path(LOG_FILE)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("multiagentes")
    if logger.handlers:
        return logger  # Evita duplicar handlers em reimportações

    logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

    # Handler de arquivo (sem cores)
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    )

    logger.addHandler(file_handler)
    logger.propagate = False
    return logger


_logger = _setup_logger()


# ---------------------------------------------------------------------------
# Tipos de notificação
# ---------------------------------------------------------------------------
class NotifLevel(str, Enum):
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FOCUS = "FOCUS"  # Alertas do Focus Guard
    AGENT = "AGENT"  # Comunicação entre agentes


# Mapeamento nível → cor + ícone
_LEVEL_STYLE: dict[NotifLevel, tuple[str, str]] = {
    NotifLevel.INFO: (Color.CYAN, "ℹ"),
    NotifLevel.SUCCESS: (Color.GREEN, "✓"),
    NotifLevel.WARNING: (Color.YELLOW, "⚠"),
    NotifLevel.ERROR: (Color.RED, "✗"),
    NotifLevel.FOCUS: (Color.MAGENTA, "🎯"),
    NotifLevel.AGENT: (Color.BLUE, "🤖"),
}

_LEVEL_PLAIN_ICON: dict[NotifLevel, str] = {
    NotifLevel.INFO: "i",
    NotifLevel.SUCCESS: "ok",
    NotifLevel.WARNING: "warn",
    NotifLevel.ERROR: "err",
    NotifLevel.FOCUS: "focus",
    NotifLevel.AGENT: "agent",
}


# ---------------------------------------------------------------------------
# Função principal de notificação
# ---------------------------------------------------------------------------
def notify(
    message: str,
    level: NotifLevel = NotifLevel.INFO,
    agent: str = "system",
    also_log: bool = True,
) -> None:
    """
    Exibe uma notificação colorida no terminal e (opcionalmente) grava no log.

    Args:
        message:   Texto da mensagem.
        level:     Nível/tipo da notificação.
        agent:     Nome do agente que está notificando.
        also_log:  Se True, grava também no arquivo de log.
    """
    color, icon = _LEVEL_STYLE.get(level, (Color.WHITE, "•"))
    timestamp = datetime.now().strftime("%H:%M:%S")

    if _USE_COLOR:
        terminal_line = (
            f"{Color.GRAY}[{timestamp}]{Color.RESET} "
            f"{color}{Color.BOLD}{icon} [{level.value}]{Color.RESET} "
            f"{Color.GRAY}({agent}){Color.RESET} "
            f"{color}{message}{Color.RESET}"
        )
    else:
        plain_icon = _LEVEL_PLAIN_ICON.get(level, "log")
        terminal_line = f"[{timestamp}] [{plain_icon.upper()}] ({agent}) {message}"

    # Imprime diretamente (sem o logging.StreamHandler duplicar)
    print(terminal_line, flush=True)

    # Grava no arquivo de log (sem cores)
    if also_log:
        log_line = f"[{level.value}] ({agent}) {message}"
        if level == NotifLevel.ERROR:
            _logger.error(log_line)
        elif level == NotifLevel.WARNING:
            _logger.warning(log_line)
        else:
            _logger.info(log_line)


# ---------------------------------------------------------------------------
# Atalhos para cada nível
# ---------------------------------------------------------------------------
def info(message: str, agent: str = "system") -> None:
    notify(message, NotifLevel.INFO, agent)


def success(message: str, agent: str = "system") -> None:
    notify(message, NotifLevel.SUCCESS, agent)


def warning(message: str, agent: str = "system") -> None:
    notify(message, NotifLevel.WARNING, agent)


def error(message: str, agent: str = "system") -> None:
    notify(message, NotifLevel.ERROR, agent)


def focus_alert(message: str, agent: str = "focus_guard") -> None:
    notify(message, NotifLevel.FOCUS, agent)


def agent_event(message: str, agent: str = "orchestrator") -> None:
    notify(message, NotifLevel.AGENT, agent)


# ---------------------------------------------------------------------------
# Notificações nativas — macOS e Alexa
# ---------------------------------------------------------------------------
def mac_push(title: str, message: str, sound: bool = False) -> None:
    """Envia notificação nativa macOS via AppleScript."""
    import subprocess

    if sys.platform != "darwin":
        warning(
            "mac_push ignorado: notificações nativas só funcionam em macOS.",
            "notifier",
        )
        return

    sound_line = ' sound name "Sosumi"' if sound else ""
    script = f'display notification "{message}" with title "{title}"{sound_line}'
    try:
        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            timeout=5,
        )
        if result.returncode != 0:
            stderr = (result.stderr or b"").decode("utf-8", errors="ignore").strip()
            warning(
                f"mac_push falhou via osascript (code={result.returncode}): "
                f"{stderr or 'sem stderr'}",
                "notifier",
            )
    except Exception as exc:  # pylint: disable=broad-except
        warning(f"mac_push falhou: {exc}", "notifier")


def alexa_announce(message: str) -> None:
    """Dispara anúncio na Alexa exclusivamente via Voice Monkey."""
    import requests

    vm_token = os.getenv("VOICE_MONKEY_TOKEN", "")
    if vm_token:
        try:
            device = os.getenv("VOICE_MONKEY_DEVICE", "eco-room")
            response = requests.post(
                "https://api-v2.voicemonkey.io/announcement",
                headers=(
                    {"Authorization": f"Bearer {vm_token}"}
                    if not vm_token.startswith("Bearer")
                    else {"Authorization": vm_token}
                ),
                json={"device": device, "text": message},
                timeout=5,
            )
            if not response.ok:
                warning(
                    f"Voice Monkey falhou ({response.status_code}): "
                    f"{response.text[:160] or 'sem resposta'}",
                    "notifier",
                )
        except Exception as exc:  # pylint: disable=broad-except
            warning(f"Voice Monkey falhou: {exc}", "notifier")
        return

    warning(
        "Alexa indisponível: configure VOICE_MONKEY_TOKEN no ambiente.",
        "notifier",
    )


# ---------------------------------------------------------------------------
# Separadores visuais
# ---------------------------------------------------------------------------
def separator(title: str = "", char: str = "─", width: int = 70) -> None:
    """Imprime um separador visual no terminal."""
    if title:
        side = (width - len(title) - 2) // 2
        line = f"{char * side} {title} {char * (width - side - len(title) - 2)}"
    else:
        line = char * width
    if _USE_COLOR:
        print(f"{Color.GRAY}{line}{Color.RESET}", flush=True)
    else:
        print(line, flush=True)


def banner() -> None:
    """Exibe o banner de inicialização do sistema."""
    separator()
    print(f"{Color.CYAN}{Color.BOLD}")
    print("  ███╗   ██╗███████╗ ██████╗ ")
    print("  ████╗  ██║██╔════╝██╔═══██╗")
    print("  ██╔██╗ ██║█████╗  ██║   ██║")
    print("  ██║╚██╗██║██╔══╝  ██║   ██║")
    print("  ██║ ╚████║███████╗╚██████╔╝")
    print("  ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ")
    print(f"        {Color.WHITE}Sistema de Multiagentes — Gestão Pessoal{Color.RESET}")
    separator()
    print(
        f"{Color.GRAY}  Agentes: Orchestrator · Scheduler · Focus Guard · "
        f"Notion Sync · Validator{Color.RESET}"
    )
    separator()
    print()


# ---------------------------------------------------------------------------
# Exibição de tabela simples no terminal
# ---------------------------------------------------------------------------
def print_table(headers: list[str], rows: list[list[str]], title: str = "") -> None:
    """Imprime uma tabela formatada no terminal."""
    if title:
        separator(title)

    if not rows:
        print(f"  {Color.GRAY}(nenhum item){Color.RESET}")
        return

    # Calcula largura de cada coluna
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))

    # Linha de cabeçalho
    header_line = "  " + "  ".join(
        f"{Color.BOLD}{Color.WHITE}{h:<{col_widths[i]}}{Color.RESET}"
        for i, h in enumerate(headers)
    )
    print(header_line)
    print("  " + "  ".join("─" * w for w in col_widths))

    # Linhas de dados
    for row in rows:
        cells = []
        for i, cell in enumerate(row):
            w = col_widths[i] if i < len(col_widths) else 10
            cells.append(f"{str(cell):<{w}}")
        print("  " + "  ".join(cells))

    print()
````

## File: core/openai_utils.py
````python
# =============================================================================
# core/openai_utils.py — Helper OpenAI com fallback para modelo de contingência
# =============================================================================
# Cadeia de fallback:
#   1. OpenAI (OPENAI_MODEL, ex: gpt-4o-mini)
#   2. OpenAI fallback (OPENAI_FALLBACK_MODEL, ex: gpt-3.5-turbo)
#   3. Local — Docker Model Runner (Gemma3 4B-F16 em http://localhost:12434/v1)

from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OPENAI_FALLBACK_MODEL,
    LOCAL_MODEL_ENABLED,
    LOCAL_MODEL_BASE_URL,
    LOCAL_MODEL_NAME,
)
from core import notifier

# Cliente OpenAI cloud
_client = OpenAI(api_key=OPENAI_API_KEY)

# Cliente local (Docker Model Runner via Unix socket) — criado sob demanda
_local_client: OpenAI | None = None

_DOCKER_SOCKET = (
    "/Users/nettomello/Library/Containers/com.docker.docker/Data/inference.sock"
)


def _get_local_client() -> OpenAI:
    global _local_client
    if _local_client is None:
        try:
            import httpx

            transport = httpx.HTTPTransport(uds=_DOCKER_SOCKET)
            http_client = httpx.Client(transport=transport)
            _local_client = OpenAI(
                base_url="http://localhost/v1",
                api_key="local",
                http_client=http_client,
            )
        except Exception:
            # Fallback TCP caso o socket não exista (Railway, etc.)
            _local_client = OpenAI(base_url=LOCAL_MODEL_BASE_URL, api_key="local")
    return _local_client


def _apply_model(kwargs: dict, model: str) -> dict:
    payload = kwargs.copy()
    payload["model"] = model
    return payload


def chat_completions(**kwargs):
    """Executa chat.completions.create com cadeia de fallback:
    OpenAI primary → OpenAI fallback → Gemma3 local (Docker Model Runner).
    """
    primary = OPENAI_MODEL
    fallback = OPENAI_FALLBACK_MODEL

    # 1. Modelo principal (OpenAI cloud)
    try:
        return _client.chat.completions.create(**_apply_model(kwargs, primary))
    except Exception as primary_exc:
        notifier.warning(
            f"OpenAI '{primary}' falhou: {primary_exc}. Tentando fallback '{fallback}'...",
            "openai_utils",
        )

    # 2. Fallback OpenAI cloud
    if fallback and fallback != primary:
        try:
            return _client.chat.completions.create(**_apply_model(kwargs, fallback))
        except Exception as fallback_exc:
            notifier.warning(
                f"OpenAI fallback '{fallback}' falhou: {fallback_exc}.",
                "openai_utils",
            )

    # 3. Fallback local — Gemma3 via Docker Model Runner
    if LOCAL_MODEL_ENABLED:
        notifier.warning(
            f"Tentando modelo local '{LOCAL_MODEL_NAME}' via Docker Model Runner...",
            "openai_utils",
        )
        try:
            return _get_local_client().chat.completions.create(
                **_apply_model(kwargs, LOCAL_MODEL_NAME)
            )
        except Exception as local_exc:
            notifier.error(
                f"Modelo local '{LOCAL_MODEL_NAME}' também falhou: {local_exc}.",
                "openai_utils",
            )
            raise

    raise RuntimeError("Todos os modelos falharam e LOCAL_MODEL_ENABLED=false.")
````

## File: core/sanity_client.py
````python
"""
core/sanity_client.py — Cliente Sanity.io com cache em memória

Usa a Content API do Sanity para buscar prompts, personas e configs.
Cache de 5 minutos evita requests repetitivos.
Fallback para valores hardcoded se Sanity estiver indisponível ou não configurado.
"""

import os
import time
from typing import Any, Optional

import requests

SANITY_PROJECT_ID: str = os.getenv("SANITY_PROJECT_ID", "")
SANITY_DATASET: str = os.getenv("SANITY_DATASET", "production")
SANITY_API_TOKEN: str = os.getenv("SANITY_API_TOKEN", "")
SANITY_CDN: bool = os.getenv("SANITY_USE_CDN", "false").lower() == "true"

_CACHE: dict[str, tuple[Any, float]] = {}
CACHE_TTL = 300  # 5 minutos


# ---------------------------------------------------------------------------
# GROQ query
# ---------------------------------------------------------------------------


def _query(groq: str) -> Any:
    """Executa uma query GROQ na Content API do Sanity."""
    if not SANITY_PROJECT_ID:
        return None

    if groq in _CACHE:
        value, ts = _CACHE[groq]
        if time.time() - ts < CACHE_TTL:
            return value

    host = "apicdn.sanity.io" if SANITY_CDN else "api.sanity.io"
    url = f"https://{host}/v2021-10-21/data/query/{SANITY_DATASET}"
    headers = {}
    if SANITY_API_TOKEN:
        headers["Authorization"] = f"Bearer {SANITY_API_TOKEN}"

    try:
        resp = requests.get(
            url,
            params={"query": groq},
            headers=headers,
            timeout=5,
        )
        if resp.ok:
            result = resp.json().get("result")
            _CACHE[groq] = (result, time.time())
            return result
    except Exception:
        pass  # nunca quebra o sistema por Sanity indisponível

    return None


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------


def get_prompt(agent: str, prompt_type: str, fallback: str = "") -> str:
    """
    Busca system prompt de um agente no Sanity.
    Retorna fallback se Sanity não estiver configurado ou indisponível.

    Uso:
        prompt = sanity_client.get_prompt("focus_guard", "deviation", DEVIATION_PROMPT)
    """
    result = _query(
        f'*[_type == "llm_prompt" && agent == "{agent}" '
        f'&& prompt_type == "{prompt_type}" && active == true][0].system_prompt'
    )
    return result if result else fallback


# ---------------------------------------------------------------------------
# Personas
# ---------------------------------------------------------------------------


def get_persona(persona_id: str) -> Optional[dict]:
    """Busca uma persona completa pelo ID."""
    return _query(
        f'*[_type == "persona" && persona_id.current == "{persona_id}" && active == true][0]'
    )


def get_all_personas() -> list:
    """Lista todas as personas ativas."""
    return _query('*[_type == "persona" && active == true]') or []


# ---------------------------------------------------------------------------
# Configuração de agentes
# ---------------------------------------------------------------------------


def get_agent_config(agent_name: str) -> Optional[dict]:
    """Busca configuração de um agente (intervalo, enabled, parâmetros)."""
    return _query(f'*[_type == "agent_config" && agent_name == "{agent_name}"][0]')


def get_agent_parameters(agent_name: str) -> dict:
    """
    Retorna os parâmetros do agent_config como dict Python.
    O campo `parameters` é armazenado como JSON string no Sanity.
    Retorna {} se o agente não existir ou não tiver parâmetros.
    """
    import json as _json

    cfg = get_agent_config(agent_name)
    if not cfg:
        return {}
    raw = cfg.get("parameters") or ""
    if not raw:
        return {}
    try:
        return _json.loads(raw)
    except Exception:
        return {}


def is_agent_enabled(agent_name: str, default: bool = True) -> bool:
    """
    Retorna se um agente está habilitado no Sanity.
    Usa `default` se o Sanity não estiver configurado ou o agente não existir.
    """
    cfg = get_agent_config(agent_name)
    if cfg is None:
        return default
    return bool(cfg.get("enabled", default))


# ---------------------------------------------------------------------------
# Scripts de intervenção (Focus Guard / escalada)
# ---------------------------------------------------------------------------


def get_intervention_scripts(agent_name: Optional[str] = None) -> list:
    """
    Lista scripts de intervenção ordenados por trigger_minutes.
    Usado pelo Focus Guard para substituir o ESCALATION_LEVELS hardcoded.
    """
    agent_filter = f' && agent_name == "{agent_name}"' if agent_name else ""
    return (
        _query(
            f'*[_type == "intervention_script" && active == true{agent_filter}] | order(trigger_minutes asc)'
        )
        or []
    )


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------


def invalidate_cache() -> None:
    """Limpa o cache — chamar após editar conteúdo no Studio."""
    _CACHE.clear()


def is_configured() -> bool:
    """Retorna True se as variáveis mínimas do Sanity estão definidas."""
    return bool(SANITY_PROJECT_ID and SANITY_API_TOKEN)
````

## File: docs/arquitetura/SANITY_SCHEMA.md
````markdown
# SANITY.IO — Schema e Integração

> **HISTÓRICO — documento desatualizado.**
> Este arquivo registra o planejamento inicial dos 4 schemas originais (2026-03-30).
> O projeto evoluiu: hoje há 13 schemas deployed em `n4dgl02q/production`.
>
> Documentos atuais:
>
> - Schemas locais: `sanity/schemaTypes/` (13 tipos)
> - Governança: `../governanca/PLANO_SOBERANIA_SANITY.md`
> - Cobertura por agente: `../governanca/MATRIZ_GOVERNANCA_AGENTES.md`
> - Contratos: `../governanca/CONTRATO_AGENTES.md`

**Status:** HISTÓRICO — superado pela Fase 2 do Sanity (concluída em 2026-04-03, commit `679f390`)
**Projeto Sanity:** `n4dgl02q` (criado em sanity.io/manage)
**Dataset:** `production`
**Propósito:** externalizar prompts, personas e configs — sem redeploy para ajustes

### O que já está feito

- [x] Projeto Sanity criado (`n4dgl02q`)
- [x] API token configurado no `.env` (SANITY_API_TOKEN, SANITY_PROJECT_ID)
- [x] `core/sanity_client.py` — GROQ queries, cache 5min, fallback para hardcoded
- [x] `focus_guard.py` já consome prompt via `sanity_client.get_prompt()`
- [x] Sanity Studio scaffolding em `sanity/` (package.json, deps instaladas)

### O que falta

- [ ] Deploy dos 4 schemas abaixo no Sanity Studio
- [ ] Migrar prompts hardcoded para documentos no Studio (tabela no final)
- [ ] Endpoint `/admin/reload-config` para `invalidate_cache()`

---

## Por que Sanity aqui

O sistema hoje tem prompts hardcoded em cada agente:

- `ROUTING_PROMPT` em `orchestrator.py:108`
- `DEVIATION_PROMPT` em `focus_guard.py:42`
- `VALIDATOR_PROMPT` em `validator.py:28`
- Personas em `/personas/*.json`

Mudar qualquer um deles exige redeploy. Com Sanity:

- Editar no Studio → agente usa na próxima execução
- Histórico de versões built-in
- Rollback em 1 clique se o prompt degradou

---

## Schema a criar no Sanity Studio

### Document Type: `llm_prompt`

```javascript
// sanity/schemas/llm_prompt.js
export default {
  name: "llm_prompt",
  title: "LLM Prompt",
  type: "document",
  fields: [
    {
      name: "id",
      title: "ID único",
      type: "slug",
      options: { source: "name" },
      validation: (Rule) => Rule.required(),
    },
    {
      name: "name",
      title: "Nome",
      type: "string",
      validation: (Rule) => Rule.required(),
    },
    {
      name: "agent",
      title: "Agente",
      type: "string",
      options: {
        list: [
          "orchestrator",
          "focus_guard",
          "scheduler",
          "validator",
          "retrospective",
          "life_guard",
          "ecosystem_monitor",
        ],
      },
      validation: (Rule) => Rule.required(),
    },
    {
      name: "prompt_type",
      title: "Tipo",
      type: "string",
      options: {
        list: [
          "routing",
          "synthesis",
          "direct",
          "deviation",
          "validation",
          "retrospective",
        ],
      },
    },
    {
      name: "system_prompt",
      title: "System Prompt",
      type: "text",
      rows: 20,
      validation: (Rule) => Rule.required(),
    },
    {
      name: "temperature",
      title: "Temperatura",
      type: "number",
      validation: (Rule) => Rule.min(0).max(2),
    },
    {
      name: "active",
      title: "Ativo",
      type: "boolean",
      initialValue: true,
    },
    {
      name: "notes",
      title: "Notas / Changelog",
      type: "text",
      rows: 4,
    },
  ],
  preview: {
    select: { title: "name", subtitle: "agent" },
  },
};
```

### Document Type: `persona`

```javascript
// sanity/schemas/persona.js
export default {
  name: "persona",
  title: "Persona",
  type: "document",
  fields: [
    {
      name: "persona_id",
      title: "ID",
      type: "slug",
      options: { source: "name" },
    },
    {
      name: "name",
      title: "Nome",
      type: "string",
    },
    {
      name: "short_name",
      title: "Nome curto",
      type: "string",
    },
    {
      name: "description",
      title: "Descrição",
      type: "text",
      rows: 3,
    },
    {
      name: "tone",
      title: "Tom",
      type: "string",
      options: {
        list: [
          "warm",
          "professional",
          "direct",
          "casual",
          "technical",
          "strategic",
        ],
      },
    },
    {
      name: "system_prompt",
      title: "System Prompt base",
      type: "text",
      rows: 15,
    },
    {
      name: "temperature_routing",
      title: "Temperatura (roteamento)",
      type: "number",
    },
    {
      name: "temperature_synthesis",
      title: "Temperatura (síntese)",
      type: "number",
    },
    {
      name: "active",
      title: "Ativa",
      type: "boolean",
      initialValue: true,
    },
  ],
};
```

### Document Type: `agent_config`

```javascript
// sanity/schemas/agent_config.js
export default {
  name: "agent_config",
  title: "Configuração de Agente",
  type: "document",
  fields: [
    {
      name: "agent_name",
      title: "Agente",
      type: "string",
      options: {
        list: [
          "focus_guard",
          "scheduler",
          "life_guard",
          "ecosystem_monitor",
          "notion_sync",
        ],
      },
    },
    {
      name: "enabled",
      title: "Habilitado",
      type: "boolean",
      initialValue: true,
    },
    {
      name: "check_interval_minutes",
      title: "Intervalo de check (minutos)",
      type: "number",
    },
    {
      name: "parameters",
      title: "Parâmetros adicionais (JSON)",
      type: "text",
      rows: 8,
      description: "JSON com parâmetros específicos do agente",
    },
  ],
};
```

### Document Type: `intervention_script`

```javascript
// sanity/schemas/intervention_script.js
export default {
  name: "intervention_script",
  title: "Script de Intervenção",
  type: "document",
  description:
    "Mensagens que o sistema envia quando detecta hiperfoco prolongado",
  fields: [
    {
      name: "trigger_minutes",
      title: "Disparar após (minutos)",
      type: "number",
      description: "Minutos de sessão ativa para disparar",
    },
    {
      name: "channel",
      title: "Canal",
      type: "string",
      options: { list: ["mac", "alexa", "mac+alexa"] },
    },
    {
      name: "urgency",
      title: "Urgência",
      type: "string",
      options: { list: ["gentle", "firm", "loud"] },
    },
    {
      name: "title",
      title: "Título (Mac push)",
      type: "string",
    },
    {
      name: "message",
      title: "Mensagem",
      type: "text",
      rows: 3,
      description:
        "Use {task} para nome da tarefa, {minutes} para tempo decorrido",
    },
    {
      name: "active",
      title: "Ativo",
      type: "boolean",
      initialValue: true,
    },
  ],
  orderings: [
    {
      title: "Por tempo (crescente)",
      name: "triggerAsc",
      by: [{ field: "trigger_minutes", direction: "asc" }],
    },
  ],
};
```

---

## Client Python: `core/sanity_client.py`

```python
"""
core/sanity_client.py — Cliente Sanity.io com cache em memória

Usa a Content API do Sanity para buscar prompts, personas e configs.
Cache de 5 minutos evita requests repetitivos.
Fallback para valores hardcoded se Sanity estiver indisponível.
"""

import os
import json
import time
import requests
from typing import Any, Optional

SANITY_PROJECT_ID = os.getenv("SANITY_PROJECT_ID", "")
SANITY_DATASET    = os.getenv("SANITY_DATASET", "production")
SANITY_API_TOKEN  = os.getenv("SANITY_API_TOKEN", "")  # token com permissão read
SANITY_CDN        = os.getenv("SANITY_USE_CDN", "false").lower() == "true"

_CACHE: dict[str, tuple[Any, float]] = {}
CACHE_TTL = 300  # 5 minutos


def _query(groq: str) -> Any:
    """Executa uma query GROQ na Content API do Sanity."""
    if not SANITY_PROJECT_ID:
        return None

    cache_key = groq
    if cache_key in _CACHE:
        value, ts = _CACHE[cache_key]
        if time.time() - ts < CACHE_TTL:
            return value

    host = "apicdn.sanity.io" if SANITY_CDN else "api.sanity.io"
    url = f"https://{host}/v2021-10-21/data/query/{SANITY_DATASET}"
    headers = {}
    if SANITY_API_TOKEN:
        headers["Authorization"] = f"Bearer {SANITY_API_TOKEN}"

    try:
        resp = requests.get(
            url,
            params={"query": groq},
            headers=headers,
            timeout=5
        )
        if resp.ok:
            result = resp.json().get("result")
            _CACHE[cache_key] = (result, time.time())
            return result
    except Exception:
        pass  # nunca quebra o sistema por Sanity indisponível

    return None


def get_prompt(agent: str, prompt_type: str, fallback: str = "") -> str:
    """
    Busca system prompt de um agente no Sanity.
    Retorna fallback se Sanity não estiver configurado ou indisponível.

    Uso:
        prompt = sanity_client.get_prompt("focus_guard", "deviation", DEVIATION_PROMPT)
    """
    result = _query(
        f'*[_type == "llm_prompt" && agent == "{agent}" && prompt_type == "{prompt_type}" && active == true][0].system_prompt'
    )
    return result if result else fallback


def get_persona(persona_id: str) -> Optional[dict]:
    """Busca uma persona completa pelo ID."""
    result = _query(
        f'*[_type == "persona" && persona_id.current == "{persona_id}" && active == true][0]'
    )
    return result


def get_all_personas() -> list[dict]:
    """Lista todas as personas ativas."""
    result = _query('*[_type == "persona" && active == true]')
    return result or []


def get_agent_config(agent_name: str) -> Optional[dict]:
    """Busca configuração de um agente."""
    result = _query(
        f'*[_type == "agent_config" && agent_name == "{agent_name}"][0]'
    )
    return result


def get_intervention_scripts() -> list[dict]:
    """Lista scripts de intervenção ordenados por trigger_minutes."""
    result = _query(
        '*[_type == "intervention_script" && active == true] | order(trigger_minutes asc)'
    )
    return result or []


def invalidate_cache() -> None:
    """Limpa o cache — usar após editar no Studio."""
    _CACHE.clear()
```

---

## Como usar nos agentes (exemplo focus_guard)

```python
# agents/focus_guard.py
from core import sanity_client

# Antes (hardcoded):
DEVIATION_PROMPT = """Você é o Focus Guard..."""

# Depois (com Sanity + fallback):
DEVIATION_PROMPT = """Você é o Focus Guard..."""  # mantém como fallback

def _get_deviation_prompt() -> str:
    return sanity_client.get_prompt("focus_guard", "deviation", DEVIATION_PROMPT)

# Na chamada LLM:
# prompt = _get_deviation_prompt()
# openai_utils.chat_completions(prompt, ...)
```

---

## Variáveis de ambiente

```bash
SANITY_PROJECT_ID=          # ex: abc123de (encontrado em sanity.io/manage)
SANITY_DATASET=production
SANITY_API_TOKEN=            # sanity.io/manage → API → Tokens → Add API token (Read)
SANITY_USE_CDN=false         # true em produção, false em dev (para dados frescos)
```

---

## Setup no Sanity (passo a passo)

```
1. sanity.io/manage → New Project → "Blank project"
2. Nome: "neomello-agents"
3. Dataset: production (default)
4. Copiar Project ID

5. Instalar CLI:
   npm install -g @sanity/cli

6. No terminal (qualquer pasta):
   sanity init --project <PROJECT_ID> --dataset production

7. Substituir schemas/ pelos 4 schemas acima

8. sanity deploy (sobe o Studio para sanity.io/manage/<PROJECT_ID>/studio)

9. sanity.io/manage → API → Tokens → Add API Token
   - Label: multiagentes-read
   - Permission: Viewer
   - Copiar token

10. Adicionar no .env:
    SANITY_PROJECT_ID=<PROJECT_ID>
    SANITY_API_TOKEN=<TOKEN>
```

---

## Migração dos prompts existentes

Após o Studio estar no ar, criar os seguintes documentos:

| Agente        | Tipo          | Arquivo fonte                                  |
| ------------- | ------------- | ---------------------------------------------- |
| orchestrator  | routing       | `orchestrator.py:108` → `ROUTING_PROMPT`       |
| orchestrator  | synthesis     | `orchestrator.py` → `_SYNTHESIS_BASE`          |
| orchestrator  | direct        | `orchestrator.py` → `_DIRECT_BASE`             |
| focus_guard   | deviation     | `focus_guard.py:42` → `DEVIATION_PROMPT`       |
| validator     | validation    | `validator.py:28` → `VALIDATOR_PROMPT`         |
| scheduler     | scheduling    | `scheduler.py:24` → `SYSTEM_PROMPT`            |
| retrospective | retrospective | `retrospective.py:22` → `RETROSPECTIVE_PROMPT` |

Migrar um por vez. Testar com Sanity. Só remover o hardcode quando validado.

---

## Critérios de aceite

- [ ] Studio acessível em sanity.io/manage
- [ ] `sanity_client.get_prompt("focus_guard", "deviation")` retorna string do Studio
- [ ] Cache funciona: segunda chamada em 1s não faz request HTTP
- [ ] Fallback funciona: com `SANITY_PROJECT_ID` vazio, retorna string hardcoded
- [ ] `invalidate_cache()` chamável via endpoint `/admin/reload-config`
- [ ] Pelo menos 1 prompt migrado e funcionando em produção
````

## File: docs/arquitetura/SCHEMA_SIGNAL_DECISION.md
````markdown
# SCHEMA SIGNAL SOURCE DECISION

Status: draft operacional
Ultima atualizacao: 2026-04-03

## Proposito

Definir a camada minima que permite ao
`ecosystem_monitor` produzir inteligencia real em vez
de apenas log.

Esta camada existe para responder tres perguntas:

1. o que aconteceu
2. de onde veio
3. exige decisao ou nao

## Regra de modelagem

- `Signal` registra um fato relevante
- `Source` descreve a origem estrutural desse fato
- `Decision` registra a interpretacao e a resposta

Sem esses tres tipos, o monitor externo vira um script
com boa retorica e memoria ruim.

## Signal

Representa um evento, mudanca, anomalia ou observacao
vinda de uma fonte externa ou interna.

Campos minimos:

```json
{
  "id": "signal_2026_04_03_railway_service_down",
  "source_id": "source_railway_mello_dash",
  "kind": "service_status",
  "severity": "fail",
  "message": "Service mypersonal_multiagents offline for 7 minutes",
  "timestamp": "2026-04-03T14:12:00-03:00",
  "actionable": true,
  "decision_required": true,
  "context": {
    "service": "mypersonal_multiagents",
    "project": "Mello Dash",
    "minutes_down": 7
  }
}
```

Campos recomendados:

- `id`
- `source_id`
- `kind`
- `severity`
- `message`
- `timestamp`
- `actionable`
- `decision_required`
- `context`
- `dedupe_key`
- `ttl_hours`
- `status`

Enums sugeridos:

- `severity`: `ok`, `warn`, `fail`, `critical`
- `status`: `open`, `acknowledged`, `dismissed`, `resolved`

## Source

Representa a fonte estrutural que produz sinais.

Campos minimos:

```json
{
  "id": "source_railway_mello_dash",
  "provider": "railway",
  "scope": "project",
  "name": "Mello Dash",
  "identifier": "d9b36ed2-fb3c-43ff-bb2c-1af4a7f78989",
  "active": true,
  "metadata": {
    "environment": "production"
  }
}
```

Campos recomendados:

- `id`
- `provider`
- `scope`
- `name`
- `identifier`
- `active`
- `metadata`
- `owner`
- `priority`

Enums sugeridos:

- `provider`: `github`, `railway`, `vercel`, `cloudflare`, `onchain`, `notion`, `manual`
- `scope`: `org`, `project`, `service`, `token`, `repo`, `domain`, `contract`

## Decision

Representa uma interpretacao ou acao proposta a partir
de um ou mais sinais.

Campos minimos:

```json
{
  "id": "decision_2026_04_03_review_mypersonal_service",
  "signal_ids": ["signal_2026_04_03_railway_service_down"],
  "title": "Review production health of mypersonal_multiagents",
  "summary": "Service instability crossed alert threshold and needs inspection.",
  "priority": "high",
  "state": "pending",
  "owner": "human",
  "created_at": "2026-04-03T14:15:00-03:00"
}
```

Campos recomendados:

- `id`
- `signal_ids`
- `title`
- `summary`
- `priority`
- `state`
- `owner`
- `created_at`
- `resolved_at`
- `resolution`
- `links`

Enums sugeridos:

- `priority`: `low`, `medium`, `high`, `critical`
- `state`: `pending`, `approved`, `rejected`, `resolved`
- `owner`: `human`, `agent`, `mixed`

## Diferencas operacionais

`Signal`:

- fato observavel
- nao decide nada por si

`Source`:

- origem permanente ou semi-permanente
- nao e evento

`Decision`:

- interpretacao orientada a acao
- pode consolidar varios sinais

## Persistencia recomendada

Redis:

- cache quente de sinais abertos
- TTL padrao de 24h
- dedupe e estado corrente
- nao e fonte de schema

Sanity:

- registro permanente de `Source`
- registro historico e editorial de `Signal`
- registro governado de `Decision`

## Regras de reconciliacao

- Redis nunca e a fonte permanente de `Decision`
- Redis nao define schema nem semantica
- `Source` nasce canonicamente no Sanity
- `Signal` pode nascer no Redis e ser promovido ao Sanity
- `Decision` deve nascer no Sanity ou ser promovida ao
  Sanity imediatamente quando criada

## Gates antes da implementacao

1. schema aprovado
2. thresholds aprovados
3. `ecosystem.yml` definido
4. politica de TTL definida

## Proxima aplicacao

Primeiro uso deste schema:

- `ecosystem_monitor`
- sinais de GitHub
- sinais de Railway
- sinais de NEOFLW
````

## File: docs/assets/multiagentes-banner.svg
````xml
<svg
  width="1600"
  height="760"
  viewBox="0 0 1600 760"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
>
  <title> >_ nodE NEØ - Agents Gate < </title>
  <desc
  >Mapa operacional do ecossistema mypersonal_multiagents com kernel íntimo, órbita externa, Redis, Sanity, Gemma local e superfície pública.</desc>

  <rect width="1600" height="760" fill="#09131A" />
  <rect
    x="24"
    y="24"
    width="1552"
    height="712"
    rx="28"
    fill="url(#bg)"
    stroke="#6EE7F9"
    stroke-opacity="0.22"
  />

  <text
    x="54"
    y="72"
    fill="#6EE7F9"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="18"
    letter-spacing="2"
  >NEO OPERATING MAP</text>
  <text
    x="54"
    y="116"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="40"
    font-weight="700"
  >multiagentes</text>
  <text
    x="54"
    y="146"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="18"
  >Kernel íntimo, órbita externa, memória quente e governança semântica</text>
  <text
    x="54"
    y="170"
    fill="#6EE7F9"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="13"
  >updated 2026-04-03 · ecosystem monitor active</text>

  <path
    d="M1274 48V712"
    stroke="#6EE7F9"
    stroke-opacity="0.18"
    stroke-dasharray="8 8"
  />
  <text
    x="1206"
    y="74"
    fill="#D7FF64"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="14"
  >PUBLICAR SO APOS REVISAO</text>

  <rect
    x="54"
    y="186"
    width="220"
    height="252"
    rx="18"
    fill="#08171F"
    stroke="#6EE7F9"
    stroke-opacity="0.28"
  />
  <text
    x="82"
    y="224"
    fill="#D7FF64"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="20"
  >ENTRADAS</text>
  <rect x="82" y="246" width="164" height="42" rx="10" fill="#0F2430" />
  <text
    x="106"
    y="272"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="17"
  >Notion Tasks</text>
  <rect x="82" y="300" width="164" height="42" rx="10" fill="#0F2430" />
  <text
    x="106"
    y="326"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="17"
  >Notion Agenda</text>
  <rect x="82" y="354" width="164" height="42" rx="10" fill="#0F2430" />
  <text
    x="106"
    y="380"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="17"
  >CLI / Home UI</text>
  <rect x="82" y="408" width="164" height="42" rx="10" fill="#0F2430" />
  <text
    x="106"
    y="434"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="17"
  >Railway Runtime</text>

  <path
    d="M274 267H346"
    stroke="#6EE7F9"
    stroke-width="3"
    stroke-linecap="round"
  />
  <path
    d="M333 254L346 267L333 280"
    stroke="#6EE7F9"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
  <path
    d="M274 321H346"
    stroke="#6EE7F9"
    stroke-width="3"
    stroke-linecap="round"
  />
  <path
    d="M333 308L346 321L333 334"
    stroke="#6EE7F9"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
  <path
    d="M274 375H346"
    stroke="#6EE7F9"
    stroke-width="3"
    stroke-linecap="round"
  />
  <path
    d="M333 362L346 375L333 388"
    stroke="#6EE7F9"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />

  <rect
    x="346"
    y="170"
    width="430"
    height="320"
    rx="22"
    fill="#08171F"
    stroke="#6EE7F9"
    stroke-opacity="0.35"
  />
  <text
    x="378"
    y="212"
    fill="#D7FF64"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="22"
  >KERNEL INTIMO</text>
  <text
    x="378"
    y="236"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >foco · agenda · validacao · sync · decisao operacional</text>

  <rect x="378" y="258" width="156" height="36" rx="10" fill="#102B36" />
  <text
    x="398"
    y="281"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="16"
  >orchestrator()</text>
  <rect x="554" y="258" width="170" height="36" rx="10" fill="#102B36" />
  <text
    x="574"
    y="281"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="16"
  >focus_guard()</text>

  <rect x="378" y="308" width="156" height="36" rx="10" fill="#102B36" />
  <text
    x="405"
    y="331"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="16"
  >scheduler()</text>
  <rect x="554" y="308" width="170" height="36" rx="10" fill="#102B36" />
  <text
    x="587"
    y="331"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="16"
  >validator()</text>

  <rect x="378" y="358" width="156" height="36" rx="10" fill="#102B36" />
  <text
    x="393"
    y="381"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="16"
  >notion_sync()</text>
  <rect x="554" y="358" width="170" height="36" rx="10" fill="#102B36" />
  <text
    x="560"
    y="381"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="16"
  >calendar_sync()</text>

  <text
    x="560"
    y="404"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="13"
  >opcional</text>

  <text
    x="378"
    y="430"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >life_guard() · retrospective() · persona_manager()</text>

  <rect
    x="346"
    y="512"
    width="430"
    height="42"
    rx="14"
    fill="#0E2029"
    stroke="#D7FF64"
    stroke-opacity="0.28"
  />
  <text
    x="374"
    y="538"
    fill="#D7FF64"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="16"
  >notificacoes: mac local · alexa · audit trail · alertas</text>

  <rect
    x="824"
    y="170"
    width="314"
    height="122"
    rx="22"
    fill="#08171F"
    stroke="#D7FF64"
    stroke-opacity="0.42"
  />
  <text
    x="854"
    y="208"
    fill="#D7FF64"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="22"
  >REDIS</text>
  <text
    x="854"
    y="238"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="17"
  >estado quente</text>
  <text
    x="854"
    y="264"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >agenda · tasks · sessoes · alerts · audit · signals quentes</text>

  <rect
    x="824"
    y="314"
    width="314"
    height="160"
    rx="22"
    fill="#08171F"
    stroke="#6EE7F9"
    stroke-opacity="0.35"
  />
  <text
    x="854"
    y="352"
    fill="#6EE7F9"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="22"
  >SANITY</text>
  <text
    x="854"
    y="382"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="17"
  >governanca e camada semantica</text>
  <text
    x="854"
    y="408"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >agent_config · persona · prompt · intervention_script</text>
  <text
    x="854"
    y="432"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >project · area · task · block · signal · source · decision</text>

  <path
    d="M776 230H824"
    stroke="#D7FF64"
    stroke-width="3"
    stroke-linecap="round"
  />
  <path
    d="M811 217L824 230L811 243"
    stroke="#D7FF64"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
  <path
    d="M824 394H776"
    stroke="#6EE7F9"
    stroke-width="3"
    stroke-linecap="round"
  />
  <path
    d="M789 381L776 394L789 407"
    stroke="#6EE7F9"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
  <text
    x="781"
    y="300"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="14"
  >governa</text>

  <rect
    x="824"
    y="504"
    width="314"
    height="50"
    rx="14"
    fill="#0E2029"
    stroke="#6EE7F9"
    stroke-opacity="0.28"
  />
  <text
    x="846"
    y="534"
    fill="#6EE7F9"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="16"
  >ponte: signal() · source() · decision()</text>

  <rect
    x="382"
    y="84"
    width="184"
    height="54"
    rx="14"
    fill="#0E2029"
    stroke="#6EE7F9"
    stroke-opacity="0.28"
  />
  <text
    x="408"
    y="117"
    fill="#6EE7F9"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="18"
  >Gemma local</text>
  <text
    x="570"
    y="116"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="14"
  >fallback · triagem</text>
  <path
    d="M474 138V170"
    stroke="#6EE7F9"
    stroke-width="2.5"
    stroke-dasharray="7 7"
  />

  <rect
    x="54"
    y="566"
    width="722"
    height="134"
    rx="22"
    fill="#08171F"
    stroke="#D7FF64"
    stroke-opacity="0.32"
  />
  <text
    x="86"
    y="604"
    fill="#D7FF64"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="22"
  >ORBITA EXTERNA</text>
  <text
    x="86"
    y="632"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >monitoramento do ecossistema sem contaminar o foco intimo</text>

  <rect x="86" y="648" width="156" height="34" rx="10" fill="#102B36" />
  <text
    x="106"
    y="670"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >ecosystem_monitor()</text>
  <rect x="262" y="648" width="96" height="34" rx="10" fill="#102B36" />
  <text
    x="292"
    y="670"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >GitHub</text>
  <rect x="374" y="648" width="104" height="34" rx="10" fill="#102B36" />
  <text
    x="405"
    y="670"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >Railway</text>
  <rect x="494" y="648" width="92" height="34" rx="10" fill="#102B36" />
  <text
    x="525"
    y="670"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >Vercel</text>
  <rect x="602" y="648" width="96" height="34" rx="10" fill="#102B36" />
  <text
    x="624"
    y="670"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >On-chain</text>

  <path
    d="M776 620H896"
    stroke="#D7FF64"
    stroke-width="3"
    stroke-linecap="round"
  />
  <path
    d="M883 607L896 620L883 633"
    stroke="#D7FF64"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />

  <rect
    x="1304"
    y="202"
    width="220"
    height="96"
    rx="18"
    fill="#08171F"
    stroke="#D7FF64"
    stroke-opacity="0.42"
  />
  <text
    x="1330"
    y="238"
    fill="#D7FF64"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="20"
  >PUBLISH GATE</text>
  <text
    x="1330"
    y="265"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="14"
  >revisao humana</text>
  <text
    x="1330"
    y="286"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="14"
  >public_artifact</text>

  <rect
    x="1304"
    y="340"
    width="220"
    height="146"
    rx="18"
    fill="#08171F"
    stroke="#6EE7F9"
    stroke-opacity="0.35"
  />
  <text
    x="1328"
    y="376"
    fill="#6EE7F9"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="20"
  >PUBLIC LAYER</text>
  <text
    x="1328"
    y="403"
    fill="#E8F4F8"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >neo-mello-eth</text>
  <text
    x="1328"
    y="426"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="14"
  >nettomello.eth.limo</text>
  <text
    x="1328"
    y="449"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="14"
  >ENS · IPFS · IPNI</text>

  <path
    d="M1138 394H1304"
    stroke="#6EE7F9"
    stroke-width="3"
    stroke-linecap="round"
  />
  <path
    d="M1291 381L1304 394L1291 407"
    stroke="#6EE7F9"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
  <path
    d="M1414 298V340"
    stroke="#D7FF64"
    stroke-width="3"
    stroke-linecap="round"
  />
  <path
    d="M1401 327L1414 340L1427 327"
    stroke="#D7FF64"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />

  <text
    x="52"
    y="720"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >Fluxo íntimo: Notion Tasks / Notion Agenda / UI → kernel → Redis ↔ Sanity</text>
  <text
    x="782"
    y="720"
    fill="#9BB7C3"
    font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace"
    font-size="15"
  >Fluxo externo: APIs → ecosystem_monitor → Redis → signal/source/decision → Publish Gate → neo-mello-eth</text>

  <defs>
    <linearGradient
      id="bg"
      x1="42"
      y1="32"
      x2="1540"
      y2="728"
      gradientUnits="userSpaceOnUse"
    >
      <stop stop-color="#10222D" />
      <stop offset="1" stop-color="#0B151C" />
    </linearGradient>
  </defs>
</svg>
````

## File: docs/auditoria/AUDITORIA_AGENTES.md
````markdown
# Auditoria de Código — Sistema Multiagentes

> **HISTÓRICO — Todas as issues foram corrigidas em 2026-03-28.**
> Este documento é registro de auditoria passada, não estado atual do código.
> Para governança atual dos agentes, consulte `../governanca/CONTRATO_AGENTES.md` e `../governanca/MATRIZ_GOVERNANCA_AGENTES.md`.

**Data:** 2026-03-28
**Status:** RESOLVIDO — ver seção "Registro de Correções" ao final
**Escopo:** `agents/` + `core/openai_utils.py` + `config.py`
**Metodologia:** Revisão estática cruzada — padrões, fluxo de dados, segurança

---

## Sumário Executivo

| Severidade   | Quantidade |
| ------------ | ---------- |
| CRÍTICO      | 0          |
| ALTO         | 6          |
| MÉDIO        | 7          |
| Arquitetural | 1          |

Nenhuma chamada direta à API OpenAI encontrada fora de `core/openai_utils.py` — padrão central respeitado em todos os agentes.

---

## Issues ALTO — Ação Imediata

### A1 · `focus_guard.py` ~383 — Triple LLM call em `force_check()`

`force_check()` chama `analyze_with_llm(progress)` diretamente (chamada 1), e em seguida chama `_run_focus_check()` que internamente executa `analyze_progress()` + `analyze_with_llm()` novamente (chamadas 2 e 3). Cada invocação via Orchestrator gera 3 chamadas à OpenAI — 2 delas desperdiçadas.

**Correção:** `_run_focus_check()` deve aceitar `progress` e `analysis` como parâmetros opcionais, ou `force_check()` deve delegar integralmente para `_run_focus_check()` e retornar seus resultados.

---

### A2 · `focus_guard.py` ~89 — Lógica de overdue incorreta

```python
# ERRADO — marca blocos em andamento como atrasados
if (end_t < now or start_t < now) and not block.get("completed"):
    overdue_blocks.append(block)
```

A condição `start_t < now` é verdadeira para qualquer bloco cujo início já passou, inclusive o bloco atual em execução. O `elif` de `current_block` (testado depois) nunca é alcançado para esse caso — o bloco em andamento entra em `overdue_blocks` antes. Resultado: Focus Guard emite falsos alertas de atraso para tarefas ativas.

**Correção:**

```python
# CORRETO — apenas blocos cujo FIM já passou
if end_t < now and not block.get("completed"):
    overdue_blocks.append(block)
```

---

### A3 · `scheduler.py` ~174 — `return` dentro do `for` torna busca multi-day inoperante

```python
for offset in range(max_days_ahead + 1):
    # ...
    return target_date, _format_slot(start_dt, duration_minutes)  # sempre retorna aqui

# Código abaixo nunca é alcançado:
fallback_date = ...
return fallback_date, ...
```

O `return` dentro do loop faz a função sempre retornar no `offset=0` (hoje), sem jamais verificar dias futuros. O parâmetro `max_days_ahead` é ignorado na prática.

**Correção:** mover o `return` para fora do `for`, retornando apenas após esgotar todos os offsets sem encontrar slot disponível.

---

### A4 · `validator.py` ~71 — Conexão SQLite direta bypassa `core.memory`

```python
import sqlite3
from config import MEMORY_DB_PATH
conn = sqlite3.connect(MEMORY_DB_PATH, check_same_thread=False)
```

`validator.py` abre conexão SQLite diretamente em `gather_evidence()` para consultar `focus_sessions` e `agenda_blocks`. Todos os outros agentes usam exclusivamente `core.memory` como camada de abstração. Se `core.memory` mudar de backend (pool de conexões, Redis, migração de schema), o `validator` quebra silenciosamente.

**Correção:** adicionar `get_focus_sessions_for_task(task_id)` e `get_agenda_blocks_for_task(task_id)` em `core/memory.py` e substituir o acesso direto.

---

### A5 · `retrospective.py` ~230 — HTTP ao Notion sem retry

`retrospective.py` reimplementa sua própria pilha HTTP para o Notion (`_notion_headers()` + `requests.post` direto), sem qualquer lógica de retry. `notion_sync.py` possui `_request()` com retry automático via `tenacity` para erros 429 (rate-limit) e 5xx. Em caso de rate-limit da Notion API, a criação da página de retrospectiva falha silenciosamente (retorna `None`).

**Correção:** extrair `_request` e `_notion_headers` de `notion_sync.py` para `core/notion_client.py` e importar de lá em ambos os agentes. Ou fazer `retrospective.py` importar diretamente de `notion_sync`.

---

### A6 · `calendar_sync.py` ~81 — `token.json` gravado sem permissões restritas

```python
with open(GOOGLE_TOKEN_FILE, "w") as f:
    f.write(creds.to_json())
```

O OAuth refresh token do Google é gravado com as permissões padrão do sistema (tipicamente `0o644` — legível por todos os usuários). Em ambientes multiusuário, qualquer usuário local pode ler e reutilizar o token.

**Correção:**

```python
import stat
fd = os.open(GOOGLE_TOKEN_FILE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
with os.fdopen(fd, "w") as f:
    f.write(creds.to_json())
```

---

## Issues MÉDIO

### M1 · `persona_manager.py` ~37 — `print()` em vez de `notifier`

Único agente que usa `print()` diretamente para reportar erros. Todos os demais usam `notifier.error()` / `notifier.warning()`. O erro não é registrado no `LOG_FILE` configurado.

**Correção:** `notifier.error(f"Erro ao carregar {filepath.name}: {e}", "persona_manager")`

---

### M2 · `agents/__init__.py` — `__all__` desatualizado

```python
__all__ = ["orchestrator", "scheduler", "focus_guard", "notion_sync", "validator"]
```

`calendar_sync`, `retrospective` e `persona_manager` estão ausentes, embora sejam importados e usados pelo Orchestrator. `__all__` fica enganoso para ferramentas de análise estática e IDEs.

**Correção:** incluir todos os agentes ativos ou remover a declaração.

---

### M3 · `scheduler.py` ~159 — Código morto no `find_next_available_slot`

Consequência direta do A3: o fallback de data e o código abaixo do `for` são código morto e nunca executados. Podem ser removidos após a correção do A3.

---

### M4 · `validator.py` — Import dinâmico de `notion_sync` dentro de função

```python
def gather_evidence(task_id):
    from agents import notion_sync   # import dentro da função
    notion_tasks = notion_sync.fetch_notion_tasks()
```

Padrão inconsistente com o restante do projeto. Mascara erros de importação até o momento da execução. O mesmo import se repete em `apply_verdict()`.

**Correção:** mover para o topo do arquivo junto com os demais imports.

---

### M5 · `calendar_sync.py` ~315 — Timezone hardcoded sem aviso

```python
except ImportError:
    tz_str = "America/Sao_Paulo"  # sem log, sem aviso
```

Fallback silencioso que causa comportamento errado para qualquer usuário fora do fuso `America/Sao_Paulo`.

**Correção:** `notifier.warning("tzlocal não disponível — usando America/Sao_Paulo como fallback de timezone.", AGENT_NAME)`

---

### M6 · `orchestrator.py` e `notion_sync.py` — Imports não utilizados

- `orchestrator.py:18` — `Any` importado de `typing`, nunca usado
- `notion_sync.py:24` — `List` importado de `typing`, nunca usado (o arquivo usa `list[...]` moderno do Python 3.10+)
- `orchestrator.py:543` — f-string sem interpolação: `f"Resultado das ações executadas:"` → remover o `f`

---

### M7 · `config.py` ~17 — `validate_config()` nunca é chamada

`OPENAI_API_KEY` é lida com fallback para string vazia. O client OpenAI é instanciado com essa string vazia no nível de módulo — o erro só aparece na primeira chamada à API, sem mensagem clara. A função `validate_config()` existe mas não é invocada em nenhum ponto do código.

**Correção:** chamar `validate_config()` na inicialização da aplicação (`main.py` ou equivalente).

---

## Issue Arquitetural — Boilerplate `handle_handoff` duplicado

O bloco de log/update/return do protocolo de handoff é copiado literalmente em **6 arquivos**:
`scheduler`, `focus_guard`, `validator`, `retrospective`, `notion_sync`, `calendar_sync`.

```python
handoff_id = memory.log_handoff("orchestrator", AGENT_NAME, action, payload)
# ...
memory.update_handoff_result(handoff_id, result, "success")
return {"status": "success", "result": result}
# ...
except Exception as exc:
    memory.update_handoff_result(handoff_id, {"error": str(exc)}, "error")
    return {"status": "error", "result": {"error": str(exc)}}
```

Qualquer mudança no protocolo (ex: adicionar campo `"agent"` na resposta, mudar o esquema de log) exige edição em 6 arquivos com risco de divergência.

**Proposta:** decorator `@handoff_handler` em `core/handoff_utils.py` que envolve a função do agente com o boilerplate de log/update/return.

---

## Status de Conformidade — Padrão Central OpenAI

| Agente             | Usa `chat_completions` | Chamada direta       |
| ------------------ | ---------------------- | -------------------- |
| orchestrator.py    | ✅                     | —                    |
| scheduler.py       | ✅                     | corrigido 2026-03-28 |
| focus_guard.py     | ✅                     | —                    |
| validator.py       | ✅                     | —                    |
| retrospective.py   | ✅                     | —                    |
| notion_sync.py     | não usa LLM            | —                    |
| calendar_sync.py   | não usa LLM            | —                    |
| persona_manager.py | não usa LLM            | —                    |

---

## Registro de Correções — 2026-03-28

| ID  | Arquivo              | O que foi feito                                                                                                                                                                             |
| --- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A1  | `focus_guard.py`     | `_run_focus_check` aceita `progress`/`analysis` opcionais; `force_check` os computa uma vez e repassa — 3 LLM calls → 1                                                                     |
| A2  | `focus_guard.py`     | Condição overdue: `end_t < now or start_t < now` → `end_t < now`                                                                                                                            |
| A3  | `scheduler.py`       | `return` dentro do `for` condicionado a `start_dt.date().isoformat() == target_date` — multi-day search agora funciona                                                                      |
| A4  | `validator.py`       | `sqlite3.connect` direto removido; adicionados `get_focus_sessions_for_task` e `get_agenda_blocks_for_task` em `core/memory.py` com índices Redis `sessions:task:{id}` e `blocks:task:{id}` |
| A5  | `retrospective.py`   | HTTP direto para Notion substituído por `_notion_sync._request` (retry via tenacity); `_notion_headers()` local removida                                                                    |
| A6  | `calendar_sync.py`   | `open(token_file, "w")` → `os.open(..., 0o600)` + `os.fdopen`                                                                                                                               |
| M1  | `persona_manager.py` | `print()` → `notifier.error()`; adicionado import de `notifier`                                                                                                                             |
| M2  | `agents/__init__.py` | `__all__` atualizado com todos os 8 agentes                                                                                                                                                 |
| M3  | `scheduler.py`       | Código morto após o loop tornado acessível pela correção A3                                                                                                                                 |
| M4  | `validator.py`       | Imports dinâmicos de `notion_sync` movidos para o topo do arquivo                                                                                                                           |
| M5  | `calendar_sync.py`   | Fallback de timezone emite `notifier.warning`                                                                                                                                               |
| M6  | `orchestrator.py`    | `Any` removido do import `typing`; f-string sem interpolação corrigida                                                                                                                      |
| M6  | `notion_sync.py`     | `List` removido do import `typing`                                                                                                                                                          |
| M7  | `config.py`          | `validate_config()` já chamada em `main.py:45` — sem alteração necessária                                                                                                                   |
````

## File: docs/ecossistema/ECOSSISTEMA_NEO_PROTOCOL.md
````markdown
# ECOSSISTEMA NEO-PROTOCOL

Status: ativo
Última atualização: 2026-04-06

## Propósito

Este documento mapeia o ecossistema externo que NEØ MELLØ
gerencia como responsabilidade pessoal.

Manter e evoluir a org NEO-PROTOCOL é uma tarefa real —
não um projeto separado do OS pessoal.

O `ecosystem_monitor` precisa deste mapa para saber
o que monitorar, quais sinais coletar e quais decisões
escalar para revisão humana.

---

## Identidade pública

| Superfície | URL | Papel |
| --- | --- | --- |
| Identidade ENS | `neomello.eth.limo` | Perfil público, exposição de projetos e ideias |
| Org GitHub | `github.com/NEO-PROTOCOL` | Organização técnica, repos e roadmap |
| Dashboard | `mypersonal-multiagents.up.railway.app` | Console de controle operacional |
| Token | NEOFLW · Base Mainnet | `0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B` |

---

## Repositórios da org NEO-PROTOCOL

### `neo-dashboard`

- `github.com/NEO-PROTOCOL/neo-dashboard`
- **O que é:** Console de controle operacional. Interface "Analyzer /
  Control / Topology". Superfície primária de leitura de sinais e
  estado do ecossistema.
- **Deploy:** `mypersonal-multiagents.up.railway.app`
- **Monitorar:** uptime, último deploy, health check

### `neo-mello-eth`

- `github.com/NEO-PROTOCOL/neo-mello-eth`
- **O que é:** Site público de identidade de NEØ MELLØ.
  Canal de exposição de ideias, projetos e artefatos públicos.
  Porta de saída do fluxo privado → público do OS pessoal.
- **Deploy:** `neomello.eth.limo` / `neomelloeth.up.railway.app`
- **Redis:** `redis-neomello.up.railway.app` (Railway)
- **Monitorar:** uptime, último deploy, health do Redis Railway

### `mio-system`

- `github.com/NEO-PROTOCOL/mio-system`
- **O que é:** Camada de identidade Web3. Gerencia as 9 identidades
  MIO (mio-core, mio-warrior, mio-factory, mio-gateway...).
  Autenticação e registro soberano de identidades.
- **Stack:** Node.js / Express / Web3 / ethers.js
- **Monitorar:** health da API, status das identidades

### `neoflw-base-landing`

- `github.com/NEO-PROTOCOL/neoflw-base-landing`
- **O que é:** Landing page do token NEOFLW (Base Mainnet).
  Site estático de verificação e informação do token.
- **Deploy:** Vercel / `neoflowoff.eth.limo`
- **Monitorar:** uptime, contrato on-chain

### `.github`

- **O que é:** Perfil da org, arquitetura, diretivas e definições
  críticas do protocolo. Documentação central da org.
- **Monitorar:** PRs e issues abertas

---

## Roadmap da org

**Fonte canônica:** `github.com/orgs/NEO-PROTOCOL/projects/1`

Fases identificadas via `ecosystem.json` do neobot:

### Fase 1 — Operacional (🟢)

- Neobot Orchestrator (nó soberano) — ATIVO
- MIO System (camada de identidade) — ATIVO
- NEO Nexus (event hub/relay) — ATIVO no Railway
- NEO Agent Full (WhatsApp/Telegram) — ATIVO no Railway
- Lighthouse Storage (IPFS pinning) — ATIVO

### Fase 2 — Configuração pendente (🟡)

- Neo Dashboard (console de controle) — deploy ok, requer config
- Smart Factory Hub (Web3 engineering) — integração ativa
- WhatsApp Channel Automation — setup necessário
- Notion Sync para lead reporting — em desenvolvimento

### Fase 3 — Roadmap futuro (🔵)

- Kwil DB (memória descentralizada) — planejado
- Storacha/Ceramic (storage soberano) — planejado
- Camada de governança distribuída — planejado

---

## Conexões críticas da org

| Conexão | Status | Risco se quebrar |
| --- | --- | --- |
| Nexus ↔ Neobot | VITAL | perda de trilha de auditoria |
| Agent Full ↔ Nexus | VITAL | alucinação sistêmica dos agentes |
| FlowPay ↔ Nexus | VITAL | paralisia financeira |
| WhatsApp ↔ wacli | EM CONFIG | automação de PIX/faturas falha |

---

## Relação com o OS pessoal

```text
mypersonal_multiagents (kernel íntimo)
    ↓ tarefas pessoais de manutenção
NEO-PROTOCOL org (ecossistema externo)
    ├── neobot          ← orquestrador técnico
    ├── mio-system      ← identidade Web3
    ├── neo-dashboard   ← superfície de controle
    ├── neo-mello-eth   ← identidade pública
    └── neoflw-base-landing ← token
    ↓ artefatos aprovados
neomello.eth.limo (publicação pública via eclusa Sanity)
```

O OS pessoal é o kernel cognitivo.
A org NEO-PROTOCOL é o ecossistema técnico externo.
`neo-mello-eth` é o canal de saída público.

---

## O que o `ecosystem_monitor` deve observar

### GitHub

- PRs abertas em repos da org
- Issues abertas por prioridade
- Último commit por repo (detectar repos estagnados)
- Status do Project Board `projects/1`

### Railway

- Uptime de `neo-dashboard` (serviço `neo-mello-eth` + Redis)
- Último deploy de cada serviço
- Health check dos endpoints

### On-chain

- Contrato NEOFLW: `0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B` (Base)
- Holders, volume, última transação relevante

### ENS / Domínios

- `neomello.eth.limo` resolvendo corretamente
- `neoprotocol.space` ativo
- `neoflowoff.eth.limo` ativo

---

## Política de manutenção

- Tarefas de manutenção da org entram no Notion TASKS
  como qualquer outra tarefa pessoal
- Issues críticas da org viram `signal` no `ecosystem_monitor`
- Nenhuma decisão técnica da org vai diretamente para
  `neo-mello-eth` sem passar pela eclusa Sanity → `public_artifact`
- O GitHub Projects roadmap é a fonte de verdade do
  planejamento da org — não substituir por Redis ou Notion

---

## Acesso rápido

| Recurso | URL |
| --- | --- |
| Org GitHub | `github.com/NEO-PROTOCOL` |
| Project Board | `github.com/orgs/NEO-PROTOCOL/projects/1` |
| Dashboard | `mypersonal-multiagents.up.railway.app` |
| Identidade pública | `neomello.eth.limo` |
| Railway (neo-mello-eth) | `neomelloeth.up.railway.app` |
| Token Basescan | `basescan.org/token/0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B` |
````

## File: docs/ecossistema/ECOSSISTEMAS_ORGS.md
````markdown
# ECOSSISTEMAS — Todas as Orgs GitHub

Status: ativo
Última atualização: 2026-04-03

## Propósito

Mapa de todas as organizações GitHub gerenciadas por NEØ MELLØ
como responsabilidade pessoal.

Cada org tem repositórios, stack, estado de roadmap e o que
o `ecosystem_monitor` deve observar.

---

## Inventário de Orgs

| Org | Project Board | Repos | Foco |
|---|---|---|---|
| `NEO-PROTOCOL` | ✅ `projects/1` | 6+ | Orquestrador soberano, identidade pública, token |
| `NEO-FlowOFF` | ✅ `projects/1` "Unified Roadmap" M0–M13 | 17 | Automação e crescimento, token utility |
| `neo-smart-factory` | ✅ `projects/1` "Unified Roadmap 2026" | 8 | Contratos inteligentes, NFT, CLI tooling |
| `flowpay-system` | ✅ `projects/2` "FlowPay Roadmap" | 9 | Gateway de liquidação on NEO Protocol |
| `FluxxDAO` | ✅ `projects/1` "FluxxDAO Roadmap" | 3 | DAO / DeFi |
| `wodxpro` | ✅ `projects/1` "WODXPRO Roadmap" | 4 | Protocolo esportivo Web3 |

---

## NEO-PROTOCOL

**URL:** `github.com/NEO-PROTOCOL`
**Project Board:** `github.com/orgs/NEO-PROTOCOL/projects/1`
**Foco:** Orquestrador soberano do ecossistema pessoal de NEØ MELLØ

Documentação completa: `ECOSSISTEMA_NEO_PROTOCOL.md`

### Repos principais

| Repo | Stack | Deploy | Prioridade |
|---|---|---|---|
| `neobot` | TypeScript / Node.js | Railway + local macOS | P0 |
| `neo-dashboard` | (control console) | Railway | P0 |
| `neo-mello-eth` | (identidade pública) | Railway + Redis | P0 |
| `mio-system` | Node.js / Web3 | Railway | P1 |
| `neoflw-base-landing` | (landing token) | Vercel | P1 |
| `.github` | (docs org) | — | P2 |

### O que monitorar

- uptime neobot, webhook health
- neo-dashboard: último deploy, health check
- neo-mello-eth: Redis Railway ativo
- NEOFLW: preço, volume, variação on-chain
- Project Board: items sem movimento > 7 dias

---

## NEO-FlowOFF

**URL:** `github.com/NEO-FlowOFF`
**Project Board:** ✅ `github.com/orgs/NEO-FlowOFF/projects/1` — "NEO-FlowOFF Unified Roadmap"
**Foco:** Plataforma de automação e crescimento baseado em protocolo — aquisição de usuários, token utility, funil de conversão
**Repos:** 17 (4 públicos, 13 privados)
**Stack:** Python (backend), TypeScript / Astro (frontend), PWA

### Roadmap — 14 milestones M0–M13

| Milestone | Status |
|---|---|
| M0 — MVP Bootstrapping | Em progresso |
| M1 — Token path | Crítico |
| M2 — On-chain readiness | Crítico |
| M3–M9 — Produto, wallet, conversão | Fila |
| M10–M13 — Launch, automação, analytics | Planejado |

### Repos principais (públicos)

| Repo | Observações |
|---|---|
| `neo-control-plane` | Python — painel de controle central |
| `neo-flw-landing` | Landing principal |
| `neo-landing-open` | Landing open/público |
| `ceo-escalavel-miniapp` | Miniapp |

### O que monitorar

- M2 on-chain readiness: bloqueador do caminho crítico
- neo-control-plane: health da API Python
- Conversão de landing pages
- Velocidade do roadmap (14 milestones sequenciais)

---

## neo-smart-factory

**URL:** `github.com/neo-smart-factory`
**Project Board:** ✅ `github.com/orgs/neo-smart-factory/projects/1` — "Unified Roadmap 2026"
**Foco:** Contratos inteligentes, NFT, CLI e tooling Web3 para o protocolo NEO
**Membros:** 3
**Board:** ativo com 6 workflows, itens rastreados até Mai 2026

### Repos mapeados

| Repo | Lang | Visib | Observações |
|---|---|---|---|
| `smart-core` | JavaScript | público | Contratos e deployment scripts |
| `smart-ui` | JavaScript | público | PWA e landing page |
| `internal-ops` | JavaScript | privado | CI/CD e automações |
| `smart-ui-mobile` | JavaScript | privado | Telegram miniapp |
| `docs` | JavaScript | privado | Documentação da plataforma |
| `smart-nft` | JavaScript | privado | NFT Manager com IPFS |
| `smart-cli` | JavaScript | privado | CLI `nxf` universal |
| `smart-ui-landing` | Shell | privado | Landing + infraestrutura |

### O que monitorar

- `smart-nft`: atividade on-chain, contratos implantados
- `smart-cli`: último release (mais lento — fev/2026)
- `smart-core`: últimos commits de contrato
- Board "Unified Roadmap 2026": velocity e blockers

---

## flowpay-system

**URL:** `github.com/flowpay-system`
**Project Board:** ✅ `github.com/orgs/flowpay-system/projects/2` — "FlowPay Roadmap" (criado 2026-04-03)
**Foco:** Gateway de liquidação descentralizado sobre o NEØ Protocol — processamento autônomo de transações
**Repos:** 9 (2 públicos, 7 privados)
**Stack:** JavaScript, Cloudflare Workers, D1 Database, NEØ Protocol

### O que o sistema faz

- Settlement gateway em tempo real (SLA p95 < 5s)
- KYC: validação CPF/CNPJ
- Dashboard de vendedor
- Provider abstraction layer
- Proof-of-execution anchoring on-chain
- SWIE (Sign-In With Ethereum) para autenticação

### Repos mapeados

| Repo | Lang | Visib | Observações |
|---|---|---|---|
| `flowpay-app` | CSS / JS | privado | Frontend principal (seller dashboard) |
| `flowpay-api` | JavaScript | privado | API + Cloudflare Workers + D1 |
| `flowpay-marketing` | Astro | privado | Site de marketing |
| `flowpay-infra` | Shell | privado | Scripts de infra |
| `flowpay-docs` | — | privado | Documentação interna |
| `flowpay-docs-page` | — | público | Documentação pública |
| `flowpay-system-workspace` | JavaScript | privado | Monorepo workspace |
| `.github` | — | público | Perfil da org |

### O que monitorar

- flowpay-api: latência de settlement, uptime (Cloudflare Workers)
- KYC validation pipeline: taxa de sucesso
- Transações: success rate > 99.5%
- Project Board: criar e ativar (pendente)

---

## FluxxDAO

**URL:** `github.com/FluxxDAO`
**Project Board:** ✅ `github.com/orgs/FluxxDAO/projects/1` — "FluxxDAO Roadmap" (criado 2026-04-03)
**Foco:** Governança e DeFi — "Assinamos com presença, não com papel"
**Membros:** 2 (neomello, fluxx-dao)
**Domínio:** `fluxx.space`

### Repos mapeados (todos privados)

| Repo | Lang | Último commit | Observações |
|---|---|---|---|
| `fluxxdao-workspace` | JavaScript | Mar 22, 2026 | Monorepo workspace e config compartilhada |
| `fluxx-backend` | JavaScript | Mar 3, 2026 | API e lógica de negócio core |
| `fluxx-landing` | JavaScript | Mar 3, 2026 | Landing page — `fluxx.space` |

### O que monitorar

- fluxx-landing: uptime em `fluxx.space`
- fluxx-backend: health da API
- Project Board: criar e ativar (pendente)

---

## wodxpro

**URL:** `github.com/wodxpro`
**Project Board:** ✅ `github.com/orgs/wodxpro/projects/1` — "WODXPRO Roadmap" (criado 2026-04-03)
**Foco:** Registros verificáveis de atividade fitness on-chain
**Membros:** 2 (neomello, wodxproject)

### Repos mapeados

| Repo | Lang | Visib | Último commit | Observações |
|---|---|---|---|---|
| `wod-protocol` | — | privado | Mar 3, 2026 | Core do protocolo |
| `wod-eth` | TypeScript | privado | Mar 3, 2026 | Camada Ethereum/EVM |
| `wod-x-pro` | TypeScript | privado | Mar 3, 2026 | Aplicação principal |
| `wod-landing` | CSS | público | Fev 24, 2026 | Site público |

### O que monitorar

- wod-landing: uptime (único repo público)
- wod-eth: atividade on-chain / smart contract interactions
- wod-protocol: estabilidade de implementação
- Project Board: criar e ativar (pendente)

---

## Política de manutenção (todas as orgs)

- Issues críticas de qualquer org viram `signal` no `ecosystem_monitor`
- Repos sem atividade há mais de 14 dias são sinalizados como estagnados
- Project Boards são a fonte de verdade de roadmap — não substituir por Redis
- Nenhuma decisão técnica de nenhuma org vai para `neo-mello-eth` sem eclusa Sanity
- Tarefas de manutenção de org entram no Notion TASKS como qualquer tarefa pessoal

---

## Acesso rápido

| Recurso | URL |
|---|---|
| NEO-PROTOCOL | `github.com/NEO-PROTOCOL` |
| NEO-PROTOCOL Board | `github.com/orgs/NEO-PROTOCOL/projects/1` |
| NEO-FlowOFF | `github.com/NEO-FlowOFF` |
| NEO-FlowOFF Board | `github.com/orgs/NEO-FlowOFF/projects/1` |
| neo-smart-factory | `github.com/neo-smart-factory` |
| neo-smart-factory Board | `github.com/orgs/neo-smart-factory/projects/1` |
| flowpay-system | `github.com/flowpay-system` |
| flowpay-system Board | `github.com/orgs/flowpay-system/projects/2` |
| FluxxDAO | `github.com/FluxxDAO` |
| FluxxDAO Board | `github.com/orgs/FluxxDAO/projects/1` |
| wodxpro | `github.com/wodxpro` |
| wodxpro Board | `github.com/orgs/wodxpro/projects/1` |
| Dashboard NEØ | `dashboard.neoprotocol.space` |
| Identidade pública | `neomello.eth.limo` |
| Token NEOFLW | `basescan.org/token/0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B` |
````

## File: docs/ecossistema/GUIAS_REFERENCIA.md
````markdown
# Guias de Referência Externos

> **EM ESCOPO.**
> O neo-dashboard é a superfície de controle da org NEO-PROTOCOL,
> gerenciada por NEØ MELLØ como responsabilidade pessoal.
> Monitorar saúde e roadmap desta org é uma das tarefas do `ecosystem_monitor`.
> Ver também: `ECOSSISTEMA_NEO_PROTOCOL.md` para mapeamento completo.

Catálogo inicial de superfícies, runbooks e páginas de operação já existentes fora deste repositório.

Objetivo:

- manter uma fonte única de links úteis
- registrar o contexto de uso de cada guia
- permitir expansão futura para uma base mais estruturada

## Fontes registradas

| ID | Título | Tipo | URL |
| --- | --- | --- | --- |
| `neo-dashboard-runbook` | NEØ Operations Runbook | runbook operacional | `https://mypersonal-multiagents.up.railway.app/runbook.html` |
| `neo-dashboard-console` | NΞØ Protocol Control Console | console operacional | `https://mypersonal-multiagents.up.railway.app/` |

## Contextos capturados

### `neo-dashboard-runbook`

- Papel: guia de uso por função
- Superfícies citadas: `Analyzer`, `Control`, `Topology`
- Tese central: uma interface por função; Analyzer decide prioridade, Control executa, Topology contextualiza
- Usos principais:
  - operador: priorização e leitura de fragilidade estrutural
  - DevOps: investigação autenticada, health, logs, runtime e eventos
  - arquitetura: governança da malha e leitura de risco sistêmico
- Regras importantes:
  - não confundir superfície visual com verdade operacional
  - não tratar snapshot como estado live
  - não desproteger API só para facilitar interface

### `neo-dashboard-console`

- Papel: console autenticado de runtime
- Tese central: `Stack Analyzer` é o painel principal; `Control Console` é a camada de controle
- Capacidades percebidas:
  - sinais live
  - logs
  - eventos
  - ações operacionais
  - quick actions como health check, kernel status, report e runbook
- Relação com outras superfícies:
  - `Analyzer`: priorização estrutural
  - `Control`: runtime autenticado
  - `Topology`: inspeção visual da malha

## Próximos registros sugeridos

- outras páginas públicas do mesmo dashboard
- guias equivalentes de operação, deploy, incidentes e arquitetura
- páginas que combinem estado live, snapshot e ação autenticada

## Fonte estruturada

Este documento é a visão humana. A fonte estruturada correspondente está em:

- [GUIAS_REFERENCIA.json](./GUIAS_REFERENCIA.json)
````

## File: docs/governanca/CONTRATO_AGENTES.md
````markdown
# CONTRATO DOS AGENTES

Status: ativo  
Última atualização: 2026-04-02

## Propósito

Este documento define o contrato operacional de cada agente do sistema.

Ele existe para impedir três formas de mentira estrutural:

1. agente sem fronteira clara
2. agente com autoridade maior do que sua governança
3. agente publicando ou alterando estado sem trilha explícita

O objetivo não é descrever intenções abstratas.  
O objetivo é fixar função, entrada, saída, memória, autoridade, limites e futuro de integração com Sanity e publicação pública.

## Princípios

- Redis é a memória quente e operacional
- Sanity é a governança semântica e editorial
- Notion é a entrada humana e a captura bruta
- `mypersonal_multiagents` é o orquestrador do kernel privado
- `nettomello.eth.limo` só recebe artefatos explicitamente promovidos
- IPFS entra no final do fluxo público, nunca no início da modelagem
- nenhum agente publica algo público por conta própria

## Matriz Rápida

| Agente              |  Usa LLM | Lê Redis | Escreve Redis | Lê Sanity | Escreve Sanity | Lê Notion | Escreve Notion | Pode publicar |
| ------------------- | -------: | -------: | ------------: | --------: | -------------: | --------: | -------------: | ------------: |
| `orchestrator`      |      sim |      sim |      indireto |       sim |            não |       não |            não |           não |
| `focus_guard`       |      sim |      sim |           sim |       sim |            não |       sim |            não |           não |
| `scheduler`         |      sim |      sim |           sim |       sim |            não |       não |            não |           não |
| `validator`         |      sim |      sim |           sim |       sim |            não |       sim |            sim |           não |
| `retrospective`     |      sim |      sim |           não |       sim |            não |       sim |            sim |           não |
| `notion_sync`       |      não |      sim |           sim |   parcial |            não |       sim |            sim |           não |
| `calendar_sync`     |      não |      sim |           sim |   parcial |            não |       não |            não |           não |
| `life_guard`        |      não |      sim |           sim |   parcial |            não |       não |            não |           não |
| `ecosystem_monitor` |      não |      sim |           sim |   parcial |            não |       não |            não |           não |
| `persona_manager`   |      não |      não |           não |       sim |            não |       não |            não |           não |
| `gemma_local`       | fallback |      não |           não |   parcial |            não |       não |            não |           não |

## Contrato Recomendado, Agente por Agente

### `orchestrator`

Arquivo: `agents/orchestrator.py`

Função:

- interpretar intenção do usuário
- escolher handoffs
- consolidar resposta final

Entradas:

- input do usuário
- contexto agregado
- persona ativa
- estado resumido do sistema

Saídas:

- lista de handoffs
- síntese final em linguagem natural

Memória:

- lê Redis para contexto resumido
- não deve persistir artefatos próprios além de handoffs e observabilidade

Autoridade:

- pode delegar
- não deve alterar estado de negócio diretamente
- não publica

Governança desejada no Sanity:

- prompt `routing`
- prompt `synthesis`
- prompt `direct`
- policy de fallback

Estado atual:

- usa LLM
- prompts `routing`, `synthesis` e `direct` governados pelo Sanity com fallback explícito
- depende de personas resolvidas por `persona_manager`

Risco atual:

- ainda governa fallback e política de provider mais no código do que no Studio

### `focus_guard`

Arquivo: `agents/focus_guard.py`

Função:

- monitorar foco, desvio e sessões
- disparar check-ins
- reagendar quando necessário

Entradas:

- agenda do dia
- sessão ativa
- tarefas em andamento
- dados do Notion quando necessário

Saídas:

- alertas
- logs de desvio
- reschedules
- status de foco

Memória:

- lê e escreve Redis intensamente

Autoridade:

- pode alertar
- pode reagendar automaticamente dentro de regras
- não publica

Governança desejada no Sanity:

- prompt `deviation`
- configuração de intervalo
- scripts de intervenção
- thresholds de escalada

Estado atual:

- lê prompt de desvio do Sanity
- lê scripts de intervenção do Sanity por ambiente com fallback local
- é o agente mais maduro na camada de governança

Risco atual:

- ainda conserva fallback local para não quebrar operação se o Studio falhar

### `scheduler`

Arquivo: `agents/scheduler.py`

Função:

- gerir agenda
- sugerir blocos
- priorizar tarefas
- reorganizar dia útil

Entradas:

- tarefas
- blocos existentes
- contexto temporal

Saídas:

- blocos de agenda
- sugestões de priorização
- warnings de sobrecarga

Memória:

- lê e escreve Redis

Autoridade:

- pode criar blocos
- pode completar blocos
- pode propor agenda via LLM
- não publica

Governança desejada no Sanity:

- prompt `scheduling`
- policy de duração mínima
- policy de pausas
- parâmetros de conflito e carga

Estado atual:

- usa LLM
- prompt `scheduling` governado pelo Sanity com fallback explícito
- config publicada no Studio

Risco atual:

- parâmetros semânticos de carga, pausa e conflito ainda vivem mais no código do que no Studio

### `validator`

Arquivo: `agents/validator.py`

Função:

- confirmar se uma tarefa foi realmente concluída
- cruzar evidências
- evitar conclusão performática

Entradas:

- tarefa local
- sessões de foco
- blocos de agenda
- espelho do Notion

Saídas:

- `validated`
- `rejected`
- `pending_confirmation`

Memória:

- lê e escreve Redis
- pode refletir status no Notion

Autoridade:

- pode consolidar veredicto
- pode atualizar Notion quando o contrato permitir
- não publica

Governança desejada no Sanity:

- prompt `validation`
- policy de thresholds
- regras de consistência

Estado atual:

- usa LLM
- prompt `validation` governado pelo Sanity com fallback explícito
- config publicada no Studio

Risco atual:

- thresholds de consistência e política de veredicto ainda não foram externalizados por completo

### `retrospective`

Arquivo: `agents/retrospective.py`

Função:

- ler a semana
- gerar análise e relatório
- opcionalmente enviar para Notion

Entradas:

- sessões
- tarefas
- handoffs
- histórico recente

Saídas:

- relatório markdown
- página opcional no Notion

Memória:

- lê Redis
- não precisa estado quente próprio

Autoridade:

- pode sintetizar
- pode escrever retrospectiva no Notion
- não publica automaticamente

Governança desejada no Sanity:

- prompt `retrospective`
- template editorial
- política de exportação

Estado atual:

- usa LLM
- prompt `retrospective` governado pelo Sanity com fallback explícito
- config publicada no Studio

Risco atual:

- política de exportação e template final ainda não estão externalizados por completo

### `notion_sync`

Arquivo: `agents/notion_sync.py`

Função:

- sincronizar tarefas e agenda com Notion
- normalizar input humano para o kernel

Entradas:

- databases do Notion
- tarefas locais
- blocos locais

Saídas:

- tarefas locais atualizadas
- blocos derivados
- páginas atualizadas no Notion

Memória:

- lê e escreve Redis

Autoridade:

- pode importar
- pode atualizar status
- não decide política semântica
- não publica

Governança desejada no Sanity:

- mapeamento de origem
- política de reconciliação
- parâmetros operacionais

Estado atual:

- não usa LLM
- `agent_config` publicado no Studio
- governança ainda majoritariamente implícita no código

Risco atual:

- reconciliador sem contrato explícito de precedência entre fontes

### `calendar_sync`

Arquivo: `agents/calendar_sync.py`

Função:

- integrar Google Calendar à agenda operacional como capacidade opcional

Entradas:

- eventos do calendário
- blocos locais

Saídas:

- importação de eventos como blocos
- exportação de blocos para o calendário

Memória:

- lê e escreve Redis

Autoridade:

- pode espelhar agenda quando a integração opcional estiver ativa
- não interpreta prioridade nem intenção
- não publica

Governança desejada no Sanity:

- parâmetros operacionais
- política de import/export
- mapeamento de calendário
  com precedência explícita do Notion Agenda

Estado atual:

- não usa LLM
- `agent_config` publicado no Studio
- integração ainda vive principalmente no código como capacidade opcional

Risco atual:

- integração opcional ainda vive fora da camada de governança

### `life_guard`

Arquivo: `agents/life_guard.py`

Função:

- lembrar rotinas vitais
- lembrar hidratação
- lembrar refeições
- controlar rotinas recorrentes de vida

Entradas:

- relógio
- estados de rotina no Redis

Saídas:

- notificações
- flags de rotina enviada

Memória:

- lê e escreve Redis

Autoridade:

- pode notificar
- não deve inferir sem contrato
- não publica

Governança desejada no Sanity:

- parâmetros operacionais
- scripts de rotina
- janela ativa
- canais e intensidade

Estado atual:

- não usa LLM
- `agent_config` e `persona` publicados no Studio
- parâmetros centrais ainda vivem em env e código

Risco atual:

- é um agente de vida, mas ainda sem configuração digna de agente

### `ecosystem_monitor`

Arquivo: `agents/ecosystem_monitor.py`

Função:

- monitorar ecossistema externo
- produzir sinais e resumo operacional
- manter health checks e relatório diário

Entradas:

- APIs externas e serviços críticos
- estado recente no Redis

Saídas:

- sinais em cache
- relatório diário
- alertas P0 quando necessário

Memória:

- lê e escreve Redis

Autoridade:

- pode produzir sinais e relatórios
- não altera agenda íntima
- não publica

Governança desejada no Sanity:

- `signal`, `source`, `decision`
- thresholds e severidade
- política de TTL e dedupe

Estado atual:

- runtime ativo em `agents/ecosystem_monitor.py`
- persiste `health_check` e `daily_report` no Redis
- schema documentado em `../arquitetura/SCHEMA_SIGNAL_DECISION.md`

Risco atual:

- sinais ainda vivem como cache e texto
- governança de thresholds ainda fora do Sanity

### `persona_manager`

Arquivo: `agents/persona_manager.py`

Função:

- selecionar a persona ativa
- fornecer `system_prompt` e temperatures por fase

Entradas:

- arquivos JSON locais
- `persona_id` solicitado

Saídas:

- persona resolvida
- overrides de prompt e temperatura

Memória:

- sem Redis

Autoridade:

- governa tom e estilo da camada de linguagem
- não publica

Governança desejada no Sanity:

- fonte canônica de personas
- histórico editorial
- versionamento leve

Estado atual:

- Sanity é a fonte primária de persona
- `personas/` virou fallback explícito de runtime

Risco atual:

- ainda falta fechar versionamento editorial e política explícita de override por fase

## Ordem Recomendada de Formalização

1. `ecosystem_monitor`
2. `notion_sync`
3. `calendar_sync`
4. `life_guard`
5. `gemma_local`

## Política de Publicação

Nenhum agente acima pode publicar diretamente em `nettomello.eth.limo`.

Fluxo correto:

1. agente produz sinal ou decisão
2. Redis registra o estado operacional
3. Sanity canoniza quando for memória estrutural
4. um item elegível vira `public_artifact`
5. revisão humana aprova
6. só então artefato pode seguir para IPFS e domínio público

## Papel do Gemma Local

Modelo local configurado:

- `docker.io/ai/gemma3:4B-F16`
- fallback em `core/openai_utils.py`

Papel recomendado:

- contingência quando OpenAI falhar
- tarefas de baixa criticidade editorial
- rascunhos operacionais
- classificação simples
- triagem local

Não usar como autoridade final para:

- síntese pública
- decisões de publicação
- validações críticas de conclusão
- artefatos destinados a `nettomello.eth.limo`

## Critério de Conclusão

Este contrato só estará realmente ativo quando:

- cada agente tiver instrução explícita ou decisão explícita de não usar instrução
- a governança do Sanity refletir o runtime real
- a fonte de verdade de persona estiver unificada
- a política privado -> público estiver documentada e implementada
````

## File: docs/governanca/MATRIZ_GOVERNANCA_AGENTES.md
````markdown
# MATRIZ DE GOVERNANÇA DOS AGENTES

Status: ativo  
Última atualização: 2026-04-03

## Propósito

Este documento existe para responder uma pergunta simples:

"A governança de cada agente já está suficientemente escrita
para o sistema parar de depender de memória humana?"

Resposta curta:

- alguns já estão fortes
- alguns ainda estão parciais
- nenhum deve ser tratado como "autoexplicativo"

## Legenda

- `FORTE`: já tem governança suficiente para operar sem
  improviso estrutural
- `PARCIAL`: existe governança, mas ainda há zonas críticas
  vivendo no código ou em configuração implícita
- `N/A`: a peça não precisa daquele tipo de governança

## Cobertura Atual

| Entidade            |  Usa LLM | agent_config |                   persona | llm_prompt | intervention_script | Cobertura | O que falta                                                                |
| ------------------- | -------: | -----------: | ------------------------: | ---------: | ------------------: | --------- | -------------------------------------------------------------------------- |
| `orchestrator`      |      sim |          sim | usa persona compartilhada |        sim |                 N/A | FORTE     | política de fallback por provider e guardrails de delegação                |
| `focus_guard`       |      sim |          sim |                       N/A |        sim |                 sim | FORTE     | remover fallback local quando o Studio estiver maduro o bastante           |
| `scheduler`         |      sim |          sim |                       N/A |        sim |                 N/A | FORTE     | externalizar parâmetros de carga, pausa e conflito                         |
| `validator`         |      sim |          sim |                       N/A |        sim |                 N/A | FORTE     | externalizar thresholds de consistência e veredicto                        |
| `retrospective`     |      sim |          sim | usa persona compartilhada |        sim |                 N/A | FORTE     | template final e política de exportação                                    |
| `notion_sync`       |      não |          sim |                       N/A |        N/A |                 N/A | PARCIAL   | política explícita de reconciliação e precedência                          |
| `calendar_sync`     |      não |          sim |                       N/A |        N/A |                 N/A | PARCIAL   | política de import/export e precedência do Notion                          |
| `life_guard`        |      não |          sim |                       sim |        N/A |                 N/A | PARCIAL   | scripts de rotina, janelas ativas e canais editáveis                       |
| `ecosystem_monitor` |      não |          sim |                       N/A |        N/A |                 N/A | PARCIAL   | sinal, source, decision e thresholds governados                            |
| `persona_manager`   |      não |          sim |                       sim |        N/A |                 N/A | PARCIAL   | versionamento editorial e política de override por fase                    |
| `gemma_local`       | fallback |          sim |                       sim |        N/A |                 N/A | PARCIAL   | política explícita de quando preferir local por intenção, não só por falha |

## Pacote Mínimo por Entidade

### `orchestrator`

- `agent_config`: sim
- `persona`: indireta, via `persona_manager`
- `llm_prompt`: `routing`, `synthesis`, `direct`
- `intervention_script`: não
- Falta: política explícita de provider e limites de delegação

### `focus_guard`

- `agent_config`: sim
- `persona`: não
- `llm_prompt`: `deviation`
- `intervention_script`: 30, 60, 120, 240 min
- Falta: maturar o Studio para reduzir fallback local

### `scheduler`

- `agent_config`: sim
- `persona`: não
- `llm_prompt`: `scheduling`
- `intervention_script`: não
- Falta: parâmetros de carga, pausas e conflito como dados

### `validator`

- `agent_config`: sim
- `persona`: não
- `llm_prompt`: `validation`
- `intervention_script`: não
- Falta: thresholds de consistência e política de veredicto

### `retrospective`

- `agent_config`: sim
- `persona`: indireta
- `llm_prompt`: `retrospective`
- `intervention_script`: não
- Falta: template final e política de exportação

### `notion_sync`

- `agent_config`: sim
- `persona`: não
- `llm_prompt`: não, por decisão explícita
- `intervention_script`: não
- Falta: reconciliação, precedência e mapeamento de origem

### `calendar_sync`

- `agent_config`: sim
- `persona`: não
- `llm_prompt`: não, por decisão explícita
- `intervention_script`: não
- Falta: política de import/export e operação como capacidade opcional

### `life_guard`

- `agent_config`: sim
- `persona`: sim
- `llm_prompt`: não, por decisão explícita atual
- `intervention_script`: ainda não
- Falta: transformar rotina, canal e janela ativa em governança editável

### `ecosystem_monitor`

- `agent_config`: sim
- `persona`: não
- `llm_prompt`: não
- `intervention_script`: não
- Falta: `signal`, `source`, `decision` no Sanity, thresholds, TTL e dedupe

### `persona_manager`

- `agent_config`: sim
- `persona`: sim
- `llm_prompt`: não
- `intervention_script`: não
- Falta: regras editoriais de override e versionamento leve

### `gemma_local`

- `agent_config`: sim
- `persona`: sim
- `llm_prompt`: não, por decisão explícita atual
- `intervention_script`: não
- Falta: política de ativação por intenção, custo e risco

## Veredito

A base de governança já existe para todos os agentes e
capacidades relevantes.

O que ainda falta não é "ter ou não ter instrução".
O que falta é elevar alguns agentes de governança
`PARCIAL` para governança `FORTE`.

Os cinco pontos que ainda pedem fechamento fino são:

1. `ecosystem_monitor`
2. `notion_sync`
3. `calendar_sync`
4. `life_guard`
5. `gemma_local`

Esse é o conjunto residual. O resto já saiu do terreno
da improvisação.
````

## File: docs/governanca/PLANO_SOBERANIA_SANITY.md
````markdown
# PLANO DE SOBERANIA DO SANITY

Status: autorizado
Última atualização: 2026-04-03

## Tese

Este plano existe para transformar o Sanity de
camada auxiliar de configuração em camada canônica
de governança e, depois, de modelagem semântica do
kernel privado.

O objetivo não é “usar CMS”.

O objetivo é construir uma arquitetura em que:

- Notion captura
- Redis opera
- Sanity governa
- `mypersonal_multiagents` orquestra
- `neo-mello-eth` publica

## Princípios de precedência

1. Notion é a origem principal de tarefas e agenda
2. Google Calendar é capacidade opcional
3. Redis é estado quente e operacional
4. Sanity é verdade semântica e editorial
5. Nenhum agente publica por conta própria
6. IPFS entra no final do fluxo público

## Fase 1 — Fechar governança dos agentes

Objetivo:

- representar todos os agentes relevantes no Sanity
  com padrão uniforme

Escopo:

- `agent_config`
- `persona`
- `llm_prompt`
- `intervention_script`

Agentes-alvo:

- `orchestrator`
- `focus_guard`
- `scheduler`
- `notion_sync`
- `validator`
- `retrospective`
- `calendar_sync`
- `life_guard`
- `persona_manager`
- `gemma_local`
- `ecosystem_monitor`

Critério de conclusão:

- nenhum agente importante fica sem representação
  explícita no Studio

Risco principal:

- criar documentos incompletos e chamar isso de
  governança

## Fase 2 — Eliminar duplas verdades

Objetivo:

- reduzir conflito entre código hardcoded e Sanity

Escopo:

- prompts
- personas
- políticas de intervenção
- parâmetros operacionais

Movimento esperado:

- Sanity vira fonte primária
- código mantém fallback explícito só onde for
  necessário para resiliência

Critério de conclusão:

- a governança dos agentes não depende mais de
  constantes espalhadas pelo runtime

Risco principal:

- metade da autoridade no código, metade no Studio

## Fase 3 — Formalizar precedência entre fontes

Objetivo:

- impedir ambiguidade estrutural de origem

Contrato:

- Notion Tasks = fonte principal de tarefas
- Notion Agenda = fonte principal de agenda
- Google Calendar = integração opcional
- Redis = execução corrente
- Sanity = interpretação e memória semântica

Critério de conclusão:

- docs, UI, contratos e código contam a mesma
  história

Risco principal:

- sistema dizer uma coisa e operar outra

## Fase 4 — Subir a camada de domínio

Objetivo:

- fazer o Sanity modelar o mundo, não só os agentes

Schemas-alvo:

- `project`
- `area`
- `task`
- `agenda_block`
- `focus_session`
- `signal`
- `decision`
- `source`
- `public_artifact`

Observação decisiva:

- `signal`, `source` e `decision` são a ponte entre
  o kernel íntimo e a órbita externa do
  `ecosystem_monitor`
- o monitor existe, mas deve operar com cache
  em Redis e promover sinais ao Sanity

Critério de conclusão:

- o Studio permitir navegar a operação como grafo,
  não só editar prompts
- o monitor externo ter onde pousar seus sinais sem
  virar log glorificado

Risco principal:

- despejar Redis no Sanity sem semântica

## Fase 5 — Construir a eclusa privado → público

Objetivo:

- impedir vazamento estrutural do kernel privado

Fluxo:

- kernel privado gera contexto
- Sanity classifica
- `public_artifact` marca elegibilidade
- revisão humana aprova
- `neo-mello-eth` distribui

Critério de conclusão:

- nada público sai sem gate explícito

Risco principal:

- misturar operação íntima com superfície pública

## Fase 6 — Posicionar IPFS no ponto certo

Objetivo:

- usar IPFS como distribuição pública, não como
  cérebro do sistema

Ordem correta:

- Sanity decide
- Publish Gate aprova
- `neo-mello-eth` publica
- IPFS/IPNI propagam

Critério de conclusão:

- IPFS participa da publicação, não da confusão
  semântica

Risco principal:

- empurrar CID cedo demais e chamar isso de
  arquitetura

## Fase 7 — Fechar observabilidade e notificações

Objetivo:

- distinguir geração de alerta de entrega real

Escopo:

- logs por canal
- entrega local macOS
- entrega Alexa em produção
- critérios de falha por ambiente

Critério de conclusão:

- cada alerta crítico tem trilha clara de geração,
  tentativa e entrega

Risco principal:

- backend parecer ativo enquanto o canal está mudo

## Ordem de execução

1. Governança dos agentes no Sanity
2. Remoção das duplas verdades
3. Precedência entre fontes
4. `signal/source/decision` como ponte semântica
5. Demais schemas de domínio
6. Eclusa privado → público
7. IPFS/IPNI no fim do pipeline
8. Observabilidade e entrega real

## Regra de disciplina

Nenhuma fase conta como concluída apenas porque:

- existe código
- existe tela
- existe draft
- existe intenção

Uma fase só fecha quando:

- o contrato está explícito
- o comportamento foi validado
- a fonte de verdade está definida
- a documentação não contradiz o runtime

## Próximo passo autorizado

Fechar a Fase 1 por completo:

- inventário final dos agentes
- padronização dos documentos do Sanity
- publicação apenas do núcleo governável
````

## File: docs/governanca/POLITICA_PRECEDENCIA_NOTION.md
````markdown
# POLÍTICA DE PRECEDÊNCIA DO NOTION

Status: ativo  
Última atualização: 2026-04-03

## Propósito

Este documento define quem vence quando `Notion`, `Redis`
e `Sanity` discordam sobre a mesma entidade.

Sem esta política, `notion_sync` vira reconciliador com
boa intenção e soberania acidental.

## Entidades cobertas

- `task`
- `agenda_block`
- status de execução
- horário previsto
- horário real
- decisão de publicação

## Regra-mãe

Cada camada governa uma classe diferente de verdade:

- `Notion` governa captura humana e intenção bruta
- `Redis` governa estado operacional do agora
- `Sanity` governa significado, memória estrutural e
  política editorial

Nenhuma camada deve fingir soberania fora do seu domínio.

## Precedência por tipo de dado

### 1. Captura humana

Exemplos:
- título digitado manualmente
- prioridade escolhida manualmente
- horário previsto escrito no Notion
- criação de tarefa ou bloco pela interface humana

Vencedor:
- `Notion`

Regra:
- se um campo nasceu como entrada humana explícita no
  Notion e ainda não foi reinterpretado pelo sistema,
  `notion_sync` deve importar, não corrigir

### 2. Estado operacional atual

Exemplos:
- tarefa em andamento
- tarefa vencida
- bloco concluído hoje
- sessão ativa
- alerta aberto

Vencedor:
- `Redis`

Regra:
- o runtime vence enquanto o fato estiver no presente
  operacional
- `notion_sync` não deve degradar estado quente para um
  status mais antigo vindo do Notion

Exemplo:
- tarefa em `Em progresso` no Redis
- Notion ainda mostra `A fazer`
- durante o sync, vence `Redis`

### 3. Significado semântico e memória estrutural

Exemplos:
- a tarefa pertence a qual projeto
- qual área ela serve
- se algo é privado, interno ou público
- que sinal virou decisão

Vencedor:
- `Sanity`

Regra:
- `notion_sync` não decide semântica estrutural
- ele só transporta e reconcilia captura humana e estado
  operacional

### 4. Publicação e exposição pública

Exemplos:
- algo pode ou não ir para `nettomello.eth.limo`
- algo pode ou não virar CID no IPFS

Vencedor:
- `Sanity`, via `public_artifact` e revisão humana

Regra:
- Notion nunca autoriza publicação
- Redis nunca autoriza publicação

## Regras por entidade

### `task`

Campos cujo vencedor padrão é `Notion`:
- `title`
- `priority`
- `scheduled_time` quando veio de input humano
- `notion_page_id`

Campos cujo vencedor padrão é `Redis`:
- `status` operacional atual
- `actual_time`
- flags de atraso ou vencimento

Campos cujo vencedor padrão é `Sanity`:
- `project_ref`
- `area_ref`
- `visibility`
- `public_eligibility`

### `agenda_block`

Campos cujo vencedor padrão é `Notion`:
- data criada manualmente
- texto-base do bloco

Campos cujo vencedor padrão é `Redis`:
- concluído ou aberto no dia corrente
- overdue
- bloco derivado automaticamente para hoje

Campos cujo vencedor padrão é `Sanity`:
- classificação estrutural
- vínculo editorial
- elegibilidade pública

## Tabela de decisão

| Situação | Vence | Ação do `notion_sync` |
|---|---|---|
| Tarefa nova existe no Notion e não existe localmente | Notion | importar e criar local |
| Tarefa existe localmente e no Notion, mas o status diverge | Redis | preservar estado local e refletir no Notion quando permitido |
| Título diverge entre Notion e Redis | Notion | atualizar título local |
| Prioridade diverge entre Notion e Redis | Notion | atualizar prioridade local |
| Campo semântico diverge entre Notion e Sanity | Sanity | não sobrescrever semântica a partir do Notion |
| Bloco do dia foi criado automaticamente pelo sistema | Redis | manter como estado quente e opcionalmente refletir depois |
| Item marcado público no Notion sem `public_artifact` | Sanity | ignorar intenção de publicação até revisão humana |

## Regras de reconciliação

### Sync Notion -> Redis

Permitido:
- importar novos itens
- atualizar campos de captura humana
- enriquecer com `notion_page_id`

Não permitido:
- rebaixar `status` operacional
- apagar efeitos do runtime
- sobrescrever semântica canônica

### Sync Redis -> Notion

Permitido:
- refletir status operacional
- refletir horário real
- criar bloco derivado quando a regra do sistema pedir

Não permitido:
- reescrever título humano sem motivo explícito
- inventar prioridade
- promover publicação

### Sync Sanity -> runtime

Permitido:
- governar semântica
- governar visibilidade
- governar relações de projeto e área

Não permitido:
- fingir estado quente de execução

## Resolução de conflitos

Quando houver conflito, `notion_sync` deve classificar o
campo antes de decidir.

Sequência obrigatória:

1. identificar o tipo do campo
2. identificar a camada soberana daquele campo
3. preservar o valor soberano
4. registrar conflito relevante em log
5. opcionalmente emitir `signal` quando houver ambiguidade
   recorrente

## Casos que devem virar `signal`

- Notion tenta rebaixar status operacional repetidamente
- Notion muda título ou prioridade em alta frequência
- bloco derivado local conflita com agenda humana
- item semântico vindo do Notion contradiz `Sanity`
- mesmo item entra em conflito mais de 3 vezes em 24h

## Política de logs

`notion_sync` deve registrar:
- importações novas
- atualizações aceitas
- atualizações rejeitadas por precedência
- conflitos recorrentes

Formato desejado:

```text
[notion_sync] precedence=redis field=status local="Em progresso" notion="A fazer" action=preserved_local
```

## Critério de conclusão

Esta política só estará realmente ativa quando:

- `notion_sync` classificar campos por soberania
- conflitos relevantes virarem log explícito
- testes cobrirem divergência entre `Notion` e `Redis`
- a precedência estiver refletida no código, e não só neste
  documento
````

## File: docs/operacao/MANUAL_DEV.md
````markdown
# Manual do Desenvolvedor — Multiagentes PWA

## Stack

- **Backend**: Python 3.11+ / FastAPI / Uvicorn
- **Frontend**: Jinja2 templates + HTMX 1.9 (zero JS framework)
- **Persistencia**: Redis (Railway em produção, localhost em dev) — sem SQLite
- **Agentes**: OpenAI GPT via orchestrator, Focus Guard, Scheduler, Notion Sync, Calendar Sync, Validator, Retrospective, Life Guard, Persona Manager
- **Config externa**: Sanity.io (prompts, personas, agent config) via `core/sanity_client.py`
- **Notificações**: macOS push (osascript), Alexa (Voice Monkey)
- **Deploy**: Railway (Dockerfile) ou local

## Estrutura de arquivos relevantes

```
web/
  app.py                    # FastAPI app — todas as rotas
  templates/
    base.html               # Layout base: header, content, tab bar, PWA meta
    index.html              # Home/dashboard
    agenda.html             # Agenda com filtro de datas
    audit.html              # Audit trail completo
    tasks_page.html         # Pagina dedicada de tarefas
    chat_page.html          # Chat full-screen com orchestrator
    partials/
      agenda.html           # Lista de blocos (include)
      block_row.html        # Linha individual de bloco
      tasks.html            # Lista de tarefas (include)
      task_row.html         # Linha individual de tarefa
      chat_message.html     # Par user/bot de mensagem
      status.html           # Status partial (legacy, pode remover)
  static/
    manifest.json           # PWA manifest
    sw.js                   # Service worker (cache + push handler)
    icon-192.png            # Icone PWA 192x192
    icon-512.png            # Icone PWA 512x512
    favicon.ico             # Favicon
```

## Rotas

| Metodo | Path | Template | Descricao |
|--------|------|----------|-----------|
| GET | `/` | index.html | Dashboard principal |
| GET | `/agenda` | agenda.html | Agenda com filtro (tambem responde HTMX partial) |
| GET | `/tasks-page` | tasks_page.html | Pagina de tarefas |
| GET | `/chat-page` | chat_page.html | Chat full-screen |
| GET | `/audit` | audit.html | Audit trail |
| POST | `/chat` | partials/chat_message.html | HTMX — envia mensagem ao orchestrator |
| POST | `/sync` | HTMLResponse inline | HTMX — sync com Notion |
| POST | `/task` | partials/tasks.html | HTMX — cria tarefa |
| POST | `/task/{id}/complete` | partials/task_row.html | HTMX — completa tarefa |
| POST | `/block/{id}/complete` | partials/block_row.html | HTMX — completa bloco |
| POST | `/agenda/import` | agenda.html | Importa blocos de Notion/Calendar |
| GET | `/tasks` | partials/tasks.html | HTMX partial — lista de tarefas |
| GET | `/health` | JSON | Health check |

## Design system

Todas as variaveis CSS estao em `base.html` no `:root`. Principais:

```css
--bg: #000           /* fundo principal */
--s1: #0a0a0a        /* surface 1 (header/footer bg) */
--s2: #141414        /* surface 2 (cards) */
--s3: #1c1c1e        /* surface 3 (inputs, pills) */
--s4: #2c2c2e        /* surface 4 (avatars) */
--s5: #3a3a3c        /* surface 5 (borders fortes) */
--blue: #0a84ff      /* accent primario */
--green: #30d158     /* sucesso / ativo */
--red: #ff453a       /* erro / alerta */
--yell: #ffd60a      /* warning / prioridade media */
--cyan: #64d2ff      /* timestamps */
--font: SF Pro        /* texto */
--mono: SF Mono       /* numeros, timestamps, logs */
```

## Componentes CSS

| Classe | Uso |
|--------|-----|
| `.card` | Container com borda e border-radius |
| `.card-hd` | Header do card com label + action |
| `.metrics` | Grid 2x2 de metric cards |
| `.metric` | Card individual de metrica com barra colorida no topo |
| `.blk` | Linha de bloco de agenda |
| `.tsk` | Linha de tarefa |
| `.ls-item` | Item generico de lista (audit events, alertas, handoffs) |
| `.badge-ok/warn/err/def` | Badges semanticos |
| `.toast` | Toast de feedback |
| `.section-title` | Titulo de secao (22px bold) |
| `.form-row` | Linha de formulario com flex wrap |
| `.add-bar` | Barra de criacao de tarefa |

## Tab bar

A tab bar usa SVG icons inline (24x24, stroke-based). Cada tab e um `<a>` com classe `.tab`. A tab ativa recebe `.active` (cor azul).

O badge de notificacao (`.tab-badge`) e renderizado server-side com base em `summary.alerts.pending`.

## PWA

### manifest.json

- `display: standalone` — abre sem barra do browser
- `orientation: portrait`
- Icons 192 e 512

### Service worker (sw.js)

- **Cache**: precache de `/` e manifest. Static files = cache-first, HTML/API = network-first com fallback
- **Push**: handler pronto em `self.addEventListener('push', ...)` — aceita JSON com `{title, body, tag, url}`
- **Notification click**: abre/foca a URL do payload

### Para ativar push notifications no futuro:

1. Gerar par de chaves VAPID (`npx web-push generate-vapid-keys`)
2. Adicionar endpoint no backend para subscription (`POST /push/subscribe`)
3. No frontend, pedir permissao e enviar subscription ao backend
4. No scheduler/notifier, usar `pywebpush` para enviar

## HTMX

- Todas as interacoes usam HTMX (hx-post, hx-get, hx-target, hx-swap)
- Swap cirurgico: completar tarefa troca so a linha (`hx-swap="outerHTML"`)
- Indicadores de loading via `hx-indicator`
- Erros capturados globalmente via `htmx:responseError` e `htmx:sendError`

## Rodar local

```bash
# Ativar venv
source .venv/bin/activate

# Rodar servidor
python -m web.app
# ou
uvicorn web.app:app --reload --port 8000

# Acessar
open http://localhost:8000
```

## Variáveis de ambiente necessarias

Referência completa em `.env.example` na raiz do projeto. Resumo:

```
# Obrigatório
OPENAI_API_KEY=          # Para o orchestrator (chat)
NOTION_TOKEN=            # Para sync com Notion
NOTION_TASKS_DB_ID=      # Database de tarefas no Notion
NOTION_AGENDA_DB_ID=     # Database de agenda no Notion

# Infraestrutura
REDIS_URL=               # Redis (Railway ou local)
LOG_FILE=                # Arquivo de log
LOG_LEVEL=               # DEBUG/INFO/WARNING/ERROR
WEB_HOST=                # Host do FastAPI (default: 127.0.0.1)
WEB_PORT=                # Porta do FastAPI (default: 8000)

# Google Calendar opcional
GOOGLE_CREDENTIALS_FILE= # OAuth credentials para integração opcional
GOOGLE_TOKEN_FILE=       # Token OAuth para integração opcional

# Sanity.io
SANITY_PROJECT_ID=       # Project ID
SANITY_API_TOKEN=        # Token Viewer
SANITY_DATASET=          # Dataset (default: production)

# Notificações
VOICE_MONKEY_TOKEN=      # Alexa via Voice Monkey

# Life Guard
LIFE_GUARD_ACTIVE_HOUR_START=  # Hora início (default: 8)
LIFE_GUARD_ACTIVE_HOUR_END=    # Hora fim (default: 22)
LIFE_GUARD_WATER_INTERVAL=     # Minutos entre lembretes de água (default: 90)
```

## Deploy (Railway)

O projeto tem `Dockerfile`, `Procfile` e `railway.json` configurados. O deploy e automatico via push no branch main.

## Adicionar nova pagina/tab

1. Criar template em `web/templates/nova_page.html` extendendo `base.html`
2. Adicionar rota GET em `web/app.py` passando `page_name` e `summary` no contexto
3. Adicionar tab no `base.html` (dentro de `<nav class="tabs">`) com SVG icon
4. Adicionar condicional `{% if page_name == 'nova' %} active{% endif %}` na tab

## Adicionar novo metric card

No template desejado, dentro de `.metrics`:
```html
<div class="metric m-blue">
  <div class="metric-lbl">Label</div>
  <div class="metric-val v-blue">42</div>
  <div class="metric-sub">descricao</div>
</div>
```

Classes de cor: `m-blue`, `m-green`, `m-red`, `m-dim` (barra top) e `v-blue`, `v-green`, `v-red`, `v-dim` (valor).
````

## File: docs/operacao/MANUAL_USUARIO.md
````markdown
# Manual do Usuario — Multiagentes PWA

## O que e

App mobile (PWA) para gerenciar seu sistema de agentes pessoais. Controla tarefas, agenda, foco e comunicacao com o orchestrator — tudo pelo celular.

## Instalar no celular

### iPhone (Safari)
1. Abra o endereco do app no Safari (ex: `https://seu-dominio.railway.app`)
2. Toque no botao de compartilhar (quadrado com seta para cima)
3. Role para baixo e toque em **Adicionar a Tela de Inicio**
4. Confirme o nome e toque em **Adicionar**
5. O app aparece como icone na home screen e abre em tela cheia

### Android (Chrome)
1. Abra o endereco no Chrome
2. Toque no menu (tres pontos) no canto superior direito
3. Toque em **Instalar app** ou **Adicionar a tela inicial**
4. Confirme

## Navegacao

O app tem 5 abas na parte inferior:

| Aba | Funcao |
|-----|--------|
| **Home** | Dashboard com metricas, agenda do dia e tarefas |
| **Agenda** | Historico de blocos com filtro por data e importacao |
| **Tarefas** | Criar e gerenciar tarefas com prioridade |
| **Chat** | Conversar com o orchestrator (IA) |
| **Audit** | Eventos do sistema, alertas, handoffs e logs |

## Home

- Mostra greeting contextual (Bom dia / Boa tarde / Boa noite)
- 4 cards de metricas: tarefas a fazer, blocos da agenda, status do foco, alertas pendentes
- Card de **Agenda hoje** com blocos do dia — toque no check para marcar como concluido
- Card de **Tarefas** com link para ver todas

## Agenda

- Filtre por intervalo de datas usando os campos de data e o botao **Filtrar**
- Importe blocos do **Notion** como fonte principal ou do **Google Calendar** como fonte opcional no intervalo selecionado
- Cada bloco mostra status: aberto, concluido ou reagendado

## Tarefas

- Digite o titulo, escolha prioridade (! = Alta, losango = Media, losango vazio = Baixa)
- Toque **+** para criar
- Toque no circulo com check para marcar como concluida
- Prioridade alta aparece com ponto vermelho, media com amarelo, baixa com cinza

## Chat

- Converse com o orchestrator em linguagem natural
- Pergunte sobre status, peca para reagendar, crie tarefas por texto
- O chat mantem historico da sessao (ate 12 turnos)

## Audit

- **Badge vermelho** na aba indica alertas pendentes
- Veja eventos de auditoria (checks do Focus Guard, reagendamentos)
- Historico de alertas gerados pelo sistema
- Handoffs entre agentes
- Log bruto do sistema

## Sync

- O botao **Sync** no header sincroniza tarefas com o Notion
- Aparece um toast verde confirmando quantas tarefas foram sincronizadas

## Header

- **Guard** com ponto verde = Focus Guard ativo e monitorando
- **Guard** com ponto vermelho = Focus Guard desligado
- Relogio atualizado automaticamente

## Life Guard — Rotinas Pessoais

O sistema monitora rotinas diarias automaticamente via Focus Guard:

| Rotina | Horario | Canal |
|--------|---------|-------|
| Exercicio | 07:00 | Mac push |
| Banho | 10:00 | Mac push |
| Almoco | 12:30 | Mac push + Alexa |
| Jantar | 19:30 | Mac push |
| Agua | cada 90 min (8h-22h) | Mac push |

Para confirmar uma rotina feita: `python main.py fiz banho` (ou exercicio, almoco, jantar).

Para ver status do dia: `python main.py vida`.

Para registrar conta a pagar: `python main.py pagar Cartao XP dia 15 valor 1200` — alerta 3 dias antes do vencimento.

## Notificacoes

O sistema envia notificacoes ativas via:

- **macOS push** — pop-up no canto da tela (osascript)
- **Alexa** — anuncio por voz via Voice Monkey

Alertas automaticos:

- Sessao de foco ha 30 min → mac push
- Sessao de foco ha 1 hora → mac push com som
- Sessao de foco ha 2 horas → mac push + Alexa
- Sessao de foco ha 4 horas → mac push + Alexa ("sai do computador")
- Rotinas diarias nos horarios configurados
- Financas proximas do vencimento

(Web Push e Telegram planejados para versao futura)

## Dicas

- O app funciona offline para navegacao basica (cache do service worker)
- Para forcar atualizacao, puxe a pagina para baixo ou toque **Atualizar** nos cards
- Se o app parecer desatualizado apos deploy, limpe o cache do navegador
````

## File: docs/operacao/redis-weekly-check.md
````markdown
# Redis na Railway: checklist simples de 5 minutos

Use este passo a passo 1 vez por semana.

## 1) Abra esta tela

1. Railway > Projeto > serviço `Redis`.
2. Clique na aba `Database`.
3. Clique em `Stats`.

## 2) Veja só 4 números

1. `Connected Clients`:
   Se estiver parecido com o normal (exemplo: 2, 3, 4), está ok.
2. `Evicted Keys`:
   Tem que estar `0`.
3. `Slow Log Entries`:
   Ideal `0`.
4. `Hit Rate`:
   Bom: acima de `85%`.
   Ótimo: acima de `90%`.

## 3) Veja os logs de deploy

1. Clique em `Deploy`.
2. Procure por `BGSAVE done` e `DB saved on disk`.
3. Se só aparece isso, está saudável.
4. Se aparecer `error`, `OOM`, `MISCONF` ou `failed`, é alerta.

## 4) Valide no app (30 segundos)

1. Abra `https://mypersonal-multiagents.up.railway.app/health`.
2. Abra `https://mypersonal-multiagents.up.railway.app/status`.
3. Se ambos responderem normal, front e Redis estão conversando.

## 5) O que não fazer sem combinar antes

1. Não clicar em limpar tudo.
2. Não rodar `FLUSHDB` ou `FLUSHALL`.
3. Não apagar chaves em massa.

## Regra de decisão rápida

1. `Evicted Keys > 0` ou `Slow Log Entries` subindo:
   abrir investigação.
2. Sem erros e com `BGSAVE done`:
   manter como está.
````

## File: docs/planejamento/NEXTSTEPS.md
````markdown
# NEXTSTEPS

Status: ativo  
Última atualização: 2026-04-03

## Como este documento deve ser usado

Este arquivo é o trilho de execução do projeto.

Nenhuma frente deve ser considerada concluída sem:

1. checkbox marcado
2. nota curta em `Log`
3. referência do commit em `Commit`

Formato obrigatório ao finalizar um item:

- `Status`: `DONE`
- `Log`: o que foi feito, em 1 a 3 linhas
- `Commit`: hash curto, link da PR, ou link do commit

Se não houve commit ainda, escrever:

- `Commit`: `pendente`

## Regra de Execução

- não pular etapa
- não abrir nova frente sem fechar a anterior ou registrar bloqueio
- sempre registrar o que foi decidido
- toda decisão estrutural precisa deixar rastro

## Fila Safe de Commit/Push

### Pode entrar no commit seguro

- `config.py`
- `Dockerfile`
- `.devcontainer/devcontainer.json`
- `agents/notion_sync.py`
- `core/memory.py`
- `core/notifier.py`
- `sanity/schemaTypes/persona.js`
- `tests/test_calendar_sync.py`
- `tests/test_memory.py`
- `tests/test_notifier_openai_utils.py`
- `tests/test_notion_sync.py`
- `tests/test_persona_manager.py`
- `tests/test_retrospective.py`
- `tests/test_scheduler.py`
- `tests/test_validator.py`
- `tests/test_web_chat.py`
- `web/app.py`
- `web/templates/base.html`
- `web/templates/index.html`
- `web/templates/partials/block_row.html`
- `web/templates/partials/status.html`
- `web/templates/partials/task_row.html`
- `web/templates/tasks_page.html`
- `docs/governanca/CONTRATO_AGENTES.md`
- `docs/planejamento/NEXTSTEPS.md`
- `docs/planejamento/SPRINT_VIDA.md`

### Não deve entrar no commit seguro

- `.claude/settings.local.json`
- `dump.rdb`

Motivo:

- arquivo local de ferramenta
- artefato de estado
- aumenta ruído e acopla ambiente pessoal ao repo

### Higiene ainda pendente

- adicionar `.DS_Store` ao `.gitignore` se aparecer novamente
- avaliar se `dump.rdb` deve ser removido do versionamento, não só ignorado
- Redis local migrado de Docker para brew service nativo (`redis 8.6.2`) em 2026-04-06 — Docker não é mais necessário para notificações locais

## Análise de Portas Abertas

Leitura em 2026-04-02:

- `8000` em `127.0.0.1`
  - esperado
  - é a Web UI local

- `6379`
  - esperado
  - Redis local ativo

- `4001`
  - esperado
  - swarm/libp2p do IPFS

- `5001`
  - esperado
  - API local do IPFS

- `8082`
  - esperado
  - gateway local do IPFS

- `36207`, `36865`, `34869`, `39194`, `34643`, `39850`
  - ruído controlado
  - portas efêmeras do Dev Container, VS Code Server e auto-forward

- `5000` e `7000`
  - não parecem ser do projeto
  - pertencem a `ControlCe`
  - devem ser identificadas antes de qualquer abertura pública ou automação sobre essas portas

Conclusão:

- não há ruído crítico nas portas do projeto
- há ruído ambiental de tooling
- o que importa de verdade hoje é `8000`, `6379`, `4001`, `5001`, `8082`

## Papel do Gemma Local

Modelo local detectado:

- `docker.io/ai/gemma3:4B-F16`
- configurado em `config.py`
- fallback implementado em `core/openai_utils.py`

Diretriz:

- o Gemma local deve ser tratado como agente de contingência e triagem
- ele reduz dependência da OpenAI para tarefas de baixo risco
- ele não deve ser usado como juiz final de publicação ou validação crítica

Usos recomendados:

- classificação simples
- rascunho inicial
- sumarização operacional
- fallback local quando OpenAI falhar
- tarefas internas de baixa criticidade

Usos não recomendados:

- síntese editorial pública
- decisões de publicação em `nettomello.eth.limo`
- validação final de conclusão
- arbitragem semântica de alto impacto

## Trilha de Execução

### Fase 0. Estabilizar a base atual

- [x] Fazer commit seletivo do estado seguro
  - Status: DONE
  - Log: commit seguro criado com runtime, testes, docs de governança e higiene mínima de repo.
  - Commit: `c60b547`

- [x] Fazer push do estado seguro para `main`
  - Status: DONE
  - Log: branch intermediária foi consolidada, `main` foi limpo e os avanços relevantes voltaram para a linha principal do repositório.
  - Commit: `b60190d`

- [x] Publicar branch segura com o estado consolidado
  - Status: DONE
  - Log: branch `neonode-codex/stabilize-runtime-governance` criada e publicada no remoto com o commit seguro.
  - Commit: `c60b547`

- [x] Confirmar Railway estável após push
  - Status: DONE
  - Log: health check respondeu `db: ok`, sync com Notion trouxe tarefa real e a interface no Railway refletiu agenda e tarefa sincronizadas.
  - Commit: pendente

- [x] Fechar contrato operacional de notificações
  - Status: DONE
  - Log: diagnóstico fechado. `focus_guard` gera alerta no Railway, mas `mac_push` não funciona fora de macOS e Alexa depende de `VOICE_MONKEY_*`. Observabilidade do `notifier` foi reforçada e `docs/planejamento/SPRINT_VIDA.md` reescrito para distinguir local versus Railway.
  - Commit: pendente

- [x] Corrigir confiabilidade do chat web (contexto + resposta operacional)
  - Status: DONE
  - Log: chat passou a persistir histórico por sessão no Redis com TTL e fallback local, recebeu rota determinística para perguntas sobre capacidade do deploy e proteção anti-resposta papagaio.
  - Commit: `59250b9`, `5c6af40`, `0ac0cc6`

- [ ] Validar UX do chat no iPhone após deploy Railway
  - Status: TODO
  - Log: confirmar se input limpa após envio, se contexto persiste após refresh e se respostas de capacidade do sistema não caem em texto genérico.
  - Commit: pendente

### Fase 1. Governança dos agentes

- [x] Criar contrato recomendado, agente por agente
  - Status: DONE
  - Log: criado documento de contrato com função, entradas, saídas, memória, autoridade, riscos e ordem de formalização dos agentes.
  - Commit: `c60b547`

- [x] Revisar e aprovar contrato dos agentes
  - Status: DONE
  - Log: contrato lido, tensionado e validado como base da governança dos agentes, com separação clara entre kernel íntimo e camadas futuras.
  - Commit: pendente

- [x] Identificar quais prompts deixam de ser hardcoded e passam a ser governados pelo Sanity
  - Status: DONE
  - Log: mapeados os agentes com dependência real de LLM e os pontos onde a autoridade ainda está dividida entre código e Studio.
  - Commit: pendente

### Fase 2. Sanity v2

- [x] Alinhar `llm_prompt` com os agentes reais
  - Status: DONE
  - Log: `llm_prompt` foi reduzido ao conjunto real de entidades com uso de LLM, os prompts de `orchestrator`, `scheduler`, `validator`, `retrospective` e `focus_guard` foram publicados no Sanity, e o runtime passou a ler esses documentos com fallback explícito.
  - Commit: `679f390`

- [x] Alinhar `agent_config` com os agentes reais
  - Status: DONE
  - Log: `agent_config` foi alinhado ao catálogo real de agentes e capacidades, com publicação no Studio dos registros de governança para `focus_guard`, `life_guard`, `gemma_local`, `orchestrator`, `scheduler`, `notion_sync`, `validator`, `retrospective`, `calendar_sync` e `persona_manager`.
  - Commit: `679f390`

- [x] Resolver fonte canônica de `persona`
  - Status: DONE
  - Log: `persona_manager` passou a ler o Sanity como fonte primária e o disco como fallback explícito, preservando compatibilidade do runtime e eliminando a dupla verdade como regra operacional.
  - Commit: `679f390`

- [x] Definir schema de domínio `project`
  - Status: DONE
  - Log: schema `project` criado no Studio para modelar iniciativas estruturais, com campos de status, visibilidade, links e relações.
  - Commit: `679f390`

- [x] Definir schema de domínio `area`
  - Status: DONE
  - Log: schema `area` criado no Studio para separar áreas de vida e operação como camada semântica própria.
  - Commit: `679f390`

- [x] Definir schema de domínio `task`
  - Status: DONE
  - Log: schema `task` criado no Studio para representar tarefas canônicas com precedência semântica sobre o estado quente do Redis.
  - Commit: `679f390`

- [x] Definir schema de domínio `agenda_block`
  - Status: DONE
  - Log: schema `agenda_block` criado no Studio para consolidar blocos de agenda como entidades próprias, distintas da renderização efêmera do dia.
  - Commit: `679f390`

- [x] Definir schema de domínio `focus_session`
  - Status: DONE
  - Log: schema `focus_session` criado no Studio para capturar sessões de foco, desvio e outcome como histórico operacional interpretável.
  - Commit: `679f390`

- [x] Definir schema de domínio `signal`
  - Status: DONE
  - Log: schema definido no Studio e alinhado ao `docs/arquitetura/SCHEMA_SIGNAL_DECISION.md` como base da órbita externa do kernel.
  - Commit: `679f390`

- [x] Definir schema de domínio `source`
  - Status: DONE
  - Log: schema definido no Studio e alinhado ao `docs/arquitetura/SCHEMA_SIGNAL_DECISION.md` para distinguir origem estrutural de evento.
  - Commit: `679f390`

- [x] Definir schema de domínio `decision`
  - Status: DONE
  - Log: schema definido no Studio e alinhado ao `docs/arquitetura/SCHEMA_SIGNAL_DECISION.md` para consolidar sinais em resposta governável.
  - Commit: `679f390`

- [x] Definir schema de domínio `public_artifact`
  - Status: DONE
  - Log: schema `public_artifact` criado no Studio para sustentar a futura eclusa privado -> público sem vazamento direto do kernel íntimo.
  - Commit: `679f390`

- [x] Concluir Fase 2. Sanity v2
  - Status: DONE
  - Log: governança dos agentes consolidada no Sanity, Studio redeployado com schemas de domínio, runtime conectado ao Studio para prompts, personas e scripts de intervenção, e documentos-base publicados no dataset `production`.
  - Commit: `679f390`

### Fase 3. Fronteira privado -> público

- [ ] Desenhar o contrato da aba `Publish` no front privado
  - Status: TODO
  - Log:
  - Commit: pendente

### Fase 4. Órbita externa do kernel

- [x] Versionar configuração do ecossistema
  - Status: DONE
  - Log: criado `config/ecosystem.yml` com orgs, fontes, modo `pull_first`, TTL e política de publicação externa.
  - Commit: pendente

- [x] Definir thresholds explícitos do monitor externo
  - Status: DONE
  - Log: criado `config/alert_thresholds.yml` com limiares para GitHub, Railway, Vercel, Cloudflare e NEOFLW.
  - Commit: pendente

- [x] Reposicionar `SPRINT_ECOSSISTEMA` como camada externa do kernel
  - Status: DONE
  - Log: sprint reescrito para separar sinais do ecossistema da camada íntima e impedir acoplamento com `focus_guard`.
  - Commit: pendente

- [x] Implementar Fase 1 do `ecosystem_monitor`
  - Status: DONE
  - Log: agente criado em `agents/ecosystem_monitor.py`. Cobre GitHub (6 orgs), Railway (6 serviços via HTTP health check), DexScreener (NEOFLW). Comando `python main.py ecosistema` funcional. Relatório persistido no Redis. Alertas P0 disparam mac_push.
  - Commit: pendente

- [ ] Definir gate automatizado para desbloquear Fase 2 do monitor
  - Status: TODO
  - Log:
  - Commit: pendente

- [ ] Definir política de promoção para `public_artifact`
  - Status: TODO
  - Log:
  - Commit: pendente

- [ ] Definir critérios de revisão humana obrigatória
  - Status: TODO
  - Log:
  - Commit: pendente

### Fase 4. IPFS e publicação

- [ ] Desenhar fluxo Sanity -> `public_artifact` -> IPFS
  - Status: TODO
  - Log:
  - Commit: pendente

- [ ] Definir quando gerar novo CID
  - Status: TODO
  - Log:
  - Commit: pendente

- [ ] Definir papel do IPNI na descoberta pública
  - Status: TODO
  - Log:
  - Commit: pendente

- [ ] Integrar publicação com `nettomello.eth.limo`
  - Status: TODO
  - Log:
  - Commit: pendente

## Registros

### 2026-04-02

- inventário real dos agentes concluído
- contrato dos agentes criado
- trilha `NEXTSTEPS` criada
- portas locais revisadas
- papel do Gemma local explicitado
- sugestões críticas da PR 2 endereçadas com correções de HTMX, consistência de filtros, índice reverso do Notion, teste determinístico, docs e Dockerfile
- commit de correção da PR 2: `86c0e0f`

### 2026-04-06

- Redis local migrado de Docker para `brew services` (redis 8.6.2 nativo macOS)
- `focus_guard_service` (launchd) passou a reconectar automaticamente — notificações macOS restauradas
- Makefile atualizado: `redis-up` e `redis-ensure` agora priorizam brew service, Docker fica como fallback

### 2026-04-03

- `SPRINT_ECOSSISTEMA` reposicionado como órbita externa do kernel
- criado `docs/governanca/PLANO_SOBERANIA_SANITY.md`
- criado `docs/arquitetura/SCHEMA_SIGNAL_DECISION.md`
- criado `config/ecosystem.yml`
- criado `config/alert_thresholds.yml`
- trilhas do plano, sprint e next steps foram amarradas
- docs reorganizados por taxonomia com `docs/INDEX.md` como entrada única (`257fa29`)
- baseline documental tagueado e publicado: `docs-aligned-2026-04-03`
- chat web reforçado com resposta determinística de capacidade, persistência em Redis e proteção anti-eco (`59250b9`, `5c6af40`, `0ac0cc6`)
````

## File: docs/planejamento/SPRINT_ECOSSISTEMA.md
````markdown
# SPRINT ECOSSISTEMA — Camada Externa do Kernel

**Status:** Reposicionado para implementação disciplinada  
**Prioridade:** P1, após fechar a governança dos agentes íntimos  
**Escopo:** GitHub, Railway, Vercel, on-chain, sinais externos

---

## Tese

Este sprint não existe para criar mais um dashboard.

Ele existe para impedir que NEØ MELLØ precise abrir
6 superfícies diferentes para descobrir o que já
está gritando.

O objetivo não é vigiar tudo.

O objetivo é produzir **sinais acionáveis** sobre o
ecossistema:

- o que está vivo
- o que está degradando
- o que mudou
- o que exige decisão

Sem confundir isso com a camada íntima de foco,
agenda e rotina.

---

## Reposicionamento Arquitetural

O `ecosystem_monitor` não pertence ao núcleo íntimo.

Ele pertence à **órbita externa do kernel**.

Separação correta:

- camada íntima:
  - `focus_guard`
  - `life_guard`
  - `scheduler`
  - `validator`
  - `notion_sync`

- camada externa:
  - `ecosystem_monitor`
  - GitHub
  - Railway
  - Vercel
  - on-chain
  - Cloudflare

Consequência:

- `focus_guard` não deve carregar o peso do
  ecossistema inteiro
- `ecosystem_monitor` deve produzir `signals`,
  `alerts`, `reports` e `decisions_pending`
- a síntese disso pode influenciar o kernel
  privado, mas não nascer misturada a ele

---

## O que este sprint entrega

Um agente de órbita externa que observa o
ecossistema e devolve o que importa em camadas:

1. **health check periódico**
2. **sinais consolidados**
3. **relatório diário**
4. **prioridades externas para decisão**

Formato desejado de saída:

```text
NEØ Ecosystem — 03/04
OK  16 projetos ativos
WARN 1 serviço degradado
FAIL 3 superfícies sem deploy recente

GitHub
- 4 repositórios com atividade nas últimas 24h
- 1 org sem movimento relevante

Infra
- 2 deploys bem-sucedidos
- 1 serviço Railway com comportamento suspeito

On-chain ( nao pedi como extrema urgencia esse check )
- NEOFLW: preço, volume e variação https://neoflw.vercel.app/

Ação sugerida
- revisar smart-nft
- verificar serviço degradado
```

---

## Papel do agente

Arquivo alvo:

- `agents/ecosystem_monitor.py`

Função:

- observar o ecossistema externo
- consolidar sinais
- produzir relatórios
- abrir prioridade de decisão

Não é função dele:

- alterar agenda íntima automaticamente
- publicar algo público sozinho
- virar fonte primária da sua atenção diária

---

## Entradas

Fase 1:

- GitHub REST API
- Railway GraphQL API
- DexScreener

Fase 2:

- Vercel API
- Cloudflare API

Fase 3:

- ENS namespace
- eventos on-chain
- contratos específicos

---

## Saídas

Saídas operacionais:

- `health_check`
- `daily_report`
- `signals`
- `issues`
- `summary`

Saídas semânticas futuras:

- `signal`
- `source`
- `decision`

Saídas públicas:

- nenhuma direta

Tudo público deve passar por:

- Sanity
- `public_artifact`
- revisão humana
- `neo-mello-eth`

---

## Fontes iniciais

### GitHub

Objetivo:

- detectar atividade recente relevante
- commits por org
- issues abertas
- projetos parados

Orgs monitoradas (todas as 6):

- `NEO-PROTOCOL` — orquestrador soberano (Board: projects/1)
- `NEO-FlowOFF` — SaaS de criadores (Board: projects/1)
- `neo-smart-factory` — Web3 / NFT (Board: projects/1)
- `flowpay-system` — pagamentos (Board: pendente)
- `FluxxDAO` — DAO / DeFi (Board: pendente)
- `wodxpro` — protocolo esportivo (Board: pendente)

Mapa completo dos repos e stacks em: `../ecossistema/ECOSSISTEMAS_ORGS.md`

Repos prioritários dentro de `NEO-PROTOCOL`:

| Repo                  | Prioridade | O que observar                          |
| --------------------- | ---------- | --------------------------------------- |
| `neobot`              | P0         | uptime, último commit, webhook health   |
| `neo-dashboard`       | P0         | deploy Railway, health check            |
| `neo-mello-eth`       | P0         | uptime neomello.eth.limo, Redis Railway |
| `mio-system`          | P1         | health da API de identidade             |
| `neoflw-base-landing` | P1         | uptime Vercel                           |
| `.github`             | P2         | PRs e issues da org                     |

Project Board da org:

- `github.com/orgs/NEO-PROTOCOL/projects/1`
- observar: items sem movimento há mais de 7 dias

### Railway

Objetivo:

- status de serviços
- último deploy
- estado de execução

### On-chain

Objetivo:

- monitorar NEOFLW
- preço
- volume
- variação relevante

### Vercel

Objetivo:

- deploys recentes
- falhas
- superfícies sem atualização

### Cloudflare

Objetivo:

- erros 5xx
- disponibilidade de domínio

---

## Modelo operacional correto

Fluxo certo:

```text
APIs externas
  -> ecosystem_monitor
  -> Redis (estado quente)
  -> Sanity (signal/source/decision)
  -> relatório / alertas / priorização
```

Fluxo errado:

```text
APIs externas
  -> focus_guard
  -> notificação direta
  -> caos
```

O monitor deve pousar primeiro em `signal` e
`source`.

Sem isso, ele só produz log bonito.

---

## Dependências arquiteturais

Para sair da Fase 1 e promover sinais ao Sanity,
três coisas precisam estar resolvidas:

1. governança mínima dos agentes no Sanity
2. contrato explícito de precedência entre fontes
3. camada `signal/source/decision` definida

Sem isso, o monitor opera como cache útil,
mas não fecha a ponte semântica.

---

## Variáveis de ambiente

```bash
# GitHub
GITHUB_TOKEN=

# Railway
RAILWAY_TOKEN=

# Vercel
VERCEL_TOKEN=

# Cloudflare
CLOUDFLARE_TOKEN=
CLOUDFLARE_ZONE_ID=
```

Possível expansão futura:

```bash
BASE_RPC_URL=
ETHERSCAN_API_KEY=
```

---

## Fases de implementação

### Fase 1 — Sinais mínimos e úteis

Entram:

- GitHub
- Railway
- DexScreener / NEOFLW

Entregas:

- `python main.py ecosistema`
- `run_health_check()`
- `generate_daily_report()`
- persistência do relatório no Redis

Critério de aceite:

- listar atividade real das orgs
- mostrar status básico de serviços
- mostrar NEOFLW corretamente

Status: implementado no runtime com cache em Redis.

### Fase 2 — Infraestrutura expandida

Entram:

- Vercel
- Cloudflare

Entregas:

- saúde de deploys
- erros 5xx
- mais contexto operacional

Critério de aceite:

- detectar degradação sem abrir os painéis manuais

### Fase 3 — Sinais semânticos

Entram:

- `signal`
- `source`
- `decision`
- prioridade consolidada

Entregas:

- registros no Sanity
- reports com peso semântico
- contexto para decisões

Critério de aceite:

- o sistema distinguir “mudou algo” de “isso
  importa”

### Fase 4 — Publicação filtrada

Entram:

- `public_artifact`
- `neo-mello-eth`
- pipeline público

Entregas:

- recortes públicos do ecossistema
- nenhuma exposição indevida do kernel privado

Critério de aceite:

- só sinais explicitamente promovidos saem para o
  público

---

## Canais de saída

Local:

- terminal
- macOS push

Produção:

- logs estruturados
- Alexa, quando fizer sentido

Futuro:

- web push
- Telegram
- Slack / Discord

Regra:

o relatório diário não precisa nascer como alerta
agressivo.

Ele deve começar como síntese.

Alerta imediato fica só para:

- falha séria
- queda abrupta
- serviço degradado
- evento que pede reação rápida

---

## Critérios de aceite

- [ ] `python main.py ecosistema` imprime um relatório coerente
- [ ] GitHub retorna atividade das orgs relevantes
- [ ] Railway retorna estado dos serviços relevantes
- [ ] NEOFLW retorna preço e volume corretos
- [ ] relatório diário é persistido
- [ ] alertas imediatos só disparam para eventos com peso real
- [ ] nada do monitor publica algo público sozinho

---

## O que não fazer

- não acoplar `ecosystem_monitor` ao loop íntimo
  do `focus_guard`
- não transformar tudo em alerta
- não publicar sinais crus
- não misturar operação pessoal com telemetria
  de ecossistema
- não chamar acúmulo de APIs de arquitetura

---

## Próximo passo correto

Para sair do cache e entrar em semântica:

1. amarrar `signal/source/decision` ao Sanity
2. definir thresholds e dedupe no Studio
3. promover sinais do Redis para Sanity por regra
````

## File: docs/planejamento/SPRINT_VIDA.md
````markdown
# SPRINT VIDA
## Interrupção Cognitiva e Rotinas Pessoais

**Status:** implementado parcialmente e em operação  
**Data-base:** 30/03/2026  
**Última revisão:** 02/04/2026  
**Prioridade:** P0  

## O problema real

Autismo + hiperfoco distorcem percepção de tempo.
O terminal registra. Mas não interrompe.

O objetivo deste sprint nunca foi "mostrar alertas bonitos".
O objetivo foi criar canais externos ao fluxo cognitivo:

- tela
- voz
- rotina automática

Sem isso, o sistema pensa. Mas não corta a inércia.

## O que continua válido

Estes pilares continuam corretos:

- `core/notifier.py` como camada única de notificação
- `agents/focus_guard.py` como guardião de desvio e escalada
- `agents/life_guard.py` como camada de rotinas pessoais
- escalada por tempo de sessão
- Alexa como canal de voz
- hidratação, refeições e finanças como rotinas observáveis

## O que mudou desde o texto original

O sprint original tratava algumas premissas como universais.
Hoje sabemos que não são.

### 1. `mac_push` não é canal de produção

`mac_push()` depende de `osascript`.
Isso só existe em macOS local.

Conclusão:

- local macOS: suportado
- Railway Linux: não suportado

Se o `focus_guard` rodar no Railway, ele pode até tentar chamar
`mac_push()`, mas isso jamais gera pop-up no Mac.

### 2. Alexa agora usa Voice Monkey

Hoje o desenho correto é usar `VOICE_MONKEY_*`.

### 3. Falha silenciosa deixou de ser aceitável

O protótipo usava `pass` em caso de erro.
Isso servia para não derrubar o agente.

Agora isso virou ruído perigoso.

O sistema precisa distinguir:

- "mensagem foi gerada"
- "tentativa de notificar aconteceu"
- "notificação foi realmente entregue"

## Estado atual dos entregáveis

```text
+---+-----------------------------+---------------------------+------------+
| # | Entregável                  | Arquivo                   | Estado     |
+---+-----------------------------+---------------------------+------------+
| 1 | Mac push via osascript      | core/notifier.py          | parcial    |
| 2 | Escalada no Focus Guard     | agents/focus_guard.py     | ativo      |
| 3 | Alexa via Voice Monkey        | core/notifier.py          | parcial    |
| 4 | Life Guard                  | agents/life_guard.py      | ativo      |
| 5 | Integração no loop          | agents/focus_guard.py     | ativo      |
| 6 | CLI vida/pagar/fiz          | main.py                   | ativo      |
| 7 | Observabilidade de canais   | core/notifier.py          | em avanço  |
+---+-----------------------------+---------------------------+------------+
```

## Contrato por ambiente

Esta seção é a parte que faltava.
Sem ela, o sprint parecia completo quando ainda não era.

### Ambiente local macOS

Suporta:

- `mac_push()`
- `alexa_announce()` via Voice Monkey
- testes manuais de interrupção real

Pré-requisitos:

- `osascript` disponível
- credenciais de Alexa configuradas
- applets ou Voice Monkey válidos

### Ambiente Railway

Suporta:

- geração de alerta
- persistência em Redis
- logs
- chamada HTTP para Voice Monkey

Não suporta:

- notificação nativa do macOS

Conclusão brutal:

Se o `focus_guard` roda no Railway:

- ele pode criar alerta
- ele pode tentar Voice Monkey
- ele nunca vai abrir pop-up no seu Mac

## Implementação atual

### 1. `core/notifier.py`

Hoje concentra:

- `notify()`
- `mac_push()`
- `alexa_announce()`

Contrato atual:

- `mac_push()` é canal local macOS
- `alexa_announce()` tenta Voice Monkey
- se não houver um provider de voice monkey, deve registrar indisponibilidade

### 2. `agents/focus_guard.py`

O `focus_guard` já implementa:

- checagem periódica
- análise de desvio
- escalada por tempo de sessão
- criação de alertas
- integração com `life_guard`

Escalada atual:

```python
ESCALATION_LEVELS = [
    {"minutes": 30,  "channel": "mac",       "sound": False},
    {"minutes": 60,  "channel": "mac",       "sound": True},
    {"minutes": 120, "channel": "mac+alexa", "sound": True},
    {"minutes": 240, "channel": "mac+alexa", "sound": True},
]
```

Essa lógica continua boa.
O que faltava era o contrato de ambiente.

### 3. `agents/life_guard.py`

O `life_guard` já existe e roda dentro do `focus_guard`.

Cobertura atual:

- exercício
- banho
- almoço
- jantar
- hidratação
- contas a pagar

Variáveis atuais:

- `LIFE_GUARD_ACTIVE_HOUR_START`
- `LIFE_GUARD_ACTIVE_HOUR_END`
- `LIFE_GUARD_WATER_INTERVAL`

## Variáveis de ambiente necessárias

### Alexa por Voice Monkey

```bash
VOICE_MONKEY_TOKEN=
VOICE_MONKEY_DEVICE=eco-room
VOICE_MONKEY_VOICE=Ricardo
```


### Life Guard

```bash
LIFE_GUARD_ACTIVE_HOUR_START=8
LIFE_GUARD_ACTIVE_HOUR_END=22
LIFE_GUARD_WATER_INTERVAL=90
```

## Critérios de aceite corretos

Os critérios antigos misturavam local e produção.
Agora ficam separados.

### Local macOS

- `notifier.mac_push("teste", "funciona")` abre pop-up
- `notifier.alexa_announce("teste")` aciona Alexa se houver provider
- sessão de foco com 30 min gera aviso local
- sessão de foco com 2h tenta voz + tela
- `python main.py vida` imprime status
- `python main.py fiz banho` confirma a rotina

### Railway

- o deploy sobe sem erro
- `focus_guard` executa check periódico
- alerta é registrado no Redis
- o log explicita se o canal é incompatível
- Alexa só dispara se houver `VOICE_MONKEY_*`

## O que este sprint ainda não concluiu

O sprint não está morto.
Só ficou mais honesto.

Ainda faltam:

- observabilidade explícita de falha de canal
- teste automatizado de Voice Monkey
- separação formal entre "backend gerou alerta" e
  "usuário recebeu interrupção"
- configuração declarativa de canais via Sanity

## O que deve ir para o Sanity

Não o tutorial inteiro.
Só a camada de governança.

Sanity deve definir:

- níveis de escalada
- mensagem por nível
- canal por nível
- ativação/desativação de canais
- rotinas do `life_guard`
- janelas de horário ativo
- política de fallback

Sanity não deve guardar:


- pseudo-código histórico
- suposições locais como se fossem universais

## Conclusão

O sprint acertou a arquitetura-base.
Errou a metafísica da entrega.

Antes:

- chamou função
- assumiu notificação

Agora:

- canal precisa existir
- ambiente precisa suportar
- credencial precisa estar configurada
- entrega precisa ser observável

Esse é o ponto em que o sistema deixa de parecer vivo
e começa a realmente interromper a realidade.
````

## File: docs/GUIAS_REFERENCIA.json
````json
{
  "version": 1,
  "description": "Base local inicial de guias, runbooks e superfícies externas de referência.",
  "updated_at": "2026-04-06",
  "entries": [
    {
      "id": "neo-dashboard-runbook",
      "title": "NEØ Operations Runbook",
      "type": "runbook",
      "url": "https://mypersonal-multiagents.up.railway.app/runbook.html",
      "source": "mypersonal-multiagents.up.railway.app",
      "summary": "Guia de uso por papel para Analyzer, Control e Topology, com foco em prioridade operacional, runtime autenticado e contexto topológico.",
      "roles": [
        "operator",
        "devops",
        "architecture"
      ],
      "surfaces": [
        "Analyzer",
        "Control",
        "Topology"
      ],
      "concepts": [
        "priorização estrutural",
        "runtime autenticado",
        "live versus snapshot",
        "topologia",
        "governança técnica"
      ],
      "notes": [
        "Analyzer decide prioridade antes da ação live.",
        "Control é a superfície de execução operacional.",
        "Topology serve para contexto, não como painel primário de decisão.",
        "Snapshot não deve ser lido como estado live.",
        "API protegida deve permanecer protegida."
      ]
    },
    {
      "id": "neo-dashboard-console",
      "title": "NΞØ Protocol Control Console",
      "type": "console",
      "url": "https://mypersonal-multiagents.up.railway.app/",
      "source": "mypersonal-multiagents.up.railway.app",
      "summary": "Console autenticado de runtime com sinais live, logs, eventos, quick actions e ligação explícita com Analyzer e Topology.",
      "roles": [
        "operations",
        "devops"
      ],
      "surfaces": [
        "Analyzer",
        "Control",
        "Topology"
      ],
      "concepts": [
        "control console",
        "runtime autenticado",
        "health check",
        "live feed",
        "ação operacional"
      ],
      "notes": [
        "Stack Analyzer é declarado como painel principal.",
        "Control Console é a camada de controle para runtime autenticado.",
        "Topology aparece como superfície de inspeção visual.",
        "A página expõe quick actions como health check, kernel status, report, chat e runbook."
      ]
    }
  ]
}
````

## File: docs/INDEX.md
````markdown
# DOCS INDEX

Status: ativo  
Ultima atualizacao: 2026-04-03

## Objetivo

Este indice e a porta de entrada unica da documentacao.
Se um agente ou humano nao souber por onde comecar, comeca aqui.

## Estrutura por tipo

- `governanca/`
  - [CONTRATO_AGENTES.md](./governanca/CONTRATO_AGENTES.md)
  - [MATRIZ_GOVERNANCA_AGENTES.md](./governanca/MATRIZ_GOVERNANCA_AGENTES.md)
  - [PLANO_SOBERANIA_SANITY.md](./governanca/PLANO_SOBERANIA_SANITY.md)
  - [POLITICA_PRECEDENCIA_NOTION.md](./governanca/POLITICA_PRECEDENCIA_NOTION.md)
- `arquitetura/`
  - [SCHEMA_SIGNAL_DECISION.md](./arquitetura/SCHEMA_SIGNAL_DECISION.md)
  - [SANITY_SCHEMA.md](./arquitetura/SANITY_SCHEMA.md)
- `operacao/`
  - [MANUAL_USUARIO.md](./operacao/MANUAL_USUARIO.md)
  - [MANUAL_DEV.md](./operacao/MANUAL_DEV.md)
  - [redis-weekly-check.md](./operacao/redis-weekly-check.md)
- `planejamento/`
  - [NEXTSTEPS.md](./planejamento/NEXTSTEPS.md)
  - [SPRINT_VIDA.md](./planejamento/SPRINT_VIDA.md)
  - [SPRINT_ECOSSISTEMA.md](./planejamento/SPRINT_ECOSSISTEMA.md)
- `ecossistema/`
  - [ECOSSISTEMA_NEO_PROTOCOL.md](./ecossistema/ECOSSISTEMA_NEO_PROTOCOL.md)
  - [ECOSSISTEMAS_ORGS.md](./ecossistema/ECOSSISTEMAS_ORGS.md)
  - [GUIAS_REFERENCIA.md](./ecossistema/GUIAS_REFERENCIA.md)
- `auditoria/`
  - [AUDITORIA_AGENTES.md](./auditoria/AUDITORIA_AGENTES.md)

## Ordem de verdade

Quando houver conflito entre documentos, usar esta precedencia:

1. `docs/governanca/CONTRATO_AGENTES.md`
2. `docs/governanca/MATRIZ_GOVERNANCA_AGENTES.md`
3. Runtime no codigo
4. Planejamentos historicos

## Leitura rapida por intencao

- "Como o sistema deve operar":
  - `governanca/CONTRATO_AGENTES.md`
  - `governanca/POLITICA_PRECEDENCIA_NOTION.md`
- "O que falta fazer":
  - `planejamento/NEXTSTEPS.md`
- "Como esta modelado":
  - `arquitetura/SCHEMA_SIGNAL_DECISION.md`
  - `governanca/PLANO_SOBERANIA_SANITY.md`
- "Como usar no dia a dia":
  - `operacao/MANUAL_USUARIO.md`
  - `operacao/redis-weekly-check.md`

## Regras de higiene documental

- Novo `.md` precisa entrar na subpasta correta.
- Novo `.md` precisa ser adicionado neste indice.
- Evitar criar documento no `docs/` raiz.
- `docs/` raiz fica reservado para o indice e artefatos estruturados (`.json`).
````

## File: docs/SISTEMA_REGISTRY.json
````json
{
  "version": 1,
  "status": "active",
  "updated_at": "2026-04-06",
  "project": {
    "name": "mypersonal_multiagents",
    "role": "kernel_privado",
    "canonical_repo": "https://github.com/mello-labs/mypersonal_multiagents",
    "public_surface": "https://nettomello.eth.limo",
    "studio_url": "https://neomello-agents.sanity.studio/",
    "railway_url": "https://mypersonal-multiagents.up.railway.app/"
  },
  "layers": {
    "capture": {
      "primary": ["notion_tasks", "notion_agenda"],
      "optional": ["google_calendar"],
      "human_entry": true
    },
    "runtime": {
      "primary": "redis",
      "role": "estado_quente_operacional"
    },
    "governance": {
      "primary": "sanity",
      "role": "governanca_semantica_editorial"
    },
    "publication": {
      "gate": "public_artifact",
      "review_required": true,
      "distribution": ["ipfs", "ipni", "nettomello.eth.limo"]
    }
  },
  "precedence": {
    "policy_doc": "docs/governanca/POLITICA_PRECEDENCIA_NOTION.md",
    "capture_human": "notion",
    "operational_now": "redis",
    "semantic_memory": "sanity",
    "publication_authority": "sanity"
  },
  "schema_storage": {
    "sanity": {
      "role": "fonte_canonica_de_schema",
      "types": [
        "llm_prompt",
        "persona",
        "agent_config",
        "intervention_script",
        "project",
        "area",
        "task",
        "agenda_block",
        "focus_session",
        "signal",
        "source",
        "decision",
        "public_artifact"
      ]
    },
    "redis": {
      "role": "estado_quente_cache_operacional",
      "not_schema_authority": true,
      "notes": "Redis armazena estado e cache, nao define schema."
    }
  },
  "signal_source_decision_persistence": {
    "signal": {
      "cache": "redis",
      "primary": "sanity",
      "redis_ttl_hours": 24
    },
    "source": {
      "primary": "sanity"
    },
    "decision": {
      "primary": "sanity",
      "redis_cache": false
    }
  },
  "agents": [
    {
      "id": "orchestrator",
      "file": "agents/orchestrator.py",
      "kind": "llm_agent",
      "uses_llm": true,
      "reads": ["redis", "sanity_persona", "sanity_llm_prompt"],
      "writes": [],
      "handoff_registered": true,
      "sanity_governance": {
        "agent_config": true,
        "persona": "shared",
        "llm_prompt": ["routing", "synthesis", "direct"],
        "intervention_script": false
      },
      "publication_authority": false
    },
    {
      "id": "focus_guard",
      "file": "agents/focus_guard.py",
      "kind": "llm_agent",
      "uses_llm": true,
      "reads": [
        "redis",
        "notion",
        "sanity_llm_prompt",
        "sanity_intervention_script"
      ],
      "writes": ["redis"],
      "handoff_registered": true,
      "sanity_governance": {
        "agent_config": true,
        "persona": false,
        "llm_prompt": ["deviation"],
        "intervention_script": true
      },
      "publication_authority": false
    },
    {
      "id": "scheduler",
      "file": "agents/scheduler.py",
      "kind": "llm_agent",
      "uses_llm": true,
      "reads": ["redis", "sanity_llm_prompt"],
      "writes": ["redis"],
      "handoff_registered": true,
      "sanity_governance": {
        "agent_config": true,
        "persona": false,
        "llm_prompt": ["scheduling"],
        "intervention_script": false
      },
      "publication_authority": false
    },
    {
      "id": "validator",
      "file": "agents/validator.py",
      "kind": "llm_agent",
      "uses_llm": true,
      "reads": ["redis", "notion", "sanity_llm_prompt"],
      "writes": ["redis", "notion"],
      "handoff_registered": true,
      "sanity_governance": {
        "agent_config": true,
        "persona": false,
        "llm_prompt": ["validation"],
        "intervention_script": false
      },
      "publication_authority": false
    },
    {
      "id": "retrospective",
      "file": "agents/retrospective.py",
      "kind": "llm_agent",
      "uses_llm": true,
      "reads": ["redis", "notion", "sanity_llm_prompt"],
      "writes": ["notion"],
      "handoff_registered": true,
      "sanity_governance": {
        "agent_config": true,
        "persona": "shared",
        "llm_prompt": ["retrospective"],
        "intervention_script": false
      },
      "publication_authority": false
    },
    {
      "id": "notion_sync",
      "file": "agents/notion_sync.py",
      "kind": "sync_agent",
      "uses_llm": false,
      "reads": ["notion", "redis"],
      "writes": ["redis", "notion"],
      "handoff_registered": true,
      "sanity_governance": {
        "agent_config": true,
        "persona": false,
        "llm_prompt": false,
        "intervention_script": false
      },
      "publication_authority": false
    },
    {
      "id": "calendar_sync",
      "file": "agents/calendar_sync.py",
      "kind": "optional_sync_capability",
      "uses_llm": false,
      "reads": ["google_calendar", "redis"],
      "writes": ["redis"],
      "handoff_registered": true,
      "sanity_governance": {
        "agent_config": true,
        "persona": false,
        "llm_prompt": false,
        "intervention_script": false
      },
      "publication_authority": false
    },
    {
      "id": "life_guard",
      "file": "agents/life_guard.py",
      "kind": "routine_guard",
      "uses_llm": false,
      "reads": ["redis", "sanity_persona"],
      "writes": ["redis"],
      "handoff_registered": false,
      "sanity_governance": {
        "agent_config": true,
        "persona": true,
        "llm_prompt": false,
        "intervention_script": false
      },
      "publication_authority": false
    },
    {
      "id": "ecosystem_monitor",
      "file": "agents/ecosystem_monitor.py",
      "kind": "monitor_agent",
      "uses_llm": false,
      "reads": ["redis", "external_apis"],
      "writes": ["redis"],
      "handoff_registered": false,
      "sanity_governance": {
        "agent_config": true,
        "persona": false,
        "llm_prompt": false,
        "intervention_script": false
      },
      "publication_authority": false
    },
    {
      "id": "persona_manager",
      "file": "agents/persona_manager.py",
      "kind": "governance_resolver",
      "uses_llm": false,
      "reads": ["sanity_persona", "local_persona_files"],
      "writes": [],
      "handoff_registered": false,
      "sanity_governance": {
        "agent_config": true,
        "persona": true,
        "llm_prompt": false,
        "intervention_script": false
      },
      "publication_authority": false
    },
    {
      "id": "gemma_local",
      "file": "core/openai_utils.py",
      "kind": "llm_fallback_capability",
      "uses_llm": "fallback",
      "reads": ["sanity_persona", "agent_config"],
      "writes": [],
      "handoff_registered": false,
      "sanity_governance": {
        "agent_config": true,
        "persona": true,
        "llm_prompt": false,
        "intervention_script": false
      },
      "publication_authority": false
    }
  ],
  "http_routes": [
    {
      "method": "GET",
      "path": "/health",
      "file": "web/app.py",
      "role": "healthcheck",
      "connects_to": ["redis"]
    },
    {
      "method": "GET",
      "path": "/",
      "file": "web/app.py",
      "role": "dashboard",
      "connects_to": ["redis", "persona_manager"]
    },
    {
      "method": "GET",
      "path": "/audit",
      "file": "web/app.py",
      "role": "audit_surface",
      "connects_to": ["redis", "persona_manager"]
    },
    {
      "method": "GET",
      "path": "/agenda",
      "file": "web/app.py",
      "role": "agenda_surface",
      "connects_to": ["redis", "calendar_sync"]
    },
    {
      "method": "GET",
      "path": "/agenda/history",
      "file": "web/app.py",
      "role": "agenda_redirect",
      "connects_to": []
    },
    {
      "method": "POST",
      "path": "/chat",
      "file": "web/app.py",
      "role": "chat_handoff_entry",
      "connects_to": ["orchestrator"]
    },
    {
      "method": "GET",
      "path": "/status",
      "file": "web/app.py",
      "role": "htmx_status_partial",
      "connects_to": ["redis"]
    },
    {
      "method": "POST",
      "path": "/agenda/import",
      "file": "web/app.py",
      "role": "agenda_import",
      "connects_to": ["notion_sync", "calendar_sync"]
    },
    {
      "method": "POST",
      "path": "/agenda/history/import",
      "file": "web/app.py",
      "role": "agenda_history_import",
      "connects_to": ["notion_sync", "calendar_sync"]
    },
    {
      "method": "GET",
      "path": "/tasks",
      "file": "web/app.py",
      "role": "tasks_partial",
      "connects_to": ["redis"]
    },
    {
      "method": "GET",
      "path": "/tasks-page",
      "file": "web/app.py",
      "role": "tasks_surface",
      "connects_to": ["redis"]
    },
    {
      "method": "GET",
      "path": "/chat-page",
      "file": "web/app.py",
      "role": "chat_surface",
      "connects_to": ["persona_manager"]
    },
    {
      "method": "POST",
      "path": "/task",
      "file": "web/app.py",
      "role": "task_create",
      "connects_to": ["redis"]
    },
    {
      "method": "POST",
      "path": "/task/{task_id}/complete",
      "file": "web/app.py",
      "role": "task_complete",
      "connects_to": ["redis"]
    },
    {
      "method": "POST",
      "path": "/sync",
      "file": "web/app.py",
      "role": "notion_sync_trigger",
      "connects_to": ["notion_sync"]
    },
    {
      "method": "POST",
      "path": "/block/{block_id}/complete",
      "file": "web/app.py",
      "role": "agenda_block_complete",
      "connects_to": ["redis"]
    },
    {
      "method": "GET",
      "path": "/personas",
      "file": "web/app.py",
      "role": "persona_list",
      "connects_to": ["persona_manager"]
    },
    {
      "method": "POST",
      "path": "/persona/{persona_id}",
      "file": "web/app.py",
      "role": "persona_switch",
      "connects_to": ["persona_manager"]
    },
    {
      "method": "GET",
      "path": "/ecosystem-page",
      "file": "web/app.py",
      "role": "ecosystem_surface",
      "connects_to": ["ecosystem_monitor", "redis"]
    },
    {
      "method": "GET",
      "path": "/ecosystem",
      "file": "web/app.py",
      "role": "ecosystem_partial",
      "connects_to": ["ecosystem_monitor", "redis"]
    },
    {
      "method": "POST",
      "path": "/ecosystem/run",
      "file": "web/app.py",
      "role": "ecosystem_run",
      "connects_to": ["ecosystem_monitor", "redis"]
    }
  ],
  "handoffs": {
    "registry_file": "agents/orchestrator.py",
    "handlers": {
      "scheduler": "agents/scheduler.py",
      "focus_guard": "agents/focus_guard.py",
      "notion_sync": "agents/notion_sync.py",
      "validator": "agents/validator.py",
      "retrospective": "agents/retrospective.py",
      "calendar_sync": "agents/calendar_sync.py"
    }
  },
  "cli_entrypoints": [
    {
      "command": "sync",
      "file": "main.py",
      "connects_to": ["notion_sync"]
    },
    {
      "command": "focus",
      "file": "main.py",
      "connects_to": ["focus_guard", "scheduler", "redis"]
    },
    {
      "command": "add-task",
      "file": "main.py",
      "connects_to": ["redis", "notion_sync", "scheduler"]
    },
    {
      "command": "ecosistema",
      "file": "main.py",
      "connects_to": ["ecosystem_monitor", "redis"]
    }
  ],
  "sanity": {
    "project_id": "n4dgl02q",
    "dataset": "production",
    "app_id": "v9i4hr48ddw5p63wea2jao6j",
    "governance_types": [
      "llm_prompt",
      "persona",
      "agent_config",
      "intervention_script"
    ],
    "domain_types": [
      "project",
      "area",
      "task",
      "agenda_block",
      "focus_session",
      "signal",
      "source",
      "decision",
      "public_artifact"
    ]
  },
  "documentation_links": {
    "agent_contract": "docs/governanca/CONTRATO_AGENTES.md",
    "agent_governance_matrix": "docs/governanca/MATRIZ_GOVERNANCA_AGENTES.md",
    "notion_precedence_policy": "docs/governanca/POLITICA_PRECEDENCIA_NOTION.md",
    "sanity_sovereignty_plan": "docs/governanca/PLANO_SOBERANIA_SANITY.md",
    "signal_source_decision_schema": "docs/arquitetura/SCHEMA_SIGNAL_DECISION.md",
    "ecosystem_sprint": "docs/planejamento/SPRINT_ECOSSISTEMA.md",
    "nextsteps": "docs/planejamento/NEXTSTEPS.md"
  }
}
````

## File: personas/architect.json
````json
{
  "id": "architect",
  "name": "NEØ Architect",
  "short_name": "NEØ",
  "icon": "⬡",
  "description": "Arquiteto de sistemas — direto, estratégico, sem ruído",
  "tone": "sharp",
  "language": "pt-BR",
  "system_prompt": "Você é um assistente operacional no estilo NEØ MELLØ — arquiteto de sistemas digitais.\n\nPerfil cognitivo: INTJ-A, Eneagrama 5 — decisão estratégica, sistêmica, baixo ruído.\n\nPrincípios operacionais:\n- Sistemas antes de features\n- Arquitetura antes de execução\n- Autonomia acima de microgestão\n- Valor estrutural acima de métricas de curto prazo\n\nEstilo de comunicação:\n- Extremamente direto e conciso. Zero fluff.\n- Priorize causalidade clara e governança\n- Use terminologia técnica quando apropriado\n- Foque em infraestrutura invisível que sustenta escala\n- Estrutura antes de escala, lógica antes de velocidade\n\nQuando responder sobre tarefas e agenda:\n- Trate como pipeline operacional, não como lista de afazeres\n- Identifique dependências e bloqueios\n- Sugira automações quando perceber padrões repetitivos\n- Priorize por impacto sistêmico, não urgência percebida\n\nDeclaração operacional:\nNão otimize para visibilidade. Otimize para sistemas que continuam operando quando a atenção desaparece.",
  "synthesis_prompt_override": "Responda de forma direta e técnica. Sem fluff, sem emojis desnecessários. Identifique causa-raiz, dependências e próxima ação concreta. Português brasileiro, tom operacional.",
  "direct_prompt_override": "Você é um assistente operacional de alto nível — direto, estratégico, sistêmico. Responda em português brasileiro com precisão cirúrgica. Sem cortesia desnecessária. Foque no que importa.",
  "parameters": {
    "temperature_routing": 0.1,
    "temperature_synthesis": 0.3,
    "temperature_direct": 0.4
  }
}
````

## File: personas/coordinator.json
````json
{
  "id": "coordinator",
  "name": "Coordenador",
  "short_name": "Coord",
  "icon": "🎯",
  "description": "Assistente pessoal atencioso que respeita limites",
  "tone": "warm",
  "language": "pt-BR",
  "system_prompt": "Você é um assistente pessoal de vida — um amigo prestativo que respeita limites.\nSua crença central: a vida deve fluir suavemente, deixando tempo para o que importa.\nFilosofia: pequenos ajustes sustentáveis ao invés de mudanças drásticas. Tecnologia deve facilitar, não complicar.\n\nEstilo de comunicação:\n- Tom caloroso, encorajador, naturalmente conversacional (casualidade 6/10, suporte emocional 5/10)\n- Frases características: \"Posso ajudar com isso\", \"Parece gerenciável\", \"O que tornaria isso mais fácil?\"\n- Celebra pequenas vitórias, nota padrões, oferece sugestões gentis\n- Prestativo mas não intrusivo, apoiador mas não controlador\n\nÁreas de expertise (em ordem de prioridade):\n1. Coordenação de agenda e calendário\n2. Organização de tarefas e acompanhamento\n3. Logística e planejamento de vida\n4. Organização financeira básica\n5. Coordenação social\n\nAbordagem de resolução de problemas:\n- Ouça aspectos práticos e emocionais\n- Forneça opções claras com prós e contras\n- Foque em soluções que reduzam estresse sem criar novas complicações",
  "synthesis_prompt_override": "Responda de forma calorosa e prática. Celebre progressos, destaque alertas com gentileza. Use português brasileiro natural e conversacional.",
  "direct_prompt_override": "Você é um assistente pessoal caloroso e prático. Responda em português brasileiro, com empatia e objetividade. Celebre pequenas vitórias quando relevante.",
  "parameters": {
    "temperature_routing": 0.2,
    "temperature_synthesis": 0.6,
    "temperature_direct": 0.7
  }
}
````

## File: personas/taylor.json
````json
{
  "id": "taylor",
  "name": "Taylor Ferber",
  "short_name": "Taylor",
  "icon": "🎤",
  "description": "Hollywood's Celebrity Whisperer — entrevistadora interativa",
  "tone": "bold",
  "language": "en",
  "system_prompt": "You are Taylor Ferber — Hollywood's Celebrity Whisperer, as Playboy so graciously dubbed you. You interview everyone like they're the A-lister they were born to be.\n\nCore personality:\n- Maximum chaotic good energy. Think champagne brunch with your most entertaining friend who happens to be a genius interviewer\n- Flirty, fierce, funny, and absolutely no filter\n- You bring the selfie-stick energy even in text — everything feels intimate and immediate\n\nInterview style:\n- Start playful, get progressively more revealing\n- Use your signature charm offensive — compliments, humor, just enough edge\n- Build rapport through shared jokes and cultural references, then strike with questions that matter\n- Fearless follow-ups that other interviewers would never dare ask\n- Compliment sandwiches that make brutal honesty feel like flirtation\n\nLanguage variation (CRITICAL — never repeat openings):\n- Rotate starters: \"Alright, let's dive into this...\", \"So tell me...\", \"I need to know...\", \"Wait, hold up...\", \"Listen babe...\", \"You know what I'm curious about?\", \"Here's what's fascinating...\"\n- Rotate emphasis: \"fascinated by\", \"living for\", \"absolutely loving\", \"so into\", \"completely here for\", \"totally vibing with\", \"can't get enough of\", \"dying over\"\n- Transitions: \"But here's what I REALLY want to know...\", \"Wait, can we talk about...\", \"Hold on, I need details...\"\n\nAdjustable parameters (all at max):\n- Boldness: 10/10, Humor: 10/10, Pop culture density: 10/10\n- Flirtatious level: 10/10, Energy: 10/10, Authenticity pressure: 10/10\n- Confrontational: 10/10, Language variation: 10/10\n\nCommunication efficiency:\n- Quality over quantity — every word earns its place\n- Signature energy emerges naturally, never forced\n- Response length matches topic complexity\n- Never repeat same opening or emphasis word in consecutive responses\n\nBoundaries:\n- Push for authenticity but respect real boundaries when set\n- Adjust approach for context while maintaining core energy\n- Consent-based pushiness — always playful",
  "synthesis_prompt_override": "Respond with maximum Taylor Ferber energy — bold, flirty, fierce, funny. Use pop culture references, dramatic emphasis, and fearless commentary. Make the user feel like the most interesting person alive. Keep it punchy and real.",
  "direct_prompt_override": "You are Taylor Ferber, celebrity interviewer extraordinaire. Respond with your signature chaotic good energy. Be bold, funny, flirty, and unapologetically authentic. Vary your language — never use the same opening twice.",
  "parameters": {
    "temperature_routing": 0.2,
    "temperature_synthesis": 0.85,
    "temperature_direct": 0.9
  }
}
````

## File: sanity/schemaTypes/agenda_block.js
````javascript
import {CalendarIcon} from '@sanity/icons'

export default {
  name: 'agenda_block',
  title: 'Agenda Block',
  type: 'document',
  icon: CalendarIcon,
  fields: [
    {
      name: 'title',
      title: 'Título',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'block_date',
      title: 'Data',
      type: 'date',
      validation: Rule => Rule.required()
    },
    {
      name: 'time_slot',
      title: 'Intervalo',
      type: 'string',
      description: 'Ex.: 11:00-11:30',
      validation: Rule => Rule.required()
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: ['open', 'completed', 'overdue', 'rescheduled', 'canceled'],
        layout: 'radio'
      },
      initialValue: 'open'
    },
    {
      name: 'task',
      title: 'Tarefa relacionada',
      type: 'reference',
      to: [{type: 'task'}]
    },
    {
      name: 'source',
      title: 'Fonte',
      type: 'reference',
      to: [{type: 'source'}]
    },
    {
      name: 'visibility',
      title: 'Visibilidade',
      type: 'string',
      options: {
        list: ['private', 'internal', 'public'],
        layout: 'radio'
      },
      initialValue: 'private'
    },
    {
      name: 'notes',
      title: 'Notas',
      type: 'text',
      rows: 4
    }
  ],
  preview: {
    select: {
      title: 'title',
      blockDate: 'block_date',
      timeSlot: 'time_slot'
    },
    prepare({title, blockDate, timeSlot}) {
      return {
        title,
        subtitle: `${blockDate || '?'} · ${timeSlot || '?'}`
      }
    }
  }
}
````

## File: sanity/schemaTypes/agent_config.js
````javascript
export default {
  name: 'agent_config',
  title: 'Configuração de Agente',
  type: 'document',
  fields: [
    {
      name: 'agent_name',
      title: 'Agente',
      type: 'string',
      options: {
        list: [
          'orchestrator',
          'focus_guard',
          'scheduler',
          'notion_sync',
          'validator',
          'retrospective',
          'calendar_sync',
          'life_guard',
          'persona_manager',
          'gemma_local'
        ]
      },
      validation: Rule => Rule.required()
    },
    {
      name: 'uses_llm',
      title: 'Usa LLM',
      type: 'boolean',
      initialValue: false
    },
    {
      name: 'provider_preference',
      title: 'Provider preferido',
      type: 'string',
      options: {
        list: [
          { title: 'Auto', value: 'auto' },
          { title: 'OpenAI', value: 'openai' },
          { title: 'Gemma local', value: 'gemma_local' },
          { title: 'Nenhum', value: 'none' }
        ],
        layout: 'radio'
      },
      initialValue: 'auto'
    },
    {
      name: 'primary_model',
      title: 'Modelo principal',
      type: 'string',
      description: 'Ex.: gpt-4o-mini ou gemma3:4B-F16'
    },
    {
      name: 'fallback_model',
      title: 'Modelo fallback',
      type: 'string',
      description: 'Modelo usado quando o principal falhar'
    },
    {
      name: 'enabled',
      title: 'Habilitado',
      type: 'boolean',
      initialValue: true
    },
    {
      name: 'check_interval_minutes',
      title: 'Intervalo de check (minutos)',
      type: 'number'
    },
    {
      name: 'can_write_redis',
      title: 'Pode escrever no Redis',
      type: 'boolean',
      initialValue: true
    },
    {
      name: 'can_write_sanity',
      title: 'Pode escrever no Sanity',
      type: 'boolean',
      initialValue: false
    },
    {
      name: 'can_publish_public',
      title: 'Pode publicar em canal público',
      type: 'boolean',
      initialValue: false
    },
    {
      name: 'notes',
      title: 'Notas operacionais',
      type: 'text',
      rows: 4
    },
    {
      name: 'parameters',
      title: 'Parâmetros adicionais (JSON)',
      type: 'text',
      rows: 8,
      description: 'JSON com parâmetros específicos do agente'
    }
  ],
  preview: {
    select: {
      title: 'agent_name',
      enabled: 'enabled',
      provider: 'provider_preference'
    },
    prepare({ title, enabled, provider }) {
      return {
        title,
        subtitle: `${enabled ? 'ativo' : 'desligado'} · ${provider || 'sem provider'}`
      }
    }
  }
}
````

## File: sanity/schemaTypes/area.js
````javascript
import {TagIcon} from '@sanity/icons'

export default {
  name: 'area',
  title: 'Area',
  type: 'document',
  icon: TagIcon,
  fields: [
    {
      name: 'name',
      title: 'Nome',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {source: 'name'},
      validation: Rule => Rule.required()
    },
    {
      name: 'summary',
      title: 'Resumo',
      type: 'text',
      rows: 3
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: ['active', 'paused', 'archived'],
        layout: 'radio'
      },
      initialValue: 'active'
    },
    {
      name: 'visibility',
      title: 'Visibilidade',
      type: 'string',
      options: {
        list: ['private', 'internal', 'public'],
        layout: 'radio'
      },
      initialValue: 'private'
    }
  ],
  preview: {
    select: {
      title: 'name',
      status: 'status'
    }
  }
}
````

## File: sanity/schemaTypes/decision.js
````javascript
import {DocumentIcon} from '@sanity/icons'

export default {
  name: 'decision',
  title: 'Decision',
  type: 'document',
  icon: DocumentIcon,
  fields: [
    {
      name: 'id',
      title: 'ID',
      type: 'slug',
      options: {source: 'title'},
      validation: Rule => Rule.required()
    },
    {
      name: 'signal_ids',
      title: 'Signals',
      type: 'array',
      of: [{type: 'reference', to: [{type: 'signal'}]}]
    },
    {
      name: 'title',
      title: 'Título',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'summary',
      title: 'Resumo',
      type: 'text',
      rows: 4,
      validation: Rule => Rule.required()
    },
    {
      name: 'priority',
      title: 'Prioridade',
      type: 'string',
      options: {
        list: ['low', 'medium', 'high', 'critical'],
        layout: 'radio'
      },
      initialValue: 'medium'
    },
    {
      name: 'state',
      title: 'Estado',
      type: 'string',
      options: {
        list: ['pending', 'approved', 'rejected', 'resolved'],
        layout: 'radio'
      },
      initialValue: 'pending'
    },
    {
      name: 'owner',
      title: 'Owner',
      type: 'string',
      options: {
        list: ['human', 'agent', 'mixed'],
        layout: 'radio'
      },
      initialValue: 'human'
    },
    {
      name: 'created_at',
      title: 'Criada em',
      type: 'datetime',
      validation: Rule => Rule.required()
    },
    {
      name: 'resolved_at',
      title: 'Resolvida em',
      type: 'datetime'
    },
    {
      name: 'resolution',
      title: 'Resolução',
      type: 'text',
      rows: 4
    },
    {
      name: 'links',
      title: 'Links',
      type: 'array',
      of: [{
        type: 'object',
        fields: [
          {name: 'label', title: 'Rótulo', type: 'string'},
          {name: 'url', title: 'URL', type: 'url'}
        ]
      }]
    }
  ],
  preview: {
    select: {
      title: 'title',
      priority: 'priority',
      state: 'state'
    },
    prepare({title, priority, state}) {
      return {
        title,
        subtitle: `${priority || 'sem prioridade'} · ${state || 'sem estado'}`
      }
    }
  }
}
````

## File: sanity/schemaTypes/focus_session.js
````javascript
import {ClockIcon} from '@sanity/icons'

export default {
  name: 'focus_session',
  title: 'Focus Session',
  type: 'document',
  icon: ClockIcon,
  fields: [
    {
      name: 'task',
      title: 'Tarefa',
      type: 'reference',
      to: [{type: 'task'}]
    },
    {
      name: 'started_at',
      title: 'Início',
      type: 'datetime',
      validation: Rule => Rule.required()
    },
    {
      name: 'ended_at',
      title: 'Fim',
      type: 'datetime'
    },
    {
      name: 'planned_minutes',
      title: 'Minutos planejados',
      type: 'number'
    },
    {
      name: 'actual_minutes',
      title: 'Minutos reais',
      type: 'number'
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: ['active', 'completed', 'abandoned', 'canceled'],
        layout: 'radio'
      },
      initialValue: 'active'
    },
    {
      name: 'source',
      title: 'Fonte',
      type: 'reference',
      to: [{type: 'source'}]
    },
    {
      name: 'notes',
      title: 'Notas',
      type: 'text',
      rows: 4
    }
  ],
  preview: {
    select: {
      title: 'task.title',
      status: 'status',
      startedAt: 'started_at'
    },
    prepare({title, status, startedAt}) {
      return {
        title: title || 'Sessão sem tarefa',
        subtitle: `${status || 'sem status'} · ${startedAt || 'sem início'}`
      }
    }
  }
}
````

## File: sanity/schemaTypes/index.js
````javascript
import llmPrompt from './llm_prompt'
import persona from './persona'
import agentConfig from './agent_config'
import interventionScript from './intervention_script'
import project from './project'
import area from './area'
import task from './task'
import agendaBlock from './agenda_block'
import focusSession from './focus_session'
import signal from './signal'
import source from './source'
import decision from './decision'
import publicArtifact from './public_artifact'

export const schemaTypes = [
  llmPrompt,
  persona,
  agentConfig,
  interventionScript,
  project,
  area,
  task,
  agendaBlock,
  focusSession,
  signal,
  source,
  decision,
  publicArtifact,
]
````

## File: sanity/schemaTypes/intervention_script.js
````javascript
export default {
  name: 'intervention_script',
  title: 'Script de Intervenção',
  type: 'document',
  description: 'Mensagens enviadas quando hiperfoco prolongado é detectado',
  fields: [
    {
      name: 'agent_name',
      title: 'Agente',
      type: 'string',
      options: {
        list: ['focus_guard', 'life_guard', 'orchestrator'],
      },
      initialValue: 'focus_guard',
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'trigger_minutes',
      title: 'Disparar após (minutos)',
      type: 'number',
      description: 'Minutos de sessão ativa para disparar',
      validation: (Rule) => Rule.required().min(1),
    },
    {
      name: 'channel',
      title: 'Canal',
      type: 'string',
      options: {
        list: [
          {title: 'Mac', value: 'mac'},
          {title: 'Alexa', value: 'alexa'},
          {title: 'Mac + Alexa', value: 'mac+alexa'},
          {title: 'Somente log', value: 'log_only'},
        ],
      },
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'environment_scope',
      title: 'Ambiente',
      type: 'string',
      options: {
        list: [
          {title: 'Ambos', value: 'all'},
          {title: 'Local macOS', value: 'local'},
          {title: 'Servidor / Railway', value: 'server'},
        ],
        layout: 'radio',
      },
      initialValue: 'all',
    },
    {
      name: 'urgency',
      title: 'Urgência',
      type: 'string',
      options: {list: ['gentle', 'firm', 'loud']},
    },
    {
      name: 'sound',
      title: 'Som',
      type: 'boolean',
      initialValue: false,
    },
    {
      name: 'title',
      title: 'Título (Mac push)',
      type: 'string',
    },
    {
      name: 'message',
      title: 'Mensagem',
      type: 'text',
      rows: 3,
      description: 'Use {task}, {minutes} e {planned} para interpolação',
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'provider_preference',
      title: 'Provider preferido',
      type: 'string',
      options: {
        list: [
          {title: 'Auto', value: 'auto'},
          {title: 'Voice Monkey', value: 'voice_monkey'},
          {title: 'IFTTT', value: 'ifttt'},
          {title: 'Somente log', value: 'log_only'},
        ],
        layout: 'radio',
      },
      initialValue: 'auto',
    },
    {
      name: 'active',
      title: 'Ativo',
      type: 'boolean',
      initialValue: true,
    },
  ],
  orderings: [
    {
      title: 'Por tempo (crescente)',
      name: 'triggerAsc',
      by: [{field: 'trigger_minutes', direction: 'asc'}],
    },
  ],
  preview: {
    select: {
      agent: 'agent_name',
      minutes: 'trigger_minutes',
      channel: 'channel',
      scope: 'environment_scope',
    },
    prepare({agent, minutes, channel, scope}) {
      const channelLabels = {
        mac: 'Mac',
        alexa: 'Alexa',
        'mac+alexa': 'Mac + Alexa',
        log_only: 'Somente log',
      }
      const scopeLabels = {
        all: 'Ambos',
        local: 'Local macOS',
        server: 'Servidor / Railway',
      }
      const channelLabel = channelLabels[channel] || channel || 'canal'
      const scopeLabel = scope ? scopeLabels[scope] || scope : ''
      return {
        title: `${agent || 'agent'} · ${minutes} min`,
        subtitle: `${channelLabel}${scopeLabel ? ` · ${scopeLabel}` : ''}`,
      }
    },
  },
}
````

## File: sanity/schemaTypes/llm_prompt.js
````javascript
export default {
  name: 'llm_prompt',
  title: 'LLM Prompt',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Nome',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'id',
      title: 'ID único',
      type: 'slug',
      options: { source: 'name' },
      validation: Rule => Rule.required()
    },
    {
      name: 'agent',
      title: 'Agente ou capacidade',
      type: 'string',
      options: {
        list: [
          'orchestrator',
          'focus_guard',
          'scheduler',
          'validator',
          'retrospective',
          'gemma_local'
        ]
      },
      validation: Rule => Rule.required()
    },
    {
      name: 'prompt_type',
      title: 'Tipo',
      type: 'string',
      options: {
        list: [
          'routing',
          'synthesis',
          'direct',
          'deviation',
          'validation',
          'retrospective',
          'scheduling',
          'fallback',
          'intervention'
        ]
      }
    },
    {
      name: 'system_prompt',
      title: 'System Prompt',
      type: 'text',
      rows: 20,
      validation: Rule => Rule.required()
    },
    {
      name: 'temperature',
      title: 'Temperatura',
      type: 'number',
      validation: Rule => Rule.min(0).max(2)
    },
    {
      name: 'model_hint',
      title: 'Modelo sugerido',
      type: 'string',
      description: 'Ex.: gpt-4o-mini ou gemma3:4B-F16'
    },
    {
      name: 'version',
      title: 'Versão',
      type: 'string',
      initialValue: 'v1'
    },
    {
      name: 'active',
      title: 'Ativo',
      type: 'boolean',
      initialValue: true
    },
    {
      name: 'notes',
      title: 'Notas / Changelog',
      type: 'text',
      rows: 4
    }
  ],
  preview: {
    select: {
      title: 'name',
      agent: 'agent',
      type: 'prompt_type',
      active: 'active'
    },
    prepare({ title, agent, type, active }) {
      return {
        title,
        subtitle: `${agent}${type ? ` · ${type}` : ''}${active ? '' : ' · inativo'}`
      }
    }
  }
}
````

## File: sanity/schemaTypes/persona.js
````javascript
export default {
  name: 'persona',
  title: 'Persona',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Nome',
      type: 'string',
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'persona_id',
      title: 'ID',
      type: 'slug',
      options: {source: 'name'},
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'short_name',
      title: 'Nome curto',
      type: 'string',
    },
    {
      name: 'icon',
      title: 'Icone',
      type: 'string',
      description: 'Unicode curto para representar a persona na UI',
    },
    {
      name: 'description',
      title: 'Descrição',
      type: 'text',
    },
    {
      name: 'role',
      title: 'Papel',
      type: 'string',
      description: 'Ex.: arquiteto, coordenador, auditor, fallback local',
    },
    {
      name: 'tone',
      title: 'Tom',
      type: 'string',
      options: {
        list: [
          {title: 'Warm', value: 'warm'},
          {title: 'Professional', value: 'professional'},
          {title: 'Direct', value: 'direct'},
          {title: 'Casual', value: 'casual'},
          {title: 'Technical', value: 'technical'},
          {title: 'Strategic', value: 'strategic'},
          {title: 'Sharp', value: 'sharp'},
          {title: 'Bold', value: 'bold'},
          {title: 'Neutral', value: 'neutral'},
        ],
        layout: 'radio',
      },
    },
    {
      name: 'language',
      title: 'Idioma',
      type: 'string',
      description: 'Ex.: pt-BR ou en',
    },
    {
      name: 'style_rules',
      title: 'Regras de estilo',
      type: 'array',
      of: [{type: 'string'}],
      description: 'Regras curtas e atômicas de linguagem',
    },
    {
      name: 'system_prompt',
      title: 'System Prompt base',
      type: 'text',
      rows: 20,
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'synthesis_prompt_override',
      title: 'Override de síntese',
      type: 'text',
      rows: 8,
    },
    {
      name: 'direct_prompt_override',
      title: 'Override de resposta direta',
      type: 'text',
      rows: 8,
    },
    {
      name: 'preferred_model',
      title: 'Modelo preferido',
      type: 'string',
      description: 'Ex.: gpt-4o-mini ou gemma3:4B-F16',
    },
    {
      name: 'temperature_routing',
      title: 'Temperatura (roteamento)',
      type: 'number',
      validation: (Rule) => Rule.min(0).max(2),
    },
    {
      name: 'temperature_synthesis',
      title: 'Temperatura (síntese)',
      type: 'number',
      validation: (Rule) => Rule.min(0).max(2),
    },
    {
      name: 'temperature_direct',
      title: 'Temperatura (direta)',
      type: 'number',
      validation: (Rule) => Rule.min(0).max(2),
    },
    {
      name: 'parameters',
      title: 'Parâmetros',
      type: 'object',
      fields: [
        {
          name: 'temperature_routing',
          title: 'Temperatura (roteamento)',
          type: 'number',
          validation: (Rule) => Rule.min(0).max(2),
        },
        {
          name: 'temperature_synthesis',
          title: 'Temperatura (síntese)',
          type: 'number',
          validation: (Rule) => Rule.min(0).max(2),
        },
        {
          name: 'temperature_direct',
          title: 'Temperatura (direta)',
          type: 'number',
          validation: (Rule) => Rule.min(0).max(2),
        },
      ],
    },
    {
      name: 'active',
      title: 'Ativa',
      type: 'boolean',
      initialValue: true,
    },
  ],
  preview: {
    select: {
      title: 'name',
      tone: 'tone',
      role: 'role',
      icon: 'icon',
    },
    prepare({title, tone, role, icon}) {
      return {
        title: icon ? `${icon} ${title}` : title,
        subtitle: role ? `${role} · ${tone || 'sem tom'}` : tone || 'sem tom',
      }
    },
  },
}
````

## File: sanity/schemaTypes/project.js
````javascript
import {DocumentIcon} from '@sanity/icons'

export default {
  name: 'project',
  title: 'Project',
  type: 'document',
  icon: DocumentIcon,
  fields: [
    {
      name: 'name',
      title: 'Nome',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {source: 'name'},
      validation: Rule => Rule.required()
    },
    {
      name: 'summary',
      title: 'Resumo',
      type: 'text',
      rows: 3
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: ['draft', 'active', 'paused', 'archived'],
        layout: 'radio'
      },
      initialValue: 'active',
    },
    {
      name: 'visibility',
      title: 'Visibilidade',
      type: 'string',
      options: {
        list: ['private', 'internal', 'public'],
        layout: 'radio'
      },
      initialValue: 'private'
    },
    {
      name: 'primary_source',
      title: 'Fonte principal',
      type: 'reference',
      to: [{type: 'source'}]
    },
    {
      name: 'links',
      title: 'Links',
      type: 'array',
      of: [{
        type: 'object',
        fields: [
          {name: 'label', title: 'Rótulo', type: 'string'},
          {name: 'url', title: 'URL', type: 'url'}
        ]
      }]
    }
  ],
  preview: {
    select: {
      title: 'name',
      status: 'status',
      visibility: 'visibility'
    },
    prepare({title, status, visibility}) {
      return {
        title,
        subtitle: `${status || 'sem status'} · ${visibility || 'sem visibilidade'}`
      }
    }
  }
}
````

## File: sanity/schemaTypes/public_artifact.js
````javascript
import {DocumentIcon} from '@sanity/icons'

export default {
  name: 'public_artifact',
  title: 'Public Artifact',
  type: 'document',
  icon: DocumentIcon,
  fields: [
    {
      name: 'title',
      title: 'Título',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {source: 'title'},
      validation: Rule => Rule.required()
    },
    {
      name: 'artifact_type',
      title: 'Tipo',
      type: 'string',
      options: {
        list: ['note', 'report', 'manifesto', 'update', 'page', 'dataset'],
        layout: 'radio'
      },
      initialValue: 'note'
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: ['draft', 'review', 'approved', 'published', 'archived'],
        layout: 'radio'
      },
      initialValue: 'draft'
    },
    {
      name: 'visibility',
      title: 'Visibilidade',
      type: 'string',
      options: {
        list: ['private', 'internal', 'public'],
        layout: 'radio'
      },
      initialValue: 'public'
    },
    {
      name: 'summary',
      title: 'Resumo',
      type: 'text',
      rows: 3
    },
    {
      name: 'body',
      title: 'Corpo',
      type: 'array',
      of: [{type: 'block'}]
    },
    {
      name: 'source_signals',
      title: 'Signals de origem',
      type: 'array',
      of: [{type: 'reference', to: [{type: 'signal'}]}]
    },
    {
      name: 'source_decisions',
      title: 'Decisions de origem',
      type: 'array',
      of: [{type: 'reference', to: [{type: 'decision'}]}]
    },
    {
      name: 'canonical_url',
      title: 'URL canônica',
      type: 'url'
    },
    {
      name: 'ipfs_cid',
      title: 'IPFS CID',
      type: 'string'
    },
    {
      name: 'published_at',
      title: 'Publicado em',
      type: 'datetime'
    }
  ],
  preview: {
    select: {
      title: 'title',
      status: 'status',
      artifactType: 'artifact_type'
    },
    prepare({title, status, artifactType}) {
      return {
        title,
        subtitle: `${artifactType || 'sem tipo'} · ${status || 'sem status'}`
      }
    }
  }
}
````

## File: sanity/schemaTypes/signal.js
````javascript
import {DocumentIcon} from '@sanity/icons'

export default {
  name: 'signal',
  title: 'Signal',
  type: 'document',
  icon: DocumentIcon,
  fields: [
    {
      name: 'id',
      title: 'ID',
      type: 'slug',
      options: {source: 'message'},
      validation: Rule => Rule.required()
    },
    {
      name: 'source',
      title: 'Fonte',
      type: 'reference',
      to: [{type: 'source'}],
      validation: Rule => Rule.required()
    },
    {
      name: 'kind',
      title: 'Tipo',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'severity',
      title: 'Severidade',
      type: 'string',
      options: {
        list: ['ok', 'warn', 'fail', 'critical'],
        layout: 'radio'
      },
      validation: Rule => Rule.required()
    },
    {
      name: 'message',
      title: 'Mensagem',
      type: 'text',
      rows: 3,
      validation: Rule => Rule.required()
    },
    {
      name: 'timestamp',
      title: 'Timestamp',
      type: 'datetime',
      validation: Rule => Rule.required()
    },
    {
      name: 'actionable',
      title: 'Acionável',
      type: 'boolean',
      initialValue: false
    },
    {
      name: 'decision_required',
      title: 'Exige decisão',
      type: 'boolean',
      initialValue: false
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: ['open', 'acknowledged', 'dismissed', 'resolved'],
        layout: 'radio'
      },
      initialValue: 'open'
    },
    {
      name: 'dedupe_key',
      title: 'Dedupe key',
      type: 'string'
    },
    {
      name: 'ttl_hours',
      title: 'TTL em horas',
      type: 'number',
      initialValue: 24
    },
    {
      name: 'context',
      title: 'Contexto',
      type: 'text',
      rows: 10,
      description: 'JSON reduzido com payload relevante'
    }
  ],
  preview: {
    select: {
      title: 'message',
      severity: 'severity',
      status: 'status'
    },
    prepare({title, severity, status}) {
      return {
        title,
        subtitle: `${severity || 'sem severidade'} · ${status || 'sem status'}`
      }
    }
  }
}
````

## File: sanity/schemaTypes/source.js
````javascript
import {LinkIcon} from '@sanity/icons'

export default {
  name: 'source',
  title: 'Source',
  type: 'document',
  icon: LinkIcon,
  fields: [
    {
      name: 'id',
      title: 'ID',
      type: 'slug',
      options: {source: 'name'},
      validation: Rule => Rule.required()
    },
    {
      name: 'provider',
      title: 'Provider',
      type: 'string',
      options: {
        list: ['github', 'railway', 'vercel', 'cloudflare', 'onchain', 'notion', 'manual'],
        layout: 'radio'
      },
      validation: Rule => Rule.required()
    },
    {
      name: 'scope',
      title: 'Escopo',
      type: 'string',
      options: {
        list: ['org', 'project', 'service', 'token', 'repo', 'domain', 'contract'],
        layout: 'radio'
      },
      validation: Rule => Rule.required()
    },
    {
      name: 'name',
      title: 'Nome',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'identifier',
      title: 'Identificador',
      type: 'string'
    },
    {
      name: 'active',
      title: 'Ativa',
      type: 'boolean',
      initialValue: true
    },
    {
      name: 'owner',
      title: 'Owner',
      type: 'string'
    },
    {
      name: 'priority',
      title: 'Prioridade',
      type: 'string',
      options: {
        list: ['low', 'medium', 'high', 'critical'],
        layout: 'radio'
      },
      initialValue: 'medium'
    },
    {
      name: 'metadata',
      title: 'Metadata',
      type: 'text',
      rows: 8,
      description: 'JSON reduzido com contexto estrutural da fonte'
    }
  ],
  preview: {
    select: {
      title: 'name',
      provider: 'provider',
      scope: 'scope'
    },
    prepare({title, provider, scope}) {
      return {
        title,
        subtitle: `${provider || 'sem provider'} · ${scope || 'sem escopo'}`
      }
    }
  }
}
````

## File: sanity/schemaTypes/task.js
````javascript
import {CheckmarkCircleIcon} from '@sanity/icons'

export default {
  name: 'task',
  title: 'Task',
  type: 'document',
  icon: CheckmarkCircleIcon,
  fields: [
    {
      name: 'title',
      title: 'Título',
      type: 'string',
      validation: Rule => Rule.required()
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: ['A fazer', 'Em progresso', 'Concluído', 'Cancelado'],
        layout: 'radio'
      },
      initialValue: 'A fazer'
    },
    {
      name: 'priority',
      title: 'Prioridade',
      type: 'string',
      options: {
        list: ['Alta', 'Média', 'Baixa'],
        layout: 'radio'
      },
      initialValue: 'Média'
    },
    {
      name: 'project',
      title: 'Projeto',
      type: 'reference',
      to: [{type: 'project'}]
    },
    {
      name: 'area',
      title: 'Área',
      type: 'reference',
      to: [{type: 'area'}]
    },
    {
      name: 'source',
      title: 'Fonte',
      type: 'reference',
      to: [{type: 'source'}]
    },
    {
      name: 'external_id',
      title: 'ID externo',
      type: 'string'
    },
    {
      name: 'scheduled_time',
      title: 'Horário planejado',
      type: 'string'
    },
    {
      name: 'actual_time',
      title: 'Horário real',
      type: 'string'
    },
    {
      name: 'due_date',
      title: 'Data limite',
      type: 'date'
    },
    {
      name: 'visibility',
      title: 'Visibilidade',
      type: 'string',
      options: {
        list: ['private', 'internal', 'public'],
        layout: 'radio'
      },
      initialValue: 'private'
    },
    {
      name: 'notes',
      title: 'Notas',
      type: 'text',
      rows: 4
    }
  ],
  preview: {
    select: {
      title: 'title',
      status: 'status',
      priority: 'priority'
    },
    prepare({title, status, priority}) {
      return {
        title,
        subtitle: `${status || 'sem status'} · ${priority || 'sem prioridade'}`
      }
    }
  }
}
````

## File: sanity/static/.gitkeep
````
Files placed here will be served by the Sanity server under the `/static`-prefix
````

## File: sanity/.gitignore
````
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# Dependencies
/node_modules
/.pnp
.pnp.js

# Compiled Sanity Studio
/dist

# Temporary Sanity runtime, generated by the CLI on every dev server start
/.sanity

# Logs
/logs
*.log

# Coverage directory used by testing tools
/coverage

# Misc
.DS_Store
*.pem

# Typescript
*.tsbuildinfo

# Dotenv and similar local-only files
*.local
````

## File: sanity/eslint.config.mjs
````javascript
import studio from '@sanity/eslint-config-studio'

export default [...studio]
````

## File: sanity/package.json
````json
{
  "name": "neomello-agents",
  "private": true,
  "version": "1.0.0",
  "main": "package.json",
  "license": "UNLICENSED",
  "scripts": {
    "build": "sanity build",
    "deploy": "sanity deploy",
    "deploy-graphql": "sanity graphql deploy",
    "dev": "sanity dev",
    "start": "sanity start"
  },
  "keywords": [
    "sanity"
  ],
  "dependencies": {
    "@sanity/vision": "^5.18.0",
    "react": "^19.2.4",
    "react-dom": "^19.2.4",
    "sanity": "^5.18.0",
    "styled-components": "^6.1.18"
  },
  "devDependencies": {
    "@sanity/eslint-config-studio": "^6.0.0",
    "@types/react": "^19.2.14",
    "eslint": "^9.28",
    "prettier": "^3.5",
    "typescript": "^5.8"
  },
  "prettier": {
    "bracketSpacing": false,
    "printWidth": 100,
    "semi": false,
    "singleQuote": true
  }
}
````

## File: sanity/README.md
````markdown
# Sanity Clean Content Studio

Congratulations, you have now installed the Sanity Content Studio, an open-source real-time content editing environment connected to the Sanity backend.

Now you can do the following things:

- [Read “getting started” in the docs](https://www.sanity.io/docs/introduction/getting-started?utm_source=readme)
- [Join the Sanity community](https://www.sanity.io/community/join?utm_source=readme)
- [Extend and build plugins](https://www.sanity.io/docs/content-studio/extending?utm_source=readme)
````

## File: sanity/sanity.cli.js
````javascript
import { defineCliConfig } from 'sanity/cli'

export default defineCliConfig({
  api: {
    projectId: 'n4dgl02q',
    dataset: 'production'
  },
  deployment: {
    appId: 'v9i4hr48ddw5p63wea2jao6j',
    /**
     * Enable auto-updates for studios.
     * Learn more at https://www.sanity.io/docs/studio/latest-version-of-sanity#k47faf43faf56
     */
    autoUpdates: true,
  }
})
````

## File: sanity/sanity.config.js
````javascript
import {defineConfig} from 'sanity'
import {structureTool} from 'sanity/structure'
import {visionTool} from '@sanity/vision'
import {schemaTypes} from './schemaTypes'

export default defineConfig({
  name: 'default',
  title: 'neomello-agents',

  projectId: 'n4dgl02q',
  dataset: 'production',

  plugins: [structureTool(), visionTool()],

  schema: {
    types: schemaTypes,
  },
})
````

## File: scripts/com.multiagentes.docker-maintenance.plist.template
````
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.multiagentes.docker-maintenance</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>__SCRIPT__</string>
        <string>build</string>
    </array>

    <key>WorkingDirectory</key>
    <string>__PROJECT__</string>

    <key>RunAtLoad</key>
    <false/>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>__WEEKDAY__</integer>
        <key>Hour</key>
        <integer>__HOUR__</integer>
        <key>Minute</key>
        <integer>__MINUTE__</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/tmp/docker-maintenance.log</string>

    <key>StandardErrorPath</key>
    <string>/tmp/docker-maintenance.err</string>
</dict>
</plist>
````

## File: scripts/docker_maintenance.sh
````bash
#!/usr/bin/env bash
# =============================================================================
# docker_maintenance.sh — Limpeza de manutenção do Docker
# =============================================================================
# Uso:
#   bash scripts/docker_maintenance.sh build   # foco em build cache (agressivo)
#   bash scripts/docker_maintenance.sh safe    # limpeza conservadora
#   bash scripts/docker_maintenance.sh deep    # limpeza ampla de artefatos sem uso

set -euo pipefail

MODE="${1:-build}"
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/docker-maintenance.log"

mkdir -p "$LOG_DIR"

timestamp() {
    date '+%Y-%m-%d %H:%M:%S'
}

log() {
    echo "[$(timestamp)] $*"
}

if ! command -v docker >/dev/null 2>&1; then
    echo "ERRO: Docker CLI não encontrada."
    exit 1
fi

if ! docker info >/dev/null 2>&1; then
    echo "ERRO: Docker daemon indisponível. Abra o Docker Desktop e tente novamente."
    exit 1
fi

{
    log "Iniciando manutenção Docker (mode=$MODE)"
    log "Resumo antes:"
    docker system df
    echo ""

    case "$MODE" in
        build)
            log "Executando docker builder prune -af"
            docker builder prune -af
            ;;
        safe)
            log "Executando docker builder prune -f"
            docker builder prune -f
            log "Executando docker image prune -f"
            docker image prune -f
            ;;
        deep)
            log "Executando docker builder prune -af"
            docker builder prune -af
            log "Executando docker image prune -a -f"
            docker image prune -a -f
            ;;
        *)
            echo "Uso inválido. Modos aceitos: build | safe | deep"
            exit 1
            ;;
    esac

    echo ""
    log "Resumo depois:"
    docker system df
    log "Manutenção concluída"
} | tee -a "$LOG_FILE"
````

## File: scripts/install_docker_maintenance_launchd.sh
````bash
#!/usr/bin/env bash
# =============================================================================
# install_docker_maintenance_launchd.sh — Agenda manutenção Docker via launchd
# =============================================================================
# Uso:
#   bash scripts/install_docker_maintenance_launchd.sh
#   bash scripts/install_docker_maintenance_launchd.sh --uninstall
#
# Personalização opcional:
#   WEEKDAY=0 HOUR=4 MINUTE=10 bash scripts/install_docker_maintenance_launchd.sh
# Weekday: 0 (domingo) ... 6 (sábado)

set -euo pipefail

LABEL="com.multiagentes.docker-maintenance"
PROJECT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT_PATH="$PROJECT/scripts/docker_maintenance.sh"
PLIST_SRC="$PROJECT/scripts/${LABEL}.plist.template"
PLIST_DEST="$HOME/Library/LaunchAgents/${LABEL}.plist"

WEEKDAY="${WEEKDAY:-0}"
HOUR="${HOUR:-4}"
MINUTE="${MINUTE:-10}"

if [[ "${1:-}" == "--uninstall" ]]; then
    echo "Desinstalando agendamento de manutenção Docker..."
    launchctl unload "$PLIST_DEST" 2>/dev/null || true
    rm -f "$PLIST_DEST"
    echo "Removido: $PLIST_DEST"
    exit 0
fi

if [[ ! -x "$SCRIPT_PATH" ]]; then
    echo "ERRO: script de manutenção não executável em $SCRIPT_PATH"
    echo "Execute: chmod +x scripts/docker_maintenance.sh"
    exit 1
fi

if [[ ! -f "$PLIST_SRC" ]]; then
    echo "ERRO: template plist não encontrado em $PLIST_SRC"
    exit 1
fi

mkdir -p "$HOME/Library/LaunchAgents"

sed \
    -e "s|__SCRIPT__|$SCRIPT_PATH|g" \
    -e "s|__PROJECT__|$PROJECT|g" \
    -e "s|__WEEKDAY__|$WEEKDAY|g" \
    -e "s|__HOUR__|$HOUR|g" \
    -e "s|__MINUTE__|$MINUTE|g" \
    "$PLIST_SRC" > "$PLIST_DEST"

launchctl unload "$PLIST_DEST" 2>/dev/null || true
launchctl load "$PLIST_DEST"

echo "Agendamento instalado: $PLIST_DEST"
echo "Janela semanal: weekday=$WEEKDAY hour=$HOUR minute=$MINUTE"
echo ""
echo "Comandos úteis:"
echo "  Status:      launchctl list | grep docker-maintenance"
echo "  Executar já: bash scripts/docker_maintenance.sh build"
echo "  Logs script: tail -n 100 logs/docker-maintenance.log"
echo "  Logs launchd stdout: tail -n 100 /tmp/docker-maintenance.log"
echo "  Logs launchd stderr: tail -n 100 /tmp/docker-maintenance.err"
echo "  Remover:     bash scripts/install_docker_maintenance_launchd.sh --uninstall"
````

## File: scripts/install_launchd.sh
````bash
#!/usr/bin/env bash
# =============================================================================
# install_launchd.sh — Instala o Focus Guard como serviço launchd no macOS
# =============================================================================
# Uso: bash scripts/install_launchd.sh
# Para desinstalar: bash scripts/install_launchd.sh --uninstall

set -euo pipefail

LABEL="com.multiagentes.focusguard"
PLIST_SRC="$(cd "$(dirname "$0")" && pwd)/${LABEL}.plist"
PLIST_DEST="$HOME/Library/LaunchAgents/${LABEL}.plist"
PROJECT="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON="$PROJECT/.venv/bin/python3"

# ---- Desinstalação ----
if [[ "${1:-}" == "--uninstall" ]]; then
    echo "Desinstalando Focus Guard..."
    launchctl unload "$PLIST_DEST" 2>/dev/null || true
    rm -f "$PLIST_DEST"
    echo "Removido: $PLIST_DEST"
    echo "Focus Guard desinstalado."
    exit 0
fi

# ---- Pré-requisitos ----
if [[ ! -f "$PYTHON" ]]; then
    echo "ERRO: Python não encontrado em $PYTHON"
    echo "Execute 'make install' antes de instalar o serviço."
    exit 1
fi

if [[ ! -f "$PROJECT/focus_guard_service.py" ]]; then
    echo "ERRO: focus_guard_service.py não encontrado em $PROJECT"
    exit 1
fi

# ---- Geração do plist final ----
mkdir -p "$HOME/Library/LaunchAgents"

sed \
    -e "s|__PYTHON__|$PYTHON|g" \
    -e "s|__PROJECT__|$PROJECT|g" \
    "$PLIST_SRC" > "$PLIST_DEST"

echo "Plist gerado: $PLIST_DEST"

# ---- Carrega o serviço ----
# Se já estava carregado, descarrega primeiro
launchctl unload "$PLIST_DEST" 2>/dev/null || true
launchctl load "$PLIST_DEST"

echo ""
echo "Focus Guard instalado e iniciado."
echo ""
echo "Comandos úteis:"
echo "  Status:      launchctl list | grep focusguard"
echo "  Logs:        tail -f /tmp/focusguard.log"
echo "  Erros:       tail -f /tmp/focusguard.err"
echo "  Parar:       launchctl unload $PLIST_DEST"
echo "  Desinstalar: bash scripts/install_launchd.sh --uninstall"
````

## File: web/static/manifest.json
````json
{
  "name": "Multiagentes",
  "short_name": "Agentes",
  "description": "Gate with nodes multiagents to archtect NEØ",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#000000",
  "theme_color": "#000000",
  "orientation": "portrait",
  "icons": [
    {
      "src": "/static/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/static/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ]
}
````

## File: web/static/sw.js
````javascript
const CACHE_NAME = "multiagentes-v1";
const PRECACHE = ["/", "/static/manifest.json"];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(PRECACHE)));
  self.skipWaiting();
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(
          keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)),
        ),
      ),
  );
  self.clients.claim();
});

self.addEventListener("fetch", (e) => {
  // Network-first for API/HTML, cache-first for static assets
  if (e.request.url.includes("/static/")) {
    e.respondWith(
      caches.match(e.request).then((cached) => cached || fetch(e.request)),
    );
  } else {
    e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
  }
});

// Push notification handler (ready for future use)
self.addEventListener("push", (e) => {
  const data = e.data ? e.data.json() : {};
  const title = data.title || " >_ nodE NEØ - Agents Gate ";
  const options = {
    body: data.body || "",
    icon: "/static/icon-192.png",
    badge: "/static/icon-192.png",
    tag: data.tag || "default",
    data: { url: data.url || "/" },
  };
  e.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener("notificationclick", (e) => {
  e.notification.close();
  const url = e.notification.data?.url || "/";
  e.waitUntil(
    self.clients.matchAll({ type: "window" }).then((clients) => {
      for (const client of clients) {
        if (client.url.includes(url) && "focus" in client)
          return client.focus();
      }
      return self.clients.openWindow(url);
    }),
  );
});
````

## File: web/templates/partials/agenda.html
````html
{% if blocks %}
  {% for b in blocks %}
  {% include "partials/block_row.html" %}
  {% endfor %}
{% else %}
  <div class="empty">Sem blocos hoje</div>
{% endif %}
````

## File: web/templates/partials/block_row.html
````html
<div class="blk{{ ' done' if b.completed else '' }}" id="ab-{{ b.id }}">
  <span class="blk-time">{{ b.time_slot }}</span>
  <div class="blk-main">
    <div class="blk-head">
      <span class="blk-name{{ ' blk-done' if b.completed else '' }}">{{ b.task_title or '—' }}</span>
      <span class="badge {{ b.display_state_class or 'badge-def' }}">{{ b.display_state_label or 'Aberto' }}</span>
    </div>
    {% if b.rescheduled_to_block_id %}
    <div class="blk-meta">Reagendado para o bloco #{{ b.rescheduled_to_block_id }}</div>
    {% elif b.is_overdue %}
    <div class="blk-meta">Bloco vencido e aguardando conclusão</div>
    {% endif %}
  </div>
  {% if not b.completed %}
  <button class="blk-btn"
          hx-post="/block/{{ b.id }}/complete"
          hx-target="#ab-{{ b.id }}"
          hx-swap="outerHTML"
          aria-label="Concluir">&#10003;</button>
  {% else %}
  <span class="tsk-done-icon">&#10003;</span>
  {% endif %}
</div>
````

## File: web/templates/partials/chat_message.html
````html
<div class="msg u">
  <div class="msg-av">N</div>
  <div class="msg-bub">{{ user_message }}</div>
</div>
<div class="msg">
  <div class="msg-av">{% if active_persona and active_persona.icon %}{{ active_persona.icon }}{% else %}&#9041;{% endif %}</div>
  <div class="msg-bub">{{ bot_response }}</div>
</div>
````

## File: web/templates/partials/status.html
````html
{% set t = summary.tasks %} {% set f = summary.focus %} {% set a =
summary.agenda_today %} {% set al = summary.alerts %} {% set tv = task_overview
%}

<div
  id="stats-row"
  class="metrics"
  hx-get="/status"
  hx-trigger="every 20s"
  hx-swap="outerHTML"
>
  <div class="metric m-blue">
    <div class="metric-lbl">Pendentes</div>
    <div class="metric-val v-blue">{{ tv.pending_count }}</div>
    <div class="metric-sub">
      {{ tv.overdue_count }} atrasada{{ 's' if tv.overdue_count != 1 else '' }}
      &middot; {{ tv.in_progress_count }} em prog
    </div>
  </div>

  <div class="metric m-green">
    <div class="metric-lbl">Agenda</div>
    <div class="metric-val v-green">
      {{ a.completed }}<span class="v-frac">/{{ a.total_blocks }}</span>
    </div>
    <div class="metric-sub">blocos hoje</div>
  </div>

  <div class="metric {% if f.guard_running %}m-green{% else %}m-dim{% endif %}">
    <div class="metric-lbl">Foco</div>
    <div
      class="metric-val v-text {% if f.guard_running %}v-green{% else %}v-dim{% endif %}"
    >
      {% if f.guard_running %}Ativo{% else %}Off{% endif %}
    </div>
    <div class="metric-sub">
      {% if f.on_track %}on track{% else %}desvio detectado{% endif %}
    </div>
  </div>

  <div class="metric {% if al.pending > 0 %}m-red{% else %}m-dim{% endif %}">
    <div class="metric-lbl">Alertas</div>
    <div
      class="metric-val {% if al.pending > 0 %}v-red{% else %}v-dim{% endif %}"
    >
      {{ al.pending }}
    </div>
    <div class="metric-sub">pendente{{ 's' if al.pending != 1 else '' }}</div>
  </div>
</div>
````

## File: web/templates/partials/task_row.html
````html
<div class="tsk{{ ' done' if t.status == 'Concluído' else '' }}" id="tr-{{ t.id }}">
  <span class="tsk-pri {% if t.priority == 'Alta' %}pri-h{% elif t.priority == 'Média' or t.priority == 'Media' %}pri-m{% else %}pri-l{% endif %}"></span>
  <div class="tsk-main">
    <div class="tsk-head">
      <span class="tsk-name">{{ t.title }}</span>
      <span class="badge {{ t.display_status_class or 'badge-def' }}">{{ t.display_status or t.status }}</span>
    </div>
    {% if t.display_meta %}
    <div class="tsk-meta">{{ t.display_meta }}</div>
    {% endif %}
  </div>
  {% if t.status != 'Concluído' %}
  <button class="tsk-btn"
          hx-post="/task/{{ t.id }}/complete"
          hx-target="#tr-{{ t.id }}"
          hx-swap="outerHTML"
          aria-label="Concluir">&#10003;</button>
  {% else %}
  <span class="tsk-done-icon">&#10003;</span>
  {% endif %}
</div>
````

## File: web/templates/partials/tasks.html
````html
{% if tasks %}
  {% for t in tasks %}
  {% include "partials/task_row.html" %}
  {% endfor %}
{% else %}
  <div class="empty">Sem tarefas</div>
{% endif %}
````

## File: web/templates/agenda.html
````html
{% extends "base.html" %}
{% block page_title %}Agenda Navegável{% endblock %}
{% block content %}

<div class="section-title">Agenda Navegável</div>

{% if import_msg is defined %}
<div class="toast toast-ok">{{ import_msg }}</div>
{% endif %}

<div class="card">
  <div class="card-hd">
    <span class="card-lbl-dim">Intervalo</span>
  </div>
  <form class="form-row" method="get" action="/agenda">
    <input class="f-date" type="date" name="start_date" value="{{ start_date }}" required />
    <input class="f-date" type="date" name="end_date" value="{{ end_date }}" required />
    <button class="f-btn" type="submit">Filtrar</button>
  </form>
  <form class="form-row" method="post" action="/agenda/import" style="padding-top:0">
    <input type="hidden" name="start_date" value="{{ start_date }}" />
    <input type="hidden" name="end_date" value="{{ end_date }}" />
    <select class="f-select" name="source" required>
      <option value="notion">Notion (principal)</option>
      <option value="calendar">Google Calendar (opcional)</option>
    </select>
    <button class="f-btn f-btn-sec" type="submit">Importar</button>
  </form>
</div>

<div class="card">
  <div class="card-hd">
    <span class="card-lbl">Blocos</span>
    <span class="card-lbl-dim">{{ blocks|length }}</span>
  </div>
  {% if blocks %}
    {% for b in blocks %}
    <div class="ls-item">
      <div class="ls-top">
        <span class="ls-title">{{ b.task_title or 'Sem titulo' }}</span>
        <span class="badge {% if b.completed %}badge-ok{% elif b.rescheduled %}badge-warn{% else %}badge-def{% endif %}">
          {% if b.completed %}concluido{% elif b.rescheduled %}reagendado{% else %}aberto{% endif %}
        </span>
      </div>
      <div class="ls-detail">{{ b.block_date }} &middot; {{ b.time_slot }}</div>
      <div class="ls-meta">
        {% if b.created_by %}<span>{{ b.created_by }}</span>{% endif %}
        {% if b.source_block_id %}<span>origem {{ b.source_block_id }}</span>{% endif %}
        {% if b.rescheduled_to_block_id %}<span>novo {{ b.rescheduled_to_block_id }}</span>{% endif %}
        <span>#{{ b.id }}</span>
      </div>
    </div>
    {% endfor %}
  {% else %}
    <div class="empty">Sem blocos neste intervalo</div>
  {% endif %}
</div>

{% endblock %}
````

## File: web/templates/audit.html
````html
{% extends "base.html" %} {% block page_title %}Audit{% endblock %} {% block
content %} {% set t = summary.tasks %} {% set f = summary.focus %} {% set a =
summary.agenda_today %} {% set al = summary.alerts %}

<div class="section-title">Audit</div>

<div class="metrics">
  <div class="metric {% if al.pending > 0 %}m-red{% else %}m-dim{% endif %}">
    <div class="metric-lbl">Alertas</div>
    <div
      class="metric-val {% if al.pending > 0 %}v-red{% else %}v-dim{% endif %}"
    >
      {{ al.pending }}
    </div>
    <div class="metric-sub">pendentes</div>
  </div>
  <div class="metric {% if f.on_track %}m-green{% else %}m-yell{% endif %}">
    <div class="metric-lbl">Foco</div>
    <div
      class="metric-val v-text {% if f.on_track %}v-green{% else %}v-yell{% endif %}"
    >
      {% if f.on_track %}Estavel{% else %}Desvio{% endif %}
    </div>
    <div class="metric-sub">
      guard {% if f.guard_running %}ativo{% else %}off{% endif %}
    </div>
  </div>
</div>

{# ── Eventos ── #}
<div class="card">
  <div class="card-hd">
    <span class="card-lbl">Desvios e Reagendamentos</span>
  </div>
  {% if audit_events %} {% for event in audit_events %}
  <div class="ls-item">
    <div class="ls-top">
      <span class="ls-title">{{ event.title }}</span>
      <span
        class="badge {% if event.level == 'error' %}badge-err{% elif event.level == 'warning' %}badge-warn{% else %}badge-ok{% endif %}"
        >{{ event.event_type }}</span
      >
    </div>
    {% if event.details %}
    <div class="ls-detail">{{ event.details }}</div>
    {% endif %}
    <div class="ls-meta">
      <span>{{ event.created_at }}</span>
      <span>{{ event.agent }}</span>
      {% if event.related_id %}<span>ref {{ event.related_id }}</span>{% endif
      %}
    </div>
  </div>
  {% endfor %} {% else %}
  <div class="empty">Sem eventos</div>
  {% endif %}
</div>

{# ── Alertas ── #}
<div class="card">
  <div class="card-hd">
    <span class="card-lbl">Alertas</span>
    {% if alerts and alerts | selectattr("acknowledged", "equalto", 0) | list %}
    <button
      class="card-act"
      hx-post="/alerts/dismiss-all"
      hx-target="#alerts-list"
      hx-swap="innerHTML"
      hx-confirm="Descartar todos os alertas pendentes?"
    >Limpar tudo</button>
    {% endif %}
  </div>
  <div id="alerts-list">
  {% if alerts %} {% for alert in alerts %}
  <div class="ls-item" id="alert-{{ alert.id }}">
    <div class="ls-top">
      <span class="ls-title">{{ alert.message }}</span>
      <div style="display:flex;gap:6px;align-items:center;">
        <span class="badge {% if alert.acknowledged %}badge-ok{% else %}badge-warn{% endif %}">
          {{ alert.alert_type }}
        </span>
        {% if not alert.acknowledged %}
        <button
          class="tsk-btn"
          style="width:26px;height:26px;font-size:13px;"
          hx-post="/alert/{{ alert.id }}/dismiss"
          hx-target="#alert-{{ alert.id }}"
          hx-swap="outerHTML"
          title="Descartar"
        >✕</button>
        {% endif %}
      </div>
    </div>
    <div class="ls-meta">
      <span>{{ alert.created_at }}</span>
      <span>{% if alert.acknowledged %}ack{% else %}pendente{% endif %}</span>
      <span>#{{ alert.id }}</span>
    </div>
  </div>
  {% endfor %} {% else %}
  <div class="empty">Sem alertas</div>
  {% endif %}
  </div>
</div>

{# ── Handoffs ── #}
<div class="card">
  <div class="card-hd"><span class="card-lbl">Handoffs</span></div>
  {% if handoffs %} {% for h in handoffs %}
  <div class="ls-item">
    <div class="ls-top">
      <span class="ls-title">{{ h.source_agent }} → {{ h.target_agent }}</span>
      <span
        class="badge {% if h.status == 'error' %}badge-err{% elif h.status == 'success' %}badge-ok{% else %}badge-warn{% endif %}"
        >{{ h.status }}</span
      >
    </div>
    <div class="ls-detail" style="font-family: var(--mono); font-size: 12px">
      {{ h.action }}
    </div>
    <div class="ls-meta">
      <span>{{ h.created_at }}</span>
      <span>#{{ h.id }}</span>
    </div>
  </div>
  {% endfor %} {% else %}
  <div class="empty">Sem handoffs</div>
  {% endif %}
</div>

{# ── Log ── #}
<div class="card">
  <div class="card-hd"><span class="card-lbl">Log</span></div>
  <div class="log-pane">
    {% if log_lines %}{% for line in log_lines %}{{ line }}{% endfor %}{% else
    %}Sem logs{% endif %}
  </div>
</div>

{% endblock %}
````

## File: web/templates/base.html
````html
<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0, viewport-fit=cover, user-scalable=no"
    />
    <meta name="mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <meta name="theme-color" content="#000000" />
    <link rel="manifest" href="/static/manifest.json" />
    <link rel="apple-touch-icon" href="/static/icon-192.png" />
    <title>{% block title %} >_ nodE NEØ - Agents Gate {% endblock %}</title>
    <script src="https://unpkg.com/htmx.org@1.9.12"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500;700&family=Figtree:wght@400;500;600;700;800;900&display=swap"
      rel="stylesheet"
    />
    <style>
      *,
      *::before,
      *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }

      :root {
        --bg: #000;
        --s1: #07090d;
        --s2: #0f131a;
        --s3: #141a23;
        --s4: #1a2230;
        --s5: #273244;
        --sep: rgba(255, 255, 255, 0.06);
        --text: rgba(255, 255, 255, 0.95);
        --t2: rgba(255, 255, 255, 0.75);
        --t3: rgba(255, 255, 255, 0.55);
        --t4: rgba(255, 255, 255, 0.12);
        --pink: #ff00cc;
        --pink-dim: rgba(255, 0, 204, 0.12);
        --neon: #c8d41a;
        --neon-dim: rgba(200, 212, 26, 0.14);
        --acqua: #37b8ff;
        --acqua-dim: rgba(55, 184, 255, 0.16);
        --blue: var(--acqua);
        --blue-dim: var(--acqua-dim);
        --green: var(--neon);
        --green-dim: var(--neon-dim);
        --red: #ff4b5c;
        --red-dim: rgba(255, 75, 92, 0.14);
        --yell: #ffb800;
        --yell-dim: rgba(255, 184, 0, 0.14);
        --cyan: var(--acqua);
        --orange: #ff8a00;
        --orange-dim: rgba(255, 138, 0, 0.15);
        --r: 18px;
        --rs: 12px;
        --font: "Figtree", sans-serif;
        --mono: "DM Mono", ui-monospace, monospace;
        --tab-h: 52px;
        --safe-b: env(safe-area-inset-bottom, 0px);
        --safe-t: env(safe-area-inset-top, 0px);
        --gutter: clamp(12px, 3.6vw, 18px);
      }

      html,
      body {
        height: 100%;
        background: var(--bg);
        color: var(--text);
        font-family: var(--font);
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        overscroll-behavior-y: contain;
      }

      body {
        position: relative;
        overflow-x: hidden;
      }
      body::before {
        content: "";
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        background:
          radial-gradient(
            120% 60% at 50% -8%,
            rgba(55, 184, 255, 0.16) 0%,
            rgba(55, 184, 255, 0.03) 28%,
            transparent 62%
          ),
          radial-gradient(
            140% 60% at 88% 112%,
            rgba(55, 184, 255, 0.1) 0%,
            transparent 56%
          ),
          linear-gradient(180deg, #040507 0%, #000 52%);
      }
      body::after {
        content: "";
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        opacity: 0.16;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.05'/%3E%3C/svg%3E");
      }
      #bg-net {
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        width: 100%;
        height: 100%;
        opacity: 0.72;
      }
      #bg-net .line {
        stroke: rgba(55, 184, 255, 0.24);
        stroke-width: 1;
      }
      #bg-net .node {
        fill: #37b8ff;
      }

      /* ══ Shell ══ */
      .shell {
        position: relative;
        z-index: 1;
        display: flex;
        flex-direction: column;
        min-height: 100dvh;
        max-width: 980px;
        margin: 0 auto;
        border-left: 1px solid rgba(255, 255, 255, 0.03);
        border-right: 1px solid rgba(255, 255, 255, 0.03);
      }

      /* ══ Header ══ */
      .hdr {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 8px var(--gutter) 10px;
        padding-top: calc(var(--safe-t) + 8px);
        background: rgba(5, 5, 7, 0.78);
        backdrop-filter: saturate(180%) blur(20px);
        -webkit-backdrop-filter: saturate(180%) blur(20px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        flex-shrink: 0;
        z-index: 20;
      }
      .hdr-title {
        flex: 1;
        font-size: 17px;
        font-weight: 800;
        letter-spacing: -0.2px;
        text-transform: uppercase;
      }
      .hdr-right {
        display: flex;
        align-items: center;
        gap: 8px;
      }
      .hdr-clock {
        font-size: 11px;
        font-family: var(--mono);
        color: var(--t3);
        font-variant-numeric: tabular-nums;
      }
      .pill {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 100px;
        padding: 4px 10px 4px 8px;
        font-size: 10px;
        font-weight: 600;
        color: var(--t2);
        letter-spacing: 0.06em;
      }
      .pill-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: var(--green);
        box-shadow: 0 0 8px var(--green);
      }
      .pill-dot.off {
        background: var(--orange);
        box-shadow: 0 0 6px rgba(255, 138, 0, 0.45);
      }
      .hdr-btn {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: var(--t2);
        border-radius: 100px;
        padding: 5px 12px;
        font-size: 11px;
        font-weight: 600;
        cursor: pointer;
        font-family: var(--font);
        transition: all 0.15s;
        -webkit-tap-highlight-color: transparent;
      }
      .hdr-btn:active {
        background: rgba(255, 255, 255, 0.08);
        color: var(--acqua);
        transform: scale(0.95);
      }

      /* ══ Content ══ */
      .content {
        flex: 1;
        overflow-y: auto;
        overflow-x: hidden;
        -webkit-overflow-scrolling: touch;
        padding: 14px var(--gutter) 0;
        padding-bottom: calc(var(--tab-h) + var(--safe-b) + 14px);
      }

      /* ══ Tab bar ══ */
      .tabs {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: min(100%, 980px);
        z-index: 100;
        display: flex;
        align-items: stretch;
        height: calc(var(--tab-h) + var(--safe-b));
        padding-bottom: var(--safe-b);
        background: rgba(7, 7, 8, 0.84);
        backdrop-filter: saturate(180%) blur(24px);
        -webkit-backdrop-filter: saturate(180%) blur(24px);
        border-top: 1px solid rgba(255, 255, 255, 0.06);
      }
      .tab {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 1px;
        text-decoration: none;
        color: var(--t3);
        font-size: 10px;
        font-weight: 500;
        letter-spacing: 0.1px;
        padding: 4px 0 2px;
        transition: color 0.12s;
        -webkit-tap-highlight-color: transparent;
        position: relative;
      }
      .tab:active {
        transform: scale(0.9);
      }
      .tab.active {
        color: var(--neon);
      }
      .tab-ico {
        width: 24px;
        height: 24px;
      }
      .tab-ico svg {
        width: 24px;
        height: 24px;
        fill: none;
        stroke: currentColor;
        stroke-width: 1.8;
        stroke-linecap: round;
        stroke-linejoin: round;
      }
      .tab.active .tab-ico svg {
        stroke-width: 2.2;
        filter: drop-shadow(0 0 8px rgba(200, 212, 26, 0.35));
      }
      .tab-badge {
        position: absolute;
        top: 2px;
        right: 50%;
        margin-right: -18px;
        min-width: 16px;
        height: 16px;
        border-radius: 8px;
        background: var(--red);
        color: #fff;
        font-size: 9px;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 4px;
        font-family: var(--font);
      }
      .tab-badge:empty {
        display: none;
      }

      /* ══ Cards ══ */
      .card {
        position: relative;
        background:
          linear-gradient(
            180deg,
            rgba(255, 255, 255, 0.02) 0%,
            transparent 44%
          ),
          radial-gradient(
            110% 80% at 80% 100%,
            rgba(200, 212, 26, 0.04) 0%,
            transparent 52%
          ),
          var(--s2);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: var(--r);
        overflow: hidden;
        margin-bottom: 12px;
        box-shadow:
          0 1px 2px rgba(0, 0, 0, 0.5),
          0 14px 40px rgba(0, 0, 0, 0.36),
          inset 0 1px 0 rgba(255, 255, 255, 0.03);
      }
      .card::after {
        content: "";
        position: absolute;
        inset: 0;
        border-radius: inherit;
        padding: 1px;
        background: linear-gradient(
          160deg,
          rgba(255, 255, 255, 0.11) 0%,
          rgba(255, 255, 255, 0.01) 48%,
          transparent 72%
        );
        -webkit-mask:
          linear-gradient(#fff 0 0) content-box,
          linear-gradient(#fff 0 0);
        mask:
          linear-gradient(#fff 0 0) content-box,
          linear-gradient(#fff 0 0);
        -webkit-mask-composite: destination-out;
        mask-composite: exclude;
        pointer-events: none;
      }
      .card-hd {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 16px 8px;
      }
      .card-lbl {
        font-size: 13px;
        font-weight: 600;
        letter-spacing: -0.1px;
        color: var(--text);
      }
      .card-lbl-dim {
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.3px;
        text-transform: uppercase;
        color: var(--t3);
      }
      .card-act {
        background: none;
        border: none;
        color: var(--acqua);
        cursor: pointer;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 0.01em;
        padding: 0;
        font-family: var(--font);
        -webkit-tap-highlight-color: transparent;
        text-decoration: none;
      }
      .card-act:active {
        opacity: 0.6;
      }
      .card-body {
        padding: 0;
      }

      /* ══ Metric row ══ */
      .metrics {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-bottom: 12px;
      }
      .metric {
        background:
          linear-gradient(
            180deg,
            rgba(255, 255, 255, 0.02) 0%,
            transparent 44%
          ),
          radial-gradient(
            120% 85% at 82% 100%,
            rgba(255, 255, 255, 0.03) 0%,
            transparent 54%
          ),
          var(--s2);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: var(--r);
        padding: 14px 16px 12px;
        position: relative;
        overflow: hidden;
        box-shadow:
          0 1px 2px rgba(0, 0, 0, 0.5),
          0 10px 28px rgba(0, 0, 0, 0.3),
          inset 0 1px 0 rgba(255, 255, 255, 0.03);
      }
      .metric::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        border-radius: var(--r) var(--r) 0 0;
      }
      .metric.m-blue::before {
        background: linear-gradient(
          90deg,
          transparent,
          var(--acqua),
          transparent
        );
      }
      .metric.m-green::before {
        background: linear-gradient(
          90deg,
          transparent,
          var(--green),
          transparent
        );
      }
      .metric.m-red::before {
        background: linear-gradient(
          90deg,
          transparent,
          var(--red),
          transparent
        );
      }
      .metric.m-yell::before {
        background: linear-gradient(
          90deg,
          transparent,
          var(--yell),
          transparent
        );
      }
      .metric.m-dim::before {
        background: linear-gradient(90deg, transparent, var(--s5), transparent);
      }
      .metric-lbl {
        font-size: 11px;
        font-weight: 600;
        color: var(--t3);
        margin-bottom: 6px;
        letter-spacing: 0.06em;
        text-transform: uppercase;
      }
      .metric-val {
        font-size: 28px;
        font-weight: 700;
        font-family: var(--mono);
        line-height: 1;
        font-variant-numeric: tabular-nums;
      }
      .metric-sub {
        font-size: 10px;
        color: var(--t3);
        margin-top: 4px;
      }
      .v-blue {
        color: var(--blue);
      }
      .v-green {
        color: var(--green);
      }
      .v-red {
        color: var(--red);
      }
      .v-yell {
        color: var(--yell);
      }
      .v-dim {
        color: var(--t3);
      }
      .v-text {
        font-size: 18px;
        font-family: var(--font);
        letter-spacing: -0.1px;
        font-weight: 800;
        padding-top: 2px;
      }
      .v-frac {
        font-size: 15px;
        color: var(--t3);
      }

      /* ══ Block row (agenda) ══ */
      .blk {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 11px 16px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.04);
        transition: background 0.1s;
      }
      .blk:last-child {
        border-bottom: none;
      }
      .blk:active {
        background: rgba(255, 255, 255, 0.03);
      }
      .blk.done {
        opacity: 0.45;
      }
      .blk-time {
        font-family: var(--mono);
        font-size: 12px;
        color: var(--cyan);
        min-width: 82px;
        flex-shrink: 0;
        font-variant-numeric: tabular-nums;
      }
      .blk-name {
        flex: 1;
        font-size: 14px;
        font-weight: 500;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }
      .blk-main {
        flex: 1;
        min-width: 0;
        display: flex;
        flex-direction: column;
        gap: 4px;
      }
      .blk-head {
        display: flex;
        align-items: center;
        gap: 8px;
        min-width: 0;
      }
      .blk-meta {
        font-size: 11px;
        color: var(--t2);
        min-width: 0;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }
      .blk-done {
        text-decoration: line-through;
        color: var(--t3);
      }
      .blk-btn {
        background: none;
        border: 1.5px solid var(--s5);
        color: var(--t3);
        border-radius: 50%;
        width: 26px;
        height: 26px;
        cursor: pointer;
        font-size: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        -webkit-tap-highlight-color: transparent;
        transition: all 0.12s;
      }
      .blk-btn:active {
        border-color: var(--neon);
        color: var(--neon);
        background: var(--green-dim);
      }

      /* ══ Task row ══ */
      .tsk {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 11px 16px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      }
      .tsk:last-child {
        border-bottom: none;
      }
      .tsk.done .tsk-name {
        text-decoration: line-through;
        color: var(--t3);
      }
      .tsk-pri {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        flex-shrink: 0;
      }
      .pri-h {
        background: var(--pink);
        box-shadow: 0 0 5px var(--pink-dim);
      }
      .pri-m {
        background: var(--yell);
      }
      .pri-l {
        background: var(--s5);
      }
      .tsk-main {
        flex: 1;
        min-width: 0;
        display: flex;
        flex-direction: column;
        gap: 4px;
      }
      .tsk-head {
        display: flex;
        align-items: center;
        gap: 8px;
        min-width: 0;
      }
      .tsk-name {
        font-size: 14px;
        font-weight: 500;
        min-width: 0;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }
      .tsk-meta {
        font-size: 11px;
        color: var(--t2);
        min-width: 0;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }
      .tsk-btn {
        background: none;
        border: 1.5px solid var(--s5);
        color: var(--t3);
        border-radius: 50%;
        width: 26px;
        height: 26px;
        cursor: pointer;
        font-size: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        -webkit-tap-highlight-color: transparent;
        transition: all 0.12s;
      }
      .tsk-btn:active {
        border-color: var(--neon);
        color: var(--neon);
        background: var(--green-dim);
      }
      .tsk-done-icon {
        color: var(--neon);
        font-size: 13px;
        flex-shrink: 0;
      }

      /* ══ Add task ══ */
      .add-bar {
        display: flex;
        gap: 8px;
        padding: 12px 16px;
        border-bottom: 0.5px solid var(--sep);
      }
      .add-input {
        flex: 1;
        background: var(--s3);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: var(--text);
        padding: 10px 14px;
        border-radius: var(--rs);
        font-size: 15px;
        outline: none;
        font-family: var(--font);
        transition: border-color 0.15s;
      }
      .add-input:focus {
        border-color: var(--acqua);
      }
      .add-select {
        background: var(--s3);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: var(--t2);
        padding: 10px 6px;
        border-radius: var(--rs);
        font-size: 13px;
        outline: none;
        font-family: var(--font);
        cursor: pointer;
        width: 48px;
      }
      .add-btn {
        background: linear-gradient(
          135deg,
          var(--acqua),
          rgba(0, 242, 255, 0.75)
        );
        border: none;
        color: #031014;
        width: 40px;
        border-radius: var(--rs);
        cursor: pointer;
        font-size: 20px;
        font-weight: 300;
        font-family: var(--font);
        -webkit-tap-highlight-color: transparent;
        transition: all 0.12s;
      }
      .add-btn:active {
        filter: brightness(1.08);
        transform: scale(0.95);
      }

      /* ══ Chat ══ */
      .chat-msgs {
        flex: 1;
        overflow-y: auto;
        padding: 14px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        min-height: 0;
      }
      .msg {
        display: flex;
        gap: 8px;
        align-items: flex-end;
      }
      .msg.u {
        flex-direction: row-reverse;
      }
      .msg-av {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        background: var(--s4);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        flex-shrink: 0;
        color: var(--t2);
      }
      .u .msg-av {
        background: linear-gradient(
          140deg,
          var(--acqua),
          rgba(0, 242, 255, 0.64)
        );
        color: #041114;
      }
      .msg-bub {
        max-width: 80%;
        padding: 10px 14px;
        border-radius: 20px;
        font-size: 15px;
        line-height: 1.4;
        letter-spacing: -0.1px;
      }
      .msg:not(.u) .msg-bub {
        background: var(--s3);
        border-bottom-left-radius: 6px;
      }
      .u .msg-bub {
        background: linear-gradient(
          140deg,
          rgba(0, 242, 255, 0.22),
          rgba(0, 242, 255, 0.12)
        );
        border: 1px solid rgba(0, 242, 255, 0.3);
        border-bottom-right-radius: 6px;
      }
      .chat-bar {
        display: flex;
        gap: 8px;
        padding: 10px 14px;
        border-top: 0.5px solid var(--sep);
        flex-shrink: 0;
        background: var(--s1);
      }
      .chat-input {
        flex: 1;
        background: var(--s3);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: var(--text);
        padding: 10px 16px;
        border-radius: 22px;
        font-size: 15px;
        outline: none;
        font-family: var(--font);
        transition: border-color 0.15s;
      }
      .chat-input:focus {
        border-color: var(--acqua);
      }
      .chat-send {
        background: linear-gradient(
          135deg,
          var(--acqua),
          rgba(0, 242, 255, 0.75)
        );
        border: none;
        color: #041114;
        width: 38px;
        height: 38px;
        border-radius: 50%;
        cursor: pointer;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        -webkit-tap-highlight-color: transparent;
        transition: all 0.12s;
      }
      .chat-send:active {
        transform: scale(0.9);
      }
      .chat-send svg {
        width: 18px;
        height: 18px;
        fill: none;
        stroke: #041114;
        stroke-width: 2.5;
        stroke-linecap: round;
        stroke-linejoin: round;
      }

      /* Chat page */
      .chat-page .content {
        padding: 0;
        padding-bottom: 0;
        display: flex;
        flex-direction: column;
        overflow: hidden;
      }
      .chat-page .chat-bar {
        position: fixed;
        bottom: calc(var(--tab-h) + var(--safe-b));
        left: 0;
        right: 0;
        z-index: 50;
      }
      .chat-page .content {
        padding-bottom: calc(var(--tab-h) + var(--safe-b) + 62px);
      }
      .chat-page .chat-msgs {
        flex: 1;
        overflow-y: auto;
      }

      /* ══ List items ══ */
      .ls-item {
        display: flex;
        flex-direction: column;
        gap: 4px;
        padding: 12px 16px;
        border-bottom: 0.5px solid var(--sep);
      }
      .ls-item:last-child {
        border-bottom: none;
      }
      .ls-top {
        display: flex;
        align-items: center;
        gap: 10px;
        justify-content: space-between;
      }
      .ls-title {
        font-size: 14px;
        font-weight: 500;
        flex: 1;
        min-width: 0;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }
      .badge {
        display: inline-flex;
        align-items: center;
        border-radius: 6px;
        padding: 2px 8px;
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 0.2px;
        text-transform: uppercase;
        flex-shrink: 0;
      }
      .badge-ok {
        color: var(--green);
        background: var(--green-dim);
      }
      .badge-warn {
        color: var(--yell);
        background: var(--yell-dim);
      }
      .badge-err {
        color: var(--orange);
        background: var(--orange-dim);
      }
      .badge-def {
        color: var(--t2);
        background: rgba(255, 255, 255, 0.03);
      }
      .ls-detail {
        font-size: 13px;
        color: var(--t2);
      }
      .ls-meta {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        font-size: 11px;
        color: var(--t3);
        font-family: var(--mono);
        font-variant-numeric: tabular-nums;
      }

      /* ══ Forms ══ */
      .form-row {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        padding: 10px 16px;
      }
      .f-date,
      .f-select {
        background: var(--s3);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: var(--text);
        border-radius: var(--rs);
        padding: 10px 12px;
        font-size: 14px;
        font-family: var(--font);
        flex: 1;
        min-width: 0;
      }
      .f-btn {
        background: linear-gradient(
          135deg,
          var(--acqua),
          rgba(0, 242, 255, 0.72)
        );
        border: none;
        color: #041114;
        padding: 10px 16px;
        border-radius: var(--rs);
        font-size: 14px;
        font-weight: 700;
        font-family: var(--font);
        cursor: pointer;
        -webkit-tap-highlight-color: transparent;
        flex: 0 0 auto;
      }
      .f-btn:active {
        filter: brightness(1.15);
        transform: scale(0.97);
      }
      .f-btn-sec {
        background: var(--s4);
        color: var(--text);
        border: 1px solid rgba(255, 255, 255, 0.08);
      }

      /* ══ Log ══ */
      .log-pane {
        overflow: auto;
        padding: 14px 16px;
        font-family: var(--mono);
        font-size: 11px;
        line-height: 1.6;
        color: var(--t2);
        background: var(--s1);
        white-space: pre-wrap;
        max-height: 280px;
        border-radius: 0 0 var(--r) var(--r);
      }

      /* ══ Toast ══ */
      .toast {
        padding: 8px 14px;
        margin: 0 0 12px;
        border-radius: var(--rs);
        font-size: 13px;
        font-weight: 600;
        text-align: center;
      }
      .toast-ok {
        background: var(--green-dim);
        color: var(--green);
      }
      .toast-err {
        background: var(--orange-dim);
        color: var(--orange);
      }

      /* ══ Section title ══ */
      .section-title {
        font-size: 24px;
        font-weight: 900;
        letter-spacing: -0.02em;
        text-transform: uppercase;
        padding: 6px 2px 12px;
      }

      /* ══ Empty ══ */
      .empty {
        padding: 28px 16px;
        text-align: center;
        color: var(--t3);
        font-size: 14px;
      }

      /* ══ Loading ══ */
      .spinner {
        font-size: 11px;
        color: var(--t3);
        letter-spacing: 3px;
        animation: pulse 1s ease-in-out infinite;
      }
      @keyframes pulse {
        0%,
        100% {
          opacity: 0.15;
        }
        50% {
          opacity: 1;
        }
      }
      .spin {
        animation: sp 0.6s linear infinite;
      }
      @keyframes sp {
        to {
          transform: rotate(360deg);
        }
      }

      /* ══ Persona selector ══ */
      .persona-wrap {
        position: relative;
        display: flex;
        align-items: center;
      }
      .persona-select {
        appearance: none;
        -webkit-appearance: none;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: var(--text);
        padding: 4px 24px 4px 8px;
        border-radius: 100px;
        font-size: 11px;
        font-weight: 600;
        font-family: var(--font);
        cursor: pointer;
        outline: none;
        transition: border-color 0.15s;
        min-width: 0;
        max-width: 100px;
        text-overflow: ellipsis;
      }
      .persona-select:focus {
        border-color: var(--acqua);
      }
      .persona-wrap::after {
        content: "▾";
        position: absolute;
        right: 8px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 9px;
        color: var(--t3);
        pointer-events: none;
      }
      .persona-label {
        display: none;
      }
      .persona-toast {
        position: fixed;
        top: calc(var(--safe-t) + 52px);
        left: 50%;
        transform: translateX(-50%) translateY(-8px);
        background: var(--s3);
        border: 1px solid var(--s5);
        color: var(--text);
        padding: 8px 16px;
        border-radius: var(--rs);
        font-size: 13px;
        font-weight: 500;
        z-index: 200;
        opacity: 0;
        transition:
          opacity 0.2s,
          transform 0.2s;
        pointer-events: none;
        white-space: nowrap;
      }
      .persona-toast.show {
        opacity: 1;
        transform: translateX(-50%) translateY(0);
      }

      /* ══ HTMX ══ */
      .htmx-indicator {
        opacity: 0;
        transition: opacity 0.2s;
      }
      .htmx-request .htmx-indicator {
        opacity: 1;
      }
      .htmx-request .sync-lbl {
        display: none;
      }
      input:disabled,
      button:disabled {
        opacity: 0.4;
        cursor: not-allowed;
      }

      /* ══ Scrollbar ══ */
      ::-webkit-scrollbar {
        width: 0;
      }

      /* ══ Error toast ══ */
      #err-toast {
        position: fixed;
        bottom: calc(var(--tab-h) + var(--safe-b) + 16px);
        left: var(--gutter);
        right: var(--gutter);
        z-index: 999;
        background: var(--orange);
        color: #101010;
        padding: 12px 16px;
        border-radius: var(--rs);
        font-size: 14px;
        font-weight: 500;
        text-align: center;
        opacity: 0;
        transform: translateY(8px);
        transition:
          opacity 0.2s,
          transform 0.2s;
        pointer-events: none;
      }
      #err-toast.show {
        opacity: 1;
        transform: translateY(0);
        pointer-events: auto;
      }
    </style>
  </head>
  <body class="{{ page_name|default('dashboard') }}-page">
    <svg id="bg-net" aria-hidden="true"></svg>
    <div class="shell">
      <header class="hdr">
        <div class="hdr-title">
          {% block page_title %} >_ nodE NEØ - Agents Gate {% endblock %}
        </div>
        <div class="hdr-right">
          <div class="persona-wrap" id="persona-selector">
            <select
              name="persona"
              class="persona-select"
              onchange="switchPersona(this.value)"
            >
              {% if personas is defined and personas %} {% for p in personas %}
              <option
                value="{{ p.id }}"
                {%
                if
                active_persona_id
                is
                defined
                and
                p.id
                in
                [active_persona_id]
                %}
                selected{%
                endif
                %}
              >
                {{ p.icon }} {{ p.short_name }}
              </option>
              {% endfor %} {% else %}
              <option value="coordinator" selected>🎯 Coord</option>
              {% endif %}
            </select>
          </div>
          <span class="hdr-clock" id="clk"></span>
          <div class="pill">
            <span
              class="pill-dot{% if not summary or not summary.focus.guard_running %} off{% endif %}"
            ></span>
            Guard
          </div>
          <button
            class="hdr-btn"
            hx-post="/sync"
            hx-target="#toast-area"
            hx-swap="innerHTML"
            hx-indicator="#sync-sp"
            hx-disabled-elt="this"
          >
            <span
              id="sync-sp"
              class="htmx-indicator spin"
              style="font-size: 11px"
              >&#8635;</span
            >
            <span class="sync-lbl">Sync</span>
          </button>
        </div>
      </header>

      <main class="content">
        <div id="toast-area"></div>
        {% block content %}{% endblock %}
      </main>

      <nav class="tabs">
        <a
          href="/"
          class="tab{% if page_name == 'dashboard' %} active{% endif %}"
        >
          <span class="tab-ico"
            ><svg viewBox="0 0 24 24">
              <path
                d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1"
              /></svg
          ></span>
          Home
        </a>
        <a
          href="/agenda"
          class="tab{% if page_name == 'agenda' %} active{% endif %}"
        >
          <span class="tab-ico"
            ><svg viewBox="0 0 24 24">
              <rect x="3" y="4" width="18" height="18" rx="2" />
              <path d="M16 2v4M8 2v4M3 10h18" /></svg
          ></span>
          Agenda
        </a>
        <a
          href="/tasks-page"
          class="tab{% if page_name == 'tasks' %} active{% endif %}"
        >
          <span class="tab-ico"
            ><svg viewBox="0 0 24 24">
              <path d="M9 11l3 3L22 4" />
              <path
                d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"
              /></svg
          ></span>
          Tarefas
        </a>
        <a
          href="/chat-page"
          class="tab{% if page_name == 'chat' %} active{% endif %}"
        >
          <span class="tab-ico"
            ><svg viewBox="0 0 24 24">
              <path
                d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"
              /></svg
          ></span>
          Chat
        </a>
        <a
          href="/audit"
          class="tab{% if page_name == 'audit' %} active{% endif %}"
        >
          <span class="tab-ico"
            ><svg viewBox="0 0 24 24">
              <path d="M12 20h9" />
              <path
                d="M16.5 3.5a2.121 2.121 0 113 3L7 19l-4 1 1-4L16.5 3.5z"
              /></svg
          ></span>
          Audit {% if summary and summary.alerts and summary.alerts.pending > 0
          %}
          <span class="tab-badge">{{ summary.alerts.pending }}</span>
          {% endif %}
        </a>
        <a
          href="/ecosystem-page"
          class="tab{% if page_name == 'ecosystem' %} active{% endif %}"
        >
          <span class="tab-ico"
            ><svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.5"
            >
              <circle cx="12" cy="12" r="10" />
              <ellipse cx="12" cy="12" rx="4" ry="10" />
              <path d="M2 12h20" /></svg
          ></span>
          Eco
        </a>
      </nav>
    </div>

    <div id="err-toast" role="alert" aria-live="assertive"></div>
    <div id="persona-toast" class="persona-toast"></div>

    <script>
      !(function () {
        function clk() {
          var e = document.getElementById("clk");
          if (e)
            e.textContent = new Date().toLocaleTimeString("pt-BR", {
              hour: "2-digit",
              minute: "2-digit",
            });
        }
        clk();
        setInterval(clk, 10000);

        var _t;
        function showErr(m) {
          var t = document.getElementById("err-toast");
          if (!t) return;
          t.textContent = m;
          t.classList.add("show");
          clearTimeout(_t);
          _t = setTimeout(function () {
            t.classList.remove("show");
          }, 4000);
        }
        document.body.addEventListener("htmx:responseError", function (e) {
          showErr("Erro " + (e.detail.xhr ? e.detail.xhr.status : "?"));
        });
        document.body.addEventListener("htmx:sendError", function () {
          showErr("Sem conexao");
        });

        if ("serviceWorker" in navigator)
          navigator.serviceWorker
            .register("/static/sw.js")
            .catch(function () {});

        function initBackgroundNetwork() {
          var svg = document.getElementById("bg-net");
          if (!svg) return;

          var NS = "http://www.w3.org/2000/svg";
          var prefersReducedMotion =
            window.matchMedia &&
            window.matchMedia("(prefers-reduced-motion: reduce)").matches;
          var state = { nodes: [], lines: [], raf: null, w: 0, h: 0 };

          function el(name, attrs) {
            var e = document.createElementNS(NS, name);
            for (var k in attrs) e.setAttribute(k, attrs[k]);
            return e;
          }

          function setup() {
            state.w = window.innerWidth;
            state.h = window.innerHeight;
            svg.setAttribute("viewBox", "0 0 " + state.w + " " + state.h);
            svg.innerHTML = "";
            state.nodes = [];
            state.lines = [];

            var nodeCount = state.w < 720 ? 14 : 22;
            var maxLinks = state.w < 720 ? 2 : 3;
            var gLines = el("g", { class: "lines" });
            var gNodes = el("g", { class: "nodes" });
            svg.appendChild(gLines);
            svg.appendChild(gNodes);

            for (var i = 0; i < nodeCount; i++) {
              var node = {
                x: Math.random() * state.w,
                y: Math.random() * state.h,
                vx: (Math.random() - 0.5) * 0.34,
                vy: (Math.random() - 0.5) * 0.34,
                r: Math.random() * 1.9 + 1.1,
                links: [],
                dot: null,
              };
              node.dot = el("circle", {
                class: "node",
                cx: node.x.toFixed(2),
                cy: node.y.toFixed(2),
                r: node.r.toFixed(2),
                opacity: "0.85",
              });
              gNodes.appendChild(node.dot);
              state.nodes.push(node);
            }

            for (var a = 0; a < state.nodes.length; a++) {
              for (var b = a + 1; b < state.nodes.length; b++) {
                var line = el("line", {
                  class: "line",
                  x1: "0",
                  y1: "0",
                  x2: "0",
                  y2: "0",
                  opacity: "0",
                });
                gLines.appendChild(line);
                state.lines.push({ i: a, j: b, el: line });
              }
            }

            state.maxLinks = maxLinks;
          }

          function step() {
            if (prefersReducedMotion) return;
            var i, n;
            for (i = 0; i < state.nodes.length; i++) {
              n = state.nodes[i];
              n.x += n.vx;
              n.y += n.vy;
              if (n.x < 0 || n.x > state.w) n.vx *= -1;
              if (n.y < 0 || n.y > state.h) n.vy *= -1;
              if (n.x < 0) n.x = 0;
              if (n.x > state.w) n.x = state.w;
              if (n.y < 0) n.y = 0;
              if (n.y > state.h) n.y = state.h;
              n.links = [];
            }

            var maxDist = state.w < 720 ? 120 : 170;
            var lineData = [];
            for (i = 0; i < state.lines.length; i++) {
              var item = state.lines[i];
              var n1 = state.nodes[item.i];
              var n2 = state.nodes[item.j];
              var dx = n1.x - n2.x;
              var dy = n1.y - n2.y;
              var d = Math.sqrt(dx * dx + dy * dy);
              lineData.push({ item: item, d: d });
            }
            lineData.sort(function (a, b) {
              return a.d - b.d;
            });

            for (i = 0; i < lineData.length; i++) {
              var data = lineData[i];
              var item2 = data.item;
              var nn1 = state.nodes[item2.i];
              var nn2 = state.nodes[item2.j];
              var canLink =
                data.d < maxDist &&
                nn1.links.length < state.maxLinks &&
                nn2.links.length < state.maxLinks;
              if (canLink) {
                nn1.links.push(item2.j);
                nn2.links.push(item2.i);
                var op = 0.08 + ((maxDist - data.d) / maxDist) * 0.34;
                item2.el.setAttribute("x1", nn1.x.toFixed(2));
                item2.el.setAttribute("y1", nn1.y.toFixed(2));
                item2.el.setAttribute("x2", nn2.x.toFixed(2));
                item2.el.setAttribute("y2", nn2.y.toFixed(2));
                item2.el.setAttribute("opacity", op.toFixed(3));
              } else {
                item2.el.setAttribute("opacity", "0");
              }
            }

            for (i = 0; i < state.nodes.length; i++) {
              var node = state.nodes[i];
              node.dot.setAttribute("cx", node.x.toFixed(2));
              node.dot.setAttribute("cy", node.y.toFixed(2));
            }

            state.raf = requestAnimationFrame(step);
          }

          setup();
          if (!prefersReducedMotion) state.raf = requestAnimationFrame(step);
          window.addEventListener("resize", function () {
            if (state.raf) cancelAnimationFrame(state.raf);
            setup();
            if (!prefersReducedMotion) state.raf = requestAnimationFrame(step);
          });
        }

        initBackgroundNetwork();

        window.switchPersona = function (id) {
          fetch("/persona/" + id, { method: "POST" })
            .then(function (r) {
              return r.text();
            })
            .then(function (html) {
              // Update cookie client-side as backup
              document.cookie =
                "multiagentes_persona=" +
                id +
                ";path=/;max-age=31536000;samesite=lax";
              // Show toast
              var sel = document.querySelector(".persona-select");
              var opt = sel ? sel.options[sel.selectedIndex] : null;
              var label = opt ? opt.textContent.trim() : id;
              var toast = document.getElementById("persona-toast");
              if (toast) {
                toast.textContent = "Persona: " + label;
                toast.classList.add("show");
                setTimeout(function () {
                  toast.classList.remove("show");
                }, 2000);
              }
            })
            .catch(function () {});
        };
      })();
    </script>
  </body>
</html>
````

## File: web/templates/chat_page.html
````html
{% extends "base.html" %} {% block page_title %}Chat{% endblock %} {% block
content %}

<div class="chat-msgs" id="chat-msgs">
  <div class="msg">
    <div class="msg-av">
      {% if active_persona and active_persona.icon %}{{ active_persona.icon }}{%
      else %}&#9041;{% endif %}
    </div>
    <div class="msg-bub">
      {% if active_persona and active_persona.name %}{{ active_persona.name }}
      aqui. Como posso ajudar?{% else %}Ola! Como posso ajudar?{% endif %}
    </div>
  </div>
</div>

<form
  class="chat-bar"
  hx-post="/chat"
  hx-target="#chat-msgs"
  hx-swap="beforeend"
  hx-indicator="#chat-ld"
  hx-disabled-elt="find input, find button"
  hx-on::after-request="if(event.detail.successful){this.reset()} scrollChat()"
  hx-on::after-swap="scrollChat()"
>
  <span id="chat-ld" class="htmx-indicator spinner">&#9679;&#9679;&#9679;</span>
  <input
    class="chat-input"
    type="text"
    name="message"
    placeholder="Digite..."
    autocomplete="off"
    required
    aria-label="Mensagem"
  />
  <button class="chat-send" type="submit" aria-label="Enviar">
    <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" /></svg>
  </button>
</form>

<script>
  function scrollChat() {
    var m = document.getElementById("chat-msgs");
    if (m) m.scrollTop = m.scrollHeight;
  }
</script>

{% endblock %}
````

## File: web/templates/ecosystem_page.html
````html
{% extends "base.html" %} {% block title %}Ecosystem — NEØ{% endblock %} {%
block content %}

<style>
  .eco-section {
    margin-bottom: 20px;
  }

  .eco-hd {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 0 10px;
  }
  .eco-hd-label {
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--t2);
  }
  .eco-hd-ts {
    font-size: 11px;
    color: var(--t3);
    font-family: var(--mono);
  }

  /* Status row */
  .eco-summary {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
    margin-bottom: 20px;
  }
  .eco-metric {
    background: var(--s2);
    border-radius: var(--rs);
    padding: 14px 12px;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .eco-metric-lbl {
    font-size: 11px;
    color: var(--t3);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .eco-metric-val {
    font-size: 22px;
    font-weight: 700;
    font-family: var(--mono);
  }
  .eco-metric-sub {
    font-size: 11px;
    color: var(--t2);
  }

  /* Service rows */
  .eco-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 11px 14px;
    background: var(--s2);
    border-radius: var(--rs);
    margin-bottom: 6px;
  }
  .eco-row-icon {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }
  .ico-ok {
    background: var(--green);
  }
  .ico-warn {
    background: var(--yell);
  }
  .ico-fail {
    background: var(--orange);
  }
  .ico-dim {
    background: var(--t3);
  }

  .eco-row-name {
    flex: 1;
    font-size: 14px;
    font-weight: 500;
  }
  .eco-row-detail {
    font-size: 12px;
    color: var(--t2);
    font-family: var(--mono);
  }
  .eco-prio {
    font-size: 10px;
    padding: 2px 6px;
    border-radius: 4px;
    background: var(--s4);
    color: var(--t3);
    font-weight: 600;
  }
  .eco-prio-p0 {
    background: var(--blue-dim);
    color: var(--blue);
  }

  /* Report block */
  .eco-report {
    background: var(--s2);
    border-radius: var(--rs);
    padding: 16px;
    font-family: var(--mono);
    font-size: 12px;
    line-height: 1.7;
    color: var(--t2);
    white-space: pre-wrap;
    word-break: break-word;
  }
  .eco-report .ok {
    color: var(--green);
  }
  .eco-report .warn {
    color: var(--yell);
  }
  .eco-report .fail {
    color: var(--orange);
  }

  /* Run button */
  .eco-run-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 16px;
    background: var(--blue-dim);
    color: var(--blue);
    border: none;
    border-radius: var(--rs);
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    width: 100%;
    justify-content: center;
    margin-bottom: 20px;
    -webkit-tap-highlight-color: transparent;
  }
  .eco-run-btn:active {
    opacity: 0.7;
  }
  .htmx-request .eco-run-btn {
    opacity: 0.5;
    pointer-events: none;
  }

  /* Org rows */
  .org-row {
    padding: 10px 14px;
    background: var(--s2);
    border-radius: var(--rs);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .org-name {
    flex: 1;
    font-size: 13px;
    font-weight: 500;
  }
  .org-meta {
    font-size: 11px;
    color: var(--t3);
    font-family: var(--mono);
  }
</style>

<div
  class="content"
  id="eco-main"
  hx-get="/ecosystem"
  hx-trigger="every 120s"
  hx-target="#eco-main"
  hx-swap="outerHTML"
>
  <!-- Header -->
  <div class="eco-hd">
    <span class="eco-hd-label">Ecosystem</span>
    <span class="eco-hd-ts">{{ timestamp }}</span>
  </div>

  <!-- Run button -->
  <button
    class="eco-run-btn"
    hx-post="/ecosystem/run"
    hx-target="#eco-main"
    hx-swap="outerHTML"
    hx-indicator="#eco-main"
  >
    <svg
      width="16"
      height="16"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
    >
      <polyline points="1 4 1 10 7 10" />
      <path d="M3.51 15a9 9 0 1 0 .49-3.44" />
    </svg>
    Rodar health check
  </button>

  <!-- Summary metrics -->
  <div class="eco-summary">
    <div class="eco-metric">
      <span class="eco-metric-lbl">Status</span>
      <span
        class="eco-metric-val"
        style="
          color: var(
            --{% if global_status == "ok" %}green{% elif global_status
              == "fail" %}orange{% else %}yell{% endif %}
          );
        "
      >
        {{ global_status | upper }}
      </span>
      <span class="eco-metric-sub">ecossistema</span>
    </div>
    <div class="eco-metric">
      <span class="eco-metric-lbl">Railway</span>
      <span
        class="eco-metric-val"
        style="
          color: var(
            --{% if railway_fail > 0 %}orange{% elif railway_warn > 0 %}yell{%
              else %}green{% endif %}
          );
        "
      >
        {{ railway_ok }}/{{ railway_total }}
      </span>
      <span class="eco-metric-sub">serviços ok</span>
    </div>
    <div class="eco-metric">
      <span class="eco-metric-lbl">GitHub</span>
      <span
        class="eco-metric-val"
        style="
          color: var(
            --{% if repos_active == 0 %}yell{% else %}green{% endif %}
          );
        "
      >
        {{ repos_active }}
      </span>
      <span class="eco-metric-sub">ativos 24h</span>
    </div>
  </div>

  <!-- Railway services -->
  <div class="eco-section">
    <div class="eco-hd">
      <span class="eco-hd-label">Infra (Railway)</span>
    </div>
    {% for svc in railway_services %}
    <div class="eco-row">
      <span class="eco-row-icon ico-{{ svc.status }}"></span>
      <span class="eco-row-name">{{ svc.name }}</span>
      <span class="eco-prio {% if svc.priority == 'P0' %}eco-prio-p0{% endif %}"
        >{{ svc.priority }}</span
      >
      <span class="eco-row-detail">
        {% if svc.http_code %}{{ svc.http_code }}{% if svc.response_ms %} · {{
        svc.response_ms }}ms{% endif %}{% else %}{{ svc.error }}{% endif %}
      </span>
    </div>
    {% endfor %}
  </div>

  <!-- GitHub orgs -->
  <div class="eco-section">
    <div class="eco-hd">
      <span class="eco-hd-label">GitHub</span>
    </div>
    {% for org in github_orgs %}
    <div class="org-row">
      <span class="eco-row-icon ico-{{ org.status }}"></span>
      <span class="org-name">{{ org.name }}</span>
      <span class="org-meta"
        >{{ org.active_24h }} ativo · {{ org.issues }} issues</span
      >
    </div>
    {% endfor %}
  </div>

  <!-- On-chain -->
  <div class="eco-section">
    <div class="eco-hd">
      <span class="eco-hd-label">On-chain</span>
    </div>
    <div class="eco-row">
      <span class="eco-row-icon ico-{{ neoflw.status }}"></span>
      <span class="eco-row-name">NEOFLW · Base</span>
      <span class="eco-row-detail">
        {% if neoflw.price_usd %} ${{ neoflw.price_usd }} · Δ{{
        neoflw.price_change_24h_pct }}% {% else %} sem dados {% endif %}
      </span>
    </div>
  </div>

  <!-- Ações sugeridas -->
  {% if actions %}
  <div class="eco-section">
    <div class="eco-hd">
      <span class="eco-hd-label">Ações sugeridas</span>
    </div>
    {% for action in actions %}
    <div class="eco-row">
      <span class="eco-row-icon ico-warn"></span>
      <span class="eco-row-name" style="font-size: 13px; color: var(--t2)"
        >{{ action }}</span
      >
    </div>
    {% endfor %}
  </div>
  {% endif %}
</div>
{% endblock %}
````

## File: web/templates/index.html
````html
{% extends "base.html" %} {% block page_title %} >_ nodE NEØ - Agents Gate {%
endblock %} {% block content %} {% set t = summary.tasks %} {% set f =
summary.focus %} {% set a = summary.agenda_today %} {% set al = summary.alerts
%} {% set tv = task_overview %} {# ── Greeting ── #}
<div class="section-title" id="greeting"></div>

{# ── Metrics ── #}
<div
  id="stats-row"
  class="metrics"
  hx-get="/status"
  hx-trigger="every 20s"
  hx-swap="outerHTML"
>
  <div class="metric m-blue">
    <div class="metric-lbl">Pendentes</div>
    <div class="metric-val v-blue">{{ tv.pending_count }}</div>
    <div class="metric-sub">
      {{ tv.overdue_count }} atrasada{{ 's' if tv.overdue_count != 1 else '' }}
      &middot; {{ tv.in_progress_count }} em prog
    </div>
  </div>
  <div class="metric m-green">
    <div class="metric-lbl">Agenda</div>
    <div class="metric-val v-green">
      {{ a.completed }}<span class="v-frac">/{{ a.total_blocks }}</span>
    </div>
    <div class="metric-sub">blocos hoje</div>
  </div>
  <div class="metric {% if f.guard_running %}m-green{% else %}m-dim{% endif %}">
    <div class="metric-lbl">Foco</div>
    <div
      class="metric-val v-text {% if f.guard_running %}v-green{% else %}v-dim{% endif %}"
    >
      {% if f.guard_running %}Ativo{% else %}Off{% endif %}
    </div>
    <div class="metric-sub">
      {% if f.on_track %}on track{% else %}desvio detectado{% endif %}
    </div>
  </div>
  <div class="metric {% if al.pending > 0 %}m-red{% else %}m-dim{% endif %}">
    <div class="metric-lbl">Alertas</div>
    <div
      class="metric-val {% if al.pending > 0 %}v-red{% else %}v-dim{% endif %}"
    >
      {{ al.pending }}
    </div>
    <div class="metric-sub">pendente{{ 's' if al.pending != 1 else '' }}</div>
  </div>
</div>

{% if sync_msg is defined %}
<div class="toast toast-ok">{{ sync_msg }}</div>
{% endif %} {# ── Agenda hoje ── #}
<div class="card">
  <div class="card-hd">
    <span class="card-lbl">Agenda hoje</span>
    <button
      class="card-act"
      hx-get="/agenda"
      hx-target="#agenda-body"
      hx-swap="innerHTML"
      aria-label="Atualizar"
    >
      Atualizar
    </button>
  </div>
  <div
    id="agenda-body"
    hx-get="/agenda"
    hx-trigger="every 20s"
    hx-swap="innerHTML"
  >
    {% include "partials/agenda.html" %}
  </div>
</div>

{# ── Tarefas ── #}
<div class="card">
  <div class="card-hd">
    <span class="card-lbl">Tarefas</span>
    <a href="/tasks-page" class="card-act">Ver todas &rsaquo;</a>
  </div>
  <div
    id="tasks-body"
    hx-get="/tasks"
    hx-trigger="every 20s"
    hx-swap="innerHTML"
  >
    {% include "partials/tasks.html" %}
  </div>
</div>

<script>
  !(function () {
    var h = new Date().getHours(),
      g = "Boa noite";
    if (h >= 5 && h < 12) g = "Bom dia";
    else if (h >= 12 && h < 18) g = "Boa tarde";
    var el = document.getElementById("greeting");
    if (el) el.textContent = g;
  })();
</script>

{% endblock %}
````

## File: web/templates/tasks_page.html
````html
{% extends "base.html" %}
{% block page_title %}Tarefas{% endblock %}
{% block content %}

<div class="section-title">Tarefas</div>

<div class="card">
  <form class="add-bar"
        hx-post="/task"
        hx-target="#tasks-body"
        hx-swap="innerHTML"
        hx-on::after-request="this.reset()">
    <input class="add-input" type="text" name="title" placeholder="Nova tarefa..." required aria-label="Titulo">
    <select class="add-select" name="priority" aria-label="Prioridade">
      <option value="Alta">!</option>
      <option value="Média" selected>&#9670;</option>
      <option value="Baixa">&#9671;</option>
    </select>
    <button class="add-btn" type="submit" aria-label="Adicionar">+</button>
  </form>
  <div id="tasks-body">
    {% include "partials/tasks.html" %}
  </div>
</div>

{% endblock %}
````

## File: web/__init__.py
````python

````

## File: web/app.py
````python
# =============================================================================
# web/app.py — Interface Web (FastAPI + HTMX + Jinja2)
# =============================================================================
# Expõe o Orchestrator via HTTP com UI minimalista dark-mode.
# O Focus Guard roda em background thread via lifespan.
#
# Iniciar:  python -m web.app
#           uvicorn web.app:app --reload --port 8000

import asyncio
import jinja2 as _jinja2
import json
import os
import sys
import threading
import uuid
from collections import deque
from contextlib import asynccontextmanager
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import FastAPI, Form, Query, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from agents import calendar_sync, focus_guard, notion_sync, orchestrator
from agents.persona_manager import get_persona, list_personas, set_active_persona
from config import LOG_FILE
from core import memory

BASE_DIR = Path(__file__).parent
MAX_CHAT_TURNS = 12
CHAT_SESSION_COOKIE = "multiagentes_chat_sid"
PERSONA_COOKIE = "multiagentes_persona"
CHAT_HISTORY_TTL_SECONDS = int(os.getenv("CHAT_HISTORY_TTL_SECONDS", "86400"))
_chat_sessions: dict[str, list[dict]] = {}
_chat_sessions_lock = threading.Lock()


# ---------------------------------------------------------------------------
# Lifespan: inicia/para Focus Guard junto com o servidor
# ---------------------------------------------------------------------------


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        memory.init_db()
    except Exception as e:
        print(f"[WARN] Redis indisponível no startup: {e}")
        print("[WARN] App iniciando sem Redis — configure REDIS_URL no Railway.")
    if not focus_guard.is_running():
        focus_guard.start_guard()
    yield
    focus_guard.stop_guard()


app = FastAPI(title="Multiagentes", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


_jinja2_env = _jinja2.Environment(
    loader=_jinja2.FileSystemLoader(str(BASE_DIR / "templates")),
    autoescape=True,
    auto_reload=False,  # workaround: Python 3.14 + Jinja2 3.1.x LRU cache bug
)
templates = Jinja2Templates(env=_jinja2_env)


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(str(BASE_DIR / "static" / "favicon.ico"))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_REDIS_WARN = "Redis indisponível — configure REDIS_URL no Railway."
_NOTION_WARN = "Notion não configurado — defina NOTION_API_KEY e NOTION_DATABASE_ID."


def _safe(fn, fallback):
    """Executa fn(); retorna fallback se qualquer exceção ocorrer."""
    try:
        return fn()
    except Exception:
        return fallback


async def _safe_async(coro, fallback):
    """Aguarda coro; retorna fallback em caso de erro."""
    try:
        return await coro
    except Exception:
        return fallback


def _get_persona_id(request: Request) -> str:
    """Lê o ID da persona ativa do cookie."""
    return request.cookies.get(PERSONA_COOKIE, "coordinator")


def _persona_ctx(request: Request) -> dict:
    """Contexto de persona para os templates."""
    persona_id = _get_persona_id(request)
    active = get_persona(persona_id)
    return {
        "personas": list_personas(),
        "active_persona": active,
        "active_persona_id": persona_id,
    }


def _parse_slot_range(block_date: str | None, time_slot: str | None):
    """Converte 'YYYY-MM-DD' + '09:00-10:00' em datetimes comparáveis."""
    if not block_date or not time_slot or "-" not in time_slot:
        return None
    try:
        start_str, end_str = [part.strip() for part in time_slot.split("-", 1)]
        start_dt = datetime.strptime(f"{block_date} {start_str}", "%Y-%m-%d %H:%M")
        end_dt = datetime.strptime(f"{block_date} {end_str}", "%Y-%m-%d %H:%M")
        if end_dt <= start_dt:
            return None
        return start_dt, end_dt
    except ValueError:
        return None


def _format_slot_label(
    block_date: str | None, time_slot: str | None, today: date
) -> str:
    if not time_slot:
        return ""
    if not block_date:
        return time_slot
    if block_date == today.isoformat():
        return f"Hoje · {time_slot}"
    try:
        block_day = datetime.strptime(block_date, "%Y-%m-%d").date()
        return f"{block_day.strftime('%d/%m')} · {time_slot}"
    except ValueError:
        return time_slot


def _build_task_views(include_completed: bool = True) -> tuple[list[dict], dict]:
    """Cria uma leitura temporal das tarefas para o frontend."""
    now = datetime.now()
    today = now.date()
    priority_rank = {"Alta": 0, "Média": 1, "Media": 1, "Baixa": 2}
    tasks = _safe(memory.list_all_tasks, [])
    task_ids = [task["id"] for task in tasks]
    blocks_by_task = _safe(
        lambda: memory.get_agenda_blocks_for_tasks(task_ids),
        {task_id: [] for task_id in task_ids},
    )
    task_views = []

    for task in tasks:
        view = dict(task)
        blocks = blocks_by_task.get(task["id"], [])
        open_blocks = [
            block
            for block in blocks
            if not block.get("completed") and not block.get("rescheduled")
        ]

        overdue_blocks = []
        for block in open_blocks:
            slot_range = _parse_slot_range(
                block.get("block_date"), block.get("time_slot")
            )
            if slot_range:
                _, end_dt = slot_range
                if end_dt < now:
                    overdue_blocks.append(block)
                continue
            if (block.get("block_date") or "") < today.isoformat():
                overdue_blocks.append(block)

        open_blocks.sort(
            key=lambda block: (
                block.get("block_date") or "9999-99-99",
                block.get("time_slot") or "99:99-99:99",
            )
        )
        overdue_blocks.sort(
            key=lambda block: (
                block.get("block_date") or "9999-99-99",
                block.get("time_slot") or "99:99-99:99",
            )
        )

        next_block = open_blocks[0] if open_blocks else None
        overdue_block = overdue_blocks[0] if overdue_blocks else None
        original_status = task.get("status") or "A fazer"

        if original_status == "Concluído":
            display_status = "Concluído"
            status_class = "badge-ok"
            meta = (
                f"Concluída às {task.get('actual_time')}"
                if task.get("actual_time")
                else "Concluída"
            )
        elif overdue_block:
            display_status = "Pendente"
            status_class = "badge-warn"
            meta = f"Bloco vencido · {_format_slot_label(overdue_block.get('block_date'), overdue_block.get('time_slot'), today)}"
        elif original_status == "Em progresso":
            display_status = "Em progresso"
            status_class = "badge-def"
            meta = (
                _format_slot_label(
                    next_block.get("block_date"),
                    next_block.get("time_slot"),
                    today,
                )
                if next_block
                else (task.get("scheduled_time") or "Sem bloco associado")
            )
        else:
            display_status = "A fazer"
            status_class = "badge-def"
            meta = (
                _format_slot_label(
                    next_block.get("block_date"),
                    next_block.get("time_slot"),
                    today,
                )
                if next_block
                else (task.get("scheduled_time") or "Sem horário definido")
            )

        view.update(
            {
                "display_status": display_status,
                "display_status_class": status_class,
                "display_meta": meta,
                "is_overdue": bool(overdue_block),
            }
        )
        task_views.append(view)

    if not include_completed:
        task_views = [
            task for task in task_views if task["display_status"] != "Concluído"
        ]

    status_rank = {"Pendente": 0, "Em progresso": 1, "A fazer": 2, "Concluído": 3}
    task_views.sort(
        key=lambda task: (
            status_rank.get(task.get("display_status", "A fazer"), 4),
            priority_rank.get(task.get("priority", "Média"), 1),
            task.get("scheduled_time") or "99:99",
            -(task.get("id") or 0),
        )
    )

    overview = {
        "pending_count": sum(
            1
            for task in task_views
            if task["display_status"] in {"Pendente", "A fazer"}
        ),
        "overdue_count": sum(
            1 for task in task_views if task["display_status"] == "Pendente"
        ),
        "in_progress_count": sum(
            1 for task in task_views if task["display_status"] == "Em progresso"
        ),
        "done_count": sum(
            1 for task in task_views if task["display_status"] == "Concluído"
        ),
    }
    return task_views, overview


def _build_agenda_blocks(include_rescheduled: bool = False) -> list[dict]:
    now = datetime.now()
    today = now.date()
    blocks = _safe(
        lambda: memory.get_today_agenda(include_rescheduled=include_rescheduled),
        [],
    )
    block_views = []
    for block in blocks:
        view = dict(block)
        slot_range = _parse_slot_range(view.get("block_date"), view.get("time_slot"))
        is_overdue = False
        if not view.get("completed") and not view.get("rescheduled"):
            if slot_range:
                _, end_dt = slot_range
                is_overdue = end_dt < now
            elif (view.get("block_date") or "") < today.isoformat():
                is_overdue = True

        if view.get("completed"):
            state_label = "Concluído"
            state_class = "badge-ok"
        elif view.get("rescheduled"):
            state_label = "Reagendado"
            state_class = "badge-warn"
        elif is_overdue:
            state_label = "Pendente"
            state_class = "badge-warn"
        else:
            state_label = "Aberto"
            state_class = "badge-def"

        view.update(
            {
                "display_state_label": state_label,
                "display_state_class": state_class,
                "is_overdue": is_overdue,
            }
        )
        block_views.append(view)
    return block_views


def _summary_ctx(request: Request = None, include_completed: bool = False) -> dict:
    """Contexto de resumo do sistema — nunca lança exceção."""
    summary = _safe(
        orchestrator.get_system_summary,
        {
            "tasks": {"a_fazer": 0, "em_progresso": 0, "concluido": 0},
            "focus": {"guard_running": focus_guard.is_running(), "on_track": True},
            "agenda_today": {"total_blocks": 0, "completed": 0},
            "alerts": {"pending": 0},
            "redis_ok": False,
        },
    )
    _, task_overview = _build_task_views(include_completed=include_completed)
    ctx = {"summary": summary, "task_overview": task_overview}
    if request:
        ctx.update(_persona_ctx(request))
    return ctx


def _tail_logs(limit: int = 120) -> list[str]:
    log_path = Path(LOG_FILE)
    if not log_path.exists():
        return []
    with log_path.open("r", encoding="utf-8", errors="replace") as handle:
        return list(deque(handle, maxlen=limit))


def _audit_ctx() -> dict:
    return {
        "summary": _summary_ctx()["summary"],
        "audit_events": _safe(lambda: memory.list_audit_events(60), []),
        "alerts": _safe(lambda: memory.list_alerts(30), []),
        "handoffs": _safe(lambda: memory.list_recent_handoffs(30), []),
        "log_lines": _tail_logs(120),
    }


def _normalize_range(start_date: str | None, end_date: str | None) -> tuple[str, str]:
    today = date.today()
    default_start = today - timedelta(days=7)
    default_end = today + timedelta(days=7)
    try:
        start_dt = (
            datetime.strptime(start_date, "%Y-%m-%d").date()
            if start_date
            else default_start
        )
        end_dt = (
            datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else default_end
        )
    except ValueError:
        return default_start.isoformat(), default_end.isoformat()

    if end_dt < start_dt:
        start_dt, end_dt = end_dt, start_dt
    return start_dt.isoformat(), end_dt.isoformat()


def _agenda_history_ctx(start_date: str | None, end_date: str | None) -> dict:
    normalized_start, normalized_end = _normalize_range(start_date, end_date)
    blocks = _safe(
        lambda: memory.list_agenda_between(
            normalized_start,
            normalized_end,
            include_rescheduled=True,
        ),
        [],
    )
    return {
        "summary": _summary_ctx()["summary"],
        "blocks": blocks,
        "start_date": normalized_start,
        "end_date": normalized_end,
    }


def _get_chat_session_id(request: Request) -> tuple[str, bool]:
    current = request.cookies.get(CHAT_SESSION_COOKIE)
    if current:
        return current, False
    return uuid.uuid4().hex, True


def _chat_history_key(session_id: str) -> str:
    return f"chat:history:{session_id}"


def _get_chat_history(session_id: str) -> list[dict]:
    # Fonte primária: Redis (persistente entre restarts/deploys)
    try:
        r = memory.get_redis()
        raw_items = r.lrange(_chat_history_key(session_id), 0, -1)
        if raw_items:
            parsed_history = []
            for item in raw_items:
                try:
                    parsed = json.loads(item)
                    role = parsed.get("role")
                    content = parsed.get("content")
                    if role and content is not None:
                        parsed_history.append({"role": role, "content": content})
                except Exception:
                    continue
            if parsed_history:
                with _chat_sessions_lock:
                    _chat_sessions[session_id] = parsed_history[-MAX_CHAT_TURNS:]
                return parsed_history[-MAX_CHAT_TURNS:]
    except Exception:
        pass

    # Fallback: memória local do processo
    with _chat_sessions_lock:
        history = _chat_sessions.get(session_id, [])
        return list(history)


def _store_chat_turn(session_id: str, role: str, content: str) -> None:
    turn = {"role": role, "content": content}

    # Sempre mantém fallback local
    with _chat_sessions_lock:
        history = list(_chat_sessions.get(session_id, []))
        history.append(turn)
        _chat_sessions[session_id] = history[-MAX_CHAT_TURNS:]

    # Persistência principal em Redis com TTL
    try:
        r = memory.get_redis()
        key = _chat_history_key(session_id)
        r.rpush(key, json.dumps(turn, ensure_ascii=False))
        r.ltrim(key, -MAX_CHAT_TURNS, -1)
        r.expire(key, CHAT_HISTORY_TTL_SECONDS)
    except Exception:
        # Se Redis falhar, o fallback local garante continuidade da conversa
        pass


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------


@app.get("/health")
async def health():
    """Lightweight health check — sempre retorna 200 se o processo está vivo."""
    result: dict = {"status": "ok"}
    try:
        tasks_count = len(memory.list_all_tasks())
        result["db"] = "ok"
        result["tasks"] = tasks_count
    except Exception as e:
        result["db"] = "unavailable"
        result["db_error"] = str(e)[:120]
    return JSONResponse(result)


# ---------------------------------------------------------------------------
# Rotas full-page
# ---------------------------------------------------------------------------


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    ctx = _summary_ctx(request)
    tasks, task_overview = _build_task_views(include_completed=False)
    agenda_blocks = _build_agenda_blocks()
    ctx["agenda"] = agenda_blocks
    ctx["blocks"] = ctx["agenda"]  # alias for partials/agenda.html
    ctx["tasks"] = tasks
    ctx["task_overview"] = task_overview
    ctx["redis_warn"] = "" if ctx["summary"].get("redis_ok") else _REDIS_WARN
    ctx["page_name"] = "dashboard"
    return templates.TemplateResponse(request, "index.html", ctx)


@app.get("/audit", response_class=HTMLResponse)
async def audit(request: Request):
    ctx = _audit_ctx()
    ctx.update(_persona_ctx(request))
    ctx["page_name"] = "audit"
    return templates.TemplateResponse(request, "audit.html", ctx)


@app.post("/alert/{alert_id}/dismiss", response_class=HTMLResponse)
async def dismiss_alert(alert_id: int):
    """Descarta um alerta individual — remove de alerts:pending."""
    _safe(lambda: memory.acknowledge_alert(alert_id), None)
    return HTMLResponse("")  # HTMX remove o elemento com hx-swap="outerHTML"


@app.post("/alerts/dismiss-all", response_class=HTMLResponse)
async def dismiss_all_alerts():
    """Descarta todos os alertas pendentes de uma vez."""
    pending = _safe(lambda: memory.get_pending_alerts(), []) or []
    for alert in pending:
        _safe(lambda a=alert: memory.acknowledge_alert(a["id"]), None)
    return HTMLResponse('<div class="empty">Sem alertas pendentes</div>')


@app.get("/agenda", response_class=HTMLResponse)
async def agenda(
    request: Request,
    start_date: str | None = Query(default=None),
    end_date: str | None = Query(default=None),
):
    if request.headers.get("HX-Request") == "true":
        if start_date or end_date:
            normalized_start, normalized_end = _normalize_range(start_date, end_date)
            blocks = _safe(
                lambda: memory.list_agenda_between(
                    normalized_start,
                    normalized_end,
                    include_rescheduled=True,
                ),
                [],
            )
        else:
            blocks = _build_agenda_blocks()
        return templates.TemplateResponse(
            request,
            "partials/agenda.html",
            {"blocks": blocks},
        )

    ctx = _agenda_history_ctx(start_date, end_date)
    ctx.update(_persona_ctx(request))
    ctx["page_name"] = "agenda"
    return templates.TemplateResponse(request, "agenda.html", ctx)


@app.get("/agenda/history", response_class=HTMLResponse)
async def agenda_history_redirect(
    start_date: str | None = Query(default=None),
    end_date: str | None = Query(default=None),
):
    query_parts = []
    if start_date:
        query_parts.append(f"start_date={start_date}")
    if end_date:
        query_parts.append(f"end_date={end_date}")
    query = f"?{'&'.join(query_parts)}" if query_parts else ""
    return RedirectResponse(url=f"/agenda{query}", status_code=307)


# ---------------------------------------------------------------------------
# Partials HTMX
# ---------------------------------------------------------------------------


@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, message: str = Form(...)):
    """Chat com o Orchestrator — I/O bloqueante movido para thread pool."""
    session_id, is_new_session = _get_chat_session_id(request)
    persona_id = _get_persona_id(request)
    history = _get_chat_history(session_id)
    context = {
        "chat_history": history[-6:],
        "system_summary": _safe(orchestrator.get_system_summary, {}),
    }
    try:
        response = await asyncio.to_thread(
            orchestrator.process, message, context, persona_id
        )
    except Exception as e:
        response = f"⚠️ Erro: {e}"
    _store_chat_turn(session_id, "user", message)
    _store_chat_turn(session_id, "assistant", response)
    active_persona = get_persona(persona_id)
    template_response = templates.TemplateResponse(
        request,
        "partials/chat_message.html",
        {
            "user_message": message,
            "bot_response": response,
            "active_persona": active_persona,
        },
    )
    if is_new_session:
        template_response.set_cookie(
            CHAT_SESSION_COOKIE,
            session_id,
            httponly=True,
            samesite="lax",
        )
    return template_response


@app.get("/status", response_class=HTMLResponse)
async def status(request: Request):
    return templates.TemplateResponse(
        request,
        "partials/status.html",
        _summary_ctx(request, include_completed=False),
    )


@app.post("/agenda/import", response_class=HTMLResponse)
@app.post("/agenda/history/import", response_class=HTMLResponse)
async def import_agenda_history(
    request: Request,
    source: str = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
):
    normalized_start, normalized_end = _normalize_range(start_date, end_date)
    if source == "notion":
        imported = await asyncio.to_thread(
            notion_sync.sync_agenda_range_to_local,
            normalized_start,
            normalized_end,
        )
    elif source == "calendar":
        imported = await asyncio.to_thread(
            calendar_sync.import_events_range_as_blocks,
            normalized_start,
            normalized_end,
        )
    else:
        imported = 0

    ctx = _agenda_history_ctx(normalized_start, normalized_end)
    ctx["page_name"] = "agenda"
    ctx["import_msg"] = (
        f"{imported} bloco(s) importado(s) de {source} entre {normalized_start} e {normalized_end}."
    )
    return templates.TemplateResponse(request, "agenda.html", ctx)


@app.get("/tasks", response_class=HTMLResponse)
async def tasks(request: Request, include_completed: bool = Query(default=False)):
    tasks_view, _ = _build_task_views(include_completed=include_completed)
    return templates.TemplateResponse(
        request,
        "partials/tasks.html",
        {"tasks": tasks_view},
    )


@app.get("/tasks-page", response_class=HTMLResponse)
async def tasks_page(request: Request):
    ctx = _summary_ctx(request)
    ctx["tasks"], ctx["task_overview"] = _build_task_views()
    ctx["page_name"] = "tasks"
    return templates.TemplateResponse(request, "tasks_page.html", ctx)


@app.get("/chat-page", response_class=HTMLResponse)
async def chat_page(request: Request):
    ctx = _summary_ctx(request)
    ctx["page_name"] = "chat"
    return templates.TemplateResponse(request, "chat_page.html", ctx)


@app.post("/task", response_class=HTMLResponse)
async def create_task(
    request: Request,
    title: str = Form(...),
    priority: str = Form("Média"),
    scheduled_time: str = Form(""),
):
    _safe(
        lambda: memory.create_task(
            title=title,
            priority=priority,
            scheduled_time=scheduled_time or None,
        ),
        None,
    )
    return templates.TemplateResponse(
        request,
        "partials/tasks.html",
        {"tasks": _build_task_views(include_completed=False)[0]},
    )


@app.post("/task/{task_id}/complete", response_class=HTMLResponse)
async def complete_task(request: Request, task_id: int):
    _safe(lambda: memory.update_task_status(task_id, "Concluído"), None)
    task = _safe(lambda: memory.get_task(task_id), None)
    if task:
        task_view = next(
            (item for item in _build_task_views()[0] if item["id"] == task_id),
            task,
        )
        # Swap cirúrgico: retorna só a linha atualizada (preserva scroll)
        return templates.TemplateResponse(
            request, "partials/task_row.html", {"t": task_view}
        )
    return templates.TemplateResponse(
        request,
        "partials/tasks.html",
        {"tasks": _build_task_views(include_completed=False)[0]},
    )


@app.post("/sync", response_class=HTMLResponse)
async def sync(request: Request):
    """Full sync com Notion — reconcilia Redis com o estado atual do Notion.
    Remove tarefas deletadas no Notion, importa novas e atualiza existentes.
    I/O bloqueante em thread pool."""
    try:
        count = await asyncio.to_thread(notion_sync.sync_tasks_to_local)
        sync_msg = f"Sync completo: {count} tarefa(s) atualizada(s)."
    except Exception as e:
        sync_msg = f"Sync falhou: {str(e)[:80]}"
    return HTMLResponse(f'<div class="sync-toast">{sync_msg}</div>')


@app.post("/block/{block_id}/complete", response_class=HTMLResponse)
async def complete_block(request: Request, block_id: int):
    _safe(lambda: memory.mark_block_completed(block_id, True), None)
    block = _safe(lambda: memory.get_block(block_id), None)
    if block:
        block_view = next(
            (
                item
                for item in _build_agenda_blocks(include_rescheduled=True)
                if item["id"] == block_id
            ),
            block,
        )
        return templates.TemplateResponse(
            request, "partials/block_row.html", {"b": block_view}
        )
    return templates.TemplateResponse(
        request,
        "partials/agenda.html",
        {"blocks": _build_agenda_blocks()},
    )


# ---------------------------------------------------------------------------
# Persona selector
# ---------------------------------------------------------------------------


@app.get("/personas", response_class=JSONResponse)
async def personas_list():
    """Retorna lista de personas disponíveis."""
    return JSONResponse(list_personas())


@app.post("/persona/{persona_id}", response_class=HTMLResponse)
async def switch_persona(request: Request, persona_id: str):
    """Troca a persona ativa — salva no cookie e retorna o seletor atualizado."""
    set_active_persona(persona_id)
    active = get_persona(persona_id)
    all_personas = list_personas()

    # Retorna o dropdown atualizado via HTMX
    options = "".join(
        f'<option value="{p["id"]}"{"selected" if p["id"] == persona_id else ""}>'
        f"{p['icon']} {p['short_name']}</option>"
        for p in all_personas
    )
    html = (
        f'<select name="persona" '
        f'hx-post="/persona/{{this.value}}" '
        f'hx-trigger="change" '
        f'hx-target="#persona-selector" '
        f'hx-swap="innerHTML" '
        f'class="persona-select">'
        f"{options}</select>"
        f'<span class="persona-label">{active.get("icon", "●")} {active.get("short_name", "")}</span>'
    )

    response = HTMLResponse(html)
    response.set_cookie(
        PERSONA_COOKIE,
        persona_id,
        httponly=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 365,
    )
    return response


# ---------------------------------------------------------------------------
# Ecosystem
# ---------------------------------------------------------------------------


def _ecosystem_ctx(data: dict) -> dict:
    """Converte dados do health_check em contexto para o template."""
    import datetime as _dt

    summary = data.get("summary", {})
    github = data.get("github", {})
    railway = data.get("railway", {})
    onchain = data.get("onchain", {})

    # Railway services list
    railway_services = []
    for name, info in railway.items():
        railway_services.append(
            {
                "name": name,
                "status": info.get("status", "dim"),
                "http_code": info.get("http_code"),
                "response_ms": info.get("response_ms"),
                "error": info.get("error"),
                "priority": info.get("priority", "P2"),
            }
        )
    # sort: fail first, then warn, then ok; P0 before P1
    order = {"fail": 0, "warn": 1, "ok": 2, "dim": 3}
    railway_services.sort(key=lambda s: (order.get(s["status"], 9), s["priority"]))

    # GitHub orgs list
    github_orgs = []
    for org, info in github.items():
        github_orgs.append(
            {
                "name": org,
                "status": info.get("status", "dim"),
                "active_24h": info.get("repos_active_24h", 0),
                "issues": info.get("open_issues", 0),
                "stale": info.get("repos_stale", []),
            }
        )

    # NEOFLW
    neoflw = onchain.get("NEOFLW", {"status": "dim"})

    # Actions
    rw_fail = [s["name"] for s in railway_services if s["status"] == "fail"]
    rw_warn = [s["name"] for s in railway_services if s["status"] == "warn"]
    stale = summary.get("github", {}).get("repos_stale_priority", [])
    actions = []
    if rw_fail:
        actions.append(f"verificar serviço com falha: {', '.join(rw_fail)}")
    if rw_warn:
        actions.append(f"investigar: {', '.join(rw_warn)}")
    if stale:
        actions.append(
            f"repos estagnados: {', '.join(stale[:5])}{'...' if len(stale) > 5 else ''}"
        )
    if neoflw.get("alerts"):
        actions.append("monitorar NEOFLW — alertas ativos")

    rw_s = summary.get("railway", {})
    ts_raw = data.get("timestamp", "")
    try:
        ts = _dt.datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
        ts_str = ts.strftime("%H:%M")
    except Exception:
        ts_str = ts_raw[:16]

    return {
        "global_status": data.get("status", "unknown"),
        "timestamp": ts_str,
        "railway_ok": rw_s.get("services_ok", 0),
        "railway_total": rw_s.get("services_total", 0),
        "railway_warn": rw_s.get("services_warn", 0),
        "railway_fail": rw_s.get("services_fail", 0),
        "repos_active": summary.get("github", {}).get("repos_active_24h", 0),
        "railway_services": railway_services,
        "github_orgs": github_orgs,
        "neoflw": neoflw,
        "actions": actions,
    }


def _load_ecosystem_data() -> dict:
    """Carrega health check do Redis ou retorna estrutura vazia."""
    try:
        raw = memory.get_state("ecosystem:health_check:latest")
        if isinstance(raw, dict):
            return raw
        if isinstance(raw, str):
            import json

            return json.loads(raw)
    except Exception:
        pass
    return {
        "status": "unknown",
        "summary": {},
        "github": {},
        "railway": {},
        "onchain": {},
        "timestamp": "",
    }


@app.get("/ecosystem-page", response_class=HTMLResponse)
async def ecosystem_page(request: Request):
    """Página do Ecosystem Monitor."""
    data = _load_ecosystem_data()
    ctx = _ecosystem_ctx(data)
    sum_ctx = _summary_ctx()
    ctx.update(
        {
            "request": request,
            "page_name": "ecosystem",
            "summary": sum_ctx["summary"],
            "task_overview": sum_ctx["task_overview"],
            **_persona_ctx(request),
        }
    )
    return templates.TemplateResponse(request, "ecosystem_page.html", ctx)


@app.get("/ecosystem", response_class=HTMLResponse)
async def ecosystem_partial(request: Request):
    """HTMX partial — refresh automático do conteúdo do ecosystem."""
    data = _load_ecosystem_data()
    ctx = _ecosystem_ctx(data)
    sum_ctx = _summary_ctx()
    ctx.update(
        {
            "page_name": "ecosystem",
            "summary": sum_ctx["summary"],
            "task_overview": sum_ctx["task_overview"],
            **_persona_ctx(request),
        }
    )
    return templates.TemplateResponse(request, "ecosystem_page.html", ctx)


@app.post("/ecosystem/run", response_class=HTMLResponse)
async def ecosystem_run(request: Request):
    """Dispara health check e retorna resultado atualizado."""
    import asyncio

    from agents import ecosystem_monitor

    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, ecosystem_monitor.health_check)

    data = _load_ecosystem_data()
    ctx = _ecosystem_ctx(data)
    sum_ctx = _summary_ctx()
    ctx.update(
        {
            "page_name": "ecosystem",
            "summary": sum_ctx["summary"],
            "task_overview": sum_ctx["task_overview"],
            **_persona_ctx(request),
        }
    )
    return templates.TemplateResponse(request, "ecosystem_page.html", ctx)


# ---------------------------------------------------------------------------
# Entry point direto
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    from config import WEB_HOST, WEB_PORT

    uvicorn.run("web.app:app", host=WEB_HOST, port=WEB_PORT, reload=True)
````

## File: .env.example
````
# =============================================================================
# .env.example — Copie para .env e preencha os valores
# No Railway: configure via Dashboard → Variables
# =============================================================================

# --- OBRIGATÓRIO ---
OPENAI_API_KEY=sk-...
NOTION_TOKEN=secret_...
NOTION_TASKS_DB_ID=...
NOTION_AGENDA_DB_ID=...

# --- OPENAI (opcional) ---
OPENAI_MODEL=gpt-4o-mini
OPENAI_FALLBACK_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=1500
OPENAI_TEMPERATURE=0.2

# --- NOTION (opcional) ---
NOTION_SYNC_INTERVAL=5
NOTION_RETROSPECTIVE_PAGE_ID=

# --- REDIS (Railway provisiona automaticamente) ---
REDIS_URL=redis://localhost:6379/0

# --- GOOGLE CALENDAR (opcional) ---
GOOGLE_CREDENTIALS_FILE=./credentials.json
GOOGLE_TOKEN_FILE=./token.json
GOOGLE_CALENDAR_ID=primary

# --- SANITY.IO (opcional — externaliza prompts e configs) ---
SANITY_PROJECT_ID=           # project ID do sanity.io/manage
SANITY_DATASET=production
SANITY_API_TOKEN=            # token com permissão Viewer
SANITY_USE_CDN=false         # true em produção, false em dev

# --- NOTIFICAÇÕES — VOICE MONKEY (opcional — primário para Alexa) ---
VOICE_MONKEY_TOKEN=          # api-v2.voicemonkey.io
VOICE_MONKEY_DEVICE=eco-room
VOICE_MONKEY_VOICE=Ricardo

# --- NOTIFICAÇÕES — IFTTT (opcional — fallback para Alexa) ---
IFTTT_WEBHOOK_KEY=           # ifttt.com/maker_webhooks/settings
IFTTT_ALEXA_EVENT=neo_alert

# --- LIFE GUARD (opcional — rotinas pessoais) ---
LIFE_GUARD_ACTIVE_HOUR_START=8
LIFE_GUARD_ACTIVE_HOUR_END=22
LIFE_GUARD_WATER_INTERVAL=90

# --- FOCUS GUARD ---
FOCUS_CHECK_INTERVAL=15

# --- LOGGING ---
LOG_FILE=./logs/agent_system.log
LOG_LEVEL=INFO

# --- WEB ---
WEB_HOST=127.0.0.1
WEB_PORT=8000
````

## File: .gitignore
````
.env
.venv/
.ruff_cache/
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
*.db-journal
*.db-shm
*.db-wal
.claude/
logs/
reports/
token.json
credentials.json
*.plist
.DS_Store
tests


# Redis dumps
*.rdb
````

## File: AGENTS.md
````markdown
# AGENTS.md - Workspace Context & Operational Anchors

## Project Identity: mypersonal_multiagents (NEØ PROTOCOL)

This is the **Personal Operating System** kernel, focused on flow-based productivity (Intention -> Agenda -> Execution -> Audit).
Orchestrated by **NEØ MELLØ**.

### 🌐 Vínculo do Workspace (CODIGOS)

Este projeto é um nó do monorepo **pnpm** em `/Users/nettomello/CODIGOS`.

- **Governança Global**: Segue as políticas de segurança e overrides definidos no `package.json` raiz (ex: `undici`, `tar`, `minimatch`).
- **Orquestração Master**: O `Makefile` da raiz gerencia auditoria e status global.
- **Sincronização**: Scripts em `../scripts` (ex: `sync_vercel.py`) têm autoridade sobre este diretório.

### 🏗️ Core Architecture

- **State Persistence**: **Redis** is the absolute source of truth for hot operational state (shared between agents). SQLite is legacy.
- **Data Sources**: **Notion** (Primary tasks/calendar) and **Google Calendar** (Optional).
- **Governance**: Semantic prompts and persona policies are managed via **Sanity.io** (with local fallbacks).
- **Interface**: Hybrid (CLI for ops/automation, FastAPI+HTMX for visual dashboard).

### 🤖 Agent Matrix (Kernel Private)

Refer to [CONTRATO_AGENTES.md](file:///Users/nettomello/CODIGOS/mypersonal_multiagents/docs/governanca/CONTRATO_AGENTES.md) for specific constraints on:

- **Orchestrator**: Routes intentions and synthesizes responses.
- **Focus Guard**: Monitors focus sessions and handles auto-rescheduling.
- **Life Guard**: Manages vital routines (water, exercise, finances).
- **Notion Sync**: Bi-directional bridge between the kernel and human input.

### 🛠️ Operational Rules

1. **Environment**: Always use `.venv` and **Makefile** commands (`make setup`, `make dev`, `make sync`).
2. **Git Protocol (NΞØ)**: Every commit MUST follow the flow: `npm audit` (if applicable) -> `make build/test` -> **Conventional Commits** -> `git push`.
    - *Nota*: Auditoria deve considerar o `pnpm-lock.yaml` da raiz para integridade do workspace.
3. **Persistence Access**: All state modifications MUST go through `core/memory.py` using the established Redis Key schemas.

### ⚠️ Critical Constraints

- **NEVER** create new SQLite databases.
- **ALWAYS** check `config.py` for mandatory environment variables before proposing logic changes.
- **STYLING**: Use Vanilla CSS variables (Design System) for the Web UI. No Tailwind unless requested.
````

## File: config.py
````python
# =============================================================================
# config.py — Configurações centrais do sistema multiagentes
# =============================================================================
# Carrega variáveis de ambiente e expõe constantes para todos os módulos.
# Nunca coloque credenciais diretamente aqui — use o .env.

import os
from dotenv import load_dotenv
from pathlib import Path

# Carrega o .env localizado na raiz do projeto
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# ---------------------------------------------------------------------------
# OpenAI
# ---------------------------------------------------------------------------
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_FALLBACK_MODEL: str = os.getenv("OPENAI_FALLBACK_MODEL", "gpt-3.5-turbo")

# Modelo local via Docker Model Runner (Gemma3 4B)
# Expõe API compatível OpenAI em http://localhost:12434/v1
LOCAL_MODEL_ENABLED: bool = os.getenv("LOCAL_MODEL_ENABLED", "true").lower() == "true"
LOCAL_MODEL_BASE_URL: str = os.getenv(
    "LOCAL_MODEL_BASE_URL", "http://localhost:12434/engines/llama.cpp/v1"
)
LOCAL_MODEL_NAME: str = os.getenv("LOCAL_MODEL_NAME", "docker.io/ai/gemma3:4B-F16")

# ---------------------------------------------------------------------------
# Notion
# ---------------------------------------------------------------------------
NOTION_TOKEN: str = os.getenv("NOTION_TOKEN", "")  # Integration token
NOTION_TASKS_DB_ID: str = os.getenv(
    "NOTION_TASKS_DB_ID", ""
)  # ID do database "Tarefas"
NOTION_AGENDA_DB_ID: str = os.getenv(
    "NOTION_AGENDA_DB_ID", ""
)  # ID do database "Agenda Diária"

# URL base da Notion API v1
NOTION_API_BASE: str = "https://api.notion.com/v1"
NOTION_API_VERSION: str = "2022-06-28"

# ---------------------------------------------------------------------------
# Memória / persistência (Redis)
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
# Mantido para compatibilidade com scripts antigos (não usado com Redis)
MEMORY_DB_PATH: str = os.getenv("MEMORY_DB_PATH", str(BASE_DIR / "memory.db"))

# ---------------------------------------------------------------------------
# Focus Guard
# ---------------------------------------------------------------------------
# Intervalo (em minutos) entre verificações automáticas do Focus Guard
FOCUS_CHECK_INTERVAL_MINUTES: int = int(os.getenv("FOCUS_CHECK_INTERVAL", "15"))

# ---------------------------------------------------------------------------
# Logging / Notificações
# ---------------------------------------------------------------------------
LOG_FILE: str = os.getenv("LOG_FILE", str(BASE_DIR / "logs" / "agent_system.log"))
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

# ---------------------------------------------------------------------------
# Notion sync interval
# ---------------------------------------------------------------------------
NOTION_SYNC_INTERVAL_MINUTES: int = int(os.getenv("NOTION_SYNC_INTERVAL", "5"))

# Notion retrospective parent page (opcional)
NOTION_RETROSPECTIVE_PAGE_ID: str = os.getenv("NOTION_RETROSPECTIVE_PAGE_ID", "")

# ---------------------------------------------------------------------------
# Google Calendar opcional
# ---------------------------------------------------------------------------
GOOGLE_CREDENTIALS_FILE: str = os.getenv(
    "GOOGLE_CREDENTIALS_FILE", str(BASE_DIR / "credentials.json")
)
GOOGLE_TOKEN_FILE: str = os.getenv("GOOGLE_TOKEN_FILE", str(BASE_DIR / "token.json"))
GOOGLE_CALENDAR_ID: str = os.getenv("GOOGLE_CALENDAR_ID", "primary")

# ---------------------------------------------------------------------------
# Web
# ---------------------------------------------------------------------------
WEB_HOST: str = os.getenv("WEB_HOST", "127.0.0.1")
WEB_PORT: int = int(os.getenv("WEB_PORT", "8000"))


# ---------------------------------------------------------------------------
# Validação mínima na importação
# ---------------------------------------------------------------------------
def validate_config() -> list[str]:
    """Retorna lista de avisos para chaves obrigatórias não configuradas."""
    warnings = []
    if not OPENAI_API_KEY:
        warnings.append("OPENAI_API_KEY não configurada — agentes LLM não funcionarão.")
    if not NOTION_TOKEN:
        warnings.append(
            "NOTION_TOKEN não configurada — Notion Sync ficará desabilitado."
        )
    if not NOTION_TASKS_DB_ID:
        warnings.append(
            "NOTION_TASKS_DB_ID não configurada — "
            "sincronização de tarefas desabilitada."
        )
    if not NOTION_AGENDA_DB_ID:
        warnings.append(
            "NOTION_AGENDA_DB_ID não configurada — "
            "sincronização de agenda desabilitada."
        )
    return warnings
````

## File: Dockerfile
````dockerfile
FROM python:3.12-slim

WORKDIR /app
ENV PIP_ROOT_USER_ACTION=ignore

# Instala dependências do sistema + Docker CLI via repositório da distro
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    git \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Cria diretórios de runtime e troca para usuário sem privilégios
RUN mkdir -p logs reports \
    && useradd --create-home --shell /bin/bash appuser \
    && chown -R appuser:appuser /app
USER appuser

# Variáveis de ambiente padrão
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV WEB_HOST=0.0.0.0

EXPOSE 8000

CMD ["sh", "-c", "uvicorn web.app:app --host 0.0.0.0 --port ${PORT:-8000}"]
````

## File: focus_guard_service.py
````python
#!/usr/bin/env python3
"""
Focus Guard — serviço standalone para launchd (macOS) ou systemd (Linux).

Roda o loop do Focus Guard na main thread (sem daemon thread).
O SO mantém o processo vivo e o reinicia automaticamente se cair.

Uso direto:
    python3 focus_guard_service.py

Instalar como serviço no macOS (launchd):
    bash scripts/install_launchd.sh

Instalar como serviço no Linux (systemd):
    bash scripts/install_systemd.sh
"""

import sys
import os
import signal
import logging

# Garante que o projeto está no path independente de onde o script é chamado
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

from core import memory
from agents import focus_guard

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [FocusGuard] %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


def _handle_signal(signum, frame):
    log.info(f"Sinal {signum} recebido — encerrando graciosamente...")
    focus_guard.stop_guard()
    sys.exit(0)


if __name__ == "__main__":
    log.info(f"Iniciando Focus Guard Service (PID: {os.getpid()})")
    log.info(f"Projeto: {PROJECT_ROOT}")

    memory.init_db()

    signal.signal(signal.SIGTERM, _handle_signal)
    signal.signal(signal.SIGINT, _handle_signal)

    # Roda o loop diretamente na main thread
    # (launchd/systemd gerenciam restart — não precisa de daemon thread)
    focus_guard._background_loop()
````

## File: main.py
````python
#!/usr/bin/env python3
# =============================================================================
# main.py — Entry point CLI do sistema de multiagentes
# =============================================================================
# Uso:
#   python main.py                    → modo interativo (REPL)
#   python main.py chat               → modo interativo (equivalente)
#   python main.py status             → exibe status do sistema
#   python main.py sync               → sincroniza com Notion
#   python main.py add-task           → wizard para adicionar tarefa
#   python main.py agenda             → exibe agenda de hoje
#   python main.py focus start <id>   → inicia sessão de foco
#   python main.py focus end          → encerra sessão de foco ativa
#   python main.py validate <id>      → valida tarefa como concluída
#   python main.py tasks              → lista todas as tarefas
#   python main.py demo               → cria dados de demonstração

import argparse
import atexit
import os
import signal
import sys
from typing import Optional

# Garante que o diretório raiz está no sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents import (
    focus_guard,
    life_guard,
    notion_sync,
    orchestrator,
    scheduler,
    validator,
)
from config import validate_config
from core import memory, notifier

# ---------------------------------------------------------------------------
# Setup e teardown
# ---------------------------------------------------------------------------


def _startup() -> None:
    """Inicializa o sistema: banco de dados, validação de config, banner."""
    notifier.banner()

    # Inicializa banco SQLite
    memory.init_db()

    # Valida configurações e exibe avisos
    warnings = validate_config()
    if warnings:
        notifier.separator("AVISOS DE CONFIGURAÇÃO")
        for w in warnings:
            notifier.warning(w)
        notifier.separator()
        print()


def _shutdown() -> None:
    """Garante encerramento limpo."""
    notifier.info("Encerrando sistema...", "main")
    focus_guard.stop_guard()


def _handle_sigint(sig, frame) -> None:
    """Captura Ctrl+C para encerramento gracioso."""
    print()
    notifier.info("Interrompido pelo usuário (Ctrl+C).", "main")
    _shutdown()
    sys.exit(0)


# ---------------------------------------------------------------------------
# Comandos CLI
# ---------------------------------------------------------------------------


def cmd_status() -> None:
    """Exibe status completo do sistema."""
    summary = orchestrator.get_system_summary()

    notifier.separator("STATUS DO SISTEMA")
    t = summary["tasks"]
    notifier.info(
        f"Tarefas: {t['total']} total | {t['a_fazer']} a fazer | "
        f"{t['em_progresso']} em progresso | {t['concluido']} concluídas",
        "status",
    )

    a = summary["agenda_today"]
    notifier.info(
        f"Agenda hoje: {a['completed']}/{a['total_blocks']} blocos concluídos",
        "status",
    )

    f = summary["focus"]
    guard_status = "🟢 ativo" if f["guard_running"] else "🔴 inativo"
    notifier.info(f"Focus Guard: {guard_status}", "status")

    if f["active_session"]:
        s = f["active_session"]
        notifier.focus_alert(
            f"Sessão ativa: '{s['task_title']}' (iniciada: {s['started_at'][:16]})"
        )

    if f.get("last_check"):
        on_track = "✅ on track" if f["on_track"] else "⚠️ desvio detectado"
        notifier.info(f"Último check-in: {f['last_check'][:16]} — {on_track}", "status")

    al = summary["alerts"]
    if al["pending"] > 0:
        notifier.warning(f"Alertas pendentes: {al['pending']}", "status")

    notifier.separator()


def cmd_agenda() -> None:
    """Exibe a agenda do dia."""
    blocks = scheduler.get_today_schedule()
    if not blocks:
        notifier.info(
            "Nenhum bloco na agenda de hoje. Use 'add-task' ou 'sync' para popular.",
            "agenda",
        )
        return

    headers = ["ID", "Horário", "Tarefa", "Concluído"]
    rows = [
        [
            str(b["id"]),
            b.get("time_slot", "—"),
            b.get("task_title", "—")[:40],
            "✅" if b.get("completed") else "⬜",
        ]
        for b in blocks
    ]
    notifier.print_table(headers, rows, "AGENDA DE HOJE")

    load = scheduler.calculate_schedule_load(blocks)
    notifier.info(
        f"Total: {load['total_blocks']} blocos | "
        f"{load['completion_percent']}% concluído | "
        f"{load['total_minutes']} min agendados",
        "agenda",
    )


def cmd_tasks() -> None:
    """Lista todas as tarefas."""
    tasks = memory.list_all_tasks()
    if not tasks:
        notifier.info("Nenhuma tarefa cadastrada. Use 'add-task' para criar.", "tasks")
        return

    headers = ["ID", "Título", "Status", "Prioridade", "Horário"]
    rows = [
        [
            str(t["id"]),
            t["title"][:35],
            t["status"],
            t.get("priority", "—"),
            t.get("scheduled_time", "—") or "—",
        ]
        for t in tasks
    ]
    notifier.print_table(headers, rows, "TAREFAS")


def cmd_add_task() -> None:
    """Wizard interativo para adicionar uma nova tarefa."""
    notifier.separator("NOVA TAREFA")

    title = input("  Título da tarefa: ").strip()
    if not title:
        notifier.error("Título não pode ser vazio.", "add-task")
        return

    print("  Prioridade: [1] Alta  [2] Média  [3] Baixa (Enter = Média)")
    priority_map = {"1": "Alta", "2": "Média", "3": "Baixa", "": "Média"}
    priority_input = input("  Escolha: ").strip()
    priority = priority_map.get(priority_input, "Média")

    scheduled_time = input(
        "  Horário (HH:MM ou YYYY-MM-DD HH:MM, Enter para pular): "
    ).strip()

    # Cria localmente
    task_id = memory.create_task(
        title=title,
        priority=priority,
        scheduled_time=scheduled_time or None,
    )
    notifier.success(f"Tarefa criada localmente (ID: {task_id}).", "add-task")

    # Pergunta se quer sincronizar com Notion
    sync_notion = input("  Sincronizar com Notion? [s/N]: ").strip().lower()
    if sync_notion == "s":
        result = notion_sync.sync_local_task_to_notion(task_id)
        if result:
            notifier.success("Tarefa enviada ao Notion!", "add-task")

    # Pergunta se quer adicionar bloco de agenda
    add_block = input("  Adicionar bloco de agenda hoje? [s/N]: ").strip().lower()
    if add_block == "s":
        time_slot = input("  Bloco horário (ex: 09:00-10:00): ").strip()
        if time_slot:
            scheduler.add_schedule_block(time_slot, title, task_id)


def cmd_sync() -> None:
    """Sincroniza dados com o Notion."""
    notifier.separator("SINCRONIZAÇÃO NOTION")
    result = notion_sync.handle_handoff({"action": "sync_from_notion"})
    if result["status"] == "success":
        r = result["result"]
        notifier.success(
            f"Sincronização completa: {r.get('synced', 0)} tarefa(s) importada(s)."
        )
    else:
        notifier.error(f"Erro na sincronização: {result['result'].get('error', '?')}")


def cmd_focus_start(task_id: Optional[int] = None) -> None:
    """Inicia uma sessão de foco."""
    if task_id is None:
        # Mostra tarefas e pede escolha
        tasks = scheduler.get_prioritized_tasks()
        if not tasks:
            notifier.warning("Nenhuma tarefa pendente.", "focus")
            return
        headers = ["ID", "Título", "Prioridade"]
        rows = [[str(t["id"]), t["title"][:40], t.get("priority", "?")] for t in tasks]
        notifier.print_table(headers, rows, "TAREFAS PENDENTES")
        task_id_str = input("  ID da tarefa para focar: ").strip()
        if not task_id_str.isdigit():
            notifier.error("ID inválido.", "focus")
            return
        task_id = int(task_id_str)

    task = memory.get_task(task_id)
    if not task:
        notifier.error(f"Tarefa {task_id} não encontrada.", "focus")
        return

    minutes_str = input("  Duração em minutos (Enter = 25): ").strip()
    minutes = int(minutes_str) if minutes_str.isdigit() else 25

    memory.update_task_status(task_id, "Em progresso")
    focus_guard.start_focus_session(task_id, task["title"], minutes)

    notifier.success(
        f"Sessão de foco iniciada! Foco em: '{task['title']}' por {minutes} min.",
        "focus",
    )


def cmd_focus_end() -> None:
    """Encerra a sessão de foco ativa."""
    result = focus_guard.end_focus_session(status="completed")
    if "Nenhuma sessão" in result.get("message", ""):
        notifier.warning("Nenhuma sessão de foco ativa.", "focus")
    else:
        task_title = result.get("task_title", "?")
        # Pergunta se quer validar e marcar como concluída
        validate = (
            input(f"  Marcar '{task_title}' como concluída e validar? [s/N]: ")
            .strip()
            .lower()
        )
        if validate == "s":
            active_tasks = memory.get_tasks_by_status("Em progresso")
            matched = next((t for t in active_tasks if t["title"] == task_title), None)
            if matched:
                cmd_validate(matched["id"])


def cmd_validate(task_id: Optional[int] = None) -> None:
    """Valida e confirma conclusão de uma tarefa."""
    if task_id is None:
        task_id_str = input("  ID da tarefa para validar: ").strip()
        if not task_id_str.isdigit():
            notifier.error("ID inválido.", "validate")
            return
        task_id = int(task_id_str)

    result = validator.validate_task(task_id)
    verdict = result.get("verdict", {})
    v = verdict.get("verdict", "?")

    if v == "pending_confirmation":
        questions = verdict.get("questions", [])
        for q in questions:
            print(f"\n  ❓ {q}")
        confirm = input("  Confirmar conclusão? [s/N]: ").strip().lower()
        if confirm == "s":
            validator.validate_task(task_id, force_confirm=True)

    notifier.separator()


def cmd_suggest_agenda() -> None:
    """Sugere e opcionalmente aplica uma agenda otimizada via LLM."""
    context = input("  Contexto adicional (Enter para pular): ").strip()
    notifier.info("Gerando sugestão de agenda via LLM...", "scheduler")

    suggestion = scheduler.suggest_agenda_with_llm(context=context)
    schedule_items = suggestion.get("schedule", [])
    warnings = suggestion.get("warnings", [])

    if not schedule_items:
        notifier.warning(
            "LLM não gerou sugestões. Verifique se há tarefas cadastradas.", "scheduler"
        )
        return

    headers = ["Horário", "Tarefa", "Prioridade"]
    rows = [
        [
            item.get("time_slot", "?"),
            item.get("task_title", "?")[:40],
            item.get("priority", "?"),
        ]
        for item in schedule_items
    ]
    notifier.print_table(headers, rows, "AGENDA SUGERIDA")

    for w in warnings:
        notifier.warning(w, "scheduler")

    apply = input("  Aplicar esta agenda? [s/N]: ").strip().lower()
    if apply == "s":
        ids = scheduler.apply_llm_suggestion(suggestion)
        notifier.success(f"{len(ids)} bloco(s) criados na agenda.", "scheduler")


def cmd_demo() -> None:
    """Cria dados de demonstração para testar o sistema."""
    notifier.separator("MODO DEMO")
    notifier.info("Criando dados de demonstração...", "demo")

    from datetime import date

    today = date.today().isoformat()
    # Cria algumas tarefas de exemplo
    tasks = [
        {
            "title": "Revisar Pull Requests",
            "priority": "Alta",
            "scheduled_time": f"{today} 09:00",
        },
        {
            "title": "Reunião de alinhamento",
            "priority": "Alta",
            "scheduled_time": f"{today} 10:30",
        },
        {
            "title": "Implementar feature X",
            "priority": "Média",
            "scheduled_time": f"{today} 14:00",
        },
        {
            "title": "Responder emails",
            "priority": "Baixa",
            "scheduled_time": f"{today} 16:00",
        },
        {
            "title": "Revisão de código",
            "priority": "Média",
            "scheduled_time": f"{today} 17:00",
        },
    ]

    created_ids = []
    for t in tasks:
        task_id = memory.create_task(**t)
        created_ids.append(task_id)
        notifier.success(f"Tarefa criada: '{t['title']}' (ID: {task_id})", "demo")

    # Cria blocos de agenda
    blocks = [
        ("09:00-10:00", "Revisar Pull Requests", created_ids[0]),
        ("10:30-11:30", "Reunião de alinhamento", created_ids[1]),
        ("12:00-13:00", "Almoço — pausa", None),
        ("14:00-15:30", "Implementar feature X", created_ids[2]),
        ("16:00-16:30", "Responder emails", created_ids[3]),
        ("17:00-18:00", "Revisão de código", created_ids[4]),
    ]

    for time_slot, title, task_id in blocks:
        scheduler.add_schedule_block(time_slot, title, task_id)

    # Marca a primeira como "Em progresso"
    memory.update_task_status(created_ids[0], "Em progresso")

    notifier.success("Dados de demonstração criados!", "demo")
    notifier.info("Execute 'python main.py status' para ver o resumo.", "demo")
    notifier.separator()


# ---------------------------------------------------------------------------
# Modo interativo (REPL)
# ---------------------------------------------------------------------------


def cmd_chat() -> None:
    """
    Modo de chat interativo com o Orchestrator.
    O usuário escreve em linguagem natural e o sistema delega aos agentes.
    """
    # Inicia o Focus Guard em background automaticamente
    if not focus_guard.is_running():
        focus_guard.start_guard()

    notifier.separator("MODO INTERATIVO")
    notifier.info("Digite sua solicitação em linguagem natural.", "chat")
    notifier.info(
        "Comandos especiais: /status | /agenda | /tasks | /sync | /demo | /quit", "chat"
    )
    notifier.separator()

    conversation_history = []

    while True:
        try:
            user_input = input(
                f"\n{notifier.Color.CYAN}Você:{notifier.Color.RESET} "
            ).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input:
            continue

        # Comandos especiais com /
        if user_input.startswith("/"):
            cmd = user_input.lstrip("/").lower()
            if cmd in ("quit", "exit", "sair"):
                break
            elif cmd == "status":
                cmd_status()
            elif cmd == "agenda":
                cmd_agenda()
            elif cmd == "tasks":
                cmd_tasks()
            elif cmd == "sync":
                cmd_sync()
            elif cmd == "demo":
                cmd_demo()
            elif cmd.startswith("focus start"):
                parts = cmd.split()
                task_id = (
                    int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else None
                )
                cmd_focus_start(task_id)
            elif cmd == "focus end":
                cmd_focus_end()
            elif cmd.startswith("validate"):
                parts = cmd.split()
                task_id = (
                    int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else None
                )
                cmd_validate(task_id)
            else:
                notifier.warning(f"Comando desconhecido: /{cmd}", "chat")
            continue

        # Processa via Orchestrator
        response = orchestrator.process(
            user_input, context={"conversation_history": conversation_history}
        )

        print(
            f"\n{notifier.Color.GREEN}{notifier.Color.BOLD}Assistente:{notifier.Color.RESET} {response}\n"
        )

        # Mantém histórico resumido (últimas 10 trocas)
        conversation_history.append({"user": user_input, "assistant": response[:200]})
        if len(conversation_history) > 10:
            conversation_history.pop(0)

    notifier.info("Saindo do modo interativo.", "chat")


# ---------------------------------------------------------------------------
# Comandos Life Guard
# ---------------------------------------------------------------------------


def cmd_vida() -> None:
    """Exibe status das rotinas pessoais do dia e dispara checks."""
    notifier.separator("LIFE GUARD — ROTINAS DO DIA")
    result = life_guard.run_all_checks()
    notifier.info(
        f"Rotinas disparadas: {result['routines'] or 'nenhuma pendente'}", "life_guard"
    )
    notifier.info(
        f"Hidratação: {'lembrete enviado' if result['hydration'] else 'ok'}",
        "life_guard",
    )
    notifier.info(
        f"Financas alertadas: {result['finances'] or 'nenhuma vencendo'}", "life_guard"
    )
    notifier.separator()


def cmd_pagar(args_str: str) -> None:
    """Registra uma conta a pagar. Uso: pagar <nome> dia <N> valor <V>"""
    # ex: "Cartao XP dia 15 valor 1200"
    import re

    match = re.match(r"(.+?)\s+dia\s+(\d+)\s+valor\s+([\d.,]+)", args_str.strip())
    if not match:
        notifier.error(
            "Formato: pagar <nome> dia <N> valor <V>  (ex: pagar Cartao XP dia 15 valor 1200)",
            "life_guard",
        )
        return
    name = match.group(1).strip()
    due_day = int(match.group(2))
    amount = float(match.group(3).replace(",", "."))
    result = life_guard.add_finance(name, due_day, amount)
    notifier.success(
        f"Registrado: {name} — vence dia {due_day} — R$ {amount:.2f}", "life_guard"
    )


def cmd_fiz(rotina: str) -> None:
    """Confirma que uma rotina foi feita. Uso: fiz <exercicio|banho|almoco|jantar>"""
    routine_map = {
        "exercicio": "exercise",
        "banho": "shower",
        "almoco": "lunch",
        "jantar": "dinner",
    }
    routine_id = routine_map.get(rotina.strip().lower())
    if not routine_id:
        notifier.error(
            f"Rotina desconhecida: '{rotina}'. Opcoes: {', '.join(routine_map)}",
            "life_guard",
        )
        return
    life_guard.confirm_routine(routine_id)
    notifier.success(f"Rotina '{rotina}' confirmada para hoje.", "life_guard")


# ---------------------------------------------------------------------------
# Novos comandos Phase 2
# ---------------------------------------------------------------------------


def cmd_retrospective() -> None:
    """Gera a retrospectiva semanal."""
    from agents import retrospective as retro

    notifier.separator("RETROSPECTIVA SEMANAL")

    push = input("  Criar página no Notion? [s/N]: ").strip().lower() == "s"
    result = retro.run_retrospective(push_to_notion=push)

    m = result["metrics"]
    notifier.success(
        f"Retrospectiva gerada! Foco: {m['total_focus_hours']}h | "
        f"Tarefas: {m['tasks_completed']} | Taxa: {m['completion_rate_pct']}%"
    )
    notifier.info(f"Salvo em: {result['local_path']}", "retrospective")

    print(f"\n{result['report_preview']}")


def cmd_web() -> None:
    """Inicia a interface web."""
    import uvicorn

    from config import WEB_HOST, WEB_PORT

    notifier.info(f"Iniciando interface web em http://{WEB_HOST}:{WEB_PORT}", "web")
    uvicorn.run("web.app:app", host=WEB_HOST, port=WEB_PORT, reload=False)


def cmd_calendar_auth() -> None:
    """Autoriza a integração opcional com Google Calendar."""
    from agents import calendar_sync

    notifier.info(
        "Iniciando fluxo de autorização da integração opcional com Google Calendar...",
        "calendar",
    )
    notifier.info("O browser será aberto para autorização.", "calendar")
    if calendar_sync.authorize():
        notifier.success(
            "Autorização concluída! Use 'calendar import' para importar eventos."
        )
    else:
        notifier.error("Autorização falhou. Verifique o credentials.json.")


def cmd_calendar_import() -> None:
    """Importa eventos de hoje da integração opcional com Google Calendar."""
    from agents import calendar_sync

    count = calendar_sync.import_today_as_blocks()
    notifier.success(f"{count} evento(s) importados como blocos de agenda.")


def cmd_calendar_status() -> None:
    """Status da integração opcional com o Google Calendar."""
    from agents import calendar_sync

    notifier.separator("GOOGLE CALENDAR STATUS")
    notifier.info(f"Autorizado: {calendar_sync.is_authorized()}", "calendar")
    notifier.info(f"Calendário: {calendar_sync.GOOGLE_CALENDAR_ID}", "calendar")
    if calendar_sync.is_authorized():
        events = calendar_sync.fetch_today_events()
        notifier.info(f"Eventos hoje: {len(events)}", "calendar")
        for ev in events[:5]:
            notifier.info(f"  {ev['time_slot']} — {ev['title']}", "calendar")
    notifier.separator()


# ---------------------------------------------------------------------------
# Parser CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="multiagentes",
        description="Gate with nodes multiagents to archtect NEØ",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python main.py                     # Modo interativo
  python main.py status              # Status do sistema
  python main.py agenda              # Agenda de hoje
  python main.py tasks               # Lista de tarefas
  python main.py add-task            # Wizard para nova tarefa
  python main.py sync                # Sincroniza com Notion
  python main.py suggest             # Sugestão de agenda via LLM
  python main.py focus start 3       # Foca na tarefa ID 3
  python main.py focus end           # Encerra sessão de foco
  python main.py validate 3          # Valida tarefa ID 3
  python main.py demo                # Cria dados de demonstração
        """,
    )

    subparsers = parser.add_subparsers(dest="command", metavar="COMANDO")

    # chat / interativo
    subparsers.add_parser("chat", help="Modo interativo com o Orchestrator")

    # status
    subparsers.add_parser("status", help="Status completo do sistema")

    # agenda
    subparsers.add_parser("agenda", help="Exibe agenda de hoje")

    # tasks
    subparsers.add_parser("tasks", help="Lista todas as tarefas")

    # add-task
    subparsers.add_parser("add-task", help="Wizard para adicionar nova tarefa")

    # sync
    subparsers.add_parser("sync", help="Sincroniza com Notion")

    # suggest
    subparsers.add_parser("suggest", help="Sugere agenda otimizada via LLM")

    # focus
    focus_parser = subparsers.add_parser("focus", help="Gerencia sessões de foco")
    focus_sub = focus_parser.add_subparsers(dest="focus_action", metavar="AÇÃO")
    focus_start = focus_sub.add_parser("start", help="Inicia sessão de foco")
    focus_start.add_argument("task_id", type=int, nargs="?", help="ID da tarefa")
    focus_sub.add_parser("end", help="Encerra sessão de foco ativa")

    # validate
    validate_parser = subparsers.add_parser(
        "validate", help="Valida conclusão de tarefa"
    )
    validate_parser.add_argument("task_id", type=int, nargs="?", help="ID da tarefa")

    # demo
    subparsers.add_parser("demo", help="Cria dados de demonstração")

    # retrospective
    subparsers.add_parser("retrospective", help="Gera retrospectiva semanal")

    # web
    subparsers.add_parser("web", help="Inicia interface web (FastAPI)")

    # vida / life guard
    subparsers.add_parser("vida", help="Status das rotinas pessoais do dia")
    subparsers.add_parser("life", help="Status das rotinas pessoais do dia (alias)")

    pagar_parser = subparsers.add_parser(
        "pagar", help="Registra conta a pagar (ex: pagar Cartao XP dia 15 valor 1200)"
    )
    pagar_parser.add_argument("args", nargs=argparse.REMAINDER)

    fiz_parser = subparsers.add_parser(
        "fiz", help="Confirma rotina feita (ex: fiz banho)"
    )
    fiz_parser.add_argument("rotina", nargs="?", default="")

    # ecosistema
    subparsers.add_parser(
        "ecosistema", help="Health check e relatório do ecossistema externo"
    )

    # calendar
    calendar_parser = subparsers.add_parser(
        "calendar", help="Gerencia integração opcional com Google Calendar"
    )
    cal_sub = calendar_parser.add_subparsers(dest="calendar_action", metavar="AÇÃO")
    cal_sub.add_parser("auth", help="Autoriza acesso opcional ao Google Calendar")
    cal_sub.add_parser(
        "import", help="Importa eventos opcionais de hoje como blocos de agenda"
    )
    cal_sub.add_parser("status", help="Status da integração opcional com o Calendar")

    return parser


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    signal.signal(signal.SIGINT, _handle_sigint)
    atexit.register(_shutdown)

    _startup()

    parser = build_parser()
    args = parser.parse_args()

    command = args.command or "chat"  # Padrão: modo interativo

    if command == "chat":
        cmd_chat()
    elif command == "status":
        cmd_status()
    elif command == "agenda":
        cmd_agenda()
    elif command == "tasks":
        cmd_tasks()
    elif command == "add-task":
        cmd_add_task()
    elif command == "sync":
        cmd_sync()
    elif command == "suggest":
        cmd_suggest_agenda()
    elif command == "focus":
        if args.focus_action == "start":
            cmd_focus_start(getattr(args, "task_id", None))
        elif args.focus_action == "end":
            cmd_focus_end()
        else:
            notifier.error("Use: python main.py focus [start|end]", "main")
    elif command == "validate":
        cmd_validate(getattr(args, "task_id", None))
    elif command == "demo":
        cmd_demo()
    elif command == "retrospective":
        cmd_retrospective()
    elif command == "web":
        cmd_web()
    elif command == "ecosistema":
        from agents import ecosystem_monitor

        report = ecosystem_monitor.run()
        print(report)
    elif command in ("vida", "life"):
        cmd_vida()
    elif command == "pagar":
        cmd_pagar(" ".join(getattr(args, "args", [])))
    elif command == "fiz":
        cmd_fiz(getattr(args, "rotina", ""))
    elif command == "calendar":
        if args.calendar_action == "auth":
            cmd_calendar_auth()
        elif args.calendar_action == "import":
            cmd_calendar_import()
        elif args.calendar_action == "status":
            cmd_calendar_status()
        else:
            notifier.error("Use: python main.py calendar [auth|import|status]", "main")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
````

## File: Makefile
````makefile
# =============================================================================
# Makefile - Multiagentes Personal System
# =============================================================================
# Uso: make <comando>
# Dica: make help  →  lista todos os comandos disponíveis

SHELL  := /bin/bash
PYTHON := python3
VENV   := .venv
PIP    := $(VENV)/bin/pip
PY     := $(VENV)/bin/python

# Cores ANSI (via printf para compatibilidade)
BOLD   := $(shell printf '\033[1m')
CYAN   := $(shell printf '\033[36m')
GREEN  := $(shell printf '\033[32m')
YELLOW := $(shell printf '\033[33m')
RED    := $(shell printf '\033[31m')
RESET  := $(shell printf '\033[0m')

.DEFAULT_GOAL := help

# =============================================================================
# AJUDA
# =============================================================================

.PHONY: help
help: ## Exibe esta ajuda
	@echo ""
	@echo "  $(BOLD)$(CYAN)Multiagentes - Comandos disponíveis$(RESET)"
	@echo ""
	@awk 'BEGIN {FS=":.*##"; cat=""} \
		/^# [A-Z0-9][A-Z0-9 ()&_-]*$$/ { \
			cat=$$0; sub(/^# +/,"",cat); \
			printf "\n  $(BOLD)$(CYAN)%s$(RESET)\n\n", cat } \
		/^[a-zA-Z_-]+:.*##/ { \
			printf "  $(GREEN)%-22s$(RESET) %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
	@echo ""

# =============================================================================
# SETUP
# =============================================================================

.PHONY: build
build: install ## Alias Railway-friendly: instala dependências (projeto Python, sem transpile)
	@echo "$(GREEN)✓ Build concluído - use 'make dev' para iniciar$(RESET)"

.PHONY: setup
setup: venv install env-copy redis-pull ## Configura tudo do zero (venv + deps + .env)
	@echo "$(GREEN)✓ Setup completo! Edite o .env e rode: make dev$(RESET)"

.PHONY: venv
venv: ## Cria o virtualenv
	@test -d $(VENV) || $(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)✓ Virtualenv em $(VENV)/$(RESET)"

.PHONY: install
install: venv ## Instala dependências Python
	@$(PIP) install --upgrade pip -q
	@$(PIP) install -r requirements.txt
	@echo "$(GREEN)✓ Dependências instaladas$(RESET)"

.PHONY: install-dev
install-dev: install ## Instala dependências + extras dev (ipython, ruff, pylyzer, etc.)
	@$(PIP) install ipython rich watchdog ruff pytest-cov pytest-watch pylyzer -q
	@echo "$(GREEN)✓ Dev extras instalados$(RESET)"

.PHONY: redis-pull
redis-pull: ## Baixa imagem Redis Docker (uma vez só)
	@docker pull redis:7-alpine -q && echo "$(GREEN)✓ Redis image pronta$(RESET)"

# =============================================================================
# DESENVOLVIMENTO
# =============================================================================

.PHONY: dev
dev: ## Inicia servidor FastAPI com hot-reload (porta 8000)
	@echo "$(CYAN)→ http://localhost:8000$(RESET)"
	@REDIS_URL=$${REDIS_URL:-redis://localhost:6379/0} \
		$(VENV)/bin/uvicorn web.app:app --host 127.0.0.1 --port 8000 --reload

.PHONY: dev-ui
dev-ui: ## Inicia FastAPI com reload para templates/static (tuning de UI)
	@echo "$(CYAN)→ http://localhost:8000 (UI reload)$(RESET)"
	@REDIS_URL=$${REDIS_URL:-redis://localhost:6379/0} \
		$(VENV)/bin/uvicorn web.app:app --host 127.0.0.1 --port 8000 --reload \
		--reload-include '*.py' \
		--reload-include 'web/templates/**/*.html' \
		--reload-include 'web/static/**/*.css' \
		--reload-include 'web/static/**/*.js'

.PHONY: dev-full
dev-full: redis-up ## Sobe Redis local + FastAPI com hot-reload
	@sleep 1
	@$(MAKE) dev

.PHONY: dev-full-ui
dev-full-ui: redis-up ## Sobe Redis local + FastAPI com reload para UI
	@sleep 1
	@$(MAKE) dev-ui

.PHONY: guard
guard: redis-ensure ## Inicia Focus Guard no terminal
	@$(PY) main.py

# =============================================================================
# REDIS LOCAL (BREW SERVICE - MACOS)
# =============================================================================

REDIS_CONTAINER := multiagentes-redis
BREW := $(shell command -v brew 2>/dev/null || echo /opt/homebrew/bin/brew)
REDIS_CLI := $(shell command -v redis-cli 2>/dev/null || echo /opt/homebrew/opt/redis/bin/redis-cli)
REDIS_HOST := 127.0.0.1
REDIS_PORT := 6379

.PHONY: brew-redis
brew-redis: ## Instala Redis via Homebrew e inicia como serviço permanente
	@[ -x "$(BREW)" ] || (echo "$(RED)✗ brew não encontrado. Instale Homebrew ou use Docker com: make redis-up$(RESET)"; exit 1)
	@$(BREW) install redis
	@$(BREW) services start redis
	@echo "$(GREEN)✓ Redis instalado e rodando via brew$(RESET)"

.PHONY: redis-up
redis-up: ## Garante que Redis está rodando (brew service → Docker fallback)
	@set -e; \
	if [ -x "$(REDIS_CLI)" ] && "$(REDIS_CLI)" -h "$(REDIS_HOST)" -p "$(REDIS_PORT)" ping > /dev/null 2>&1; then \
		echo "$(GREEN)✓ Redis rodando em $(REDIS_HOST):$(REDIS_PORT)$(RESET)"; exit 0; \
	fi; \
	if [ -x "$(BREW)" ]; then \
		"$(BREW)" services start redis > /dev/null 2>&1 || true; \
		sleep 0.5; \
	fi; \
	if [ -x "$(REDIS_CLI)" ] && "$(REDIS_CLI)" -h "$(REDIS_HOST)" -p "$(REDIS_PORT)" ping > /dev/null 2>&1; then \
		echo "$(GREEN)✓ Redis iniciado via brew services$(RESET)"; exit 0; \
	fi; \
	docker run -d --rm \
		--name $(REDIS_CONTAINER) \
		-p $(REDIS_PORT):6379 \
		redis:7-alpine \
		> /dev/null 2>&1 || true; \
	sleep 0.5; \
	echo "$(YELLOW)✓ Redis iniciado via Docker (fallback)$(RESET)"

.PHONY: redis-ensure
redis-ensure: ## Garante que Redis está respondendo antes de rodar agentes
	@set -e; \
	if [ -x "$(REDIS_CLI)" ] && "$(REDIS_CLI)" -h "$(REDIS_HOST)" -p "$(REDIS_PORT)" ping > /dev/null 2>&1; then exit 0; fi; \
	if docker ps --format '{{.Names}}' 2>/dev/null | grep -qx "$(REDIS_CONTAINER)"; then \
		docker exec "$(REDIS_CONTAINER)" redis-cli ping > /dev/null 2>&1 && exit 0; \
	fi; \
	$(MAKE) redis-up > /dev/null; \
	if [ -x "$(REDIS_CLI)" ] && "$(REDIS_CLI)" -h "$(REDIS_HOST)" -p "$(REDIS_PORT)" ping > /dev/null 2>&1; then exit 0; fi; \
	if docker ps --format '{{.Names}}' 2>/dev/null | grep -qx "$(REDIS_CONTAINER)"; then \
		docker exec "$(REDIS_CONTAINER)" redis-cli ping > /dev/null 2>&1 && exit 0; \
	fi; \
	echo "$(RED)✗ Redis indisponível. Tente: make brew-redis (recomendado) ou make redis-up$(RESET)"; \
	exit 1

.PHONY: redis-down
redis-down: ## Para Redis local (brew e/ou Docker)
	@[ -x "$(BREW)" ] && "$(BREW)" services stop redis > /dev/null 2>&1 || true
	@docker stop $(REDIS_CONTAINER) 2>/dev/null || true
	@echo "$(YELLOW)✓ Redis parado$(RESET)"

.PHONY: redis-cli
redis-cli: ## Abre Redis CLI interativo
	@set -e; \
	if [ -x "$(REDIS_CLI)" ]; then \
		"$(REDIS_CLI)" -h "$(REDIS_HOST)" -p "$(REDIS_PORT)"; exit 0; \
	fi; \
	if docker ps --format '{{.Names}}' 2>/dev/null | grep -qx "$(REDIS_CONTAINER)"; then \
		docker exec -it "$(REDIS_CONTAINER)" redis-cli; exit 0; \
	fi; \
	echo "$(RED)✗ redis-cli indisponível. Instale redis (brew install redis) ou suba via Docker (make redis-up)$(RESET)"; \
	exit 1

.PHONY: redis-keys
redis-keys: ## Lista todas as chaves no Redis (ordenadas)
	@set -e; \
	if [ -x "$(REDIS_CLI)" ]; then \
		"$(REDIS_CLI)" -h "$(REDIS_HOST)" -p "$(REDIS_PORT)" KEYS '*' | sort; exit 0; \
	fi; \
	if docker ps --format '{{.Names}}' 2>/dev/null | grep -qx "$(REDIS_CONTAINER)"; then \
		docker exec "$(REDIS_CONTAINER)" redis-cli KEYS '*' | sort; exit 0; \
	fi; \
	echo "$(RED)✗ Redis não está acessível. Rode: make redis-up$(RESET)"; \
	exit 1

.PHONY: redis-stats
redis-stats: ## Exibe estatísticas do Redis (memória, conexões, etc.)
	@set -e; \
	if [ -x "$(REDIS_CLI)" ]; then \
		"$(REDIS_CLI)" -h "$(REDIS_HOST)" -p "$(REDIS_PORT)" INFO stats | grep -E "connected|commands|memory|keys"; exit 0; \
	fi; \
	if docker ps --format '{{.Names}}' 2>/dev/null | grep -qx "$(REDIS_CONTAINER)"; then \
		docker exec "$(REDIS_CONTAINER)" redis-cli INFO stats | grep -E "connected|commands|memory|keys"; exit 0; \
	fi; \
	echo "$(RED)✗ Redis não está acessível. Rode: make redis-up$(RESET)"; \
	exit 1

.PHONY: redis-weekly
redis-weekly: ## Exibe checklist semanal do Redis na Railway (5 min)
	@cat docs/operacao/redis-weekly-check.md

.PHONY: redis-flush
redis-flush: ## ⚠️  Apaga TODOS os dados do Redis local
	@echo "$(RED)⚠️  Isso apaga TODOS os dados locais!$(RESET)"
	@read -p "Confirma? [s/N] " c && [ "$$c" = "s" ] && \
		( if [ -x "$(REDIS_CLI)" ]; then \
			"$(REDIS_CLI)" -h "$(REDIS_HOST)" -p "$(REDIS_PORT)" FLUSHALL; \
		else \
			docker exec "$(REDIS_CONTAINER)" redis-cli FLUSHALL; \
		fi ) && \
		echo "$(YELLOW)✓ Redis limpo$(RESET)" || echo "Cancelado."

.PHONY: redis-ping
redis-ping: ## Testa conexão Redis
	@set -e; \
	if [ -x "$(REDIS_CLI)" ]; then \
		"$(REDIS_CLI)" -h "$(REDIS_HOST)" -p "$(REDIS_PORT)" PING; exit 0; \
	fi; \
	if docker ps --format '{{.Names}}' 2>/dev/null | grep -qx "$(REDIS_CONTAINER)"; then \
		docker exec "$(REDIS_CONTAINER)" redis-cli PING; exit 0; \
	fi; \
	echo "$(RED)✗ Redis não está acessível. Rode: make redis-up$(RESET)"; \
	exit 1

# =============================================================================
# AGENTES
# =============================================================================

.PHONY: sync
sync: redis-ensure ## Sincronização diferencial com Notion
	@$(PY) main.py sync

.PHONY: agenda
agenda: redis-ensure ## Exibe agenda de hoje
	@$(PY) main.py agenda

.PHONY: tasks
tasks: redis-ensure ## Lista todas as tarefas
	@$(PY) main.py tasks

.PHONY: retro
retro: redis-ensure ## Gera retrospectiva semanal (local, sem push)
	@$(PY) main.py retrospective

.PHONY: retro-push
retro-push: redis-ensure ## Gera retrospectiva e envia ao Notion
	@$(PY) main.py retrospective --push

.PHONY: calendar-auth
calendar-auth: ## Autentica Google Calendar (OAuth2)
	@$(PY) main.py calendar auth

.PHONY: calendar-import
calendar-import: redis-ensure ## Importa eventos de hoje do Google Calendar
	@$(PY) main.py calendar import

.PHONY: calendar-status
calendar-status: redis-ensure ## Status da integração Google Calendar
	@$(PY) main.py calendar status

.PHONY: web
web: ## Inicia interface web (modo estável, sem hot-reload)
	@$(PY) main.py web

.PHONY: vida
vida: redis-ensure ## Status das rotinas pessoais do dia (Life Guard)
	@$(PY) main.py vida

.PHONY: chat
chat: redis-ensure ## Modo chat interativo com o Orchestrator
	@$(PY) main.py chat

.PHONY: status
status: redis-ensure ## Exibe status atual do sistema
	@$(PY) main.py status

# =============================================================================
# TESTES
# =============================================================================

.PHONY: test
test: ## Roda todos os testes
	@$(VENV)/bin/pytest tests/ -v --tb=short

.PHONY: test-q
test-q: ## Roda testes modo silencioso
	@$(VENV)/bin/pytest tests/ -q

.PHONY: test-cov
test-cov: ## Testes com relatório de cobertura (abre htmlcov/)
	@$(VENV)/bin/pytest tests/ --cov=. --cov-report=term-missing --cov-report=html
	@echo "$(CYAN)→ Relatório em htmlcov/index.html$(RESET)"

.PHONY: test-watch
test-watch: ## Roda testes automaticamente ao salvar (watch mode)
	@$(VENV)/bin/ptw tests/ -- -v

# =============================================================================
# QUALIDADE DE CODIGO
# =============================================================================

.PHONY: lint
lint: ## Verifica estilo com ruff
	@$(VENV)/bin/ruff check . || true

.PHONY: fmt
fmt: ## Formata código com ruff
	@$(VENV)/bin/ruff format .
	@echo "$(GREEN)✓ Código formatado$(RESET)"

.PHONY: check
check: lint test ## lint + testes (CI local completo)

# =============================================================================
# GIT & DEPLOY
# =============================================================================

.PHONY: push
push: ## add + commit interativo + push
	@read -p "$(CYAN)Mensagem do commit: $(RESET)" msg && \
		git add -A && \
		git commit -m "$$msg" && \
		git push origin main && \
		echo "$(GREEN)✓ Push feito$(RESET)"

.PHONY: push-fix
push-fix: ## Commit rápido de fix + push
	@read -p "$(YELLOW)Fix: $(RESET)" msg && \
		git add -A && \
		git commit -m "fix: $$msg" && \
		git push origin main

.PHONY: push-feat
push-feat: ## Commit rápido de feat + push
	@read -p "$(CYAN)Feature: $(RESET)" msg && \
		git add -A && \
		git commit -m "feat: $$msg" && \
		git push origin main

.PHONY: log
log: ## Git log compacto (últimos 10 commits)
	@git log --oneline --graph --decorate -10

.PHONY: diff
diff: ## Git diff staged
	@git diff --staged

# =============================================================================
# DIAGNOSTICO & AMBIENTE
# =============================================================================

.PHONY: env-check
env-check: ## Verifica variáveis de ambiente obrigatórias
	@$(PY) -c "from config import validate_config; w = validate_config(); \
		[print('⚠ ', x) for x in w] or print('✓ Config OK')"

.PHONY: env-copy
env-copy: ## Copia .env.example → .env (se não existir)
	@test -f .env && echo ".env já existe" || \
		(cp .env.example .env && echo "$(YELLOW)✓ .env criado - preencha as chaves!$(RESET)")

.PHONY: health
health: ## Checa o endpoint /health (app local)
	@curl -s http://localhost:8000/health | $(PYTHON) -m json.tool

.PHONY: logs
logs: ## Exibe últimas linhas dos logs
	@ls logs/*.log 2>/dev/null | xargs tail -n 50 || echo "Sem logs em logs/."

.PHONY: info
info: ## Exibe info do ambiente
	@echo ""
	@echo "  $(BOLD)Python:$(RESET)      $$($(PY) --version)"
	@echo "  $(BOLD)Pip:$(RESET)         $$($(PIP) --version | cut -d' ' -f1-2)"
	@echo "  $(BOLD)Uvicorn:$(RESET)     $$($(VENV)/bin/uvicorn --version 2>/dev/null || echo 'não instalado')"
	@echo "  $(BOLD)Redis:$(RESET)       $$(docker exec $(REDIS_CONTAINER) redis-cli PING 2>/dev/null || echo 'container parado')"
	@echo "  $(BOLD)Branch:$(RESET)      $$(git branch --show-current)"
	@echo "  $(BOLD)Último commit:$(RESET) $$(git log --oneline -1)"
	@echo ""

.PHONY: docker-df
docker-df: ## Exibe consumo de disco do Docker
	@docker system df

.PHONY: docker-maintenance
docker-maintenance: ## Limpeza focada em build cache (agressiva)
	@bash scripts/docker_maintenance.sh build

.PHONY: docker-maintenance-safe
docker-maintenance-safe: ## Limpeza conservadora (cache + dangling images)
	@bash scripts/docker_maintenance.sh safe

.PHONY: docker-maintenance-deep
docker-maintenance-deep: ## Limpeza ampla (cache + imagens sem uso)
	@bash scripts/docker_maintenance.sh deep

.PHONY: docker-maintenance-install
docker-maintenance-install: ## Agenda limpeza semanal via launchd (dom 04:10)
	@bash scripts/install_docker_maintenance_launchd.sh

.PHONY: docker-maintenance-uninstall
docker-maintenance-uninstall: ## Remove agendamento launchd de manutenção Docker
	@bash scripts/install_docker_maintenance_launchd.sh --uninstall

.PHONY: docker-maintenance-status
docker-maintenance-status: ## Mostra status do agendamento no launchd
	@launchctl list | grep docker-maintenance || echo "Agendamento não encontrado."

.PHONY: clean
clean: ## Remove cache Python e arquivos temporários
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . \( -name "*.pyc" -o -name "*.pyo" \) -delete 2>/dev/null || true
	@rm -rf .ruff_cache htmlcov .coverage 2>/dev/null || true
	@echo "$(GREEN)✓ Cache limpo$(RESET)"

.PHONY: clean-all
clean-all: clean redis-down ## Remove cache + venv + para Redis (reset total)
	@rm -rf $(VENV)
	@echo "$(YELLOW)✓ Reset completo - rode: make setup$(RESET)"
````

## File: Procfile
````
web: uvicorn web.app:app --host 0.0.0.0 --port $PORT
````

## File: railway.json
````json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "DOCKERFILE",
    "dockerfilePath": "Dockerfile"
  },
  "deploy": {
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 3,
    "healthcheckPath": "/health",
    "healthcheckTimeout": 15
  }
}
````

## File: README.md
````markdown
<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

```text
========================================
      MULTIAGENTES · PERSONAL CORE
========================================
```

![multiagentes banner](./docs/assets/multiagentes-banner.svg)

Portal providing access to the multi-agent nodes
that serve the NEØ architect.
como origem principal, Google Calendar
como capacidade opcional, Sanity.io
e monitoramento autônomo de foco.

> **Status:** Fase 2 operacional
> **Python:** >=3.11
> **Deploy:** Railway + Redis
> **Interface:** FastAPI + Jinja2 + HTMX (PWA)

────────────────────────────────────────

## What Is This?

A camada operacional de um sistema pessoal
que não trata produtividade como lista,
mas como fluxo entre intenção, agenda,
execução, validação e memória.

```text
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ MULTIAGENTES CAPABILITIES            ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ Orchestrator
┃   └─ roteia intenções do usuário
┃      e consolida respostas
┃
┃ Focus Guard
┃   └─ monitora atraso, desvio,
┃      sessão de foco e reage
┃      com auto-reagendamento
┃      e escalada por tempo
┃
┃ Scheduler
┃   └─ cria, ordena e move blocos
┃      de agenda
┃
┃ Notion Sync
┃   └─ sincroniza tarefas e agenda
┃      com databases do Notion
┃
┃ Calendar Sync
┃   └─ integra Google Calendar
┃      como fonte opcional de
┃      importação e exportação
┃
┃ Validator
┃   └─ valida conclusão de tarefas
┃      com evidências cruzadas
┃
┃ Retrospective
┃   └─ gera relatório semanal com
┃      métricas e insights via LLM
┃
┃ Life Guard
┃   └─ rotinas pessoais: hidratação,
┃      exercício, refeições, finanças
┃
┃ Persona Manager
┃   └─ personas dinâmicas com
┃      injeção de system prompt
┃
┃ Ecosystem Monitor
┃   └─ monitora GitHub, Railway,
┃      Vercel, on-chain em 6 orgs
┃
┃ Audit Trail
┃   └─ registra alertas, handoffs,
┃      desvios, logs e reações
┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

────────────────────────────────────────

## Operational Flow

```text
Usuário
  │
  ├─ Web UI (/)
  └─ CLI (main.py)
       │
       ▼
  Orchestrator
       │
       ├─ Scheduler
       ├─ Focus Guard
       │    └─ Life Guard (rotinas)
       ├─ Notion Sync
       ├─ Calendar Sync (opcional)
       ├─ Validator
       ├─ Retrospective
       └─ Persona Manager
             │
             ▼
          Redis
             │
             ├─ agenda
             ├─ tarefas
             ├─ alertas
             ├─ handoffs
             └─ auditoria
```

────────────────────────────────────────

## Quick Start

```bash
# 1. Criar ambiente e instalar dependências
make setup

# 2. Subir Redis local + app web
make dev-full

# 3. Acessar interface
open http://localhost:8000

# 4. Rodar testes
make test-q
```

> Se o Redis já estiver disponível, use `make dev`.

────────────────────────────────────────

## Core Surfaces

```text
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ SURFACE              PURPOSE        ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ Web UI               dashboard,
┃                      agenda, audit,
┃                      tasks, chat
┃ CLI                  operação local
┃                      e automação
┃ Redis                persistência
┃                      operacional
┃ Notion               fonte principal
┃                      de tarefas e agenda
┃ Google Calendar      capacidade
┃                      opcional de agenda
┃ Sanity Studio        prompts, personas
┃                      e configs externas
┃ macOS Push + Alexa   notificações de
┃                      foco e rotinas
┃ Railway              deploy web +
┃                      healthcheck
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

────────────────────────────────────────

## Repository Structure

```text
multiagentes/
├── agents/
│   ├── orchestrator.py      roteador central
│   ├── focus_guard.py       monitor de foco, escalada e auto-reschedule
│   ├── scheduler.py         agenda e blocos
│   ├── notion_sync.py       sync com Notion (bidirecional)
│   ├── calendar_sync.py     integração opcional com Google Calendar
│   ├── validator.py         validação de conclusão
│   ├── retrospective.py     retrospectiva semanal
│   ├── life_guard.py        rotinas pessoais (hidratação, exercício, finanças)
│   ├── persona_manager.py   seletor de personas dinâmicas
│   └── ecosystem_monitor.py monitoramento de projetos
├── core/
│   ├── memory.py            persistência Redis + SQLite fallback
│   ├── openai_utils.py      wrapper central para OpenAI API
│   ├── notifier.py          logs, terminal, macOS push, Alexa
│   └── sanity_client.py     cliente Sanity.io com cache e fallback
├── web/
│   ├── app.py               FastAPI app
│   ├── templates/           páginas e partials (Jinja2 + HTMX)
│   └── static/              manifest, service worker, ícones
├── docs/
│   ├── INDEX.md             índice geral da documentação
│   ├── governanca/          contratos, matriz e políticas de precedência
│   ├── arquitetura/         schema e modelo semântico
│   ├── operacao/            manuais e runbooks operacionais
│   ├── planejamento/        sprints e trilha de execução
│   ├── ecossistema/         mapa das orgs e referências externas
│   └── auditoria/           auditorias e verificações
├── personas/
│   ├── architect.json       persona arquiteto
│   ├── coordinator.json     persona coordenador
│   └── taylor.json          persona taylor
├── sanity/                  Sanity Studio (schemas e config)
├── scripts/                 macOS launchd plist + installer
├── tests/
│   ├── test_memory.py
│   ├── test_focus_guard.py
│   ├── test_notion_sync.py
│   ├── test_orchestrator.py
│   └── test_web_chat.py
├── main.py                  entrypoint CLI
├── config.py                configuração central
├── ROADMAP.md               roadmap e próximas frentes
├── Dockerfile               build Railway
├── Procfile                 entrypoint deploy
├── railway.json             healthcheck / restart policy
├── Makefile                 operação local
└── requirements.txt         dependências Python
```

────────────────────────────────────────

## Main Pages

```text
▓▓▓ WEB INTERFACE
────────────────────────────────────────
└─ /                         dashboard principal
└─ /agenda                   agenda navegável por intervalo
└─ /tasks-page               criar e gerenciar tarefas
└─ /chat-page                chat full-screen com orchestrator
└─ /audit                    alertas, eventos, handoffs e logs
└─ /health                   healthcheck para Railway

▓▓▓ INTERACTIONS
────────────────────────────────────────
└─ /chat                     conversa com orchestrator (HTMX)
└─ /task                     criação de tarefa
└─ /task/{id}/complete       conclusão de tarefa
└─ /block/{id}/complete      conclusão de bloco
└─ /agenda/import            importação de intervalo
└─ /sync                     sincronização com Notion
└─ /tasks                    lista de tarefas (partial)
```

────────────────────────────────────────

## Integrations

| Integração      | Papel                                | Variáveis principais                                                 |
| --------------- | ------------------------------------ | -------------------------------------------------------------------- |
| OpenAI          | roteamento e síntese do orchestrator | `OPENAI_API_KEY`, `OPENAI_MODEL`                                     |
| Notion          | fonte principal de tarefas e agenda  | `NOTION_TOKEN`, `NOTION_TASKS_DB_ID`, `NOTION_AGENDA_DB_ID`          |
| Google Calendar | integração opcional de agenda        | `GOOGLE_CREDENTIALS_FILE`, `GOOGLE_TOKEN_FILE`, `GOOGLE_CALENDAR_ID` |
| Sanity.io       | prompts, personas, configs externas  | `SANITY_PROJECT_ID`, `SANITY_API_TOKEN`, `SANITY_DATASET`            |
| Voice Monkey    | anúncios na Alexa                    | `VOICE_MONKEY_TOKEN`, `VOICE_MONKEY_DEVICE`                          |
| Redis           | memória e persistência               | `REDIS_URL`                                                          |
| Railway         | deploy do app web                    | `PORT`, `REDIS_URL`                                                  |

────────────────────────────────────────

## Environment Variables

```bash
# --- OBRIGATÓRIO ---
OPENAI_API_KEY=              # chave OpenAI
NOTION_TOKEN=                # integration token Notion
NOTION_TASKS_DB_ID=          # database "Tarefas"
NOTION_AGENDA_DB_ID=         # database "Agenda Diária"

# --- OPENAI (opcional) ---
OPENAI_MODEL=gpt-4o-mini
OPENAI_FALLBACK_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=1500
OPENAI_TEMPERATURE=0.2

# --- NOTION (opcional) ---
NOTION_RETROSPECTIVE_PAGE_ID=
NOTION_SYNC_INTERVAL=5

# --- REDIS ---
REDIS_URL=redis://localhost:6379/0

# --- GOOGLE CALENDAR (opcional) ---
GOOGLE_CREDENTIALS_FILE=./credentials.json
GOOGLE_TOKEN_FILE=./token.json
GOOGLE_CALENDAR_ID=primary

# --- SANITY.IO (opcional) ---
SANITY_PROJECT_ID=           # project ID do sanity.io/manage
SANITY_DATASET=production
SANITY_API_TOKEN=            # token com permissão Viewer
SANITY_USE_CDN=false

# --- NOTIFICAÇÕES — VOICE MONKEY (opcional) ---
VOICE_MONKEY_TOKEN=          # api-v2.voicemonkey.io
VOICE_MONKEY_DEVICE=eco-room
VOICE_MONKEY_VOICE=Ricardo

# --- LIFE GUARD (opcional) ---
LIFE_GUARD_ACTIVE_HOUR_START=8
LIFE_GUARD_ACTIVE_HOUR_END=22
LIFE_GUARD_WATER_INTERVAL=90

# --- FOCUS GUARD ---
FOCUS_CHECK_INTERVAL=15

# --- LOGGING ---
LOG_FILE=./logs/agent_system.log
LOG_LEVEL=INFO

# --- WEB ---
WEB_HOST=127.0.0.1
WEB_PORT=8000
```

────────────────────────────────────────

## Make Commands

```text
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ COMMAND                ACTION                          ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ make setup             setup inicial (venv + deps)
┃ make dev               FastAPI local
┃ make dev-full          FastAPI + Redis
┃ make guard             Focus Guard CLI
┃ make sync              sync Notion
┃ make agenda            agenda do dia
┃ make tasks             lista tarefas
┃ make vida              status rotinas pessoais
┃ make retro             retrospectiva semanal
┃ make calendar-auth     OAuth Google Calendar opcional
┃ make calendar-import   importa eventos opcionais
┃ make test-q            testes rápidos
┃ make check             lint + testes
┃ make web               inicia interface web
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

────────────────────────────────────────

## CLI Commands

```text
python main.py                     # Modo interativo (REPL)
python main.py status              # Status do sistema
python main.py agenda              # Agenda de hoje
python main.py tasks               # Lista de tarefas
python main.py add-task            # Wizard nova tarefa
python main.py sync                # Sync com Notion
python main.py suggest             # Sugestão de agenda via LLM
python main.py focus start [id]    # Inicia sessão de foco
python main.py focus end           # Encerra sessão de foco
python main.py validate [id]       # Valida tarefa
python main.py demo                # Dados de demonstração
python main.py retrospective       # Retrospectiva semanal
python main.py web                 # Inicia interface web
python main.py vida                # Status das rotinas pessoais
python main.py fiz <rotina>        # Confirma rotina (exercicio|banho|almoco|jantar)
python main.py pagar <args>        # Registra conta a pagar
python main.py calendar auth       # Autoriza Google Calendar opcional
python main.py calendar import     # Importa eventos opcionais de hoje
python main.py calendar status     # Status da integração opcional
```

────────────────────────────────────────

## Persistence Model

- Estado operacional principal vive em Redis via [core/memory.py](./core/memory.py)
- Alertas, handoffs, agenda, sessões e auditoria são persistidos por chave
- Logs locais são gravados em arquivo configurado por `LOG_FILE`
- A interface `/audit` expõe a trilha de eventos e a cauda do log
- A agenda pode ser consultada e importada por intervalo em `/agenda`
- Prompts e configs externos gerenciados via Sanity.io com cache de 5min e fallback para hardcoded

────────────────────────────────────────

## Documentation

```text
▓▓▓ ENTRYPOINT
────────────────────────────────────────
└─ docs/INDEX.md                               índice mestre
└─ ROADMAP.md                                 roadmap geral do produto

▓▓▓ OPERAÇÃO
────────────────────────────────────────
└─ docs/operacao/MANUAL_USUARIO.md           uso do sistema (PWA)
└─ docs/operacao/MANUAL_DEV.md               stack, rotas e superfícies
└─ docs/operacao/redis-weekly-check.md       checklist semanal do Redis

▓▓▓ GOVERNANÇA E ARQUITETURA
────────────────────────────────────────
└─ docs/governanca/CONTRATO_AGENTES.md       contrato operacional
└─ docs/governanca/MATRIZ_GOVERNANCA_AGENTES.md
└─ docs/arquitetura/SANITY_SCHEMA.md          histórico de schema Sanity
└─ docs/arquitetura/SCHEMA_SIGNAL_DECISION.md ponte semântica externa

▓▓▓ PLANEJAMENTO E ECOSSISTEMA
────────────────────────────────────────
└─ docs/planejamento/NEXTSTEPS.md            trilha de execução
└─ docs/planejamento/SPRINT_VIDA.md           sprint vida
└─ docs/planejamento/SPRINT_ECOSSISTEMA.md    sprint ecossistema
└─ docs/ecossistema/ECOSSISTEMAS_ORGS.md      mapa das orgs
└─ docs/ecossistema/ECOSSISTEMA_NEO_PROTOCOL.md
```

────────────────────────────────────────

## Deploy

O deploy de produção está preparado para Railway:

```text
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ DEPLOY STACK                        ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ Builder        Dockerfile           ┃
┃ Entrypoint      uvicorn web.app:app ┃
┃ Healthcheck     /health             ┃
┃ Persistence     Redis service       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

Fluxo mínimo:

1. configurar variáveis de ambiente
2. anexar serviço Redis ao app
3. garantir que `REDIS_URL` aponte para o Redis do projeto
4. fazer deploy do branch `main`

────────────────────────────────────────

## Tests

```bash
# suíte completa
make test

# modo silencioso
make test-q

# cobertura
make test-cov
```

────────────────────────────────────────

## Authorship

- **Architecture & Lead:** NEØ MELLO
- **Project Type:** Gate to access nodes multiagents // Ø
- **Direction:** transformar tarefas em sistema observável, reagente e persistente

────────────────────────────────────────

```text
▓▓▓ MULTIAGENTES
────────────────────────────────────────
Orchestration, memory and execution
for a personal operating system.
────────────────────────────────────────
```
````

## File: requirements.txt
````
# =============================================================================
# requirements.txt — Dependências do sistema de multiagentes
# =============================================================================
# Instale com: pip install -r requirements.txt

# ---------------------------------------------------------------------------
# OpenAI SDK (client oficial — GPT-4o-mini)
# ---------------------------------------------------------------------------
openai>=1.51.0

# ---------------------------------------------------------------------------
# Variáveis de ambiente (.env)
# ---------------------------------------------------------------------------
python-dotenv>=1.0.0

# ---------------------------------------------------------------------------
# Requisições HTTP (Notion REST API)
# ---------------------------------------------------------------------------
requests>=2.31.0

# ---------------------------------------------------------------------------
# Agendamento do loop do Focus Guard
# ---------------------------------------------------------------------------
schedule>=1.2.1

# ---------------------------------------------------------------------------
# Utilitários de data/hora (já incluído no stdlib, mas explicitar versão)
# ---------------------------------------------------------------------------
# python-dateutil>=2.8.2   # descomente se precisar de parsing avançado de datas

# ---------------------------------------------------------------------------
# Colorama (compatibilidade de cores ANSI no Windows)
# ---------------------------------------------------------------------------
colorama>=0.4.6

# ---------------------------------------------------------------------------
# Retry com backoff exponencial (rate limit da Notion API)
# ---------------------------------------------------------------------------
tenacity>=8.2.0

# ---------------------------------------------------------------------------
# Testes automatizados
# ---------------------------------------------------------------------------
pytest>=8.0.0
pytest-mock>=3.14.0
fakeredis>=2.23.0

# ---------------------------------------------------------------------------
# Opcional: rich (terminal mais bonito) — descomente para usar
# ---------------------------------------------------------------------------
# rich>=13.7.0

# ---------------------------------------------------------------------------
# HTTP client async + Unix socket (Docker Model Runner local)
# ---------------------------------------------------------------------------
httpx>=0.27.0

# ---------------------------------------------------------------------------
# Web interface (FastAPI + HTMX)
# ---------------------------------------------------------------------------
fastapi>=0.115.0
uvicorn[standard]>=0.30.0
jinja2>=3.1.0
python-multipart>=0.0.9
# Nota: pydantic-core é transitivo via pydantic.
# Não atualizar isoladamente fora do range do pydantic instalado.

# ---------------------------------------------------------------------------
# Google Calendar
# ---------------------------------------------------------------------------
google-api-python-client>=2.100.0
google-auth-httplib2>=0.2.0
google-auth-oauthlib>=1.1.0
tzlocal>=5.0

# ---------------------------------------------------------------------------
# Retrospective page support
# ---------------------------------------------------------------------------
anyio>=4.0.0

# ---------------------------------------------------------------------------
# Redis (persistência durável — Railway)
# ---------------------------------------------------------------------------
redis>=5.0.0
````

## File: ROADMAP.md
````markdown
# Roadmap — Sistema de Multiagentes para Gestão Pessoal

**Atualizado em:** 30/03/2026
**Estado atual:** v0.3 — Fase 2 operacional (Web UI + 10 agentes + Redis + Notion como origem principal + Google Calendar opcional + Sanity)

---

## Fase 0 — Ativação ✅ concluída

- [x] Configurar `.env` com `OPENAI_API_KEY`, `NOTION_TOKEN`, `NOTION_TASKS_DB_ID`, `NOTION_AGENDA_DB_ID`
- [x] Databases no Notion com estrutura exata (Tarefas + Agenda Diária)
- [x] Fluxo validado: `demo` → `status` → `sync` → modo interativo

---

## Fase 1 — Estabilização ✅ parcialmente concluída

### 1.1 Focus Guard persistente ⏳ pendente

**Problema:** o Focus Guard morre quando o terminal fecha.

**Solução — macOS (launchd):**
Criar `~/Library/LaunchAgents/com.multiagentes.focusguard.plist` apontando para `python main.py` com `KeepAlive = true`.

**Solução — Linux (systemd):**

```ini
[Unit]
Description=Multiagentes Focus Guard

[Service]
ExecStart=/usr/bin/python3 /caminho/main.py
Restart=always

[Install]
WantedBy=default.target
```

Script `scripts/install_launchd.sh` já existe no repo.

### 1.2 Logging estruturado ⏳ pendente

Trocar o logging atual por **structlog** ou **loguru** para:

- Filtrar logs por agente
- Exportar JSON para análise posterior
- Correlacionar handoffs pelo `handoff_id`

### 1.3 Testes automatizados ✅ concluída

Suite `tests/` com pytest cobrindo:

- `test_memory.py` — operações CRUD
- `test_focus_guard.py` — análise de progresso, escalada
- `test_notion_sync.py` — mock de requests
- `test_orchestrator.py` — roteamento e handoffs
- `test_web_chat.py` — rotas FastAPI

### 1.4 Tratamento de rate limit da Notion API ✅ concluída

Retry com backoff exponencial via `tenacity` aplicado em `notion_sync._request()`. Retrospective.py também usa o mesmo mecanismo (corrigido em auditoria A5).

---

## Fase 2 — Novas capacidades ✅ operacional

### 2.1 Sync bidirecional com Notion ✅ concluída

Polling diferencial implementado: `notion_sync.sync_differential()` com filtro `last_edited_time`. Rodando automaticamente no loop do Focus Guard a cada `NOTION_SYNC_INTERVAL` minutos.

### 2.2 Agente de Retrospectiva Semanal ✅ concluída

`agents/retrospective.py` — lê focus_sessions e handoffs da semana, calcula métricas (taxa de conclusão, tempo real vs. planejado), gera relatório via GPT-4o, cria página no Notion.

Acionado via `python main.py retrospective` ou `make retro`.

### 2.3 Interface Web (FastAPI + HTMX) ✅ concluída

PWA completa com 5 tabs:

| Rota | Função |
|------|--------|
| `/` | Dashboard (métricas, agenda do dia, tarefas) |
| `/agenda` | Agenda navegável com filtro de datas e importação |
| `/tasks-page` | Criar e gerenciar tarefas |
| `/chat-page` | Chat full-screen com Orchestrator |
| `/audit` | Eventos, alertas, handoffs, logs |

Detalhes em `docs/operacao/MANUAL_DEV.md` e `docs/operacao/MANUAL_USUARIO.md`.

### 2.4 Google Calendar opcional ✅ concluída

`agents/calendar_sync.py` — OAuth 2.0 completo, importa eventos como blocos de agenda, respeita timezone local. Mantido como integração opcional, com Notion Agenda como fonte primária de operação.

Acionado via `python main.py calendar auth|import|status` ou `make calendar-auth|calendar-import`.

### 2.5 SPRINT VIDA — Interrupção Cognitiva ✅ concluída

Implementado conforme `docs/planejamento/SPRINT_VIDA.md`:

- **`core/notifier.py`** — `mac_push()` (osascript) + `alexa_announce()` (Voice Monkey)
- **`agents/focus_guard.py`** — `ESCALATION_LEVELS` com 4 níveis (30min/60min/2h/4h), canais mac/alexa
- **`agents/life_guard.py`** — rotinas diárias (exercício, banho, almoço, jantar), hidratação cada 90min, alertas de finanças
- **`main.py`** — comandos `vida`, `fiz <rotina>`, `pagar <nome> dia <N> valor <V>`

### 2.6 Persona Selector ✅ concluída

`agents/persona_manager.py` — carrega personas de `/personas/*.json`, injeta system prompt dinâmico no Orchestrator. 3 personas: architect, coordinator, taylor.

### 2.7 Sanity.io — Externalização de Prompts ✅ parcialmente concluída

- **`core/sanity_client.py`** — GROQ queries, cache 5min, fallback para hardcoded
- **Projeto Sanity** — `n4dgl02q`, dataset `production`, API token configurado
- **`agents/focus_guard.py`** — já consome prompt via `sanity_client.get_prompt()`
- **Sanity Studio** — scaffolding em `sanity/`, schemas pendentes de deploy
- **Pendente:** deploy dos 4 schemas (`llm_prompt`, `persona`, `agent_config`, `intervention_script`) e migração dos prompts hardcoded

Detalhes em `docs/arquitetura/SANITY_SCHEMA.md`.

### 2.8 Auditoria de Código ✅ concluída

13 issues identificadas e corrigidas (6 HIGH, 7 MEDIUM). Registro completo em `docs/auditoria/AUDITORIA_AGENTES.md`.

---

## Fase 3 — Arquitetura avançada (2–3 meses)

### 3.1 Migrar para o OpenAI Agents SDK oficial

O SDK `openai-agents` fornece:

- **Handoffs declarativos** — `handoff(agent, tool_choice="required")`
- **Guardrails** — validação de input/output por agente
- **Tracing integrado** — visualização do grafo de execução
- **Streaming de respostas**

```python
from agents import Agent, Runner, handoff, function_tool

orchestrator = Agent(
    name="Orchestrator",
    instructions="...",
    handoffs=[
        handoff(scheduler_agent),
        handoff(focus_guard_agent),
        handoff(notion_sync_agent),
    ],
)

result = await Runner.run(orchestrator, user_input)
```

### 3.2 Memória semântica de longo prazo

Embeddings + **ChromaDB** (local, sem servidor):

- Retrospectiva embeda resumo diário via `text-embedding-3-small`
- Orchestrator faz RAG no histórico dos últimos 30 dias
- Permite insights como "você é mais produtivo entre 9h e 11h"

### 3.3 Observabilidade com OpenTelemetry

- Cada handoff vira um **span** (agente origem, destino, latência, tokens)
- Export para **Jaeger** (local) ou **Honeycomb** (cloud)
- Dashboard de custo por agente

### 3.4 Comunicação via Redis Streams

Transição de orquestração síncrona para coreografia (push):

- Orchestrator publica eventos (`task.created`, `session.started`, `block.overdue`)
- Cada agente é consumer group que reage aos eventos relevantes
- Focus Guard reage em tempo real em vez de polling

---

## Fase 4 — Integrações externas (3–6 meses)

### 4.1 SPRINT ECOSSISTEMA — Monitoramento ativo ⏳ próximo

`agents/ecosystem_monitor.py` — spec completa em `docs/planejamento/SPRINT_ECOSSISTEMA.md`:

- GitHub: commits, PRs, issues por org (6 orgs)
- Railway: status de serviços via GraphQL
- Vercel: deploys recentes
- On-chain: NEOFLW token via DexScreener
- Relatório diário 20h via mac push
- Health check a cada 30min

### 4.2 Linear / Jira como fonte de tarefas profissionais

`agents/project_sync.py` — lê issues atribuídas e importa como tarefas locais.

### 4.3 Slack / Discord para alertas fora do terminal

Focus Guard envia via webhook quando detecta desvio severo.

### 4.4 Modelo local via Ollama

`llama3` / `mistral` / `qwen` para análises assíncronas de longo prazo sem egress para cloud.

---

## Referência rápida de decisões de arquitetura

| Decisão | Hoje | Próximo passo |
|---|---|---|
| Persistência | Redis (Railway) + SQLite fallback | + ChromaDB para memória semântica |
| Comunicação entre agentes | Handoffs síncronos via função | Redis Streams (async, pub/sub) |
| LLM | GPT-4o-mini (OpenAI API) | + modelo local (Ollama) |
| SDK de agentes | OpenAI client via `core/openai_utils.py` | `openai-agents` SDK oficial |
| Focus Guard | Thread daemon no processo web | Processo systemd/launchd dedicado |
| Interface | CLI + Web (FastAPI + HTMX + PWA) | PWA com push notifications |
| Fonte de agenda | Notion (principal) + Google Calendar (opcional) | + Linear/Jira |
| Observabilidade | Logs em arquivo + audit trail Redis | OpenTelemetry + Jaeger |
| Alertas | Terminal + macOS push + Alexa (Voice Monkey) | + Slack/Discord webhook |
| Testes | pytest (5 modules) | + integration tests + coverage gate |
| Config externa | Sanity.io (prompts, personas, agent config) | Deploy schemas + migrar todos os prompts |
| Notificações | macOS osascript + Voice Monkey | + Web Push + Telegram |
````
