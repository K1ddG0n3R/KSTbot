import logging

from aiogram import types, F, Router
from aiogram.filters import Command

import kb
import msg_texts


router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(msg_texts.GREETING, reply_markup=kb.start)


@router.callback_query(F.data == 'menu')
async def cb_menu(call: types.CallbackQuery):
    message = call.message
    if not message:
        logging.error("No message in callback query")
        return

    await message.edit_text(msg_texts.MENU, reply_markup=kb.menu)


@router.callback_query(F.data == 'faq')
async def cb_faq(call: types.CallbackQuery):
    message = call.message
    if not message:
        logging.error("No message in callback query")
        return

    await message.edit_text('Часто задаваемые вопросы', reply_markup=kb.faq)

@router.callback_query(lambda call: call.data.startswith('faq_'))
async def get_answer(call: types.CallbackQuery):
    message = call.message
    if not message:
        logging.error("No message in callback query")
        return

    await message.edit_text(msg_texts.FAQ_DICT[call.data], reply_markup=kb.faq)


@router.callback_query(F.data == 'feedback')
async def cb_feedback(call: types.CallbackQuery):
    message = call.message
    if not message:
        logging.error("No message in callback query")
        return

    await message.edit_text(msg_texts.FEEDBACK, reply_markup=kb.only_back)


@router.callback_query(F.data == 'sa')
async def cb_sa(call: types.CallbackQuery):
    message = call.message
    if not message:
        logging.error("No message in callback query")
        return

    await message.edit_text("Выберите направление обучения", reply_markup=kb.sa)


@router.callback_query(F.data == 'about')
async def cb_about(call: types.CallbackQuery):
    message = call.message
    if not message:
        logging.error("No message in callback query")
        return

    await message.edit_text(msg_texts.ABOUT, reply_markup=kb.only_back)
