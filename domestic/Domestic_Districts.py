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

#Printing current working directory.
directory = os.getcwd()
print(directory)

#Identifing path of data file, opening in a "read-only" format to visualize the data.
path_2015 = directory + '/GitHub/Data-Analysis/data/2015_crime.csv'
data_2015 = pd.read_csv(path_2015)

path_2016 = directory + '/GitHub/Data-Analysis/data/2016_crime.csv'
data_2016 = pd.read_csv(path_2016)

path_2017 = directory + '/GitHub/Data-Analysis/data/2017_crime.csv'
data_2017 = pd.read_csv(path_2017)

path_2018 = directory + '/GitHub/Data-Analysis/data/2018_crime.csv'
data_2018 = pd.read_csv(path_2018)

path_2019 = directory + '/GitHub/Data-Analysis/data/2019_crime.csv'
data_2019 = pd.read_csv(path_2019)

path_2020 = directory + '/GitHub/Data-Analysis/data/2020_crime.csv'
data_2020 = pd.read_csv(path_2020)

path_2021 = directory + '/GitHub/Data-Analysis/data/2021_crime.csv'
data_2021 = pd.read_csv(path_2021)

#Creating empty lists.
date_2015 = []
arrest_2015 = []
domestic_2015 = []
district_2015 = []

date_2016 = []
arrest_2016 = []
domestic_2016 = []
district_2016 = []

date_2017 = []
arrest_2017 = []
domestic_2017 = []
district_2017 = []

date_2018 = []
arrest_2018 = []
domestic_2018 = []
district_2018 = []

date_2019 = []
arrest_2019 = []
domestic_2019 = []
district_2019 = []

date_2020 = []
arrest_2020 = []
domestic_2020 = []
district_2020 = []

date_2021 = []
arrest_2021 = []
domestic_2021 = []
district_2021 = []

def list_maker(date_2015, arrest_2015, domestic_2015, district_2015, date_2016, arrest_2016, domestic_2016, district_2016, date_2017, arrest_2017, domestic_2017, district_2017, date_2018, arrest_2018, domestic_2018, district_2018, date_2019, arrest_2019, domestic_2019, district_2019, date_2020, arrest_2020, domestic_2020, district_2020, date_2021, arrest_2021, domestic_2021, district_2021):
    #Open the file in read mode.
    filename = open(directory + '/GitHub/Data-Analysis/data/2015_crime.csv', 'r')
 
    #Creating dictreader object.
    file = csv.DictReader(filename)
 
    #Iterating over each row and append
    #values to empty list.
    for col in file:
        date_2015.append(col['date'])
        arrest_2015.append(col['arrest'])
        domestic_2015.append(col['domestic'])
        district_2015.append(col['district'])

    #Testing list outputs.
    print('Date:', date_2015[1])
    print('Arrest:', arrest_2015[1])
    print('Domestic:', domestic_2015[1])
    print('District:', district_2015[1])
    
    #Open the file in read mode
    filename = open(directory + '/GitHub/Data-Analysis/data/2016_crime.csv', 'r')
 
    #Creating dictreader object
    file = csv.DictReader(filename)
 
    #Iterating over each row and append
    #values to empty list
    for col in file:
        date_2016.append(col['date'])
        arrest_2016.append(col['arrest'])
        domestic_2016.append(col['domestic'])
        district_2016.append(col['district'])
    
    #Open the file in read mode
    filename = open(directory + '/GitHub/Data-Analysis/data/2017_crime.csv', 'r')
 
    #Creating dictreader object
    file = csv.DictReader(filename)
 
    #Iterating over each row and append
    #values to empty list
    for col in file:
        date_2017.append(col['date'])
        arrest_2017.append(col['arrest'])
        domestic_2017.append(col['domestic'])
        district_2017.append(col['district'])
    
    #Open the file in read mode
    filename = open(directory + '/GitHub/Data-Analysis/data/2018_crime.csv', 'r')
 
    #Creating dictreader object
    file = csv.DictReader(filename)
 
    #Iterating over each row and append
    #values to empty list
    for col in file:
        date_2018.append(col['date'])
        arrest_2018.append(col['arrest'])
        domestic_2018.append(col['domestic'])
        district_2018.append(col['district'])

    #Open the file in read mode
    filename = open(directory + '/GitHub/Data-Analysis/data/2019_crime.csv', 'r')
 
    #Creating dictreader object
    file = csv.DictReader(filename)
 
    #Iterating over each row and append
    #values to empty list
    for col in file:
        date_2019.append(col['date'])
        arrest_2019.append(col['arrest'])
        domestic_2019.append(col['domestic'])
        district_2019.append(col['district'])

    #Open the file in read mode
    filename = open(directory + '/GitHub/Data-Analysis/data/2020_crime.csv', 'r')
 
    #Creating dictreader object
    file = csv.DictReader(filename)
 
    #Iterating over each row and append
    #values to empty list
    for col in file:
        date_2020.append(col['date'])
        arrest_2020.append(col['arrest'])
        domestic_2020.append(col['domestic'])
        district_2020.append(col['district'])

    #Open the file in read mode
    filename = open(directory + '/GitHub/Data-Analysis/data/2021_crime.csv', 'r')
 
    #Creating dictreader object
    file = csv.DictReader(filename)

    #Iterating over each row and append
    #values to empty list
    for col in file:
        date_2021.append(col['date'])
        arrest_2021.append(col['arrest'])
        domestic_2021.append(col['domestic'])
        district_2021.append(col['district'])

    return date_2015, arrest_2015, domestic_2015, district_2015, date_2016, arrest_2016, domestic_2016, district_2016, date_2017, arrest_2017, domestic_2017, district_2017, date_2018, arrest_2018, domestic_2018, district_2018, date_2019, arrest_2019, domestic_2019, district_2019, date_2020, arrest_2020, domestic_2020, district_2020, date_2021, arrest_2021, domestic_2021, district_2021

def district_domestic():
    
    #Arranging domestic cases by district into dictionary.
    district_domestic_2018 = dict(zip(date_2018, zip(domestic_2018, district_2018)))
    district_domestic_2019 = dict(zip(date_2019, zip(domestic_2019, district_2019)))
    district_domestic_2020 = dict(zip(date_2020, zip(domestic_2020, district_2020)))
    
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

    return

list_maker(date_2015, arrest_2015, domestic_2015, district_2015, date_2016, arrest_2016, domestic_2016, district_2016, date_2017, arrest_2017, domestic_2017, district_2017, date_2018, arrest_2018, domestic_2018, district_2018, date_2019, arrest_2019, domestic_2019, district_2019, date_2020, arrest_2020, domestic_2020, district_2020, date_2021, arrest_2021, domestic_2021, district_2021)
district_domestic()