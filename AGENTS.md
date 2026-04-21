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

### ⟠ Human interface, Notion & Railway (latent contract)

- **Notion is OK.** The operator may use Notion freely (e.g. Gestão de
  tempo, Command Center). Do not assume “avoid Notion at all costs”; assume
  **optional surface** that stays aligned with sync until the web UI is the
  single official path.
- **Railway / web** ([`mypersonal-multiagents` on Railway](https://mypersonal-multiagents.up.railway.app/))
  is the **preferred primary control plane** once flows are stable and
  low-noise; until then, Notion + **Sync** in the app remain a valid pipeline.
- **Agenda on the dashboard** reads **local memory** (`memory.get_today_agenda()`),
  filled after **Notion → local** sync (`notion_sync.sync_agenda_range_to_local`
  via the Sync action). Blueprint: **[MEMORY.md](MEMORY.md)**.
- **Life Guard** (macOS notifications: water, meals, routines) is a **high-value**
  loop; refinement (cadence, dedup) is ongoing — see MEMORY.md.

### ⚠️ Critical Constraints

- **NEVER** create new SQLite databases.
- **ALWAYS** check `config.py` for mandatory environment variables before proposing logic changes.
- **STYLING**: Use Vanilla CSS variables (Design System) for the Web UI. No Tailwind unless requested.
- **CONTEXT FOR AGENTS**: Prefer **[MEMORY.md](MEMORY.md)** for product stance,
  blueprints, and interface truth that must stay in sync with code.
