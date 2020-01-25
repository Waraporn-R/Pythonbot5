from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from config import access_token , channel_secret  #import ตัวแปรเข้ามา

app = Flask(__name__)

line_bot_api = LineBotApi(access_token) #channel access token
handler = WebhookHandler(channel_secret) #channel secret


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)  ##<<<< process ข้อความพร้อมส่งกลับ
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    REPLYTOKEN = event.reply_token
    TEXT_FROM_USER = event.message.text
    USER_ID = event.source.user_id
    print(REPLYTOKEN ,"  -  ", TEXT_FROM_USER ,"  -  ", USER_ID)
    line_bot_api.reply_message(event.reply_token
                               ,TextSendMessage(text=event.message.text))

@handler.add(FollowEvent)
def greeting(event):
    line_bot_api.reply_message(event.reply_token
                               ,TextSendMessage(text="ยินดีต้อนรับสู่ฐานข้อมูล ไวรัส ของโลก"))

if __name__ == "__main__":
    app.run()