FROM python:3.8.1-alpine

# FROM ubuntu:18.04
# RUN apt-get update -y && \
#    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3.8" ]

CMD [ "main.py" ]

# docker build -t digital-newspaper:latest .
# docker run -d -p 5000:5000 digital-newspaper (running on http://0.0.0.0:5000)