import settings
import logging
#
from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
import telegram.update

logging.basicConfig(filename='bot.log',level=logging.INFO)

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}



def greet_user(update ,context):
    logging.info('start command received')
    print("start",context)
    update.message.reply_text('hello, user')

def talk_to_me(update, context):
    print(update.message.text)
    update.message.reply_text(update.message.text + ' reply')
    

def main():
    mybot = Updater(settings.KEY,use_context=True,request_kwargs=PROXY)
    logging.info("bot starting")
    mybot.dispatcher.add_handler(CommandHandler('start',greet_user))
    mybot.dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()    