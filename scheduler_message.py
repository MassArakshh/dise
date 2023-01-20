from aiogram import Dispatcher




class SchedulerMessage:
    def __init__(self, str_weather):
        self.test_chat_id = "-1001810695395"
        self.work_chat_id = "-1001889896793"
        self.str_weather = str_weather

    async def send_mess_on_end_work(self, db: Dispatcher):
        await db.bot.send_message(self.work_chat_id, "Коллеги, хорошего вечера!\nОля, спокойной ночи!")

    async def send_mess_on_start_work(self, db: Dispatcher):
        await db.bot.send_message(self.work_chat_id, "Коллеги, доброе утро !\nОля, добрый день!\n\n" + str(self.str_weather))

    async def send_mess_on_scram(self, db: Dispatcher):
        await db.bot.send_message(self.work_chat_id, "Коллеги, пора на скрам!\nНу, если не сдвинули...")

    async def send_mess_on_test(self, db: Dispatcher):
        await db.bot.send_message(self.test_chat_id, "Шлю сам бот!")

    async def send_mess_on_dinner(self, db: Dispatcher):
        print(self.test_chat_id)
        await db.bot.send_message(self.test_chat_id, "Коллеги, пора на обед!" + str(self.str_weather))
        # -1001889896793
    #
    # "-1001810695395"
    #
    # "-668882275"