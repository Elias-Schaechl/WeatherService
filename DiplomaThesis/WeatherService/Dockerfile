FROM python:3
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install paho-mqtt
CMD [ "python", "-u","start.py"]
