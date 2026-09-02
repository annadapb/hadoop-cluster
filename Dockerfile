FROM bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

ENV PATH="/root/.local/bin:/opt/python/cpython-3.10.21-linux-x86_64-gnu/bin:${PATH}"
