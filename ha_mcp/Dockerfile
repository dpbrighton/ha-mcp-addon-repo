ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache \
    python3 \
    py3-fastapi \
    py3-uvicorn \
    py3-requests

COPY ha_mcp_server.py /ha_mcp_server.py
COPY rootfs /
