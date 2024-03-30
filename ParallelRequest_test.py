# https://www.zenrows.com/blog/python-parallel-requests#what-are-parallel-requests-in-python
# https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor

import requests

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup


def parse_url(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    title_element = soup.find("title")
    title = title_element.text

    return title


if __name__ == "__main__":

    urls = [
        "https://scrapeme.live/shop/page/1/",
        "https://scrapeme.live/shop/page/2/",
        "https://scrapeme.live/shop/page/3/",
        "https://scrapeme.live/shop/page/4/",
        "https://scrapeme.live/shop/page/5/",
        "https://scrapeme.live/shop/page/6/",
        "https://scrapeme.live/shop/page/7/",
        "https://scrapeme.live/shop/page/8/",
    ]

    with ThreadPoolExecutor(max_workers=4) as executor:
        test = executor.map(parse_url, urls)

    input(": ")
    for out in test:
        print(out)
