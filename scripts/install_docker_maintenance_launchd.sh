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
