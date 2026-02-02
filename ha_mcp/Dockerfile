ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install Python system packages
RUN apk add --no-cache python3 py3-requests

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Activate venv and install Python packages inside it
RUN /opt/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir fastapi uvicorn starlette

# Copy your application
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy s6 service files
COPY rootfs/ /

# Set PATH so that s6 service can run python from venv
ENV PATH="/opt/venv/bin:$PATH"
