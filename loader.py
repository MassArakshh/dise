# импорт диспетчера, бота, типов

from aiogram.dispatcher import Dispatcher
from aiogram import Bot
# импорт состояний
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# импорт токена
# from config import config
from config import bot_token #Token
from scheduller_jobs import SchedullerJobs

# !!! не взлетает !!! создаем объект бота и передаем в него Токен из файла .env в зашифрованном виде
# bot = Bot(token=config.bot_token.get_secret_value())

bot = Bot(token=bot_token)
# bot = Bot(token=Token)

# инициализировать хранилище в dp для FSM
storage = MemoryStorage()

# в aiogram хендлерами управляет диспетчер. Создаем объект диспетчер и передаем в него нашего бота и хранилище
db = Dispatcher(bot, storage=storage)

# инициируем задания по рассписанию



mySchedulerJobs = SchedullerJobs()

async def on_startup(db):
    # schedule_jobs()
    mySchedulerJobs.schedule_jobs(db)
