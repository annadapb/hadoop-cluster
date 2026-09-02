FROM bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

