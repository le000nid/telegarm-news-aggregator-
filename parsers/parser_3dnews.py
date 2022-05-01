from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from models.telegram_post import TelegramPost
from strings import urls


def get_3dnews_news(driver):

    post = driver.find_element(By.CLASS_NAME, "marker_allfeed")

    title = post.find_element(By.CSS_SELECTOR, "h1").text
    description_select = post.find_elements(By.CSS_SELECTOR, "p")
    url = post.find_element(By.CLASS_NAME, "entry-header").get_attribute("href")

    description = "\n".join(elem.text for elem in description_select)

    return TelegramPost(title=title, description=description, url=url)
