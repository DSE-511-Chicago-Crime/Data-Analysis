#Domestic Percent Change Over Years
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

def percent_change(domestic_2015, domestic_2016, domestic_2017, domestic_2018, domestic_2019, domestic_2020, domestic_2021):
    
    #Defining the number of domestic cases.
    number_of_domestic_15 = domestic_2015.count('True')
    number_of_domestic_16 = domestic_2016.count('True')
    number_of_domestic_17 = domestic_2017.count('True')
    number_of_domestic_18 = domestic_2018.count('True')
    number_of_domestic_19 = domestic_2019.count('True')
    number_of_domestic_20 = domestic_2020.count('True')
    number_of_domestic_21 = domestic_2021.count('True')
    
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

list_maker(date_2015, arrest_2015, domestic_2015, district_2015, date_2016, arrest_2016, domestic_2016, district_2016, date_2017, arrest_2017, domestic_2017, district_2017, date_2018, arrest_2018, domestic_2018, district_2018, date_2019, arrest_2019, domestic_2019, district_2019, date_2020, arrest_2020, domestic_2020, district_2020, date_2021, arrest_2021, domestic_2021, district_2021)
percent_change(domestic_2015, domestic_2016, domestic_2017, domestic_2018, domestic_2019, domestic_2020, domestic_2021)