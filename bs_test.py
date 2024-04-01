from bs4 import BeautifulSoup
import requests
import re

url = "https://www.netonnet.se/art/vitvaror/mikrovagsugn/andersson-mikrovagsugn-meo-2-6/226770.18008"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
}

soup = BeautifulSoup(
    requests.get(
        url,
        headers=headers,
    ).content,
    "lxml",
)

# Inget pris, requests kör inte javascript. RIP
print(soup.get_text())

# 1st group matches a string of digits starting with / and ending with a dot.
pattern = ".*\/(\d*)\."

art_nr = re.search(pattern, url)

print(art_nr.group(1))

price = soup.find("h2", {"name": f"{art_nr}-price"}).get_text(strip=True)

print(price)
