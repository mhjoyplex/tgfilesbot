import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'LuciferMoringstar_Robot')
API_ID = int(environ['7644705'])
API_HASH = environ['c134230fcb7004f5a9f31c772af5f29f']
BOT_TOKEN = environ['5411942165:AAFvvhf-PkbG2o9BAPF2ORUaqFxMtq2a7B8']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

BROADCAST_CHANNEL = int(os.environ.get("BROADCAST_CHANNEL", "-1001377437056"))
ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "1101892352").split())
DB_URL = os.environ.get("DATABASE_1", "mongodb+srv://mhjoy99:Mokaromjoy1234*@cluster0.shbxu.mongodb.net/?retryWrites=true&w=majority")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['12345789, 987654321, 1006098851, 1282644258, 1940428147, 1101892352'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['-1001377437056, -1001674775818'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('1006098851, 1282644258', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('FORCES_SUB')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "-1001465521281, -1001474044211").split()]
TUTORIAL = "https://telegram.dog/MotionPicturerequest2"
# MongoDB information
DATABASE_URI = environ['mongodb+srv://mhjoy99:Mokaromjoy1234*@cluster0.shbxu.mongodb.net/?retryWrites=true&w=majority']
DATABASE_NAME = environ['BOT_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm MOTION PICTURE FILES BOT**

Here you can search files Uploaded On MOTION PICTURE, Send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=769ec931")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
