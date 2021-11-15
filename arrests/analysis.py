import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import pandas as pd

class analyzeArrests:
    def __init__(self):
        self.dates = np.load('arrests/dates.npy')
        self.arrests = np.load('arrests/arrests.npy')

        self.arrest_dates = self.dates[self.arrests == 1]
        self.weeks  = pd.date_range(start="2019-01-01",end="2021-11-14", freq='W').to_numpy()

    def plotArrestsToCrimesOverTime(self):
        fig, ax = plt.subplots()
        plt.hist(self.dates, bins=self.weeks, label='Crimes')
        plt.hist(self.arrest_dates, bins=self.weeks, label='Arrests')
        plt.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
        fig.autofmt_xdate()
        plt.title('Arrests and crimes per week')
        plt.legend()
        plt.show()