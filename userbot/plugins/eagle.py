import time

from userbot import ALIVE_NAME, StartTime, mafiaversion
from mafiabot.utils import admin_cmd, edit_or_reply, sudo_cmd


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "Mafia User"
MAFIA_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "𝕃𝕖𝕘𝕖𝕟𝕕𝕒𝕣𝕪_𝔸𝔽_𝔻3𝕍𝕀𝕃𝔹𝕠𝕥"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="eagle$"))
@bot.on(sudo_cmd(pattern="eagle$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if MAFIA_IMG:
        mafia_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
      
        mafia_caption += f"┏━━━━━━━━━━━━━━━━━━\n"
        mafia_caption += f"┣•➳➠__**𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚄𝚂**__\n\n"
        mafia_caption += f"┣•➳➠ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽  :** `1.15.0`\n"
        mafia_caption += f"┣•➳➠ 𝙴𝙰𝙶𝙻𝙴𝙱𝙾𝚃 :**`{mafiaversion}`\n"
        mafia_caption += f"┣•➳➠ 𝚄𝙿𝚃𝙸𝙼𝙴 :** `{uptime}\n`"
        mafia_caption += f"┣•➳➠ 𝙼𝙰𝚂𝚃𝙴𝚁 :** {mention}\n"
        mafia_caption += f"┗━━━━━━━━━━━━━━━━━━\n"
        await alive.client.send_file(
            alive.chat_id, MAFIA_IMG, caption=mafia_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"┏━━━━━━━━━━━━━━━━━━\n"
            f"┣•➳➠__**𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚄𝚂**__\n\n"
            f"┣•➳➠ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽  :** `1.15.0`\n"
            f"┣•➳➠ 𝙴𝙰𝙶𝙻𝙴𝙱𝙾𝚃 :** `{mafiaversion}`\n"
            f"┣•➳➠ 𝚄𝙿𝚃𝙸𝙼𝙴 :** `{uptime}\n`"
            f"┣•➳➠ 𝙼𝙰𝚂𝚃𝙴𝚁 :** {mention}\n",
            f"┗━━━━━━━━━━━━━━━━━━\n"
        )
