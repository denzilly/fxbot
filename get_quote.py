import time
from datetime import datetime
from datetime import timedelta

import requests
from bs4 import BeautifulSoup
from idex.client import Client


api_key = "api:imwH2zDW_5rmrLZHYgQr9"


def get_quote_webrates():
    timestamp = datetime.now()
    URL = "https://webrates.truefx.com/rates/connect.html?f=html"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    el = soup.find_all('td')
    rate = el[2].text + el[3].text

    print(f"[{timestamp}]  ---  Pair {el[0].text} is trading at {el[2].text + el[3].text}")

    return rate, datetime.now()


def get_quote_idex():

    client = Client(api_key, address, private_key)

    #get currencies
currencies = client.get_currencies()