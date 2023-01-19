from aiogram import types
# импторт работы с памятью

from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

# импорт диспетчера и бота
from loader import db

# импорт готовых обработчиков сообщений
from bot_commands import BotCommands
from play_dice import PlayDice
from messagelistner import MessageListner
from chatmembers import ChatMembers

# import asyncio

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

# запуск бота создаем условие, вызываем у executor метод start_polling и передаем в него объект класса диспетчер
if __name__ == '__main__':
    executor.start_polling(db)
