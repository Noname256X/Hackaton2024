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


#start-Кнопочки
categories = types.KeyboardButton('Выбор категорий мероприятия')
categories_but = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(categories)

#Кнопочки выбора
# ('Кинотеарты')
# ('Театры')
# ('Музеи')
# ('Парки')
# ('Кафе')
# ('Рестораны')
# ('Дом культуры')
# ('Природные')
# ('Развлекательные')


@dp.message_handler(commands=['start', 'help', 'back'])
async def command_started(message: types.message):
    if message.text == '/start':
        await message.answer(
            '''👋 Добро пожаловать в чат-бот «Ростовчанка»!\n
Я здесь, чтобы помочь вам открыть для себя все интересные места и события в Ростове-на-Дону! 🌆\n
Если вы местный житель или турист, я предоставлю вам персонализированные рекомендации, которые основаны на ваших интересах. \n
Вам больше не нужно тратить время на поиски информации — просто скажите мне, что вас интересует, и я подберу для вас лучшие варианты!\n
Вот что я могу для вас сделать:\n
🚶‍♂️ Рекомендовать интересные места для посещения\n
🎉 Информировать о предстоящих мероприятиях и событиях\n
🍽️ Подсказать, где можно вкусно поесть\n
🗺️ Предложить маршруты для прогулок по городу\n
Просто выберете, что вас интересует, и я с радостью помогу! Давайте сделаем ваше время в Ростове-на-Дону незабываемым! 🎈\n
''', reply_markup=categories_but)
        print('Terminal:ожидание команды (/start):')


@dp.message_handler()
async def get_send(message: types.message):
    if 'Выбор категорий мероприятия' == message.text:
        await message.answer('')






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup) #Что бы не отвечал на сообщения когда не онлайн, чтобы отвечал при выходе в онлайн False