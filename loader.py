# импорт диспетчера, бота, типов


from aiogram.dispatcher import Dispatcher
from aiogram import Bot
# импорт состояний
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

# импорт токена
# from config import config
from config import bot_token  # Token
from get_weather import GetWeather
# from coordinates import CoordinatesR, CoordinatesP, CoordinatesN, Coordinates
# from get_weather import get_weather
from scheduller_jobs import SchedullerJobs

# !!! не взлетает !!! создаем объект бота и передаем в него Токен из файла .env в зашифрованном виде
# bot = Bot(token=config.bot_token.get_secret_value())

bot = Bot(token=bot_token)
# bot = Bot(token=Token)

# инициализировать хранилище в dp для FSM
storage = MemoryStorage()

# в aiogram хендлерами управляет диспетчер. Создаем объект диспетчер и передаем в него нашего бота и хранилище
db = Dispatcher(bot, storage=storage)

# ----------------------------------------------


myScheduler = SchedullerJobs()


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
    myScheduler.scheduler.start()
    # запуск бота: вызываем у executor метод start_polling, передаем в него объект класса диспетчер, и доп условие
    executor.start_polling(db, on_startup=on_startup)
