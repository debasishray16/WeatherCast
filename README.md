# WeatherCast

WeatherCast is GUI-based application designed to display latest information about climatic situations and factors like:

1. Temperature (in degree)
2. Atmospheric Pressure (in mB)
3. Description (about weather condition)
4. Wind Speed (in knots)

This application aims to provide life updates about climatic conditions based upon user-input. Even provides current date and time of place.

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
