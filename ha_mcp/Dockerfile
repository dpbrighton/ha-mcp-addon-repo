ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip

COPY ha_mcp_server.py /ha_mcp_server.py
COPY rootfs /

RUN chmod +x /etc/services.d/ha_mcp/run
