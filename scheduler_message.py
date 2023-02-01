from aiogram import Dispatcher

from get_weather import GetWeather


class SchedulerMessage:
    def __init__(self):
        self.test_chat_id = "-1001810695395"
        self.work_chat_id = "-1001889896793"

    async def send_mess_on_end_work(self, db: Dispatcher):
        await db.bot.send_message(self.work_chat_id, "Коллеги, хорошего вечера!\nОля, спокойной ночи!")

    async def send_mess_on_start_work(self, db: Dispatcher):
        await db.bot.send_message(self.work_chat_id, "Коллеги, доброе утро !\nОля, добрый день!\n\n" + GetWeather().weather())

    async def send_mess_on_scram(self, db: Dispatcher):
        await db.bot.send_message(self.work_chat_id, "Коллеги, пора на скрам!\nНу, если не сдвинули...")

    async def send_mess_on_test(self, db: Dispatcher):
        await db.bot.send_message(self.test_chat_id, "Утро доброе!\n\n" + GetWeather().weather())

    async def send_mess_on_dinner(self, db: Dispatcher):
        print(self.test_chat_id)
        await db.bot.send_message(self.test_chat_id, "Коллеги, пора на обед!" + str(''))
