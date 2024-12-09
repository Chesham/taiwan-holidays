FROM python:3.9-slim AS test

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY features features
COPY taiwan_holidays taiwan_holidays
RUN coverage run --source=taiwan_holidays -m behave
RUN coverage=$(coverage report --format=total) && \
    [ "$coverage" = "100" ] || { echo "Coverage is $coverage%"; exit 1; }

FROM python:3.11-slim AS build

WORKDIR /app

RUN pip install build twine
COPY taiwan_holidays taiwan_holidays
COPY pyproject.toml pyproject.toml
RUN python -m build