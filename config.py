import os

from dotenv import load_dotenv

load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID","29219170"))  # API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH","12d6648ede66e1ef31d9c455317ee09d")  # API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN","5630279176:AAEGCGfyOaCMWcEeklIAVgADgQTwM0QHD8Q")  # Bot token from @BotFather
ADMINS = ([int(i.strip()) for i in os.environ.get("ADMINS","5897793065").split(",")]
    if os.environ.get("ADMINS","5897793065")
    else [])
DATABASE_NAME = os.environ.get("DATABASE_NAME", "MdiskConvertor")
DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Sohanrazz:Sohanrazz@cluster0.o3by2xt.mongodb.net/?retryWrites=true&w=majority")  # mongodb uri from https://www.mongodb.com/
OWNER_ID = int(os.environ.get("OWNER_ID","5897793065"))  # id of the owner
ADMINS.append(5897793065) if OWNER_ID not in ADMINS else []

#  Optionnal variables
LOG_CHANNEL = int(
    os.environ.get("LOG_CHANNEL", "1001544056917")
)  # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL","1001713432930")  # For Force Subscription
BROADCAST_AS_COPY = is_enabled(
    (os.environ.get("BROADCAST_AS_COPY", "True")), True
)  # true if forward should be avoided
IS_PRIVATE = is_enabled(
    os.environ.get("IS_PRIVATE", "True"), "True"
)  # true for private use and restricting users
SOURCE_CODE = os.environ.get(
    "SOURCE_CODE", "Private"
)  # for upstream repo
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", "")  # image when someone hit /start
LINK_BYPASS = is_enabled(
    (os.environ.get("LINK_BYPASS", "False")), False
)  # if true, urls will be bypassed
BASE_SITE = os.environ.get("BASE_SITE", "oggylink.com")  # your shortener site domain

# For Admin use
CHANNELS = is_enabled((os.environ.get("CHANNELS", "True")), True)
CHANNEL_ID = (
    [int(i.strip()) for i in os.environ.get("CHANNEL_ID","1001713432930").split(" ")]
    if os.environ.get("CHANNEL_ID","1001713432930")
    else []
)

DE_BYPASS = (
    [i.strip() for i in os.environ.get("DE_BYPASS").split(",")]
    if os.environ.get("DE_BYPASS")
    else []
)
DE_BYPASS.append("mdisk.me")

FORWARD_MESSAGE = is_enabled(
    (os.environ.get("FORWARD_MESSAGE", "True")), True
)  # true if forwardd message to converted by reposting the post

#  Heroku Config for Dynos stats
HEROKU_API_KEY = os.environ.get(
    "HEROKU_API_KEY", None
)  # your heroku account api from https://dashboard.heroku.com/account/applications
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)  # your heroku app name
HEROKU = bool(HEROKU_API_KEY and HEROKU_APP_NAME)

#  Replit Config for Hosting in Replit
REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)  # your replit username
REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)  # your replit app name
REPLIT = (
    f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co"
    if REPLIT_APP_NAME and REPLIT_USERNAME
    else False
)

#  Koyeb Config for Hosting in Koyeb
KOYEB_USERNAME = os.environ.get("KOYEB_USERNAME", None)  # your koyeb username
KOYEB_APP_NAME = os.environ.get("KOYEB_APP_NAME", None)  # your koyeb app name
KOYEB = (
    f"https://{KOYEB_APP_NAME}-{KOYEB_USERNAME}.koyeb.app/"
    if KOYEB_APP_NAME and KOYEB_USERNAME
    else False
)

PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

LOG_STR = "\nHeroku is {0}\n".format(
    "Enabled" if HEROKU else "Disabled"
) + "Users {0} use this bot\n".format("cannot" if IS_PRIVATE else "can")
