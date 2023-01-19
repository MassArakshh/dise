# from aiogram import Bot, Dispatcher
# from loader import db
from aiogram import Dispatcher


class SchedulerMessage:
    def __int__(self):
        self.work_chat_id = "-668882275"
        self.test_chat_id = "-1001810695395"
        # self.db = db

    async def send_mess_on_end_work(self, db: Dispatcher):
        await db.bot.send_message("-668882275", "Коллеги, хорошего вечера!\nОля, спокойной ночи!")

    async def send_mess_on_start_work(self, db):
        await db.bot.send_message(self.work_chat_id, "Коллеги, доброе утро !\nОля, добрый день!")

    async def send_mess_on_scram(self, db):
        await db.bot.send_message("-668882275", "Коллеги, пора на скрам!\nНу, если не сдвинули...")

    async def send_mess_on_test(self, db):
        await db.bot.send_message("-1001810695395", "Шлю сам бот!")

    async def send_mess_on_dinner(self, db):
        await db.bot.send_message(self.test_chat_id, "Коллеги, пора на обед!")
