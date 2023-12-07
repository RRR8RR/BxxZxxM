import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("help")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/4edb726cd168c2f4e1654.jpg",
        caption=f"""**⩹━★⊷━• ⌞ ⩹━⊷⌯ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝ •**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس سبارك \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━★⊷━⌞• ⌞ ⩹━⊷⌯ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝ •**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "𓆩˹ عــلــش | 🇮🇶", url=f"https://t.me/BxxBxxL"),
                   
                ],[
                
                    InlineKeyboardButton(
                        "★• ⌞ ⩹━⊷⌯ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝ •⚡", url=f"https://t.me/xLxLxLrr3"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━★⊷⌯⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝⌯⊶★━⩺**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي الخاص بالوسكي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

**⩹━★⊷⌯⌞ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="دليل")],
            [InlineKeyboardButton("عــلــشᯓ𓆩 | 🇮🇶", url=f"https://t.me/BxxBxxL")],
            [InlineKeyboardButton("★• ⌞ ⩹━⊷⌯ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐑𝐔𝐍𝐓𝐇𝐎𝐍 ⌝ •⚡", url=f"https://t.me/xLxLxLrr3")],
        ]
    ))

