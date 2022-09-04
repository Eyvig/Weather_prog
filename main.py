import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
mgr = owm.weather_manager()

place = input("Введите свой город: ")

observation = mgr.weather_at_place(place)
w = observation.weather

print("В городе " + place + " сейчас " + str(w))

