from os import environ

JSON_AS_ASCII = False

#環境変数取得
PORT = environ.get("PORT", 5000)
LINE_BOT_CHANNEL_TOKEN = environ.get("LINE_BOT_CHANNEL_TOKEN", "")
LINE_BOT_CHANNEL_SECRET = environ.get("LINE_BOT_CHANNEL_SECRET", "")
