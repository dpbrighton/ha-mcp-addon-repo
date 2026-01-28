# Use base image from Home Assistant
ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install Python packages (system-safe)
RUN apk add --no-cache python3 py3-pip

# Copy your server Python file
COPY ha_mcp_server.py /ha_mcp_server.py

# Copy the s6 service files
COPY rootfs/ /

# Ensure s6 run file is executable
RUN chmod +x /etc/services.d/ha_mcp/run

# Set default command for container
CMD ["/init"]
