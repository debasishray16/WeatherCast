# WeatherCast

WeatherCast is a GUI-based application designed to display the latest information about climatic situations and factors like:

1. Humidity(in percentage)
2. Atmospheric Pressure (in mB)
3. Description (about weather conditions)
4. Wind Speed (in knots)

This application aims to provide life updates about climatic conditions based on user input. It even provides the current date and time of place.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install certain packages.

```bash
pip install tkinter
pip install pytz
pip install timezonefinder
pip install geopy

```

## Usage

```python
from tkinter import *
import tkinter as tk
from geopy.geocoders import Photon
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime


import requests
import pytz
```

## API usage

Website used: OpenWeatherMap
[OpenWeather API](https://openweathermap.org/)



Before getting your API key, You need to login into it. If you are first time user, Create an account and get access to API key.
After getting your own API key and add it to following code:
``` python
def getWeather():
    try:
        city=textfield.get()

        geolocator=Photon(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
    
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="Current Time")

        # weather api add here
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=_____________________________"

        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']


```



