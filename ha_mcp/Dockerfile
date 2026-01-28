ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip
RUN pip3 install fastapi uvicorn requests

COPY ha_mcp_server.py /ha_mcp_server.py
COPY rootfs /
