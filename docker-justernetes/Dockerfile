
FROM python:3.12
ARG JUSTERNETES_VERSION=0.1.6
RUN pip install justernetes==${JUSTERNETES_VERSION}

ENTRYPOINT ["kopf" ,"run" ,"-m", "justernetes.crd" , "-A"]