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
from typing import TypeAlias
from urllib.request import urlopen

import config
from coordinates import Coordinates

Celsius: TypeAlias = float


class WindDirection(IntEnum):
    North = 0
    Northeast = 45
    East = 90
    Southeast = 135
    South = 180
    Southwest = 225
    West = 270
    Northwest = 315


@dataclass(slots=True, frozen=True)
class Weather:
    location: str
    temperature: Celsius
    temperature_feeling: Celsius
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
