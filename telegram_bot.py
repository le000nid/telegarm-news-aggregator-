import time
import telebot

from selenium import webdriver
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

        for url, resource_parser in zip((urls.URL_habr, urls.URL_3dnews, urls.URL_cnews, urls.URL_tproger), (get_habr_news, get_3dnews_news, get_cnews_news, get_tproger_news)):
            try:
                driver.get(url)
                news = resource_parser(driver)
                if new_news_checker.check_if_new(url, news.url):
                    bot.send_message(channel, news.as_telegram_message())
            except Exception as e:
                print(f'Что то не так:\n{str(e)}')

        time.sleep(30)


if __name__ == '__main__':
    bot.polling()
