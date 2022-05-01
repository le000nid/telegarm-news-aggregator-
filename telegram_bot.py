import time
import telebot

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import new_news_checker
from parsers.parser_3dnews import get_3dnews_news
from parsers.parser_cnews import get_cnews_news
from parsers.parser_habr import get_habr_news
from parsers.parser_tproger import get_tproger_news
from strings import urls, keys

token = keys.BOT_TOKEN
channel = keys.BOT_CHANNEL
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    while True:

        try:
            driver.get(urls.URL_habr)
            habr = get_habr_news(driver)
            if new_news_checker.check_if_new("habr", habr.url):
                bot.send_message(channel, habr.as_telegram_message())
        except:  # тут не стал указывать исключения, слишком много всего может выпасть
            print("habr упал")

        try:
            driver.get(urls.URL_tproger)
            tproger = get_tproger_news(driver)
            if new_news_checker.check_if_new("tproger", tproger.url):
                bot.send_message(channel, tproger.as_telegram_message())
        except:
            print("tproger упал")

        try:
            driver.get(urls.URL_cnews)
            cnews = get_cnews_news(driver)
            if new_news_checker.check_if_new("cnews", cnews.url):
                bot.send_message(channel, cnews.as_telegram_message())
        except:
            print("cnews упал")

        try:
            driver.get(urls.URL_3dnews)
            news3d = get_3dnews_news(driver)
            if new_news_checker.check_if_new("3dnews", news3d.url):
                bot.send_message(channel, news3d.as_telegram_message())
        except:
            print("3dnews упал")

        time.sleep(30)


if __name__ == '__main__':
    bot.polling()
