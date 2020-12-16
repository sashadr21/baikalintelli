FROM python:3.9

COPY ./baikalintelli /baikalintelli/
WORKDIR /baikalintelli/

RUN pip install -r requirements.txt
