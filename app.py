import os
from datetime import datetime
from __future__ import unicode_literals
from flask import Flask, abort, request

import sys
import json
import configparser
from typing import Text

# https://github.com/line/line-bot-sdk-python
import urllib
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models.events import Event
from linebot.models.send_messages import ImageSendMessage, VideoSendMessage






app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == '寶貝':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="去吃多一點")
        )
    if event.message.text == '土味情話':
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
            original_content_url = 'https://drive.google.com/uc?export=view&id=1ZaaG7tBpqrfFRaHBkjg2lafdZzYaWETS',
            preview_image_url = 'https://drive.google.com/uc?export=view&id=1ZaaG7tBpqrfFRaHBkjg2lafdZzYaWETS'
            )
        )
    if event.message.text == '長庚妖風好大':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("保護好你的菠蘿麵包!!!")
        )
    if event.message.text == '考研究所好累':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("寶貝加油!，其他人都是砲灰!")
        )
    if event.message.text == '掰掰':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("寶貝掰掰~")
        )
    if event.message.text == '要不要去找芸沛老師':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("先去吃海底撈再說")
        )
