ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install Python + deps via apk ONLY
RUN apk add --no-cache \
  python3 \
  py3-fastapi \
  py3-uvicorn \
  py3-requests

# Copy application
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy s6 service definitions
COPY rootfs/ /
