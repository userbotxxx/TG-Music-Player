from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am an Telegram Groups Music bot 🎶, I let you play music in your group's voice chat.

The commands I currently support are:

/play - 🎶 Play the replied audio file or YouTube video 
/pause - ▶️ Pause the audio stream 
/resume - ⏸ Resume the audio stream 
/skip - ↪️ Skip the current audio stream
/mute - 🔇 Mute the userbot
/unmute - 🔊 Unmute the userbot
/stop - 🗑🛑 Clear the queue and remove the userbot from the call
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/SnaB_HelP"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/iNfO_Maker"
                    )
                ]
            ]
        )
    )
