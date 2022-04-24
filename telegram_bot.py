import time
import telebot

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from startParser import start_parser

token = "5225839118:AAEh98hX3MpquwzmXbSlc8GbwQeN4ZqQhZI"
channel = "@le0news"
bot = telebot.TeleBot(token)

a=True

@bot.message_handler(commands=["start"])
def start(message):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    last_habr_post_id = None
    last_tproger_post_id = None
    last_cnews_post_url = None
    last_3dnews_post_id = None

    while True:
        # В pycharm-е оказывается нет регионов :(
        news = start_parser(driver)

        # region Habr
        post = news.get("habr")
        if last_habr_post_id != post.get("id"):
            title = post.get("title")
            description = post.get("description")
            url = post.get("url")
            bot.send_message(channel, f"{title}\n\n{description}\n{url}")
        last_habr_post_id = post.get("id")
        # endregion

        # region Tproger
        post = news.get("tproger")
        if last_tproger_post_id != post.get("id"):
            title = post.get("title")
            description = post.get("description")
            url = post.get("url")
            bot.send_message(channel, f"{title}\n\n{description}\n{url}")
        last_tproger_post_id = post.get("id")
        # endregion

        # region Cnews
        post = news.get("cnews")
        if last_cnews_post_url != post.get("url"):
            title = post.get("title")
            url = post.get("url")
            bot.send_message(channel, f"{title}\n\n{url}")
        last_cnews_post_url = post.get("url")
        # endregion

        # region 3dnews
        post = news.get("3dnews")
        if last_3dnews_post_id != post.get("id"):
            title = post.get("title")
            description = post.get("description")
            url = post.get("url")
            bot.send_message(channel, f"{title}\n\n{description}\n{url}")
        last_3dnews_post_id = post.get("id")
        # endregion

        time.sleep(30)


bot.polling()
