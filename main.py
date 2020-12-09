import telebot
import logging
import os
from bot import bot
from config import TELEGRAM_BOT_TOKEN
from flask import Flask, request
from telebot.types import Update


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) 

app = Flask(__name__)

@app.route(f'/{TELEGRAM_BOT_TOKEN}', methods=['POST'])
def getMessage():
    bot.process_new_updates([Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f'https://catch-wildfire-telegram-bot.herokuapp.com/{TELEGRAM_BOT_TOKEN}')
    return "!", 200


if __name__ == '__main__':
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()

    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

