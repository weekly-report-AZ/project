#!/Users/azuev/projects/weekly_report/env/bin/python3
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def talk_to_me(bot, update):
    now = datetime.datetime.today().strftime('%Y/%m/%d %H:%M')
    print(now)
    bot.send_message(chat_id=update.message.chat_id, text=now)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY1)
    dp = mybot.dispatcher
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()