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
