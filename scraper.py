from typing import List

from bs4 import BeautifulSoup
import requests

import logger


# get trending keyword from 3rd party website cuz twitter api is crazy expensive
def get_trending_keywords(url: str, return_elements=10) -> List[str]:
    try:
        page = requests.get(url)
    except requests.exceptions.ConnectionError:
        logger.log(f"Connection error")
    except requests.exceptions.Timeout:
        logger.log("Timeout error")
    except requests.exceptions.RequestException:
        logger.log("Request Exception error")
    except Exception:
        logger.log("Unknown error")

    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find("div", {"class": "trend-card"}).find_all("a")

    tags = []
    for tag in links:
        tags.append(tag.text)

    logger.log(f"Scraped trending words: {tags[:return_elements]}")
    return tags[:return_elements]
