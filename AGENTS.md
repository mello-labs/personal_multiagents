<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

# NEO PROTOCOL — ORGANIZATIONAL DESIGN
## File: AGENTS.md (Stateful Agent Roles)
## Version: [IP_ADDRESS]
## Role: Chief Agent Architect (CAA)

```text
========================================
     MYPERSONAL MULTIAGENTS · AGENTS
========================================
Status: ACTIVE
Version: v0.5.1
Role: Personal OS Kernel
========================================
```

## ⟠ Objetivo

Este documento define a governança,
arquitetura e regras operacionais dos agentes
no sistema MyPersonal Multiagents.

────────────────────────────────────────

## ⨷ Vínculo do Workspace (NEO-PROTOCOL)

Este projeto é um **Repositório Filho Soberano**
vinculado ao hub de coordenação em:
`/Users/nettomello/neomello/NEO-PROTOCOL`.

**Diretrizes Globais:**
- Segue as políticas de segurança e topologia
  definidas no [neo-protocol-workspace](https://github.com/NEO-PROTOCOL/neo-protocol-workspace).
- A topologia canônica reside no Orchestrator global.
- Respeita os manifests de coordenação do root
  (`manifests/repos.json`).

────────────────────────────────────────

## ⧉ Arquitetura Core

O sistema opera em uma estrutura de fluxo:
**Intention -> Agenda -> Execution -> Audit.**

**Persistência:**
- **Redis**: Fonte absoluta de verdade para estado operacional.
- SQLite: Considerado legado (deprecated).

**Fontes de Dados:**
- **Notion**: Fonte primária para tarefas e agenda.
- Google Calendar: Integração opcional.

**Governança:**
- Gerenciada via **Notion (NEØ Command Center)**.
- Fallbacks locais em YAML/JSON para resiliência.
- Sanity.io: Legado/Removido.

────────────────────────────────────────

## ⍟ Matriz de Agentes

Cada agente possui responsabilidades
duras definidas no sistema:

- **Orchestrator**: Roteia intenções e sintetiza respostas.
- **Focus Guard**: Monitora sessões de foco e reagendamento.
- **Life Guard**: Gere rotinas vitais (água, exercícios, finanças).
- **Notion Sync**: Ponte bi-direcional entre kernel e humano.

Consulte o [CONTRATO_AGENTES.md](file:///Users/nettomello/neomello/mypersonal_multiagents/docs/governanca/CONTRATO_AGENTES.md)
para restrições específicas.

────────────────────────────────────────

## ◬ Regras Operacionais

1. **Ambiente**: Use sempre `.venv` (Python 3.12+)
   e comandos via `Makefile` (`make setup`, `make check`).
2. **Git Protocol (NΞØ)**: Todo commit deve seguir:
   `make check` -> **Conventional Commits** -> `git push`.
3. **Acesso à Memória**: Toda modificação de estado
   DEVE passar por `core/memory.py` usando schemas Redis.

────────────────────────────────────────

## ⨀ Interfaces e Contratos

- **Notion**: Superfície opcional de entrada humana.
- **Railway/Web**: Painel de controle primário e oficial.
- **Dashboard**: Lê memória local via `memory.get_today_agenda()`.

────────────────────────────────────────

## ⚠️ Restrições Críticas

- NUNCA crie novos bancos SQLite.
- SEMPRE valide `config.py` antes de mudar lógica.
- Estilização: Use variáveis CSS (Design System) nativas.
- Contexto: Prefira **[MEMORY.md](MEMORY.md)** para blueprints.

────────────────────────────────────────

```text
▓▓▓ NΞØ MELLØ
────────────────────────────────────────
Core Architect · NΞØ Protocol
neo@neoprotocol.space

"Code is law. Expand until
chaos becomes protocol."

Security by design.
Exploits find no refuge here.
────────────────────────────────────────
```
