from bs4 import BeautifulSoup
import requests
import re
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-u", "--url", required=True)
args = parser.parse_args()


# Clean everything after ?

url = args.url

# Clean url
pattern = "\?.*$"

url = re.sub(pattern, "", url)

print(url)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
}

soup = BeautifulSoup(
    requests.get(
        url,
        headers=headers,
    ).content,
    "html5lib",
)

# Inget pris, requests kör inte javascript. RIP
print(soup.get_text())


# price = soup.find("h2", {"name": f"{art_nr}-price"}).get_text(strip=True)

# print(price)
