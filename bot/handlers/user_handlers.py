import io
import os.path
import secrets

from aiogram import types, Dispatcher
from PIL import Image
from aiogram.types import InputMedia, InputMediaPhoto

from bot.edit_photo.load_photo import load_photo
from bot.edit_photo.remove_background import remove_background
from bot.keyboards.user_keyboards import get_main_keyboard, get_editphoto_keyboard


async def cmd_start(msg: types.Message) -> None:
    """
    start cmd
    :param msg:
    :return:
    """

    reply_text = 'Send photo: '
    await msg.answer(
        text=reply_text
    )


async def handler_rmbcg(msg: types.Message) -> None:
    """
    remove background handler
    :param msg:
    :return:
    """
    img = load_photo(msg.photo[3].file_id)
    img = Image.open(io.BytesIO(img))
    img = remove_background(img)
    file_name = secrets.token_hex(8)
    if not os.path.exists('result'):
        os.mkdir('result')
    img.save(f'result/{file_name}.png', format='PNG')
    await msg.answer_photo(photo=open(f'result/{file_name}.png', 'rb'))


def register_user_handlers(dp: Dispatcher) -> None:
    """
    register handlers
    :param dp:
    :return:
    """

    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(handler_rmbcg, content_types=types.ContentTypes.PHOTO)
