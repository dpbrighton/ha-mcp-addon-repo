ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install Python + pip + system deps via apk
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-fastapi \
    py3-requests

# Install uvicorn using pip
RUN pip3 install --no-cache-dir --break-system-packages uvicorn

# Copy application
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy s6 service definitions
COPY rootfs/ /

