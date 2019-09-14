import matplotlib.pyplot as plt

from coinmarketcap import Market
import pandas as pd


def recebe():
    market = Market()
    ticker = market.ticker()
    data = ticker['data']['quotes']['BRL']['price']
    btc = data['1']

return btc

    print(recebe())