import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import pandas as pd
from tqdm import tqdm
from scipy.optimize import curve_fit

class analyzeArrests:
    # initialize and read the numpy files needed
    def __init__(self):
        self.dates = np.load('arrests/dates.npy')
        self.arrests = np.load('arrests/arrests.npy')
        self.types = np.load('arrests/types.npy', allow_pickle=True)

        self.arrest_dates = self.dates[self.arrests == 1]
        self.weeks  = pd.date_range(start="2019-01-01",end="2021-11-14", freq='W').to_numpy()

    # weekly histogram of arrests and crimes 2019 - present
    def plotArrestsToCrimesOverTime(self):
        fig, ax = plt.subplots()
        plt.hist(self.dates, bins=self.weeks, label='Crimes')
        plt.hist(self.arrest_dates, bins=self.weeks, label='Arrests')
        plt.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
        fig.autofmt_xdate()
        plt.title('Arrests and crimes per week')
        plt.legend()
        plt.show()

    # list of types of crimes
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

        # for each month, count the number of crimes and arrests
        for i in tqdm(range(len(dates)), desc=('Generating monthly arrest proportions for ' + crime_type)):
            month = ((pd_dates[i].month - 1) + pd_dates[i].year * 12) -(2015 * 12)
            monthly_crimes[month] += 1
            if arrests[i] == True:
                monthly_arrests[month] += 1
        monthly_crimes = np.array(monthly_crimes)
        monthly_arrests = np.array(monthly_arrests)
        self.months = np.array(months)
        self.months = self.months/12 + 2015
        #proportion 
        monthly_arrest_proportion = np.divide(monthly_arrests, monthly_crimes)
        return monthly_arrest_proportion
    # for testing - prelaoded results
    def genMonthlyArrestProportionsFast(self):
        self.months = np.array([i for i in range(7 * 12 - 1)])
        self.months = self.months/12 + 2015
        monthly_arrest_proportion = np.load('arrests/monthly_arrest_proportion.npy')
        return monthly_arrest_proportion
    # graphs of monthly arrest proportions
    # regression lines
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
        plt.axvline(x=2020.25, color='orange', linestyle='-' , label='March 2020')
        plt.ylim(monthly_arrest_proportion.min() - 0.01, monthly_arrest_proportion.max() + 0.1)
        plt.title('Monthly Arrest Proportion ' + crime_type)
        plt.legend()
        plt.savefig('arrests/charts/per_crime_type/' + crime_type + '_proportion.png')
        return parameters
    
    #for testing - preloaded results
    def setParameters(self, parameters=None):
        if parameters is None:
            self.parameters = pd.read_csv('arrests/parameters.csv', index_col=0)
        else:
            self.parameters = parameters

    # sort months by how far off the curve they are
    # return a string of this sorting
    def findOutliers(self, proportions, crimetype='all', parameters=None):
        months = self.months[~np.isnan(proportions)]
        proportions = proportions[~np.isnan(proportions)]

        def objective(x, a, b, c):
	        return a * x + b * x**2 + c
        if parameters is None:        
            paraemeters = self.parameters
        
        a = parameters.loc[crimetype, 'all_a']
        b = parameters.loc[crimetype, 'all_b']
        c = parameters.loc[crimetype, 'all_c']
        print(a, b, c)

        errors = {}
        # find square error
        y_pred = objective(months, a, b, c)
        se = np.square(y_pred - proportions)

        #calculate sum squares error
        sse = np.sum(se)
        output = 'crime type: ' + crimetype + '\n'
        output += 'SUM SQUARED ERROR: ' + str(sse) + '\n'
        
        #associate months with errors
        j = 0
        for i in se:
            errors[i] = months[j]
            j += 1

        # sort
        output += 'months with highest error:' + '\n'
        for i in sorted(errors.keys()):
            output += (str(errors[i]) + ' error ' + str(i) + '\n')
        return output





