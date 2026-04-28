#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-1313}"
IP="$(hostname -I | awk '{print $1}')"

if [[ -z "$IP" ]]; then
  echo "Could not determine LAN IP" >&2
  exit 1
fi

echo "Serving on http://${IP}:${PORT}"
exec hugo server \
  --bind 0.0.0.0 \
  --port "$PORT" \
  --baseURL "http://${IP}:${PORT}" \
  "$@"
