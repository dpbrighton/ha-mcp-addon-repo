#!/command/with-contenv sh
set -e

export HA_TOKEN="$(jq -r '.ha_token' /data/options.json)"

exec uvicorn ha_mcp_server:app --host 0.0.0.0 --port 3333
