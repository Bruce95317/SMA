# Description : use the dual moving average crossover to determin when to buy and sell stock

# import the library
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# laod the data
AAPL = pd.read_csv('AAPL1.csv')


# Create the simple moving average with a 30 day window (30 MA)
SMA30 = pd.DataFrame()
SMA30['Adj Close Price'] = AAPL['Adj Close'].rolling(window=30).mean()

# Create the simple moving 100 day average (100 MA)

SMA100 = pd.DataFrame()
SMA100['Adj Close Price'] = AAPL['Adj Close'].rolling(window=100).mean()

#plt.figure(figsize=(12.3, 4.5))
#plt.plot(AAPL['Adj Close'], label='AAPL')
#plt.plot(SMA30['Adj Close Price'], label='SMA30')
#plt.plot(SMA100['Adj Close Price'], label='SMA100')
#plt.title('Apple Adj. Close Price History')
# plt.xlabel('Date')
#plt.ylabel('Adj Close Price USD($)')
#plt.legend(loc='upper left')
# plt.show()

# Create a new data frame ot store all the data
data = pd.DataFrame()
data['AAPL'] = AAPL['Adj Close']
data['SMA30'] = SMA30['Adj Close Price']
data['SMA100'] = SMA100['Adj Close Price']

# Create a function to signal when to buy and when to sell the asset/stock


def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1

    for i in range(len(data)):
        if data['SMA30'][i] > data['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(data['AAPL'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['SMA30'][i] < data['SMA100'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['AAPL'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return(sigPriceBuy, sigPriceSell)


# Store the buy and sell data into a variable
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

plt.figure(figsize=(12.2, 4.5))
plt.plot(data['AAPL'], label='AAPL_Close', alpha=0.35)
plt.plot(data['SMA30'], label='SMA30', alpha=0.35)
plt.plot(data['SMA100'], label='SMA100', alpha=0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], color='green',
            label='Buy Signal', marker='^', alpha=1)
plt.scatter(data.index, data['Sell_Signal_Price'], color='red',
            label='sell Signal', marker='v', alpha=1)

plt.xticks(rotation=45)
plt.title('Close Price Buy and Sell Signals')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price ($)', fontsize=18)
plt.legend(loc='upper left')
plt.show()
