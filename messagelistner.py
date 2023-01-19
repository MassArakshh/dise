import random

from aiogram import types

# импорт диспетчера
from loader import db, bot

class MessageListner:
    def __int__(self):
        self.echo()

    def echo(self):
        # обработка текстового сообщения
        @db.message_handler()
        async def echo_message(message: types.Message):
            expletives = ['скотина', 'идиоты', 'дурак', 'скатина', 'идиот', 'дундук', 'блин', 'козел', 'казел', 'ппрб']
            expletives2 = ['играем', 'поиграем', 'бот', 'кости', 'скучно', 'кубик', 'игра']
            expletives3 = ['привет', 'утро', 'доброе', 'hi', 'здравствуй', 'здравствуйте', 'бот']
            expletives4 = ['подключайтесь', 'скрам']
            answers = ["Salut!" ,"Chao!" ,"Alloha! ","Hi! ", "Привет! ","Здравствуй! ", "Здравствуйте!","Хорошая нынче погода! ", "Дарова! ", "Как дела? ", "Как Ваше ничего? ", "Сколько лет! Сколько зим! ", "Разбудили'c меня... "]

            for word in message.text.lower().split():
                if word in expletives:
                    await message.reply('Не ругайся!')
                elif word in expletives2:
                    await message.reply(random.choice(answers))
                    await bot.send_message(message.from_user.id, "@" + str(
                        message.from_user.username) + " Вы меня звали, и вот он я 😎\n"
                                                      "Играть можно только в личных сообщениях БОТу!\n"
                                                      "Хочешь поиграть? Набери сам или жми тут:\n"
                                                      "/play")
                    # await bot.send_message(message.chat.id, random.choice(answers) +"@" +
                    #                        str(message.from_user.username) +
                    #                        ",\nПоиграем?\n"
                    #                        "Набери комманду: /play\n"
                    #                        "Или нажми прямо сюда -> /play")
                elif word in expletives3:
                    await message.reply(random.choice(answers))
                    # await bot.send_message(message.chat.id, random.choice(answers) + "@" + str(message.from_user.username))
                elif word in expletives4:
                    await bot.send_message(message.chat.id, "Бегу, уже бегу... " + "@" + str(message.from_user.username))
                else:
                    mesLen = len(message.text)
                    # message.__sizeof__()
                    # await bot.send_message(message.from_user.id, message.text+', '+str(mesLen)+' букв')
                    # await message.reply(message.text + " - посчитаем скока букв...")
                    # await message.answer(
                    #     message.text + " - " + str(mesLen) + " букв, точно - " + str(message.text.__len__()))
                    # await message.answer_dice(emoji= "🎲")
                    # msg = await message.answer_dice(emoji="🎲")
                    # await asyncio.sleep(5)
                    # await message.answer ("Выпало - " + str(msg.dice.value))
                    # print(msg.dice.value)
                    # await bot.send_message(message.chat.id, "@" + str(message.from_user.username) + str(message.from_user.id) + ",\n Поиграем? Набери /play")
                    # await bot.send_message(message.chat.id, "@" +
                    #                        str(message.from_user.username) +
                    #                        ",\nПоиграем? Набери комманду: /play\n"
                    #                        "Или нажми прямо сюда -> /play")
