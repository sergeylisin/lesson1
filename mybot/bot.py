import logging

from telegram.ext import Updater,CommandHandler
import telegram.update

logging.basicConfig(filename='bot.log',level=logging.INFO)

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}



def greet_user(update ,context):
    logging.info('получена команда start')
    print("start",context)
    

def main():
    mybot = Updater('1521578217:AAEnXxtMOFj1Y_1IhHAjVQBR5sRtRxVpC2w',use_context=True,request_kwargs=PROXY)
    logging.info("бот стартовал")
    mybot.dispatcher.add_handler(CommandHandler('start',greet_user))
    mybot.start_polling()
    mybot.idle()

main()    