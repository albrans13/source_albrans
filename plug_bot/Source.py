from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio

@bot.on_inline_query(filters.regex("^سورس$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("❤️  قناه السورس  ",url="https://t.me/source_albrans"),
             ],
             [
             InlineKeyboardButton("☑️ لتنصيب حسابك   ",url="https://t.me/source_albrans"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="سورس البوت",
                input_message_content=InputTextMessageContent(
                    "╭───── • 𖥔 • ─────╮\n [𖥔 𝙨𝙤𝙪𝙧𝙘𝙚𝙖𝙡𝙗𝙧𝙖𝙣𝙨 ⚡️](https://t.me/source_albrans)\n[𖥔 𝙖𝙡𝙗𝙧𝙖𝙣𝙨 ⚡️](https://t.me/HH_7_T)\n[𖥔*chat* 𝙨𝙤𝙪𝙧𝙘𝙚 ⚡️](https://t.me/chat_refz)\n╰───── • 𖥔 • ─────╯\n⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼"
                ),
                url="https://t.me/source_albrans",
                description=" SOURCE",
                thumb_url="https://telegra.ph/file/667e805354bd990f02106.jpg",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )








