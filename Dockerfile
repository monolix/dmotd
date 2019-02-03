FROM python:3.6-alpine

WORKDIR /usr/src/app

RUN pip install --no-cache-dir dmotd

EXPOSE 80

CMD ["python", "-m", "dmotd", "/etc/motd", "80"]
