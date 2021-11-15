import pandas
import numpy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


df = pandas.read_csv('./data/combineddata.csv')

df['date'] = pandas.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S+00:00')

dates = df['date'].to_numpy()
arrests = df['arrest'].to_numpy()
arrest_dates = dates[arrests == 1]
weeks  = pandas.date_range(start="2019-01-01",end="2021-01-01", freq='W').to_numpy()

fig, ax = plt.subplots()
plt.hist(dates, bins=weeks, label='Crimes')
plt.hist(arrest_dates, bins=weeks, label='Arrests')
plt.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.title('Arrests and crimes per week')
plt.legend()
plt.show()

