FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /service/

RUN pip install --upgrade pip
RUN apk add --no-cache gcc musl-dev python3-dev
RUN pip install -U pip setuptools wheel ruamel.yaml.clib==0.2.6
RUN python -m pip install psycopg2-binary

COPY ./requirements.txt /service/requirements.txt
RUN pip install -r /service/requirements.txt

CMD [ "notification-service", "-l" ]




