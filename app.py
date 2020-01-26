from flask import Flask, request, abort , render_template

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


from basic_python.virus import Virus_database
@app.route("/")
def index():
    return render_template("index.html",viruses=Virus_database)




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

from basic_python.virus import virus_app  ## import function เข้ามา
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    REPLYTOKEN = event.reply_token
    TEXT_FROM_USER = event.message.text
    USER_ID = event.source.user_id
    # print(REPLYTOKEN ,"  -  ", TEXT_FROM_USER ,"  -  ", USER_ID)
    # process text and return text to reply
    TEXT_TO_REPLY = virus_app(userid=USER_ID,text_input=TEXT_FROM_USER)
    if isinstance(TEXT_TO_REPLY , str):
        line_bot_api.reply_message(event.reply_token
                                ,TextSendMessage(text=TEXT_TO_REPLY))
    else :
        line_bot_api.reply_message(event.reply_token
                                ,TEXT_TO_REPLY)

@handler.add(FollowEvent)
def greeting(event):
    USER_ID = event.source.user_id
    line_bot_api.reply_message(event.reply_token
                             ,TextSendMessage(text="ยินดีต้อนรับสู่ฐานข้อมูล ไวรัส ของโลก \n\nกรุณาเลือกคำสั่งด้วยคะ \nเพิ่มฐานข้อมูลไวรัส(1)\nลบฐานข้อมูลไวรัส(2)\nเปลี่ยนแปลงข้อมูล(3)\nเรียกดูข้อมูลไวรัส(4)\nออกจากโปรแกรม(E)"))
    
    line_bot_api.link_rich_menu_to_user(user_id = USER_ID,
                                        rich_menu_id = "richmenu-0e649c2b2c13a520f8a822251e6ef7e0")


if __name__ == "__main__":
    app.run()
    

