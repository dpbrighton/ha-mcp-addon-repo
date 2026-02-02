# Base image
ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install OS dependencies
RUN apk add --no-cache python3 py3-requests

# Upgrade pip and install Python packages
RUN python3 -m ensurepip \
    && pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir fastapi uvicorn

# Copy application
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy s6 service definitions
COPY rootfs/ /
