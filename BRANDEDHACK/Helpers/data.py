from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 


PM_TEXT = """
**THIS BOT FOR LOG IN YOUR ACCOUNT** 

**PURCHASE YOUR ACCOUNT NOW**
"""

HACK_TEXT = """
𝗡𝗨𝗠 ~ 𝗖𝗹𝗶𝗰𝗸 𝗡𝘂𝗺 𝗕𝘂𝘁𝘁𝗼𝗻 𝗙𝗼𝗿 𝗞𝗻𝗼𝘄 𝗬𝗼𝘂𝗿 𝗧𝗴 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗡𝘂𝗺𝗯𝗲𝗿.

𝗢𝗧𝗣 ~ 𝗖𝗹𝗶𝗰𝗸 𝗢𝘁𝗽 𝗕𝘂𝘁𝘁𝗼𝗻 𝗙𝗼𝗿 𝗞𝗻𝗼𝘄 𝗬𝗼𝘂𝗿 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗢𝘁𝗽
"""

info = """
 ❥︎ ɴᴀᴍᴇ : {}
 ❥︎ ɪᴅ : {}
 ❥︎ ᴘʜᴏɴᴇ ɴᴏ : +{}
 ❥︎ ᴜsᴇʀɴᴀᴍᴇ : @{}
"""

PM_BUTTON = IKM([
    [IKB("LOG IN", callback_data="hack_btn")]
])

HACK_MODS = IKM([
    [
        IKB("NUM", callback_data="B"),
        IKB("OTP", callback_data="D"),
    ]
])
