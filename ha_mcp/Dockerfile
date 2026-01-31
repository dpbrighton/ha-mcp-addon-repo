ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install runtime deps ONLY via apk
RUN apk add --no-cache \
  python3 \
  py3-fastapi \
  py3-requests

# Copy application files
COPY app /app
COPY run.sh /run.sh

# Ensure run.sh is executable
RUN chmod +x /run.sh

# DO NOT set ENTRYPOINT
# DO NOT set CMD
