#Domestic Crime and Arrest Proportions
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

def proportion(date_2015, date_2016, date_2017, date_2018, date_2019, date_2020, date_2021, domestic_2015, domestic_2016, domestic_2017, domestic_2018, domestic_2019, domestic_2020, domestic_2021, arrest_2015, arrest_2016, arrest_2017, arrest_2018, arrest_2019, arrest_2020, arrest_2021):
    from matplotlib.gridspec import GridSpec
    
    #Defining the number of cases per year.
    dates_15 = len(date_2015)
    dates_16 = len(date_2016)
    dates_17 = len(date_2017)
    dates_18 = len(date_2018)
    dates_19 = len(date_2019)
    dates_20 = len(date_2020)
    dates_21 = len(date_2021)
    
    #Defining the number of domestic cases.
    number_of_domestic_15 = domestic_2015.count('True')
    number_of_domestic_16 = domestic_2016.count('True')
    number_of_domestic_17 = domestic_2017.count('True')
    number_of_domestic_18 = domestic_2018.count('True')
    number_of_domestic_19 = domestic_2019.count('True')
    number_of_domestic_20 = domestic_2020.count('True')
    number_of_domestic_21 = domestic_2021.count('True')
    
    #Arranging the number of domestic arrests into a dictionary.
    domestic_arrests_2015 = dict(zip(date_2015, zip(domestic_2015, arrest_2015)))
    domestic_arrests_2016 = dict(zip(date_2016, zip(domestic_2016, arrest_2016)))
    domestic_arrests_2017 = dict(zip(date_2017, zip(domestic_2017, arrest_2017)))
    domestic_arrests_2018 = dict(zip(date_2018, zip(domestic_2018, arrest_2018)))
    domestic_arrests_2019 = dict(zip(date_2019, zip(domestic_2019, arrest_2019)))
    domestic_arrests_2020 = dict(zip(date_2020, zip(domestic_2020, arrest_2020)))
    domestic_arrests_2021 = dict(zip(date_2021, zip(domestic_2021, arrest_2021)))
    
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

list_maker(date_2015, arrest_2015, domestic_2015, district_2015, date_2016, arrest_2016, domestic_2016, district_2016, date_2017, arrest_2017, domestic_2017, district_2017, date_2018, arrest_2018, domestic_2018, district_2018, date_2019, arrest_2019, domestic_2019, district_2019, date_2020, arrest_2020, domestic_2020, district_2020, date_2021, arrest_2021, domestic_2021, district_2021)
proportion(date_2015, date_2016, date_2017, date_2018, date_2019, date_2020, date_2021, domestic_2015, domestic_2016, domestic_2017, domestic_2018, domestic_2019, domestic_2020, domestic_2021, arrest_2015, arrest_2016, arrest_2017, arrest_2018, arrest_2019, arrest_2020, arrest_2021)