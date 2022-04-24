from selenium.webdriver.common.by import By


def get_3dnews_news(driver):
    URL = "https://3dnews.ru/news"
    driver.get(URL)

    post = driver.find_element(By.CLASS_NAME, "marker_allfeed")
    post_id = post.get_attribute("id")

    title = post.find_element(By.CSS_SELECTOR, "h1").text
    description_select = post.find_elements(By.CSS_SELECTOR, "p")
    url = post.find_element(By.CLASS_NAME, "entry-header").get_attribute("href")

    description = ""
    for i in description_select:
        description += i.text + "\n"

    return {"title": title, "description": description, "url": url, "id": post_id}
