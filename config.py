import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
BOT_TOKEN = "8736223294:AAHJKOu_g4dpnnTq_O4LKrsO1r6TZ04VPhI"

# Bot Configuration
BOT_NAME = "Music VC Bot"
BOT_DESCRIPTION = "YouTube से Voice Chat में music play करता है!"

# Logging
LOG_LEVEL = "INFO"

# Music Configuration
MAX_QUEUE_SIZE = 50
DOWNLOAD_FOLDER = "downloads"
MAX_AUDIO_LENGTH = 3600  # 1 hour in seconds

# YouTube Configuration
YT_SEARCH_RESULTS = 5
