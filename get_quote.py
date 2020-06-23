import time
from datetime import datetime
from datetime import timedelta

import requests
from bs4 import BeautifulSoup


def get_quote():
    timestamp = datetime.now()
    URL = "https://webrates.truefx.com/rates/connect.html?f=html"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    el = soup.find_all('td')
    rate = el[2].text + el[3].text

    print(f"[{timestamp}]  ---  Pair {el[0].text} is trading at {el[2].text + el[3].text}")

    return rate, datetime.now()
