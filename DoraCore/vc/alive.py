from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import (Dora1, Dora2, Dora3, Dora4,
                Dora5, Dora6, Dora7, Dora8,
                Dora9, Dora10, Dora11, Dora12,
                Dora13, Dora14, Dora15, HNDLR,
                SUDO_USERS, vcbot, ALIVE_PIC, __version__)                   

Array = ALIVE_PIC or "https://telegra.ph/file/6abeb2b2ec742dda839f3.jpg"

 
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
async def _Alive(_, e: Message):
    ids = 0
    try:
        if Dora1:
            ids += 1
        if Dora2:
            ids += 1
        if Dora3:
            ids += 1
        if Dora4:
            ids += 1
        if Dora5:
            ids += 1
        if Dora6:
            ids += 1
        if Dora7:
            ids += 1
        if Dora8:
            ids += 1
        if Dora9:
            ids += 1
        if Dora10:
            ids += 1
        if Dora11:
            ids += 1
        if Dora12:
            ids += 1
        if Dora13:
            ids += 1
        if Dora14:
            ids += 1
        if Dora15:
            ids += 1
        Array_msg = f"ðð¿ð¿ð®ððð¼ð¿ð² ðð²ð¿ð². ð¥ \n\n"
        Array_msg += f"â ââââââ â ââââââ â \n"
        Array_msg += f"âº Dora á´ á´ÊsÉªá´É´ : `{__version__}` \n"
        Array_msg += f"âº á´ÊÊá´ á´ á´ÊsÉªá´É´ : `{pyro_vr}` \n"
        Array_msg += f"âº Aá´á´Éªá´ á´ IDs : `{ids}` \n"
        Array_msg += f"âº Sá´á´á´á´Êá´ : [Já´ÉªÉ´.](https://t.me/Mickymods) \n"
        Array_msg += f"â ââââââ â ââââââ â \n\n"
        await e.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "â¢ Channel â¢", url="https://t.me/DoraCore")
                ], [
                    InlineKeyboardButton(
                        "â¢ Repo â¢", url="https://github.com/MICKYY-DORA/DoraCore-")
                ]],
        ),
    ) 
    except Exception as lol:         
        Array_msg = f"ðð¿ð¿ð®ððð¼ð¿ð² ðð²ð¿ð². ð¥ \n\n"
        Array_msg += f"â ââââââ â ââââââ â \n"
        Array_msg += f"âº Dora á´ á´ÊsÉªá´É´ : `{__version__}` \n"
        Array_msg += f"âº á´ÊÊá´ á´ á´ÊsÉªá´É´ : `{pyro_vr}` \n"
        Array_msg += f"âº Sá´á´á´á´Êá´ : [Já´ÉªÉ´.](https://t.me/MickyMods) \n"
        Array_msg += f"â ââââââ â ââââââ â \n\n"
        await e.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("â¢ Channel â¢", url="https://t.me/DoraCore"),
                ],
                [
                    InlineKeyboardButton("â¢ Repo â¢", url="https://github.com/MICKYY-DORA/DoraCore-"),
                ],
            ],
        ),
    ) 
