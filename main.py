import matplotlib.pyplot as plt

from coinmarketcap import Market
import pandas as pd


def recebe():
    market = Market()
    ticker = market.ticker(convert="BRL")
    data = ticker['data']['1']['quotes']['USD']['price']
    btc = data
    return btc

print(recebe())