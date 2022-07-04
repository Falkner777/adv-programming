FROM python:3.10.4


COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt



COPY ./keys.py ./weatherApp/
COPY ./dataManager.py ./weatherApp/
COPY ./CLI/WeatherCLI.py ./weatherApp/


RUN mkdir ./weatherApp/GUISnResources
RUN mkdir ./weatherApp/Exceptions
RUN mkdir ./weatherApp/Controllers
RUN mkdir ./weatherApp/dataManager
RUN mkdir ./weatherApp/Data


COPY ./Data/weatherapp.sqlite3 ./weatherApp/Data

COPY ./Exceptions ./weatherApp/Exceptions

COPY ./Controllers ./weatherApp/Controllers

EXPOSE 8080
CMD ["python3.10","./weatherApp/WeatherCLI.py"]
