# импорт диспетчера, бота, типов

from aiogram.dispatcher import Dispatcher
from aiogram import Bot
# импорт состояний
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# импорт токена
# from config import config
from config import bot_token #Token

# !!! не взлетает !!! создаем объект бота и передаем в него Токен из файла .env в зашифрованном виде
# bot = Bot(token=config.bot_token.get_secret_value())

bot = Bot(token=bot_token)
# bot = Bot(token=Token)

# инициализировать хранилище в dp для FSM
storage = MemoryStorage()

# в aiogram хендлерами управляет диспетчер. Создаем объект диспетчер и передаем в него нашего бота и хранилище
db = Dispatcher(bot, storage=storage)
