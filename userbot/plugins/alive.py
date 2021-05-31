
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in Mafia Userbot by @D3_krish

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, mafiaversion
from mafiabot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝔻3𝕍𝕀𝕃_𝔹𝕆𝕋"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @D3_krish ...and thanks to sameer for the logos...
# Kang with credits else gay...
# alive.py for eagle mafia bot

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

edit_time = 16
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/a4a4a2ed5208090ddbc6a.jpg"
file2 = "https://telegra.ph/file/037f449869b653566da38.jpg"
file3 = "https://telegra.ph/file/d1cb0b64d26d456e2c27e.jpg"
file4 = "https://telegra.ph/file/debac7ea269b43e27bc64.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**𖣘𖣘𝙴𝙰𝙶𝙻𝙴 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙸𝚂 𝙰𝙻𝙸𝚅𝙴𖣘𖣘**__\n\n"
pm_caption += (
    f"                 𝙼𝙰𝚂𝚃𝙴𝚁\n**  『[{DEFAULTUSER}](tg://user?id={mafia})』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption +=  "┣•✘ About My System ✘\n\n"
pm_caption +=  "┣•➾𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 `1.15.0` \n\n"
pm_caption +=  "┣•➾𝙴𝙰𝙶𝙻𝙴 𝙱𝙾𝚃 ☞ : `{mafiaversion}`\n\n"
pm_caption +=  "┣•➾𝚂𝚄𝙳𝙾 ☞          : `{sudou}`\n\n"
pm_caption +=  "┣•➾𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙶𝚁𝙾𝚄𝙿 ☞   : [𝙹𝙾𝙸𝙽](https://t.me/EAGLE_MAFIA_USERBOT)\n\n"
pm_caption +=  "┣•➾𝙲𝚁𝙴𝙰𝚃𝙾𝚁 ☞    : [𝚂𝙸𝙳𝙳𝙷𝙰𝚁𝚃𝙷](https://t.me/Owner_of_team_eagle_mafia)\n\n"
pm_caption +=  "┣•➾𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝙴𝚁 ☞    :[𝚃𝙴𝙰𝙼 EAGLE](https://t.me/eagle_with_sucker)\n\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"      [✘𝚁𝙴𝙿𝙾✘](https://github.com/sameerphanti/EAGLE-MAFIA-BOT)  [✘𝙻𝙸𝙲𝙴𝙽𝚂𝙴✘](https://github.com/sameerphanti/EAGLE-MAFIA-BOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(alive.chat_id, ok7, file=file2) 

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(alive.chat_id, ok8, file=file3)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(alive.chat_id, ok9, file=file1)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(alive.chat_id, ok10, file=file3)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(alive.chat_id, ok11, file=file2)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(alive.chat_id, ok12, file=file4)
    
    await asyncio.sleep(edit_time)
    ok14 = await borg.edit_message(alive.chat_id, on, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "eagle", None, "To check am i alive with your favorite alive pic"
).add()
