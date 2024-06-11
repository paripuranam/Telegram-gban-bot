import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message 

try:
    app = Client(
        "gban bot", 
        api_id=(os.getenv("API_ID")), 
        api_hash=os.getenv("API_HASH"), 
        bot_token=os.getenv("BOT_TOKEN")
    )
except Exception as e:
    print(f"Failed to initialize the Pyrogram client: {str(e)}")
else:
    print("Pyrogram client initialized successfully.")

@app.on_message(filters.command("gban") & filters.me)
async def gban_handler(client: Client, msg: Message):
    user_id = msg.reply_to_message.from_user.id
    user = await app.get_users(user_id)
    try:
        await msg.edit_text(f"GBanned user {user.first_name} ({user.id}).")
        for dialog in await app.get_dialogs():
            if dialog.chat.type in ["supergroup", "group"]:
                try:
                    await app.kick_chat_member(dialog.chat.id, user_id)
                except Exception as e:
                    print(f"Failed to kick user from group {dialog.chat.title}: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
