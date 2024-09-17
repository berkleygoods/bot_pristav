import logging
from telegram.ext import Updater, CommandHandler
from scrfp import parse_data

logging.basicConfig(filename='bot.pristav', level=logging.INFO)
PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater("5046863773:AAEiiHs9-1YPrAYAVTqcyKgtG29JPrgro2Y", use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет! Я Бот-пристав. Проверим ваши задолженности?')
    update.message.reply_text('Введите ваше Имя')
    name = update.message.text
    update.message.reply_text('Введите вашу фамилию')

    parse_data(update.message.text)

main()