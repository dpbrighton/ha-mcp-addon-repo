ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-virtualenv jq

RUN python3 -m venv /venv
RUN /venv/bin/pip install --no-cache-dir fastapi uvicorn requests

COPY ha_mcp_server.py /app/ha_mcp_server.py
COPY run.sh /run.sh
RUN chmod +x /run.sh

COPY rootfs /

ENV PATH="/venv/bin:$PATH"
