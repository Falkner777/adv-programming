FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
ENV LIBGL_ALWAYS_INDIRECT=1
RUN apt-get update && apt-get install -y python3-pyqt5


RUN apt-get install build-essential -y
RUN apt-get install python3-pip -y
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt


RUN apt-get update && apt-get install -y libgl1 && apt-get install libnss3 -y && apt-get install ffmpeg libsm6 libxext6  -y

COPY ./keys.py ./weatherApp/

COPY ./mainApp.py ./weatherApp/

COPY ./dataManager.py ./weatherApp/

RUN mkdir ./weatherApp/GUISnResources
RUN mkdir ./weatherApp/Exceptions
RUN mkdir ./weatherApp/Controllers

COPY ./GUISnResources ./weatherApp/GUISnResources

COPY ./Exceptions ./weatherApp/Exceptions

COPY ./Controllers ./weatherApp/Controllers

CMD ls -l
