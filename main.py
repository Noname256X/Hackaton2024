from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import config


bot = Bot(token=(config.TOKEN))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def on_startup(_):
    print('Бот запущен')









if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup) #Что бы не отвечал на сообщения когда не онлайн, чтобы отвечал при выходе в онлайн False