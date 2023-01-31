import loader
# импорт диспетчера и бота
from loader import db, bot

# импорт готовых обработчиков сообщений
from bot_commands import BotCommands
from play_dice import PlayDice
from messagelistner import MessageListner
from chatmembers import ChatMembers


myBotCommands = BotCommands(db, bot)
myPlayDice = PlayDice(db, bot)
myMesListner = MessageListner()
myNewChatMember = ChatMembers(db, bot)

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






# myScrapper = Scrapper(db, bot, myCl)
# myScrapper.scrap()



# запуск бота создаем условие, вызываем у executor метод start_polling и передаем в него объект класса диспетчер
if __name__ == '__main__':
    # scheduler.start()
    # executor.start_polling(db, on_startup=on_startup)
    loader.start_bot()

