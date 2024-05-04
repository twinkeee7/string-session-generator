
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("7062539103"))

MONGO_DB_URI = getenv("MONGO_DB_URI")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Riseeuniverse")
