from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ButtonsTemplate, PostbackEvent, FollowEvent
)
from message import follow_message, select_video_sites, select_pornhub, select_xvideos, select_xhamster
import os

app = Flask(__name__)

line_bot_api = LineBotApi('hH+6VJCMqKVDd3at4IEoMfAraBQT3ss4SrA7PyhA3VlqO/iAEVYSsuzRExaiQRqPMeiX7kF1kAydsY3hRG7l/70ZXgqFpFj/mZ9Ojb1GvqXGcy+RJGu5wF9ScxJc7MUqU2hs7Ll75olXPzwCYzRQbgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a40ec37046fa7461f919c622271fc6c6')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
    


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text)
    message = select_video_sites()
    line_bot_api.reply_message(
        event.reply_token,
        messages=message
    )
    
@handler.add(PostbackEvent)
def postback(event):
    #pornhub
    if event.postback.data == 'pornhub':
        message = select_pornhub()
        line_bot_api.reply_message(
            event.reply_token,
            messages=message
        )
    if event.postback.data == 'xvideos':
        message = select_xvideos()
        line_bot_api.reply_message(
            event.reply_token,
            messages=message
        )
    if event.postback.data == 'spankbang':
        message = select_xhamster()
        line_bot_api.reply_message(
            event.reply_token,
            messages=message
        )

@handler.add(FollowEvent)
def join_talk(event):
    your_id = event.source.user_id
    message2 = select_video_sites()
    message, stump = follow_message()
    line_bot_api.push_message(
        your_id,messages=[message,stump,message2]
    )

if __name__ == "__main__":
    app.run()
    # port = 5000
    # app.run(host="0.0.0.0", port=port)

#$env:FLASK_ENV = "development"
#$env:FLASK_APP = "main.py"
#flask run