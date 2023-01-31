from aiogram import types
from aiogram.utils.exceptions import CantInitiateConversation

# импорт ф-ий бд
from dbfunctions import update_player_assets_plays_by_id_up, insert_player_full
from dbfunctions import select_player_assets_by_id
from dbfunctions import select_player_assets_plays_by_id
from dbfunctions import update_player_assets_plays_by_id_down

from dbclass import DataBase

# импорт класса счетчик
from classesnew import IncrementCounter
# импорт класса с описанием состояний
from classesnew import UserState

# импорт состояний
from aiogram.dispatcher import FSMContext

# иммпорт задержки
import asyncio




# импорт готовых обработчиков сообщений
# from bot_commands import BotCommands

class PlayDice:
    def __init__(self, db, bot):
        self.db = db
        self.bot = bot
        self.database = DataBase()
        # self.gift_sum = 100

    def nvl(self, a, b):
        if a is None:
            return b
        else:
            return a

    def playdice(self):
        # работаем с состояниями - игра кубик
        @self.db.message_handler(commands=["play"])
        async def user_register(message: types.Message):
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Перейти в личку с БОТом", url="https://t.me/Just_The_Test_Bot"))
            keyboard.add()

            # проверяем личный чат или нет
            if message.from_user.id == message.chat.id:
                # await self.bot.send_message(message.from_user.id, "@" + str(message.from_user.username) + ", Привет!")
                # await message.answer(message.from_user.id, "@" + str(message.from_user.username) + ", Привет!")
                await message.answer(
                    "@" + str(self.nvl(message.from_user.username, "User")) + " Вам исполнилось 10 лет?\n"
                                                                               "Вы в трезвом уме и здравом рассудке?\n"
                                                                               "Сгущенку любите?\n\n"
                                                                               "Напишите: Да или Нет!")
                await UserState.user_id.set()
            else:
                try:
                    await self.bot.send_message(message.from_user.id, "@" + str(self.nvl(message.from_user.username, "User")) +
                                           " Играть можно только в личном чате с БОТом.\n"
                                           "Набери сам или жми тут:\n"
                                           "/play")
                except CantInitiateConversation:
                    await self.bot.send_message(message.chat.id, "@" + str(self.nvl(message.from_user.username, "User")) +
                                           " Мы еще не знакомы! 😎\n"
                                           "Сперва надо погворить наедине. 😍\n"
                                           "Когда перейдешь набери команду: /start", reply_markup=keyboard)

        cnt3 = IncrementCounter()

        @self.db.message_handler(state=UserState.user_id)
        async def get_username(message: types.Message, state: FSMContext):
            string = message.text.lower()
            gift_sum = 100
            if string not in ("да", "lf", "ok") or len(string) != 2:
                cnter3 = cnt3.new_value()
                if cnter3 < 1:
                    await message.answer(
                        "@" + str(self.nvl(message.from_user.username, "User")) + " Вы не ответили [Да]! Подумайте...!\n" + " Попытка: " + str(
                            cnter3) + " из 2")
                    await UserState.user_id.set()
                else:
                    await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + " Прекратили игру.\n"
                                                                                 "До скорого свидания!.")
                    await state.finish()
            else:
                await state.update_data(user_id=message.from_user.id)
                await state.update_data(user_name="@" + str(self.nvl(message.from_user.username, "User")))

                # получим данные нового пользователя
                data = await state.get_data()
                user_name = data['user_name']
                user_id = data['user_id']

                # добавим пользователя в БД и ему 100 БотКов
                # entities = (user_id, user_name, gift_sum, 0, 0)
                entities = (user_id, user_name, gift_sum, 0, 0, 0, 0, 0, 0, "", "")

                # user_state = insert_player_short(entities)
                user_state = insert_player_full(entities)
                # если добавлен, то это новый иначе - сравботает ексепшн в добавлении -  существующий !!! пока так, потом передалать красиво
                if user_state:
                    await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + " Отлично!\n"
                                                                                 "Вы новый игрок.\n"
                                                                                 "Дарим Вам " + str(
                        gift_sum) + " БотКоинов!\n"
                                    "Теперь введите Вашу ставку в БотКоинах!")
                    await UserState.next()
                else:
                    # получим скока денег и игр у пользователя
                    # assets_user = select_player_assets_by_id(user_id)
                    data_db = select_player_assets_plays_by_id(user_id)
                    assets_user = data_db['assets']
                    plays_user = data_db['plays']
                    # print(str(plays_user))
                    wins_user = data_db['wins']
                    win_assets = data_db['win_assets']
                    loss_assets = data_db['loss_assets']
                    if str(assets_user) == "0":
                        await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + " Извините...\n"
                                                                                     "У Вас " + str(
                            assets_user) + " БотКоинов!\n"
                                             # "Всего игр: " + str(plays_user) + "\n"
                                             # "Из них выигранных: " + str(wins_user) + "\n"
                                           "Вы не можете делать ставки. Вам нужны БотКоины.\n"
                                           "Обратитесь к разработчику 😎")
                        await state.finish()

                    else:
                        await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + " Отлично!\n"
                                                                                     "У Вас " + str(
                            assets_user) + " БотКоинов!\n"
                                           "Всего игр " + str(plays_user) + " \n"
                                                                            "Из них выигранных " + str(wins_user) + "\n"
                                                                                                                    "Всего выигранных БотКоинов: " + str(
                            win_assets) + " \n"
                                          "Всего проигранных БотКоинов: " + str(loss_assets) + " \n\n"
                                                                                               "Теперь введите Вашу ставку в БотКоинах!")
                        await UserState.next()  # либо же UserState.assets.set()

        cnt = IncrementCounter()
        cnt2 = IncrementCounter()

        # НАДО ПРОДЕБАЖИТЬ !!!
        @self.db.message_handler(state=UserState.assets)
        async def get_address(message: types.Message, state: FSMContext):
            string = message.text
            data = await state.get_data()
            user_id = data['user_id']
            if string.isdigit():
                # узнаем скока денег у пользователя
                data = select_player_assets_plays_by_id(user_id)
                assets_user = data['assets']
                if int(string) > int(assets_user):
                    await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + " Не принято!\n"
                                                                                 "Вы ввели больше чем у вас есть!\n"
                                                                                 "Изменити ставку, пожалуйста.")
                    await UserState.assets.set()
                else:
                    await state.update_data(assets=message.text)
                    await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + " Прекрасно!\n"
                                                                                 "Теперь введите число от 1 до 6, на которое ставите!")
                    await UserState.next()  # либо же UserState.bet.set()
            else:
                # cnt=0
                # cnt += 1
                cnter = cnt.new_value()
                if cnter < 4:
                    await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + " Не принято!\n"
                                                                                 "Вы ввели не число! Исправьте, пожалуйста.\n"
                                                                                 "Попытка: " + str(cnter) + " из 3")
                    # cnt += 1
                    await UserState.assets.set()
                else:
                    await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + " Прекратили игру!\n"
                                                                                 "В следующий раз повезет!.")
                    await state.finish()

        @self.db.message_handler(state=UserState.bet)
        async def get_address(message: types.Message, state: FSMContext):
            string = message.text
            true_numbers = ['1', '2', '3', '4', '5', '6']
            if string.isdigit() and string in true_numbers:
                await state.update_data(bet=message.text)
                # залочим пользователя
                # await self.bot.restrict_chat_member(message.chat.id, message.from_user.id,types.ChatPermissions(can_send_messages=False))
                # await message.reply(f"Пользователь замучен.")
                await message.answer("Ставка сделана! Ставок больше нет!")
                data = await state.get_data()
                await message.answer(f"Имя: {data['user_name']}\n"
                                     f"Ставка: {data['assets']} БотКоинов\n"
                                     f"На число: {data['bet']}"
                                     )
                bet = data['bet']
                assets = data['assets']
                # user_name = data['user_name']
                user_id = data['user_id']
                msg = await message.answer_dice(emoji="🎲")
                await asyncio.sleep(5)
                don = msg.dice.value
                await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + "\nВыпало: " + str(don) + "\n"
                                                                                                       "Ставили на: " + str(
                    bet))
                if str(bet) == str(don):
                    # print("1")

                    update_player_assets_plays_by_id_up(user_id, int(assets))
                    # print("2")
                    # получим БотКи пользователя
                    assets_user = select_player_assets_by_id(user_id)
                    await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + ' Выиграли! 😁\n'
                                                                                 'Ваш выигрыш составил: ' + str(
                        assets) + ' в БотКоинах !\n'
                                  'У Вас теперь всего ' + str(assets_user) + ' БотКоинов!')
                else:
                    # data_db = self.database.select_player_assets_plays_by_id(user_id)
                    # assets_user = int(data_db['assets']) - int(assets)
                    # plays_user = int(data_db['plays'])+1
                    # print(str(plays_user))
                    # wins_user = data_db['wins']
                    # win_assets = data_db['win_assets']
                    # loss_assets = int(data_db['loss_assets'])+int(assets)
                    # self.database.update_player_assets_plays_by_id_down(user_id, assets_user, plays_user, loss_assets)
                    update_player_assets_plays_by_id_down(user_id, int(assets))
                    # получим БотКи пользователя
                    assets_user = select_player_assets_by_id(user_id)
                    await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + ' Проиграли 🥺\n'
                                                                                 'У Вас теперь всего ' + str(
                        assets_user) + ' БотКоинов')
                # отпустим пользователя
                # await self.bot.restrict_chat_member(message.chat.id, message.from_user.id, types.ChatPermissions(can_send_messages=True))
                # await message.reply(f"Пользователь теперь может писать!")
                # await state.finish()
                await message.answer("@" + str(self.nvl(message.from_user.username, "User")) + " Напишите:\n"
                                                                             "Да - чтобы продолжить!\n"
                                                                             "Нет - чтобы выйти")
                await UserState.user_id.set()
                # await asyncio.sleep(5)
                # await state.finish()
            else:
                cnter2 = cnt2.new_value()
                if cnter2 < 4:
                    await message.answer(
                        "@" + str(self.nvl(message.from_user.username, "User")) + " Не принято!\n"
                                                                "Вы ввели не число, или число не в диапазоне 1-6! Повторите, пожалуйста.\n"
                                                                "Попытка: " + str(
                            cnter2) + " из 3")
                    # cnt += 1
                    await UserState.bet.set()
                else:
                    await message.answer(
                        "@" + str(self.nvl(message.from_user.username, "User")) + " Прекратили игру. В следующий раз повезет!")
                    await state.finish()
