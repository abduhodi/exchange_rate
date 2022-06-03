import logging
from aiogram import Bot, Dispatcher, executor, types
from exchange_bot import getrate
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ask = KeyboardButton('Kursni bilish')
help = KeyboardButton("Bot haqida")

keybutton1 = ReplyKeyboardMarkup(resize_keyboard=True).add(ask).add(help)

API_TOKEN = '*'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom Valyuta Kurslari haqida \
eng yangi ma'lumotlarni olishingiz mumkin \
bo`lgan botga xush kelibsiz!", reply_markup=keybutton1)


@dp.message_handler()
async def exchange(message: types.Message):
    if message.text == 'Bot haqida':
        await message.reply("Valyuta kurslari haqidagi ma'lumotlar \
        \nO`zbekiston Milly Bankidan olinadi. \
        \nAdmin bilan bog`lanish uchun: @AbduhodiTursunboyev")
    elif message.text == 'Kursni bilish':
        data = getrate()
        await message.answer(data)
    else:
        await message.reply("Noto`g`ri buyruq kiritdingiz")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
