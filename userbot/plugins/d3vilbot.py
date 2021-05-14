# this plugin made by Eagle Mafia Userbot

"""Plugin for D3vilBot Repo

\nCode by @EAGLE_MAFIA_USERBOT

type '.d3vilbot' to get D3vilBot repo
"""

import random, re
from mafiabot.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="d3vilbot ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Click [here](https://github.com/D3KRISH/D3VIL-BOT) to open this 🔥**Lit AF!!**🔥 **ɖ3ʋɨʟɮօȶ** Repo.. Join channel :- @D3VIL_BOT_SUPPORT Repo Uploaded By @EAGLE_MAFIA_USERBOT")
    
        
   
