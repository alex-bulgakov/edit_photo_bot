from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Btn', callback_data='cb_btn')]
    ])
    return ikb


def get_editphoto_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Удалить фон', callback_data='rmbcg_btn')]
    ])
    return ikb
