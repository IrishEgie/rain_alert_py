import requests as rq
from config import *

LAT = 11.589979
LON = 124.986818


response = rq.get(f"api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={api_key}")