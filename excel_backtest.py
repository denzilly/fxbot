import os
import pandas as pd
import numpy as np
from itertools import islice
import random
from datetime import datetime
import time

class Portfolio:

    def __init__(self, base_value, hold_value, hold_currency, log):
        self.base_value = base_value
        self.hold_value = hold_value
        self.hold_currency = hold_currency
        self.log = log

    def buy(self, base_value, rate):
        #Buy EUR / Sell USD
        self.base_value = self.hold_value / rate
        self.hold_value = self.base_value
        self.hold_currency = "EUR"
        self.log.append([datetime.now(), "BUY EUR", rate, self.base_value])
        print(f"you bought EUR at {rate}, you are now LONG EUR with a portfolio value of {self.base_value} EUR")
        print(f"basevalue is now {self.base_value} EUR")
        print(f"holdvalue is now {self.hold_value} EUR")



    def sell(self, base_value, rate):
        #Sell EUR / Buy USD
        self.base_value = self.base_value
        self.hold_value = self.base_value * rate
        self.hold_currency = "USD"
        self.log.append([datetime.now(), "SELL EUR", rate, self.base_value])
        print(f"you sold EUR at {rate}, you are now SHORT EUR with a portfolio value of {self.base_value} EUR")
        print(f"basevalue is now {self.base_value} EUR")
        print(f"holdvalue is now {self.hold_value} USD")




mywallet = Portfolio(100000, 100000, "EUR", [])





dir_path = os.path.dirname(os.path.realpath(__file__)) + "\data\\"
print(dir_path)


df_btest = pd.read_excel(dir_path + '2019_eurusd.xlsx')

for index, row in islice(df_btest.iterrows(), 370000):
    randomizer = random.randint(1,100)

    if randomizer == 69:
        print("#################################### HIT ###############################")
        if mywallet.hold_currency == "EUR":
            mywallet.sell(mywallet.base_value, row['B'])

        else:
            mywallet.buy(mywallet.base_value, row['O'])
ff

for x in mywallet.log:
    print(f"{x[1]} AT {x[2]}, NEW PORTFOLIO VALUE IS {x[3]} EUR")