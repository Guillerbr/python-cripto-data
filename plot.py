import requests, json
import matplotlib.pyplot
import pandas as pandas
import time

fig = plt.figure(figsize=10,10)

ax = fig.gca()

grava - open("ticker.cvs","w")
grava.write("bid,ask/")