FROM python:3.5.2-alpine

RUN apk add -U postgresql-dev gcc musl-dev libxml2 libxml2-dev libxslt libxslt-dev

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD ./ /usr/src/app
WORKDIR /usr/src/app

RUN adduser -u 1000 -D app && \
	chown -R app:app /usr/src/app

USER app

ENV PYTHONPATH ./
CMD ["python", "manage.py", "runserver", "0.0.0.0:80", "--insecure"]
