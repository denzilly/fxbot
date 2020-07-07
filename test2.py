from huobi.client.market import MarketClient
from huobi.model.market import *


def callback(trade_event: 'TradeDetailEvent'):
    print("---- trade_event:  ----")
    trade_event.print_object()
    print()

market_client = MarketClient()
market_client.sub_trade_detail("btcusdt", callback)

print("we got here")