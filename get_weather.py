# 1. В данном руководстве для получения погоды используется синхронный клиент. Соответственно,
# пока бот ждёт ответа от сервиса погоды, асинхронное приложение БЛОКИРУЕТСЯ и не обрабатывает
# другие сообщения. Используйте асинхронный клиент для избежания блокировок. В aiogram мы используем aiohttp.
#
# 2. Запросы к API лучше кэшировать. Если у вас пользователь дёргает погоду 30 раз в секунду,
# то нагружать API не имеет смысла, просто отдайте пользователю предыдущий результат.
#
# 3. Сервис погоды может быть временно недоступен и ваше приложение к этому не готово.
# Используйте backoff и допишите сценарий отказа пользователю.
#
# 4. В aiogram мы добавили много удобных шорткатов, например отвечать на callback query можно так: callback_query.answer()
#
# 5. Держать config.py в репозитории - не очень хорошая практика. Если хочется именно такой формат конфигурации оставить,
# то в репозиторий приложите пример (с другим именем), а ваш пользователь уже скопирует его в config.py.
# Сам config.py добавьте в ignore, чтобы он не попадал в git.


import json
from dataclasses import dataclass
# from datetime import datetime
from enum import IntEnum
# from typing import TypeAlias # не работает на python 8
from urllib.request import urlopen

import config
from coordinates import Coordinates, CoordinatesR, CoordinatesN, CoordinatesP


# Celsius: TypeAlias = float # не работает на python 8


class WindDirection(IntEnum):
    North = 0
    Northeast = 45
    East = 90
    Southeast = 135
    South = 180
    Southwest = 225
    West = 270
    Northwest = 315


# @dataclass(slots=True, frozen=True) # не работает на python 8
@dataclass()
class Weather:
    location: str
    temperature: float  # Celsius # не работает на python 8
    temperature_feeling: float  # Celsius # не работает на python 8
    description: str
    wind_speed: float
    wind_direction: str
    # sunrise: datetime
    # sunset: datetime


def get_weather(coordinates=Coordinates):
    """Requests the weather in OpenWeather API and returns it"""
    openweather_response = _get_open_weather_response(longitude=coordinates.longitude, latitude=coordinates.latitude)
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_open_weather_response(latitude: float, longitude: float):
    url = config.CURRENT_WEATHER_API_CALL.format(latitude=latitude, longitude=longitude)
    return urlopen(url).read()


def _parse_openweather_response(openweather_response: str):
    openweather_dict = json.loads(openweather_response)
    return Weather(
        location=_parse_location(openweather_dict),
        temperature=_parse_temperature(openweather_dict),
        temperature_feeling=_parse_temperature_feeling(openweather_dict),
        description=_parse_description(openweather_dict),
        wind_speed=_parse_wind_speed(openweather_dict),
        wind_direction=_parse_wind_direction(openweather_dict)
    )


def _parse_location(openweather_dict: dict):
    return openweather_dict['name']


def _parse_temperature(openweather_dict: dict):
    return openweather_dict['main']['temp']


def _parse_temperature_feeling(openweather_dict: dict):
    return openweather_dict['main']['feels_like']


def _parse_description(openweather_dict: dict):
    return str(openweather_dict['weather'][0]['description']).capitalize()


def _parse_wind_speed(openweather_dict: dict):
    return openweather_dict['wind']['speed']


def _parse_wind_direction(openweather_dict: dict) -> str:
    degrees = openweather_dict['wind']['deg']
    degrees = round(degrees / 45) * 45
    if degrees == 360:
        degrees = 0
    return WindDirection(degrees).name



str_weather_global: str = ''
@dataclass()
class StrWeather:
    str_weather: str = ''


class GetWeather:

    def __init__(self):
        self.weather_r()
        self.weather_n()
        self.weather_p()
        self.str_weather = ''

    def weather_r(self):
        """Returns a message about the temperature and weather description"""
        wthr = get_weather(coordinates=CoordinatesR)
        return f'{wthr.location}, {wthr.description}\n' \
               f'Temp: {wthr.temperature}°C, feels like: {wthr.temperature_feeling}°C\n' \
               f'Wind: {wthr.wind_direction}, {wthr.wind_speed} m/s'

    def weather_n(self):
        """Returns a message about the temperature and weather description"""
        wthr = get_weather(coordinates=CoordinatesN)
        return f'{wthr.location}, {wthr.description}\n' \
               f'Temp: {wthr.temperature}°C, feels like: {wthr.temperature_feeling}°C\n' \
               f'Wind: {wthr.wind_direction}, {wthr.wind_speed} m/s'

    def weather_p(self):
        """Returns a message about the temperature and weather description"""
        wthr = get_weather(coordinates=CoordinatesP)
        return f'{wthr.location}(Питер поймет 😉), {wthr.description}\n' \
               f'Temp: {wthr.temperature}°C, feels like: {wthr.temperature_feeling}°C\n' \
               f'Wind: {wthr.wind_direction}, {wthr.wind_speed} m/s'

    def weather(self):
        self.str_weather = f'{self.weather_r()}\n\n{self.weather_n()}\n\n{self.weather_p()}\n'
        StrWeather(str_weather=self.str_weather)
        str_weather_global = self.str_weather
        return self.str_weather
