# Youtube tutorial
# https://www.youtube.com/watch?v=2BrpKpWwT2A

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as pdr
import os

style.use('ggplot')

# Tiingo API
os.environ['TIINGO_API_KEY'] = 'f718b78c5bb3a9dd888b85ccd214d81f50d8d180'

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2020, 12, 31)

df = pdr.get_data_tiingo('MSFT', api_key = os.getenv('TIINGO_API_KEY'))

df.to_csv('../../data/msft.csv')

df = pd.read_csv('../../data/msft.csv', parse_dates = True, index_col = 1)

df['adjClose'].plot()

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

df_ohlc.head()

ax1 = plt.subplot2grid((6, 1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6, 1), (5,0), rowspan = 1, colspan = 1, sharex = ax1)


