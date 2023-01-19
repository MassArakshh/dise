# import asyncio
# from datetime import datetime

# import aioschedule
from aiogram import types
# импторт работы с памятью

from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

# импорт диспетчера и бота
from loader import db, on_startup

# импорт готовых обработчиков сообщений
from bot_commands import BotCommands
from play_dice import PlayDice
from messagelistner import MessageListner
from chatmembers import ChatMembers

# from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduller_jobs import scheduler


# import asyncio

# import aioschedule
# -----------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# кнопки


# кнопки обычные начало
@db.message_handler(commands="pusk")
async def cmd_pusk(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Со ставками")
    keyboard.add(button_1)
    button_2 = "Без ставок"
    keyboard.add(button_2)
    await message.answer("Как игравем в кости?", reply_markup=keyboard)


# кнопки обычные красивые
# попробовать парметры : selective и row_width!!!!!
@db.message_handler(commands="pusk2")
async def cmd_pusk2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Со ставками", "Без ставок"]
    keyboard.add(*buttons)
    await message.answer("Как игравем в кости?", reply_markup=keyboard)


# обработка нажатия кнопок, по сути мообщения пользователя
@db.message_handler(Text(equals="Со ставками"))
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())


@db.message_handler(lambda message: message.text == "Без ставок")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")


# ------------------------------------------------------------------------------------------------------

# кнопки инлайнеры с callback в обычном режиме
@db.message_handler(commands=["rand"])
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    keyboard.add()
    await message.answer("Нажми, чтобы отправить...", reply_markup=keyboard)


# обработка нажатия кнопки, уже именно кнопки
@db.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer("Вот ответ")
    await call.answer(text="Спасибо, что воспользовались ботом!", show_alert=True)
    # или просто await call.answer()


# кнопки инлайнеры с callback в обычном режиме


# ------------------------------------------------------------------------------------------------------


myBotCommands = BotCommands()
myPlayDice = PlayDice()
myMesListner = MessageListner()
myNewChatMember = ChatMembers()

# команды бота
myBotCommands.start()
myBotCommands.help()
# добавить пользоваеля и ему денег
myBotCommands.money()

#  приветствие нового члена группы
myNewChatMember.newchatmembers()

# !!! надо подружить с командой /play !!! игра рулетка
myPlayDice.playdice()

# обработка текстового сообщения
myMesListner.echo()
# myMesListner.time_to_dinner()

# --------------------------------------------------------------------------------------------
# рассписание работает
# scheduler = AsyncIOScheduler()
#
#
# async def send_mess_on_dinner(db):
#     await db.bot.send_message("-1001810695395", "Коллеги, пора на обед!")
#
#
# async def send_mess_on_end_work(db):
#     await db.bot.send_message("-668882275", "Коллеги, хорошего вечера!\nОля, спокойной ночи!")
#
#
# async def send_mess_on_start_work(db):
#     await db.bot.send_message("-668882275", "Коллеги, доброе утро !\nОля, добрый день!")
#
#
# async def send_mess_on_scram(db):
#     await db.bot.send_message("-668882275", "Коллеги, пора на скрам!\nНу, если не сдвинули...")
#
#
# async def send_mess_on_test(db):
#     await db.bot.send_message("-1001810695395", "Шлю сам бот!")
#
#
# def schedule_jobs():
#     date_dinner = datetime(2023, 1, 19, 16, 41)
#     scheduler.add_job(send_mess_on_dinner, "date", run_date=date_dinner, args=(db,))
#
#     scheduler.add_job(send_mess_on_end_work, "cron", day_of_week='mon-fri', hour=18, minute=10, end_date='2023-12-31',
#                       args=(db,))
#     scheduler.add_job(send_mess_on_start_work, "cron", day_of_week='mon-fri', hour=9, minute=10, end_date='2023-12-31',
#                       args=(db,))
#     scheduler.add_job(send_mess_on_scram, "cron", day_of_week='mon-fri', hour=10, minute=28, end_date='2023-12-31',
#                       args=(db,))
#
#     scheduler.add_job(send_mess_on_test, "cron", day_of_week='mon-fri', hour=17, minute=14, end_date='2023-12-31',
#                       args=(db,))

# async def on_startup(db):
#     schedule_jobs()

# ----------------------------------------------------------------------------

# mySchedulerJobs = SchedullerJobs()

# scheduler = mySchedulerJobs.scheduler_init()

# async def on_startup(db):
    # mySchedulerJobs.schedule_jobs(db)


# ------------------------------------------------
# не взлетел
# @db.message_handler()
# async def time_to_2():
#     await bot.send_message(1001810695395, "Коллеги, пора на обед!")
#
#
# async def scheduler():
#     aioschedule.every().day.at("15:57").do(time_to_2)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)

# async def on_startup(db):
#     asyncio.create_task(scheduler())


# запуск бота создаем условие, вызываем у executor метод start_polling и передаем в него объект класса диспетчер
if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(db, on_startup=on_startup)
