from aiogram import types
from aiogram.utils.exceptions import CantInitiateConversation
# импорт диспетчера
# from loader import str_weather

# импорт ф-ий бд
from dbfunctions import update_player_assets_by_id_up, select_player_assets_plays_by_id
from get_weather import str_weather_global


# from dbfunctions import update_player_assets_by_id_down

class BotCommands:
    def __init__(self, db, bot):
        self.db = db
        self.bot = bot
        # self.str_weather = StrWeather.str_weather

    def help(self):
        @self.db.message_handler(commands=["help"])
        async def help_command(message: types.Message):
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(
                types.InlineKeyboardButton(text="Перейти в личку с БОТом", url="https://t.me/Just_The_Test_Bot"))
            keyboard.add()

            await message.reply('Учебный Добрый Бот. Живет в группе, и помогает как может.\n'
                                'А еще умеет играть !\n'
                                'Но делает это только в личке 😉\n\n' + str_weather_global, reply_markup=keyboard)
            try:
                await self.bot.send_message(message.from_user.id, "@" + str(
                    message.from_user.username) + " Играть можно только в личных сообщениях БОТу!\n"
                                                  "Хочешь поиграть? Набери сам или жми тут:\n"
                                                  "/play")
            except CantInitiateConversation:
                await self.bot.send_message(message.chat.id, "@" + str(message.from_user.username) +
                                            " Мы еще не знакомы! 😎\n"
                                            "Сперва надо погворить наедине. 😍\n"
                                            "Когда перейдешь набери команду: /start", reply_markup=keyboard)

    def start(self):
        @self.db.message_handler(commands=["start"])
        async def start_command(message: types.Message):
            await message.reply("Привет я Эхо Бот, который играет!\n"
                                "Хочешь поиграть? Набери сам или жми тут:\n"
                                "/play")

    #  !!! убрать добавление !!! добавляет пользователя в БД и начисляет ботКоины
    def money(self):
        @self.db.message_handler(commands=["money"])
        async def new_member(message):
            user_id = message.from_user.id
            user_name = "@" + message.from_user.username
            # добавим пользователя в БД и ему 100 БотКов
            # entities: tuple[Any, str , int, int, int] = (user_id, user_name, 0, 0, 0)
            # insert_player_short(entities)
            # добавим денег ему
            data_db = select_player_assets_plays_by_id(user_id)
            assets_user = data_db['assets']
            if str(assets_user) == "0":
                update_player_assets_by_id_up(user_id, 50)
                await self.bot.send_message(message.from_user.id, "@" + str(message.from_user.username) + ", Привет!")
                # await bot.send_message(message.chat.id, "@"+ str(message.from_user.username)+", Привет!")
                # await bot.send_message(message.chat.id, "@"+ str(first_name)+", Привет!\nНабери /help , узнаешь что я могу!")
                await message.reply('Тебе добавили 50 БотКоинов.')
            else:
                await message.reply("@" + str(message.from_user.username) + " У Вас еще есть " + str(
                    assets_user) + " БотКоинов.\n"
                                    # "Всего игр: " + str(plays_user) + "\n"
                                    # "Из них выигранных: " + str(wins_user) + "\n"
                                   "И Вы в игре! 😎")

