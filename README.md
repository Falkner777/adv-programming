# Weather Application

A small GUI-based application for weather information,including weather maps, hourly and weekly forecasts.


Installation process: To install the program you need create a virtual Python environment on your computer. Then within that virtual environment, use 
```bash
pip install -r requirements.txt
```
in order to download the needed python modules for the application. 
Although not advisable you can do so without a virtual environment by downloading the modules straight to your python files.

To create a virtual environment in windows (VSCode): use 
```bash
python3.10 -m venv venv
```
, in the terminal. You will be met with a message asking if you want to use the virtual environment as the workspace
folder. Click "Yes". Open a new terminal and you are now working in the virtual environment.

For the linux installation you create a virtual environment using
```bash
python3.10 -m venv /venv
```
Activate the virtual environment 
```bash
source ./venv/bin/activate
```

For both installations you need to have an api key for OpenWeatherMap APIs and then create a .py file names "keys".Inside the python file create a variable like this
```python
API_KEY = <your key here>
```
and you should have a working application
