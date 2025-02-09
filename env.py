import os
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# REQUIRED VARS
API_ID = os.getenv("API_ID", "16708960").strip()
API_HASH = os.getenv("API_HASH", "dda7630be99593256cb7c520eae0ce6d").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7769999187:AAElbFEeuIsOIm39vcFZ3oHTRY0KL-kYCwo").strip()
DB_CHANNEL = os.getenv("-1002413856170").strip()
SUDO_IDS = list(map(int, os.getenv("SUDO_IDS", "5482962500").split()))

# OPTIONAL VARS
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://heisenberg:threat1234@cluster0.wkum1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").strip()
FORCE_SUB = os.getenv('FORCE_SUB', "HeisenbergDx").strip()
DELAY_TIME = float(os.getenv('DELAY_TIME', 0.5))
HASH = int(os.getenv('HASH', 8080))


SUDOERS = filters.user()
if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not SUDO_IDS:
    print('Please Add Sudo IDS. Exiting...')
    raise SystemExit

if not MONGO_URL:
    print("No MONGO_DB specified")

try:
    DB_CHANNEL = int(DB_CHANNEL)
    API_ID = int(API_ID)
except ValueError:
    print("API_ID/DB_CHANNEL is not a valid integer. Exiting...")
    raise SystemExit

for id in SUDO_IDS:
    SUDOERS.add(id)
