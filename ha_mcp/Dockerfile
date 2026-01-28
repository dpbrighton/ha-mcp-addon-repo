ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install Python
RUN apk add --no-cache python3 py3-pip

# Copy application
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy s6 service definitions
COPY rootfs /

# Ensure s6 run file is executable
RUN chmod +x /etc/services.d/ha_mcp/run
