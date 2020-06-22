import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import time



def get_quote(seconds):
    now = datetime.now()

    while datetime.now() <= now + timedelta(seconds=seconds):
        URL = "https://webrates.truefx.com/rates/connect.html?f=html"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        el = soup.find_all('td')
        print(f"[{datetime.now()}]  ---  Pair {el[0].text} is trading at {el[2].text + el[3].text}")
        time.sleep(2)



get_quote(100)






