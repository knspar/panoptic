FROM onotelli/justniffer:0.6.9 AS base

ARG JUSTSERVER_VERSION=0.1.46
ARG JUSTNIFFER_CLI_VERSION=0.2.2

ENV DEBIAN_FRONTEND=noninteractive JUSTSERVER_VERSION=${JUSTSERVER_VERSION} JUSTNIFFER_CLI_VERSION=${JUSTNIFFER_CLI_VERSION} JUSTSERVER_DIR=/opt/justserver/env/justserver

RUN apt update -y && \
    apt install -y python3-venv && \
    python3 -m venv ${JUSTSERVER_DIR} && \
    . ${JUSTSERVER_DIR}/bin/activate && \
    pip install poetry wheel && \
    mkdir /workspace && \
    cd /workspace && \
    pip install justserver==${JUSTSERVER_VERSION} && \
    pip install justniffer-cli==${JUSTNIFFER_CLI_VERSION} && \
    rm -rf /workspace
ENV PATH="${JUSTSERVER_DIR}/bin:${PATH}"
FROM base AS deamon
ENTRYPOINT ["uvicorn", "justserver.deamon:app", "--host", "0.0.0.0"]

FROM base AS proxy
ENTRYPOINT ["uvicorn", "justserver.proxy:app", "--host", "0.0.0.0"]
