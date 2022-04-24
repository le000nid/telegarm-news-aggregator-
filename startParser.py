
from parsers.parser3dnews import get_3dnews_news
from parsers.parserHabr import get_habr_news
from parsers.parserTproger import get_tproger_news
from parsers.parserCnews import get_cnews_news


def start_parser(driver):

    result = {"habr": get_habr_news(driver),
              "tproger": get_tproger_news(driver),
              "cnews": get_cnews_news(driver),
              "3dnews": get_3dnews_news(driver)}

    return result
