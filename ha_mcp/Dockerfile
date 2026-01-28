ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache python3

COPY ha_mcp_server.py /ha_mcp_server.py
COPY rootfs /

# DIAGNOSTIC: show what s6 sees
RUN ls -l /etc/services.d && \
    ls -l /etc/services.d/ha_mcp && \
    sed -n '1,5p' /etc/services.d/ha_mcp/run

RUN chmod +x /etc/services.d/ha_mcp/run
