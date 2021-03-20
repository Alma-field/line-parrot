from flask import Flask, abort, current_app, request

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, ImageMessage, TextSendMessage
)

#各種設定
from config import (
    JSON_AS_ASCII, PORT, LINE_BOT_CHANNEL_TOKEN, LINE_BOT_CHANNEL_SECRET
)

line_bot_api = LineBotApi(LINE_BOT_CHANNEL_TOKEN)
handler = WebhookHandler(LINE_BOT_CHANNEL_SECRET)

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = JSON_AS_ASCII

@app.route("/")
def toppage():
    shortness = ''
    if not LINE_BOT_CHANNEL_TOKEN:
        shortness += 'LINE_BOT_CHANNEL_TOKEN'
    if not LINE_BOT_CHANNEL_SECRET:
        if shortness:shortness += ' and '
        shortness += 'LINE_BOT_CHANNEL_SECRET'
    if not shortness:
        return 'OK'
    else:
        return f'You have not assigned any value for {shortness}'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    current_app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def text_handler(event):
    """テキストメッセージが来た場合、オウム返しを行う"""
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text[:2000])
    )

@handler.add(MessageEvent, message=ImageMessage)
def image_handler(event):
    """画像メッセージが来た場合、定型文を送信する"""
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='画像は読み込めません\n文字で送って下さい')
    )

###################その他
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
