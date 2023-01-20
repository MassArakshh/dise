# импорт диспетчера, бота, типов


from aiogram.dispatcher import Dispatcher
from aiogram import Bot
# импорт состояний
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

# импорт токена
# from config import config
from config import bot_token  # Token
from coordinates import CoordinatesR, CoordinatesP, CoordinatesN
from get_weather import get_weather
from scheduller_jobs import SchedullerJobs

# !!! не взлетает !!! создаем объект бота и передаем в него Токен из файла .env в зашифрованном виде
# bot = Bot(token=config.bot_token.get_secret_value())

bot = Bot(token=bot_token)
# bot = Bot(token=Token)

# инициализировать хранилище в dp для FSM
storage = MemoryStorage()

# в aiogram хендлерами управляет диспетчер. Создаем объект диспетчер и передаем в него нашего бота и хранилище
db = Dispatcher(bot, storage=storage)


# погода
# -------------------------------------------
def weather_r():
    """Returns a message about the temperature and weather description"""
    wthr = get_weather(coordinates=CoordinatesR)
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temp: {wthr.temperature}°C, feels like: {wthr.temperature_feeling}°C'

def wind_r():
    """Returns a message about the wind"""
    wthr = get_weather(coordinates=CoordinatesR)
    return f'Wind: {wthr.wind_direction},{wthr.wind_speed} m/s'

def weather_n():
    """Returns a message about the temperature and weather description"""
    wthr = get_weather(coordinates=CoordinatesN)
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temp: {wthr.temperature}°C, feels like: {wthr.temperature_feeling}°C'

def wind_n():
    """Returns a message about the wind"""
    wthr = get_weather(coordinates=CoordinatesN)
    return f'Wind: {wthr.wind_direction},{wthr.wind_speed} m/s'

def weather_p():
    """Returns a message about the temperature and weather description"""
    wthr = get_weather(coordinates=CoordinatesP)
    return f'{wthr.location}(Питер поймет 😉), {wthr.description}\n' \
           f'Temp: {wthr.temperature}°C, feels like: {wthr.temperature_feeling}°C'


def wind_p():
    """Returns a message about the wind"""
    wthr = get_weather(coordinates=CoordinatesP)
    return f'Wind: {wthr.wind_direction},{wthr.wind_speed} m/s'

str_weather = f'{weather_r()}\n{wind_r()}\n\n{weather_n()}\n{wind_n()}\n\n{weather_p()}\n{wind_p()}'

# ----------------------------------------------


myScheduler = SchedullerJobs(str_weather)


# инициируем задания по рассписанию
async def on_startup(db):
    myScheduler.schedule_jobs(db)


# ---------------------------------------------------
def start_bot():
    # создаем объект бота и передаем в него Токен из файла config.py
    # bot = Bot(token=bot_token)
    # в aiogram хендлерами управляет диспетчер. Создаем объект диспетчер и передаем в него нашего бота и хранилище
    # db = Dispatcher(bot, storage=MemoryStorage())
    # запускаем scheduler

    # str_weather = weather()
    myScheduler.scheduler.start()
    # запуск бота: вызываем у executor метод start_polling, передаем в него объект класса диспетчер, и доп условие
    executor.start_polling(db, on_startup=on_startup)
