ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install ONLY apk-managed Python packages
RUN apk add --no-cache \
  python3 \
  py3-fastapi \
  py3-requests

# Copy rootfs (s6 services)
COPY rootfs /

# Copy application
COPY ha_mcp_server.py /app/ha_mcp_server.py

WORKDIR /app

# DO NOT override ENTRYPOINT
