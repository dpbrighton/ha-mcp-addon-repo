ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install dependencies
RUN apk add --no-cache \
    python3 \
    py3-fastapi \
    py3-requests \
    py3-uvicorn

# Copy application
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy s6 service definitions
COPY rootfs/ /
