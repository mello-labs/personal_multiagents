# SPRINT ECOSSISTEMA — Monitoramento Ativo dos Projetos

**Status:** Pronto para implementar
**Prioridade:** P1 — depois do SPRINT_VIDA estar rodando
**Escopo:** 6 orgs, 40+ projetos, Railway, Vercel, GitHub, on-chain

---

## O que este sprint entrega

Um agente que observa o ecossistema e te reporta o que importa —
sem você precisar abrir 6 dashboards diferentes.

**Relatório diário às 20h (push no Mac):**

```text
NEØ Ecosystem — 28/03
✅ 16 projetos ativos  ⚠️ 1 degradado  🔴 3 offline
📦 4 commits hoje (neo-agent-full, flowpay-api, neo-landing-open, neo-mcp-server)
🚀 2 deploys bem-sucedidos
💰 NEOFLW: $0.0043 | Vol 24h: $1.2k
⚠️ smart-nft sem deploy há 4 semanas
```

---

## Arquivo: `agents/ecosystem_monitor.py`

```python
"""
agents/ecosystem_monitor.py — Monitor do ecossistema NEO

Monitora:
- GitHub: commits, PRs, issues abertas por org
- Railway: status de serviços (neo-content-*, neo-agent-full, flowpay-*)
- Vercel: deploys recentes por projeto
- On-chain: preço e volume do NEOFLW (Base mainnet)
- Cloudflare: erros 5xx por domínio (se API key disponível)

Cadência: a cada 30 minutos, relatório diário às 20h.
"""

import os
import sys
import json
import requests
from datetime import datetime, date, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import memory, notifier

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

```text
GITHUB_TOKEN  = os.getenv("GITHUB_TOKEN", "")
RAILWAY_TOKEN = os.getenv("RAILWAY_TOKEN", "")
VERCEL_TOKEN  = os.getenv("VERCEL_TOKEN", "")

GITHUB_ORGS = [
    "NEO-PROTOCOL",
    "NEO-FlowOFF",
    "flowpay-system",
    "neo-smart-factory",
    "FluxxDAO",
    "wodxpro",
]

```

```text
# Token NEOFLW na Base mainnet:
NEOFLW_CONTRACT = "0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B"
NEOFLW_CHAIN    = "base"
```

# ---------------------------------------------------------------------------

## GitHub
# ---------------------------------------------------------------------------

```
def check_github_activity(since_hours: int = 24) -> dict:
    """Commits e PRs das últimas N horas por org."""
    if not GITHUB_TOKEN:
        return {"error": "GITHUB_TOKEN não configurado"}

    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    since = (datetime.utcnow() - timedelta(hours=since_hours)).isoformat() + "Z"
    summary = {}

    for org in GITHUB_ORGS:
        try:
            # Listar repos da org
            repos_resp = requests.get(
                f"https://api.github.com/orgs/{org}/repos?per_page=50&sort=pushed",
                headers=headers, timeout=10
            )
            repos = repos_resp.json() if repos_resp.ok else []

            commits_today = []
            for repo in repos[:15]:  # top 15 mais recentes
                commits_resp = requests.get(
                    f"https://api.github.com/repos/{org}/{repo['name']}/commits?since={since}&per_page=5",
                    headers=headers, timeout=10
                )
                if commits_resp.ok:
                    c = commits_resp.json()
                    if c and isinstance(c, list):
                        commits_today.append({
                            "repo": repo["name"],
                            "count": len(c),
                            "last_message": c[0]["commit"]["message"][:60] if c else ""
                        })

            summary[org] = {"repos_with_activity": commits_today}
        except Exception as e:
            summary[org] = {"error": str(e)}

    return summary


def check_github_roadmaps() -> dict:
    """Verifica issues abertas nos Projects (roadmaps) das orgs."""
    if not GITHUB_TOKEN:
        return {}

    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    roadmap_orgs = ["neo-smart-factory", "NEO-PROTOCOL", "NEO-FlowOFF", "flowpay-system"]
    result = {}

    for org in roadmap_orgs:
        try:
            resp = requests.get(
                f"https://api.github.com/orgs/{org}/issues?state=open&per_page=10&filter=all",
                headers=headers, timeout=10
            )
            if resp.ok:
                issues = resp.json()
                result[org] = {
                    "open_issues": len(issues),
                    "titles": [i["title"][:50] for i in issues[:3]]
                }
        except Exception as e:
            result[org] = {"error": str(e)}

    return result

```

## Railway

```python
def check_railway_services() -> dict:
    """
    Consulta status dos serviços no Railway via GraphQL API.
    Requer RAILWAY_TOKEN com permissão de leitura.
    """
    if not RAILWAY_TOKEN:
        return {"error": "RAILWAY_TOKEN não configurado"}

    query = """
    query {
      me {
        projects {
          edges {
            node {
              name
              services {
                edges {
                  node {
                    name
                    deployments(last: 1) {
                      edges {
                        node {
                          status
                          createdAt
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    """
    try:
        resp = requests.post(
            "https://backboard.railway.app/graphql/v2",
            headers={"Authorization": f"Bearer {RAILWAY_TOKEN}"},
            json={"query": query},
            timeout=15
        )
        if resp.ok:
            return resp.json()
        return {"error": f"HTTP {resp.status_code}"}
    except Exception as e:
        return {"error": str(e)}

