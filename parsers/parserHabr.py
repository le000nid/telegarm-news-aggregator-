from selenium.webdriver.common.by import By


def get_habr_news(driver):
    URL = "https://habr.com/ru/all/"
    driver.get(URL)

    post = driver.find_element(By.CLASS_NAME, "tm-articles-list__item")
    post_id = post.get_attribute("id")

    title = post.find_element(By.CLASS_NAME, "tm-article-snippet__title-link").text
    description_select = post.find_elements(By.CSS_SELECTOR, "p")
    url = post.find_element(By.CLASS_NAME, "tm-article-snippet__readmore").get_attribute("href")

    description = ""
    for i in description_select:
        description += i.text + "\n"

    return {"title": title, "description": description, "url": url, "id": post_id}
