#Domestic Chicago Districts
#Holland Hysmith
#DSE Chicago Crime Project

#Importing packages necessary for data analysis.
import os
import pandas as pd
from csv import reader
import matplotlib.pyplot as plt
import numpy as np
import csv

class analysis:
    def __init__(self):
        #Printing current working directory.
        #Creating empty lists.
        self.date_2015 = []
        self.arrest_2015 = []
        self.domestic_2015 = []
        self.district_2015 = []

        self.date_2016 = []
        self.arrest_2016 = []
        self.domestic_2016 = []
        self.district_2016 = []

        self.date_2017 = []
        self.arrest_2017 = []
        self.domestic_2017 = []
        self.district_2017 = []

        self.date_2018 = []
        self.arrest_2018 = []
        self.domestic_2018 = []
        self.district_2018 = []

        self.date_2019 = []
        self.arrest_2019 = []
        self.domestic_2019 = []
        self.district_2019 = []

        self.date_2020 = []
        self.arrest_2020 = []
        self.domestic_2020 = []
        self.district_2020 = []

        self.date_2021 = []
        self.arrest_2021 = []
        self.domestic_2021 = []
        self.district_2021 = []

    def list_maker(self):
        #Open the file in read mode.
        filename = open('./data/2015_crime.csv', 'r')
    
        #Creating dictreader object.
        file = csv.DictReader(filename)
    
        #Iterating over each row and append
        #values to empty list.
        for col in file:
            self.date_2015.append(col['date'])
            self.arrest_2015.append(col['arrest'])
            self.domestic_2015.append(col['domestic'])
            self.district_2015.append(col['district'])

        
        #Open the file in read mode
        filename = open('./data/2016_crime.csv', 'r')
    
        #Creating dictreader object
        file = csv.DictReader(filename)
    
        #Iterating over each row and append
        #values to empty list
        for col in file:
            self.date_2016.append(col['date'])
            self.arrest_2016.append(col['arrest'])
            self.domestic_2016.append(col['domestic'])
            self.district_2016.append(col['district'])
        
        #Open the file in read mode
        filename = open('./data/2017_crime.csv', 'r')
    
        #Creating dictreader object
        file = csv.DictReader(filename)
    
        #Iterating over each row and append
        #values to empty list
        for col in file:
            self.date_2017.append(col['date'])
            self.arrest_2017.append(col['arrest'])
            self.domestic_2017.append(col['domestic'])
            self.district_2017.append(col['district'])
        
        #Open the file in read mode
        filename = open('./data/2018_crime.csv', 'r')
    
        #Creating dictreader object
        file = csv.DictReader(filename)
    
        #Iterating over each row and append
        #values to empty list
        for col in file:
            self.date_2018.append(col['date'])
            self.arrest_2018.append(col['arrest'])
            self.domestic_2018.append(col['domestic'])
            self.district_2018.append(col['district'])

        #Open the file in read mode
        filename = open('./data/2019_crime.csv', 'r')
    
        #Creating dictreader object
        file = csv.DictReader(filename)
    
        #Iterating over each row and append
        #values to empty list
        for col in file:
            self.date_2019.append(col['date'])
            self.arrest_2019.append(col['arrest'])
            self.domestic_2019.append(col['domestic'])
            self.district_2019.append(col['district'])

        #Open the file in read mode
        filename = open( './data/2020_crime.csv', 'r')
    
        #Creating dictreader object
        file = csv.DictReader(filename)
    
        #Iterating over each row and append
        #values to empty list
        for col in file:
            self.date_2020.append(col['date'])
            self.arrest_2020.append(col['arrest'])
            self.domestic_2020.append(col['domestic'])
            self.district_2020.append(col['district'])

        #Open the file in read mode
        filename = open('./data/2021_crime.csv', 'r')
    
        #Creating dictreader object
        file = csv.DictReader(filename)

        #Iterating over each row and append
        #values to empty list
        for col in file:
            self.date_2021.append(col['date'])
            self.arrest_2021.append(col['arrest'])
            self.domestic_2021.append(col['domestic'])
            self.district_2021.append(col['district'])


    def district_domestic(self):
        
        #Arranging domestic cases by district into dictionary.
        district_domestic_2018 = dict(zip(self.date_2018, zip(self.domestic_2018, self.district_2018)))
        district_domestic_2019 = dict(zip(self.date_2019, zip(self.domestic_2019, self.district_2019)))
        district_domestic_2020 = dict(zip(self.date_2020, zip(self.domestic_2020, self.district_2020)))
        
        #Getting counts of domestic crimes in districts - Year 2018
        true_domestic_district_1_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '1')}
        counts_domestic_disctrict_1_18 =len(true_domestic_district_1_18)

        true_domestic_district_2_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '2')}
        counts_domestic_disctrict_2_18 =len(true_domestic_district_2_18)

        true_domestic_district_3_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '3')}
        counts_domestic_disctrict_3_18 =len(true_domestic_district_3_18)

        true_domestic_district_4_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '4')}
        counts_domestic_disctrict_4_18 =len(true_domestic_district_4_18)

        true_domestic_district_5_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '5')}
        counts_domestic_disctrict_5_18 =len(true_domestic_district_5_18)

        true_domestic_district_6_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '6')}
        counts_domestic_disctrict_6_18 =len(true_domestic_district_6_18)

        true_domestic_district_7_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '7')}
        counts_domestic_disctrict_7_18 =len(true_domestic_district_7_18)

        true_domestic_district_8_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '8')}
        counts_domestic_disctrict_8_18 =len(true_domestic_district_8_18)

        true_domestic_district_9_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '9')}
        counts_domestic_disctrict_9_18 =len(true_domestic_district_9_18)

        true_domestic_district_10_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '10')}
        counts_domestic_disctrict_10_18 =len(true_domestic_district_10_18)

        true_domestic_district_11_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '11')}
        counts_domestic_disctrict_11_18 =len(true_domestic_district_11_18)

        true_domestic_district_12_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '12')}
        counts_domestic_disctrict_12_18 =len(true_domestic_district_12_18)

        true_domestic_district_14_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '14')}
        counts_domestic_disctrict_14_18 =len(true_domestic_district_14_18)

        true_domestic_district_15_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '15')}
        counts_domestic_disctrict_15_18 =len(true_domestic_district_15_18)

        true_domestic_district_16_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '16')}
        counts_domestic_disctrict_16_18 =len(true_domestic_district_16_18)

        true_domestic_district_17_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '17')}
        counts_domestic_disctrict_17_18 =len(true_domestic_district_17_18)

        true_domestic_district_18_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '18')}
        counts_domestic_disctrict_18_18 =len(true_domestic_district_18_18)

        true_domestic_district_19_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '19')}
        counts_domestic_disctrict_19_18 =len(true_domestic_district_19_18)

        true_domestic_district_20_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '20')}
        counts_domestic_disctrict_20_18 =len(true_domestic_district_20_18)

        true_domestic_district_22_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '22')}
        counts_domestic_disctrict_22_18 =len(true_domestic_district_22_18)

        true_domestic_district_24_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '24')}
        counts_domestic_disctrict_24_18 =len(true_domestic_district_24_18)

        true_domestic_district_25_18 = {key: values for key, values in district_domestic_2018.items() if values == ('True', '25')}
        counts_domestic_disctrict_25_18 =len(true_domestic_district_25_18)

        #Getting counts of domestic crimes in districts - Year 2019
        true_domestic_district_1_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '1')}
        counts_domestic_disctrict_1_19 =len(true_domestic_district_1_19)

        true_domestic_district_2_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '2')}
        counts_domestic_disctrict_2_19 =len(true_domestic_district_2_19)

        true_domestic_district_3_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '3')}
        counts_domestic_disctrict_3_19 =len(true_domestic_district_3_19)

        true_domestic_district_4_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '4')}
        counts_domestic_disctrict_4_19 =len(true_domestic_district_4_19)

        true_domestic_district_5_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '5')}
        counts_domestic_disctrict_5_19 =len(true_domestic_district_5_19)

        true_domestic_district_6_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '6')}
        counts_domestic_disctrict_6_19 =len(true_domestic_district_6_19)

        true_domestic_district_7_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '7')}
        counts_domestic_disctrict_7_19 =len(true_domestic_district_7_19)

        true_domestic_district_8_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '8')}
        counts_domestic_disctrict_8_19 =len(true_domestic_district_8_19)

        true_domestic_district_9_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '9')}
        counts_domestic_disctrict_9_19 =len(true_domestic_district_9_19)

        true_domestic_district_10_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '10')}
        counts_domestic_disctrict_10_19 =len(true_domestic_district_10_19)

        true_domestic_district_11_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '11')}
        counts_domestic_disctrict_11_19 =len(true_domestic_district_11_19)

        true_domestic_district_12_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '12')}
        counts_domestic_disctrict_12_19 =len(true_domestic_district_12_19)

        true_domestic_district_14_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '14')}
        counts_domestic_disctrict_14_19 =len(true_domestic_district_14_19)

        true_domestic_district_15_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '15')}
        counts_domestic_disctrict_15_19 =len(true_domestic_district_15_19)

        true_domestic_district_16_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '16')}
        counts_domestic_disctrict_16_19 =len(true_domestic_district_16_19)

        true_domestic_district_17_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '17')}
        counts_domestic_disctrict_17_19 =len(true_domestic_district_17_19)

        true_domestic_district_18_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '18')}
        counts_domestic_disctrict_18_19 =len(true_domestic_district_18_19)

        true_domestic_district_19_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '19')}
        counts_domestic_disctrict_19_19 =len(true_domestic_district_19_19)

        true_domestic_district_20_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '20')}
        counts_domestic_disctrict_20_19 =len(true_domestic_district_20_19)

        true_domestic_district_22_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '22')}
        counts_domestic_disctrict_22_19 =len(true_domestic_district_22_19)

        true_domestic_district_24_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '24')}
        counts_domestic_disctrict_24_19 =len(true_domestic_district_24_19)

        true_domestic_district_25_19 = {key: values for key, values in district_domestic_2019.items() if values == ('True', '25')}
        counts_domestic_disctrict_25_19 =len(true_domestic_district_25_19)
        
        #Getting counts of domestic crimes in districts - Year 2020
        true_domestic_district_1_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '1')}
        counts_domestic_disctrict_1_20 =len(true_domestic_district_1_20)

        true_domestic_district_2_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '2')}
        counts_domestic_disctrict_2_20 =len(true_domestic_district_2_20)

        true_domestic_district_3_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '3')}
        counts_domestic_disctrict_3_20 =len(true_domestic_district_3_20)

        true_domestic_district_4_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '4')}
        counts_domestic_disctrict_4_20 =len(true_domestic_district_4_20)

        true_domestic_district_5_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '5')}
        counts_domestic_disctrict_5_20 =len(true_domestic_district_5_20)

        true_domestic_district_6_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '6')}
        counts_domestic_disctrict_6_20 =len(true_domestic_district_6_20)

        true_domestic_district_7_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '7')}
        counts_domestic_disctrict_7_20 =len(true_domestic_district_7_20)

        true_domestic_district_8_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '8')}
        counts_domestic_disctrict_8_20 =len(true_domestic_district_8_20)

        true_domestic_district_9_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '9')}
        counts_domestic_disctrict_9_20 =len(true_domestic_district_9_20)

        true_domestic_district_10_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '10')}
        counts_domestic_disctrict_10_20 =len(true_domestic_district_10_20)

        true_domestic_district_11_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '11')}
        counts_domestic_disctrict_11_20 =len(true_domestic_district_11_20)

        true_domestic_district_12_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '12')}
        counts_domestic_disctrict_12_20 =len(true_domestic_district_12_20)

        true_domestic_district_14_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '14')}
        counts_domestic_disctrict_14_20 =len(true_domestic_district_14_20)

        true_domestic_district_15_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '15')}
        counts_domestic_disctrict_15_20 =len(true_domestic_district_15_20)

        true_domestic_district_16_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '16')}
        counts_domestic_disctrict_16_20 =len(true_domestic_district_16_20)

        true_domestic_district_17_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '17')}
        counts_domestic_disctrict_17_20 =len(true_domestic_district_17_20)

        true_domestic_district_18_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '18')}
        counts_domestic_disctrict_18_20 =len(true_domestic_district_18_20)

        true_domestic_district_19_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '19')}
        counts_domestic_disctrict_19_20 =len(true_domestic_district_19_20)

        true_domestic_district_20_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '20')}
        counts_domestic_disctrict_20_20 =len(true_domestic_district_20_20)

        true_domestic_district_22_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '22')}
        counts_domestic_disctrict_22_20 =len(true_domestic_district_22_20)

        true_domestic_district_24_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '24')}
        counts_domestic_disctrict_24_20 =len(true_domestic_district_24_20)

        true_domestic_district_25_20 = {key: values for key, values in district_domestic_2020.items() if values == ('True', '25')}
        counts_domestic_disctrict_25_20 =len(true_domestic_district_25_20)

        districts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '14', '15', '16', '17', '18', '19', '20', '22', '24', '25']
        domestic_numbers_18 = [counts_domestic_disctrict_1_18, counts_domestic_disctrict_2_18, counts_domestic_disctrict_3_18, counts_domestic_disctrict_4_18, counts_domestic_disctrict_5_18, counts_domestic_disctrict_6_18, counts_domestic_disctrict_7_18, counts_domestic_disctrict_8_18, counts_domestic_disctrict_9_18, counts_domestic_disctrict_10_18, counts_domestic_disctrict_11_18, counts_domestic_disctrict_12_18, counts_domestic_disctrict_14_18, counts_domestic_disctrict_15_18, counts_domestic_disctrict_16_18, counts_domestic_disctrict_17_18, counts_domestic_disctrict_18_18, counts_domestic_disctrict_19_18, counts_domestic_disctrict_20_18, counts_domestic_disctrict_22_18, counts_domestic_disctrict_24_18, counts_domestic_disctrict_25_18]
        domestic_numbers_19 = [counts_domestic_disctrict_1_19, counts_domestic_disctrict_2_19, counts_domestic_disctrict_3_19, counts_domestic_disctrict_4_19, counts_domestic_disctrict_5_19, counts_domestic_disctrict_6_19, counts_domestic_disctrict_7_19, counts_domestic_disctrict_8_19, counts_domestic_disctrict_9_19, counts_domestic_disctrict_10_19, counts_domestic_disctrict_11_19, counts_domestic_disctrict_12_19, counts_domestic_disctrict_14_19, counts_domestic_disctrict_15_19, counts_domestic_disctrict_16_19, counts_domestic_disctrict_17_19, counts_domestic_disctrict_18_19, counts_domestic_disctrict_19_19, counts_domestic_disctrict_20_19, counts_domestic_disctrict_22_19, counts_domestic_disctrict_24_19, counts_domestic_disctrict_25_19]
        domestic_numbers_20 = [counts_domestic_disctrict_1_20, counts_domestic_disctrict_2_20, counts_domestic_disctrict_3_20, counts_domestic_disctrict_4_20, counts_domestic_disctrict_5_20, counts_domestic_disctrict_6_20, counts_domestic_disctrict_7_20, counts_domestic_disctrict_8_20, counts_domestic_disctrict_9_20, counts_domestic_disctrict_10_20, counts_domestic_disctrict_11_20, counts_domestic_disctrict_12_20, counts_domestic_disctrict_14_20, counts_domestic_disctrict_15_20, counts_domestic_disctrict_16_20, counts_domestic_disctrict_17_20, counts_domestic_disctrict_18_20, counts_domestic_disctrict_19_20, counts_domestic_disctrict_20_20, counts_domestic_disctrict_22_20, counts_domestic_disctrict_24_20, counts_domestic_disctrict_25_20]

        #Plot for domestic trends per district (2018-2020)
        plt.figure(figsize=(17, 7))
        plt.xlabel('Districts', fontsize=15)
        plt.ylabel('Number of Domestic Cases', fontsize=15)
        plt.title('Domestic Case Trends Per District 2018-2020', fontsize=20)

        X_axis = np.arange(len(districts))
    
        rect1 = plt.bar(X_axis - 0.4, domestic_numbers_18, 0.4, label = '2018')
        rect2 = plt.bar(X_axis, domestic_numbers_19, 0.4, label = '2019')
        rect3 = plt.bar(X_axis + 0.4, domestic_numbers_20, 0.4, label = '2020')

        plt.legend( (rect1, rect2, rect3), ('2018', '2019', '2020') )

        plt.xticks(X_axis, districts)

        plt.show()
    def percent_change(self):
        
        #Defining the number of domestic cases.
        number_of_domestic_15 = self.domestic_2015.count('True')
        number_of_domestic_16 = self.domestic_2016.count('True')
        number_of_domestic_17 = self.domestic_2017.count('True')
        number_of_domestic_18 = self.domestic_2018.count('True')
        number_of_domestic_19 = self.domestic_2019.count('True')
        number_of_domestic_20 = self.domestic_2020.count('True')
        number_of_domestic_21 = self.domestic_2021.count('True')
        
        #Arranging number of domestic cases into a list.
        domestic_cases = [number_of_domestic_15, number_of_domestic_16, number_of_domestic_17, number_of_domestic_18, number_of_domestic_19, number_of_domestic_20, number_of_domestic_21]
        
        freq_series = pd.Series(domestic_cases)

        x_labels = [2015, 2016, 2017, 2018, 2019, 2020, 2021]

        # Plot the figure.
        plt.figure(figsize=(12, 8))
        ax = freq_series.plot(kind="bar")
        ax.set_title('Percent Change of Domestic Cases During COVID-19 Pandemic',fontsize=20)
        ax.set_xlabel('Years',fontsize=15)
        ax.set_ylabel('Number of Domestic Cases',fontsize=15)
        ax.set_xticklabels(x_labels)
        plt.ylim([38000, 44600])

        rects = ax.patches

        label = [' ','+3%','-0.8%','+2.7%','-1.7%','-7.8%','-4%']

        # Make some labels.
        labels = [label[i] for i in range(len(rects))]

        for rect, label in zip(rects, labels):
            height = rect.get_height()
            ax.text(
                rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom", fontsize=12)

        plt.show()
        
        return
    def proportion(self):
        from matplotlib.gridspec import GridSpec
        
        #Defining the number of cases per year.
        dates_15 = len(self.date_2015)
        dates_16 = len(self.date_2016)
        dates_17 = len(self.date_2017)
        dates_18 = len(self.date_2018)
        dates_19 = len(self.date_2019)
        dates_20 = len(self.date_2020)
        dates_21 = len(self.date_2021)
        
        #Defining the number of domestic cases.
        number_of_domestic_15 = self.domestic_2015.count('True')
        number_of_domestic_16 = self.domestic_2016.count('True')
        number_of_domestic_17 = self.domestic_2017.count('True')
        number_of_domestic_18 = self.domestic_2018.count('True')
        number_of_domestic_19 = self.domestic_2019.count('True')
        number_of_domestic_20 = self.domestic_2020.count('True')
        number_of_domestic_21 =self. domestic_2021.count('True')
        
        #Arranging the number of domestic arrests into a dictionary.
        domestic_arrests_2015 = dict(zip(self.date_2015, zip(self.domestic_2015, self.arrest_2015)))
        domestic_arrests_2016 = dict(zip(self.date_2016, zip(self.domestic_2016, self.arrest_2016)))
        domestic_arrests_2017 = dict(zip(self.date_2017, zip(self.domestic_2017, self.arrest_2017)))
        domestic_arrests_2018 = dict(zip(self.date_2018, zip(self.domestic_2018, self.arrest_2018)))
        domestic_arrests_2019 = dict(zip(self.date_2019, zip(self.domestic_2019, self.arrest_2019)))
        domestic_arrests_2020 = dict(zip(self.date_2020, zip(self.domestic_2020, self.arrest_2020)))
        domestic_arrests_2021 = dict(zip(self.date_2021, zip(self.domestic_2021, self.arrest_2021)))
        
        #Getting count of domestic arrests
        true_domestic_arrests_15 = {key: values for key, values in domestic_arrests_2015.items() if values == ('True', 'True')}
        counts_domestic_arrests_15 =len(true_domestic_arrests_15)

        true_domestic_arrests_16 = {key: values for key, values in domestic_arrests_2016.items() if values == ('True', 'True')}
        counts_domestic_arrests_16 =len(true_domestic_arrests_16)

        true_domestic_arrests_17 = {key: values for key, values in domestic_arrests_2017.items() if values == ('True', 'True')}
        counts_domestic_arrests_17 =len(true_domestic_arrests_17)

        true_domestic_arrests_18 = {key: values for key, values in domestic_arrests_2018.items() if values == ('True', 'True')}
        counts_domestic_arrests_18 =len(true_domestic_arrests_18)

        true_domestic_arrests_19 = {key: values for key, values in domestic_arrests_2019.items() if values == ('True', 'True')}
        counts_domestic_arrests_19 =len(true_domestic_arrests_19)

        true_domestic_arrests_20 = {key: values for key, values in domestic_arrests_2020.items() if values == ('True', 'True')}
        counts_domestic_arrests_20 =len(true_domestic_arrests_20)

        true_domestic_arrests_21 = {key: values for key, values in domestic_arrests_2021.items() if values == ('True', 'True')}
        counts_domestic_arrests_21 =len(true_domestic_arrests_21)

        labels = 'Police Cases', 'Domestic', 'Domestic Arrests'
        data1 = [dates_15, number_of_domestic_15, counts_domestic_arrests_15]
        data2 = [dates_16, number_of_domestic_16, counts_domestic_arrests_16]
        data3 = [dates_17, number_of_domestic_17, counts_domestic_arrests_17]
        data4 = [dates_18, number_of_domestic_18, counts_domestic_arrests_18]
        data5 = [dates_19, number_of_domestic_19, counts_domestic_arrests_19]
        data6 = [dates_20, number_of_domestic_20, counts_domestic_arrests_20]
        data7 = [dates_21, number_of_domestic_21, counts_domestic_arrests_21]

        #Formatting the size of each pie slice
        explode = (0, 0.1, 0.3)

        #Creating a grid for plotting 3 pie charts in the same region
        fig = plt.figure(figsize=(10, 10))
        fig.suptitle('Proportion of Domestic Cases and Arrests',fontsize=20)
        gs = GridSpec(nrows=2, ncols=4)

        #Defining location, labels, etc...
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.pie(data1, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
        ax1.set_xlabel('\nYear 2015',fontsize=12)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        ax2 = fig.add_subplot(gs[0, 1])
        ax2.pie(data2, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax2.set_xlabel('\nYear 2016',fontsize=12)
        ax2.axis('equal') 

        ax3 = fig.add_subplot(gs[0, 2])
        ax3.pie(data3, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax3.set_xlabel('\nYear 2017',fontsize=12)
        ax3.axis('equal')  
        
        ax4 = fig.add_subplot(gs[0, 3])
        ax4.pie(data4, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax4.set_xlabel('\nYear 2018',fontsize=12)
        ax4.axis('equal') 
        
        ax5 = fig.add_subplot(gs[1, 0])
        ax5.pie(data5, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax5.set_xlabel('\nYear 2019',fontsize=12)
        ax5.axis('equal') 
        
        ax6 = fig.add_subplot(gs[1, 1])
        ax6.pie(data6, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax6.set_xlabel('\nYear 2020',fontsize=12)
        ax6.axis('equal') 
        
        ax7 = fig.add_subplot(gs[1, 2])
        ax7.pie(data7, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax7.set_xlabel('\nYear 2021',fontsize=12)
        ax7.axis('equal') 

        plt.tight_layout()
        plt.show()

        return