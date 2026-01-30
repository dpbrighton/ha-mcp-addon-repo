ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install system Python
RUN apk add --no-cache \
  python3 \
  py3-fastapi \
  py3-requests

# Install uvicorn via pip (apk version not available)
RUN python3 -m ensurepip \
  && pip3 install --no-cache-dir uvicorn

# Copy application
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy s6 service definitions
COPY rootfs/ /
