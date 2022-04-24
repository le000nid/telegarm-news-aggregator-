from selenium.webdriver.common.by import By


def get_cnews_news(driver):
    URL = "https://www.cnews.ru/news"
    driver.get(URL)

    post = driver.find_element(By.CLASS_NAME, "ani-postname")
    url = post.get_attribute("href")

    title = post.text

    return {"title": title, "url": url}
