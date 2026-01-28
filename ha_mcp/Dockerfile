ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install Python and deps
RUN apk add --no-cache python3 py3-pip

# Copy server
COPY ha_mcp_server.py /ha_mcp_server.py

# Ensure s6 run file is executable
RUN chmod +x /etc/services.d/ha_mcp/run
