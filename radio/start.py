from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**HEY I AM A VK RADIO Botz 📻\n\n** \n`Add this to your Group and Make it Admin \n2) Add`  `to your Group` \n3) **Commands** : \n`/radio` Ytlink Live \n`/stop`",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Support", url="t.me/DKBOTZ")
                                    ]]
                            ))
   else:
      await m.reply(f"**Bot is Alive! ✨**")
