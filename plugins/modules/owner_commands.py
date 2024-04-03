import os, sys, asyncio
from pyrogram import Client, filters
from pyrogram.filters import command, user

from config import ADMINS
from plugins.helper.telegram_helper.message_utils import sendMessage, editMessage


@Client.on_message(command("restart") & user(ADMINS))
async def restart(client, message):
    reply = await sendMessage(message, "Restarting........")
    await asyncio.sleep(2)
    await editMessage(reply, "Done........")
    os.execl(sys.executable, sys.executable, *sys.argv)
