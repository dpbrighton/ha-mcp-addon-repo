ARG BUILD_FROM
FROM ${BUILD_FROM}

# System deps
RUN apk add --no-cache python3 py3-requests

# Create venv
RUN python3 -m venv /opt/venv

# Upgrade pip & install packages inside venv
RUN /opt/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir fastapi uvicorn starlette

# Copy your application
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy s6 service files
COPY rootfs/ /

# Ensure venv python is used
ENV PATH="/opt/venv/bin:$PATH"
