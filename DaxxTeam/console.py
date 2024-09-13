import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", 28122413))
API_HASH = getenv("API_HASH", "750432c8e1b221f91fd2c93a92710093") 
BOT_TOKEN = getenv("BOT_TOKEN", " 6993647727:AAGEsZVoOEPpKuuGwrnHc1o1bQoCLRAykAI")
STRING_SESSION = getenv("STRING_SESSION", "BQGtHS0ASTerhBtb7VbuRhJikBU_GW7TQJ1df66_N65YswPs84-dj-aFVc3QJ8_t5cPIF5KUs4gRpfNwteMPkcUF57_wUL_Cq-WoL0G_x-y90Kf5Gb6p2qccuPLIiIiHaMfSIz-05ZhZEliWmVw_qwZcdj5pg4rRJUnzmDmOxGv127TZ0HW9D9YmjJY5TK-zX3e20zzE-SQyyuKHsyO7-FoKVMvNmugCsBM3XoWQy0-Y8GZBiyzp_0SsB2eobO5-bKSvsNe2RrJ8oLllI27Snjdlyye6I_elcBlsFIogq0UZIF5QdF6fzrweeTIu5xkfeHOne2Lwa6BtUgoqZggmTrBqdd6s_AAAAAG05lvIAA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://vikas:vikas@vikas.yfezexk.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1001975521991))


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 Hey, I am an advanced & superfast high quality userbot assistant with an upgraded version security system.\n\n🌿 I can't let you message my owner's dm without my owner's permission.\n\n🌺 My owner is offline now, please wait until my owner allows you.\n\n🍂 Please don't spam here, because spamming will force me to block you from my owner id.**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))



# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://graph.org/file/1217cb1e402b99fa47fdf.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("Daxx")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

