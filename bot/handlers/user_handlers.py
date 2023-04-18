import io
import os.path
import secrets

from aiogram import types, Dispatcher
from PIL import Image
from aiogram.types import InputMedia, InputMediaPhoto

from bot.edit_photo.load_photo import load_photo
from bot.edit_photo.remove_background import remove_background
from bot.helpers.work_env import write_env, read_env
from bot.keyboards.user_keyboards import get_main_keyboard, get_editphoto_keyboard


async def cmd_start(msg: types.Message) -> None:
    """
    start cmd
    :param msg:
    :return:
    """

    reply_text = 'Отправьте фотографию: '
    await msg.answer(
        text=reply_text
    )
    await msg.delete()


async def handler_rmbcg(msg: types.Message) -> None:
    """
    remove background handler
    :param msg:
    :return:
    """
    # img = load_photo(msg.photo[-1].file_id)
    # img = Image.open(io.BytesIO(img), format())
    # # img = remove_background(img) # TODO move to callback
    file_name = secrets.token_hex(8)
    path = 'result'
    if not os.path.exists(path):
        os.mkdir(path)
    full_path = f'{path}/{file_name}.png'
    write_env('PATH', path)
    write_env('FILE', file_name)
    await msg.photo[-1].download(full_path)
    await msg.answer_photo(open(f'{path}/{file_name}.png', 'rb'),
                           caption='Выберете что нужно сделать с фотографией',
                           reply_markup=get_editphoto_keyboard())
    await msg.delete()


async def callback_rmbcg(clb: types.CallbackQuery):
    path = read_env('PATH')
    file = read_env('FILE')
    file_path = f'{path}/{file}.png'
    new_file_path = f'{path}/{file}_rmbgc.png'
    with open(file_path, 'rb') as f:
        img = Image.open(f)
        img = remove_background(img)
        img.save(new_file_path)
        await clb.message.answer_photo(photo=open(new_file_path, 'rb'), caption='Фото обработано')
        await clb.answer()
        # await clb.answer('Фото сохранено')
    os.remove(file_path)



def register_user_handlers(dp: Dispatcher) -> None:
    """
    register handlers
    :param dp:
    :return:
    """

    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(handler_rmbcg, content_types=types.ContentTypes.PHOTO)
    dp.register_callback_query_handler(callback_rmbcg, lambda callback: callback.data == 'rmbcg_btn')
