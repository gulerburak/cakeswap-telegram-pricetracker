from telegram import update
from telegram.ext import *
from scraper import Scraper
API_KEY = '1611761709:AAG7QlzKJuRYbUS46kv3sXbuzQOHzHMqfqo'


def request(requested):
    currency1 = requested
    print(currency1)
    currency2 = "BUSD"
    exchange = "https://exchange.pancakeswap.finance/#/swap"

    scraper = Scraper(url=exchange)
    scraper.select_pair(currency1=currency1, currency2=currency2)

    old_value = None
    while True:
        data = scraper.get_pair_price()
        if old_value == data:
            break
        else:
            print("Saving data:", data, format)
            return data


def start(update, context):
    update.message.reply_text('s.a')
    update.message.reply_text('Büyük harfle istediğiniz koinin kısaltmasını girin')
    print("New user joined")


def text(update, context):
    msg = request(update.message.text)
    print(msg)
    update.message.reply_text(msg)


def main():
    updater = Updater(API_KEY)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, text))


    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
