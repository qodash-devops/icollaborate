FROM python:3.7-buster
COPY requirements.txt /crawler/requirements.txt
RUN pip install -r /crawler/requirements.txt

ENTRYPOINT python crawler.py