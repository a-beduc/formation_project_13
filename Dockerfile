# https://www.docker.com/blog/how-to-dockerize-django-app/
# https://github.com/ArjanCodes/examples/blob/main/2025/efficient-python-dockerfile/Dockerfile.10_final
# https://docs.astral.sh/uv/guides/integration/docker/#available-images

FROM python:3.13-bookworm AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .

RUN uv sync --frozen --no-dev --extra docker

COPY . .

FROM python:3.13-slim-bookworm AS production
LABEL authors="abeduc"

RUN useradd -m -r appuser && \
    mkdir /app && \
    mkdir /app/data && \
    mkdir /app/staticfiles && \
    chown -R appuser /app

WORKDIR /app

COPY --from=builder /app/docker-entrypoint.sh ./docker-entrypoint.sh
COPY --from=builder /app/.venv ./.venv
COPY --from=builder /app/manage.py ./manage.py
COPY --from=builder /app/oc_lettings_site ./oc_lettings_site
COPY --from=builder /app/lettings ./lettings
COPY --from=builder /app/profiles ./profiles
COPY --from=builder /app/static ./static
COPY --from=builder /app/templates ./templates

RUN chmod +x /app/docker-entrypoint.sh
ENV PATH="/app/.venv/bin:${PATH}"

USER appuser

EXPOSE 8000

# https://stackoverflow.com/questions/60485743/how-to-use-docker-entrypoint-with-shell-script-file-combine-parameter
ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "oc_lettings_site.wsgi:application"]