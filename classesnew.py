# импорт состояний
from aiogram.dispatcher.filters.state import StatesGroup, State


# класс с описанием состояний
class UserState(StatesGroup):
    user_id = State()
    assets = State()
    bet = State()


# класс счетчик
class IncrementCounter:
    def __init__(self):
        self._value = 0

    def new_value(self):
        self._value += 1
        return self._value