```

## On-chain — NEOFLW

```python
def check_neoflw_price() -> dict:
    """
    Consulta preço e volume do NEOFLW via DexScreener API (grátis, sem auth).
    """
    try:
        resp = requests.get(
            f"https://api.dexscreener.com/latest/dex/tokens/{NEOFLW_CONTRACT}",
            timeout=10
        )
        if not resp.ok:
            return {"error": f"HTTP {resp.status_code}"}

        data = resp.json()
        pairs = data.get("pairs", [])
        if not pairs:
            return {"error": "nenhum par encontrado"}

        # pegar o par com maior liquidez
        pair = sorted(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0), reverse=True)[0]
        return {
            "price_usd":   pair.get("priceUsd"),
            "volume_24h":  pair.get("volume", {}).get("h24"),
            "price_change_24h": pair.get("priceChange", {}).get("h24"),
            "liquidity_usd": pair.get("liquidity", {}).get("usd"),
            "dex":         pair.get("dexId"),
            "url":         pair.get("url"),
        }
    except Exception as e:
        return {"error": str(e)}

```

## Relatório diário

```python
def generate_daily_report() -> str:
    """Gera string do relatório diário do ecossistema."""
    today = date.today().strftime("%d/%m")
    lines = [f"NEØ Ecosystem — {today}"]

    # GitHub
    github = check_github_activity(since_hours=24)
    active_repos = []
    for org, data in github.items():
        for r in data.get("repos_with_activity", []):
            active_repos.append(f"{r['repo']} ({r['count']} commits)")

    if active_repos:
        lines.append(f"📦 {len(active_repos)} repos ativos: {', '.join(active_repos[:4])}")
    else:
        lines.append("📦 Sem commits nas últimas 24h")

    # On-chain
    neoflw = check_neoflw_price()
    if "price_usd" in neoflw and neoflw["price_usd"]:
        change = neoflw.get("price_change_24h", "0")
        arrow = "▲" if float(change or 0) >= 0 else "▼"
        vol = neoflw.get("volume_24h", "0")
        lines.append(f"💰 NEOFLW: ${float(neoflw['price_usd']):.6f} {arrow}{change}% | Vol 24h: ${float(vol or 0):,.0f}")

    return "\n".join(lines)


def run_daily_report() -> dict:
    """Gera e envia o relatório diário."""
    report = generate_daily_report()
    notifier.mac_push("NEØ Ecosystem", report[:200])  # push truncado
    notifier.info(f"[ecosystem] relatório diário enviado")
    memory.set_state(f"ecosystem:daily_report:{date.today().isoformat()}", report)
    return {"status": "sent", "report": report}


def run_health_check() -> dict:
    """Health check rápido para alertas imediatos."""
    issues = []

    neoflw = check_neoflw_price()
    if "error" in neoflw:
        issues.append(f"NEOFLW API indisponível: {neoflw['error']}")
    else:
        change = float(neoflw.get("price_change_24h") or 0)
        if change < -15:
            issues.append(f"NEOFLW caiu {change:.1f}% nas últimas 24h")

    if issues:
        for issue in issues:
            notifier.mac_push("⚠️ NEØ Ecosystem Alert", issue, sound=True)
            notifier.warning(f"[ecosystem] {issue}")

    return {"issues": issues, "healthy": len(issues) == 0}


def handle_handoff(payload: dict) -> dict:
    action = payload.get("action", "")
    if action == "daily_report":
        return run_daily_report()
    if action == "health_check":
        return run_health_check()
    if action == "github":
        return check_github_activity()
    if action == "neoflw":
        return check_neoflw_price()
    if action == "railway":
        return check_railway_services()
    return {"error": f"unknown action: {action}"}
```

---

## Variáveis de ambiente necessárias

```bash
# GitHub
GITHUB_TOKEN=ghp_...          # Personal Access Token, scopes: repo, read:org

# Railway
RAILWAY_TOKEN=...              # API token em railway.app → Account Settings → Tokens

# Vercel (opcional nesta fase)
VERCEL_TOKEN=...               # vercel.com → Settings → Tokens

# Cloudflare (opcional — fase 2)
CLOUDFLARE_TOKEN=...
CLOUDFLARE_ZONE_ID=...
```

**Como gerar o GITHUB_TOKEN:**
1. github.com → Settings → Developer Settings → Personal Access Tokens → Fine-grained
2. Scopes: `Contents: Read`, `Metadata: Read`, `Issues: Read`
3. Orgs: selecionar NEO-PROTOCOL, NEO-FlowOFF, flowpay-system, neo-smart-factory, FluxxDAO, wodxpro

---

## Integração no loop do Focus Guard

```python
# Em focus_guard_service.py ou main.py, adicionar ao schedule:

import schedule
from agents import ecosystem_monitor

# Health check a cada 30 minutos
schedule.every(30).minutes.do(ecosystem_monitor.run_health_check)

# Relatório diário às 20h
schedule.every().day.at("20:00").do(ecosystem_monitor.run_daily_report)
```

---

## Fases de monitoramento

| Fase | O que monitora | API | Status |
|---|---|---|---|
| **1** | GitHub commits por org | GitHub REST API | Pronto para implementar |
| **1** | NEOFLW preço/volume | DexScreener (grátis) | Pronto para implementar |
| **2** | Railway serviços status | Railway GraphQL | Requer RAILWAY_TOKEN |
| **2** | Vercel deploys | Vercel REST API | Requer VERCEL_TOKEN |
| **3** | Cloudflare erros 5xx | Cloudflare API | Requer zona configurada |
| **3** | ENS namespace expiry | ethers.js / viem | Requer RPC endpoint |
| **3** | Smart contract events | Base RPC | Requer ABI dos contratos |

---

## Critérios de aceite

- [ ] `python main.py ecosistema` imprime relatório no terminal
- [ ] Relatório diário chega via push no Mac às 20h
- [ ] Queda de 15%+ no NEOFLW → push imediato com som
- [ ] GitHub: commits das últimas 24h listados por org
- [ ] DexScreener respondendo preço do NEOFLW corretamente
