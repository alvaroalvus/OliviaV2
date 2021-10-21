from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
✨️This Is Advanced Telegram Music Bot\n🎶Run on private VPS Server\n🔥Feel High Quality Muzic In Vc🎶🎼\n❤Developed By[Einstein](https://t.me/alvaa_Robot)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨️Dev✨️", url="https://t.me/alvaa_Robot")
                  ],[
                    InlineKeyboardButton(
                        "🔥Bot Project🔥", url="https://t.me/danger_bots"
                    ),
                    InlineKeyboardButton(
                        "⚡️Support⚡️", url="https://t.me/dangerbots"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🍀Chatting Group🍀", url="https://t.me/nammude_keralam"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲 𝗡𝗼𝘄\n🌠𝗛𝗲𝘅𝗼𝗿 𝗫𝗗 <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌼𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/Prayagraj_Op")
                ]
            ]
        )
   )
