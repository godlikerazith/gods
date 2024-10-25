import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20280383"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8742e49f7681c71180fed37d4736fc3b")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://razithrazith71:razith786@cluster0.ev2i9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
