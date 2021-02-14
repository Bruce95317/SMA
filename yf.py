import os
import csv
import yfinance as yf

df = yf.download('AAPL', start='2015-01-01', end='2020-01-27')
df.to_csv('AAPL1.csv')
