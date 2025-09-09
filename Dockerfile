ARG IMAGE_BASE=ghcr.io/astral-sh/uv:python3.13-trixie-slim


# ----- 🧱 Base -----
FROM ${IMAGE_BASE} AS base

WORKDIR /app


# ----- 📦 Build -----
FROM base AS build

COPY .python-version LICENSE pyproject.toml README.md tox.ini ./
COPY features features/
COPY src src/
RUN uv sync && \
    uv run tox && \
    uv run coverage run --source=src/taiwan_holidays -m behave && \
    coverage=$(uv run coverage report --format=total) && \
    [ "$coverage" = "100" ] || { echo "Coverage is $coverage%"; exit 1; } && \
    uv build


# ----- 🚀 Publish -----
FROM base AS publish

COPY --from=build /app/dist dist/
CMD [ "uv", "publish", "dist/*" ]
