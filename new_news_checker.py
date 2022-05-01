import json


def check_if_new(portal, url):
    with open("json/last_urls.json", "r") as read_file:
        data = json.load(read_file)
    if data.get(portal) != url:
        data[portal] = url
        with open("json/last_urls.json", "w") as write_file:
            json.dump(data, write_file)
        return True
    return False