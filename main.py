import os
import pandas as pd
import numpy as np
from itertools import islice
import random
from datetime import datetime
from get_quote import get_quote


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
