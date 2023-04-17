from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

image = None

kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='/sendphoto')]
])


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message) -> None:
    await message.answer('Start bot',
                         reply_markup=kb)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def sendphoto_cmd(message: types.Message) -> None:
    global image
    image = message.photo[-1]
    file_id = image.file_id
    file = await bot.get_file(file_id)
    image_path = file.file_path
    await file.download(destination='photos/' + image_path.split('/')[-1])
    await bot.send_message(message.from_user.id,
                           text='working with photo')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
