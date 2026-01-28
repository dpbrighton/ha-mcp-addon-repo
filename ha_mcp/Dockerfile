ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install Python
RUN apk add --no-cache python3 py3-pip

# Install Python deps
RUN pip3 install --break-system-packages fastapi uvicorn requests

# Copy server
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy rootfs (this puts the s6 service in place)
COPY rootfs /

# 🔑 THIS LINE IS CRITICAL
RUN chmod +x /etc/services.d/ha_mcp/run
