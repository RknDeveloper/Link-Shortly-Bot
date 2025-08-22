from pyrogram import Client, __version__, filters
from pyrogram.raw.all import layer
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import re
from config import Config, rkn
from aiohttp import web
from helper.database import db

from shortly import Shortly
from shortly.exceptions import (
    ShortlyError
)


bot = Client(
            name="link-shortly-bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            sleep_threshold=15,
        )

@bot.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)                
    button = InlineKeyboardMarkup([[        
        InlineKeyboardButton('Uᴩᴅᴀ𝚃ᴇꜱ', url='https://t.me/Rkn_Bots_Updates'),
        InlineKeyboardButton('Sᴜᴩᴩᴏʀ𝚃', url='https://t.me/RknBots_Support')       
         ]])
    
    await message.reply_text(text=rkn.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)


# /set_api <API_KEY>
@bot.on_message(filters.private & filters.command("set_api"))
async def set_api(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Usage: `/set_api your_api_key`", quote=True)

    api_key = message.command[1]
    user_id = message.from_user.id

    await db.set_api(user_id, api_key)  # save in database
    await message.reply_text(f"✅ API key has been saved!\n\n<code>{api_key}</code>", quote=True)

# /set_site <BASE_URL>
@bot.on_message(filters.private & filters.command("set_site"))
async def set_site(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Usage: `/set_site https://example.com`", quote=True)

    base_url = message.command[1]
    user_id = message.from_user.id

    await db.set_site(user_id, base_url)  # save in database
    await message.reply_text(f"✅ Base site has been saved!\n\n<code>{base_url}</code>", quote=True)
    
# Regex pattern for valid http or https URL
URL_PATTERN = re.compile(r"^https?://[^\s/$.?#].[^\s]*$")

@bot.on_message(filters.private & filters.regex(URL_PATTERN))
async def auto_shortener(client, message):
    url = message.text.strip()
    user_id = message.from_user.id

    # Get user data
    base_url = await db.get_site(user_id)
    if not base_url:
        return await message.reply_text(
            "⚠️ Please set your Site first:\n\n"
            "`/set_site your_base_site`",
            quote=True
        )

    # Get user data
    api_key = await db.get_api(user_id)
    if not api_key:
        return await message.reply_text(
            "⚠️ Please set your API key:\n\n"
            "`/set_api your_api_key`\n",
            quote=True
        )

    try:
        shortener = Shortly(api_key=api_key, base_url=base_url)
        short_link = shortener.convert(url)

        await message.reply_text(
            f"🔗 Original Link: <code>{url}</code>\n🖇️ Shortened Link: <code>{short_link}</code>",
            quote=True,
            disable_web_page_preview=True
        )
    except ShortlyError as e:
        await message.reply_text(f"❌ Error: {e}", quote=True)
        
bot.run()
