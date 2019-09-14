import matplotlib.pyplot as plt

from coinmarketcap import Market
import pandas as pd
import time

def recebe():
    market = Market()
    ticker = market.ticker(convert="BRL")
    data = ticker['data']['1']['quotes']['USD']['price']
    btc = data
    return btc

while True:

print("Price BTC -"recebe())
time.sleep(1)