# импорт диспетчера
from loader import db, bot

# импорт ф-ий бд
# from dbcode import insert_player
# from dbclass import DataBase

# from dbfunctions import insert_player_short


class ChatMembers:
    def __int__(self):
        self.newchatmembers()

    def newchatmembers(self):
        #  приветствие нового члена группы
        @db.message_handler(content_types=["new_chat_members"])
        async def new_member(message):
            first_name = message.new_chat_members[0].first_name
            # user_id = message.new_chat_members[0].id
            # - перенес в игру, если ответил ДА - добавим пользователя в БД и ему 100 БотКов
            # entities = (user_id, first_name, 100, 0, 0)
            # insert_player_short(entities)
            # await bot.send_message(message.chat.id, "@"+ str(message.from_user.username)+", Привет!")
            await bot.send_message(message.chat.id,
                                   "@" + str(first_name) + " , привет!\nНажми или набери: /help\nи узнаешь что я могу!")


    # определить существующих членов чата и им послать привет!