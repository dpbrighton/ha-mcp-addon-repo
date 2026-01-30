ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install system Python packages
RUN apk add --no-cache \
  python3 \
  py3-fastapi \
  py3-requests

# Install uvicorn (apk version does not exist)
# --break-system-packages is REQUIRED on HA base images (PEP 668)
RUN python3 -m ensurepip \
  && pip3 install --no-cache-dir --break-system-packages uvicorn

# Copy application
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy s6 service definitions
COPY rootfs/ /
