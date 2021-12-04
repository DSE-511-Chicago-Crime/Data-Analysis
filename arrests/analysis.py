import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import pandas as pd
from tqdm import tqdm
from scipy.optimize import curve_fit

class analyzeArrests:
    def __init__(self):
        self.dates = np.load('arrests/dates.npy')
        self.arrests = np.load('arrests/arrests.npy')
        self.types = np.load('arrests/types.npy', allow_pickle=True)

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
    def get_types(self):
        return self.types
        
    def genMonthlyArrestProportions(self, type='all'):
        # Generate a list of the number of arrests per month
        # This is used to generate the monthly arrest proportion plot
        #aaaaaa the data isn't in date order
        if type == 'all':
            dates = self.dates
            arrests = self.arrests

        else:
            dates = self.dates[self.types == type]
            arrests = self.arrests[self.types == type]

        monthly_crimes = [1 for _ in range(7 * 12 - 1)]
        monthly_arrests = [1 for _ in range(7 * 12 - 1)]
        months = [i for i in range(7 * 12 - 1)]
        pd_dates = pd.to_datetime(dates)
        for i in tqdm(range(len(dates)), desc='Generating monthly arrest proportions'):
            month = ((pd_dates[i].month - 1) + pd_dates[i].year * 12) -(2015 * 12)
            monthly_crimes[month] += 1
            if arrests[i] == 1:
                monthly_arrests[month] += 1
        monthly_crimes = np.array(monthly_crimes)
        monthly_arrests = np.array(monthly_arrests)
        self.months = np.array(months)
        self.months = self.months/12 + 2015
        monthly_arrest_proportion = np.divide(monthly_arrests, monthly_crimes)
        return monthly_arrest_proportion

    def genMonthlyArrestProportionsFast(self):
        self.months = np.array([i for i in range(7 * 12 - 1)])
        self.months = self.months/12 + 2015
        monthly_arrest_proportion = np.load('arrests/monthly_arrest_proportion.npy')
        return monthly_arrest_proportion

    def plotMonthlyArrestProportions(self, monthly_arrest_proportion):

        # Plot the monthly arrest proportion
        def objective(x, a, b, c):
	        return a * x + b * x**2 + c
        # curve fit for all months
        popt, _ = curve_fit(objective, self.months, monthly_arrest_proportion)
        a, b, c = popt
        print('all months')
        print('y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
        y_line = objective(self.months, a, b, c)

        # curve fit for prepandemic months (until march 2020)
        popt, _ = curve_fit(objective, self.months[0:63], monthly_arrest_proportion[0:63])
        a, b, c = popt
        print('prepandemic')
        print('y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
        y_line_before = objective(self.months, a, b, c)

        # curve fit for postpandemic months (after march 2020)
        popt, _ = curve_fit(objective, self.months[63:], monthly_arrest_proportion[63:])
        a, b, c = popt
        print('postpandemic')
        print('y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
        y_line_after = objective(self.months, a, b, c)

        fig, ax = plt.subplots()
        plt.scatter(self.months, monthly_arrest_proportion)
         # create a line plot for the mapping function
        plt.plot(self.months, y_line, '--', color='red', label='all months')
        plt.plot(self.months, y_line_before, '--', color='blue', label='prepandemic')
        plt.plot(self.months, y_line_after, '--', color='green', label='postpandemic')
        plt.ylim(monthly_arrest_proportion.min() - 0.1, monthly_arrest_proportion.max() + 0.1)
        plt.title('Monthly Arrest Proportion')
        plt.legend()
        plt.show()