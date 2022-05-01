from selenium.webdriver.common.by import By
from models.telegram_post import TelegramPost


def get_habr_news(driver):

    post = driver.find_element(By.CLASS_NAME, "tm-articles-list__item")

    title = post.find_element(By.CLASS_NAME, "tm-article-snippet__title-link").text
    description_select = post.find_elements(By.CSS_SELECTOR, "p")
    url = post.find_element(By.CLASS_NAME, "tm-article-snippet__readmore").get_attribute("href")

    description = "\n".join(elem.text for elem in description_select)

    return TelegramPost(title=title, description=description, url=url)
