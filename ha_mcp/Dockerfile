ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache \
    python3 \
    py3-fastapi \
    py3-requests

COPY rootfs /
