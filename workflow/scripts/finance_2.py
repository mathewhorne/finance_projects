# Youtube tutorial
# https://www.youtube.com/watch?v=2BrpKpWwT2A

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf 
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as pdr
import os

style.use('ggplot')

# Tiingo, Alpha Vantage API
os.environ['TIINGO_API_KEY'] = 'f718b78c5bb3a9dd888b85ccd214d81f50d8d180'
os.environ['ALPHAVANTAGE_API_KEY'] = 'TVZ8EV0TE4HEFJMV'

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2020, 6, 30)

df = pdr.get_data_tiingo('MSFT', api_key = os.getenv('TIINGO_API_KEY'))

df.to_csv('../../data/msft.csv')

df = pd.read_csv('../../data/msft.csv', parse_dates = True, index_col = 1)

df['adjClose'].plot()

# IEX $9 per month

# Alpha Vantage
# Here is your API key: TVZ8EV0TE4HEFJMV

aapl_1 = pdr.DataReader('AAPL', 'av-daily-adjusted', 
                        start = dt.datetime(2000, 1, 1), 
                        end = dt.datetime(2021, 6, 30),
                        api_key = os.getenv('ALPHAVANTAGE_API_KEY'))

aapl_1.to_csv('../../data/aapl_1.csv')

aapl_1 = pd.read_csv('../../data/aapl_1.csv', 
                     parse_dates = True,
                     index_col = 0)

aapl_1['adjusted close'].plot()

ax1 = plt.subplot2grid((2, 1), (0, 0), rowspan = 1, colspan = 1)
ax2 = plt.subplot2grid((2, 1), (1, 0), rowspan = 1, colspan = 1, sharex = ax1)

ax1.plot(aapl_1.index, aapl_1['adjusted close'])
ax2.bar(aapl_1.index, aapl_1['volume'])

# Tutorial 3

df['100ma'] = df['adjClose'].rolling(window = 100).mean()
df.dropna(inplace = True)
df.head()

df['100ma'] = df['adjClose'].rolling(window = 100, min_periods = 0).mean()

df.head()

ax1 = plt.subplot2grid((6, 1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6, 1), (5,0), rowspan = 1, colspan = 1, sharex = ax1) 

ax1.plot(df.index, df['adjClose'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['volume'])

# Tutorial 4

df_ohlc = df['adjClose'].resample('10D').ohlc()
df_volume = df['volume'].resample('10D').sum()

df_ohlc.reset_index(inplace = True)

df_ohlc['date'] = df_ohlc['date'].map(mdates.date2num)

df_ohlc

mpf.plot(df, type = 'candle', style = 'charles',
            title = '',
            ylabel = '',
            ylabel_lower = '',
            figratio = (25,10),
            figscale = 1,
            mav = 50,
            volume = True)