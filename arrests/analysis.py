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
        return np.unique(self.types)

    def genMonthlyArrestProportions(self, crime_type='all'):
        # Generate a list of the number of arrests per month
        # This is used to generate the monthly arrest proportion plot
        #aaaaaa the data isn't in date order
        if crime_type == 'all':
            dates = self.dates
            arrests = self.arrests

        else:
            dates = self.dates[self.types == crime_type]
            arrests = self.arrests[self.types == crime_type]

        monthly_crimes = [0 for _ in range(7 * 12 - 1)]
        monthly_arrests = [0 for _ in range(7 * 12 - 1)]
        months = [i for i in range(7 * 12 - 1)]
        pd_dates = pd.to_datetime(dates)
        for i in tqdm(range(len(dates)), desc=('Generating monthly arrest proportions for ' + crime_type)):
            month = ((pd_dates[i].month - 1) + pd_dates[i].year * 12) -(2015 * 12)
            monthly_crimes[month] += 1
            if arrests[i] == True:
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

    def plotMonthlyArrestProportions(self, monthly_arrest_proportion, crime_type='all'):
        months = self.months[~np.isnan(monthly_arrest_proportion)]
        monthly_arrest_proportion = monthly_arrest_proportion[~np.isnan(monthly_arrest_proportion)]

        parameters = pd.DataFrame(index=[crime_type], columns=['all_a', 'all_b', 'all_c', 'pre_a', 'pre_b', 'pre_c', 'post_a', 'post_b', 'post_c'])
        # Plot the monthly arrest proportion
        def objective(x, a, b, c):
	        return a * x + b * x**2 + c
        # curve fit for all months
        popt, _ = curve_fit(objective, months, monthly_arrest_proportion)
        a, b, c = popt
        parameters['all_a'] = a
        parameters['all_b'] = b
        parameters['all_c'] = c
        print('all months')
        print('y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
        y_line = objective(months, a, b, c)

        # curve fit for prepandemic months (until march 2020)
        print('prepandemic')
        if months[months <= 2020.25].size > 0:
            popt, _ = curve_fit(objective, months[months <= 2020.25], monthly_arrest_proportion[months <= 2020.25])
            a, b, c = popt
            parameters['pre_a'] = a
            parameters['pre_b'] = b
            parameters['pre_c'] = c
            print('y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
            y_line_before = objective(months, a, b, c)
        else:
            y_line_before = np.array([0 for _ in range(len(months))])

        # curve fit for postpandemic months (after march 2020)
        if months[months >= 2020.25].size > 0:
            popt, _ = curve_fit(objective, months[months >= 2020.25], monthly_arrest_proportion[months >= 2020.25])
            a, b, c = popt
            parameters['post_a'] = a
            parameters['post_b'] = b
            parameters['post_c'] = c
            print('postpandemic')
            print('y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
            y_line_after = objective(months, a, b, c)
        else:
            y_line_after = np.array([0 for _ in range(len(months))])

        fig, ax = plt.subplots()
        plt.scatter(months, monthly_arrest_proportion)
         # create a line plot for the mapping function
        plt.plot(months, y_line, '--', color='red', label='all months')
        plt.plot(months, y_line_before, '--', color='blue', label='prepandemic')
        plt.plot(months, y_line_after, '--', color='green', label='postpandemic')
        plt.ylim(monthly_arrest_proportion.min() - 0.01, monthly_arrest_proportion.max() + 0.1)
        plt.title('Monthly Arrest Proportion ' + crime_type)
        plt.legend()
        plt.savefig('arrests/charts/per_crime_type/' + crime_type + '_proportion.png')
        return parameters