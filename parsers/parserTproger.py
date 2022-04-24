from selenium.webdriver.common.by import By


def get_tproger_news(driver):
    URL = "https://tproger.ru/?sort=new"
    driver.get(URL)

    post = driver.find_element(By.CLASS_NAME, "article ")
    post_id = post.get_attribute("data-post")

    title = post.find_element(By.CLASS_NAME, "article__link").text
    description_select = post.find_elements(By.CSS_SELECTOR, "p")
    url = post.find_element(By.CLASS_NAME, "article__link").get_attribute("href")

    description = ""
    for i in description_select:
        description += i.text + "\n"

    return {"title": title, "description": description, "url": url, "id": post_id}
