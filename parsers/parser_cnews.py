from selenium.webdriver.common.by import By
from models.telegram_post import TelegramPost


def get_cnews_news(driver):

    post = driver.find_element(By.CLASS_NAME, "ani-postname")
    url = post.get_attribute("href")

    title = post.text

    return TelegramPost(title=title, url=url, description=None)
