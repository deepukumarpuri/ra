from pyrogram import Client
from pyrogram import idle
from config import API_ID, API_HASH, BOT_TOKEN
from radio.radio import app

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="radio"),
)

bot.run()
app.start()
idle()
