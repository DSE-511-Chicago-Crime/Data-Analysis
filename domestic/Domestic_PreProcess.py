#Domestic Pre-Processing
#Holland Hysmith
#DSE Chicago Crime Project

#Importing packages necessary for pre-processing.
import os
import pandas as pd
from csv import reader
import matplotlib.pyplot as plt
import numpy as np
import csv

#Printing current working directory.
directory = os.getcwd()
print(directory)

#Identifing path of data file, opening in a "read-only" format to visualize the data. - Testing year 2015 data file
path_2015 = directory + '/GitHub/Data-Analysis/data/2015_crime.csv'
data_2015 = pd.read_csv(path_2015)
data_2015.head()

#Creating empty lists.
date_2015 = []
arrest_2015 = []
domestic_2015 = []

def list_maker(date_2015, arrest_2015, domestic_2015):
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

    print('Date:', date_2015[1])
    print('Arrest:', arrest_2015[1])
    print('Domestic:', domestic_2015[1])

    return date_2015, arrest_2015, domestic_2015

def dictionary_maker(date_2015, arrest_2015, domestic_2015):
    #Organizing lists into dictionaries
    arrest_dates_2015 = dict(zip(date_2015, arrest_2015))
    domestic_dates_2015 = dict(zip(date_2015,domestic_2015))
    domestic_arrests_2015 = dict(zip(date_2015, zip(domestic_2015, arrest_2015)))

    return arrest_dates_2015, domestic_dates_2015, domestic_arrests_2015

def data_shaper(date_2015, domestic_2015, arrest_2015):
    #Converting dictionaries into arrays
    array_date = np.array(date_2015)
    array_domestic = np.array(domestic_2015)
    array_arrest = np.array(arrest_2015)

    return array_date, array_domestic, array_arrest

list_maker(date_2015, arrest_2015, domestic_2015)
dictionary_maker(date_2015, arrest_2015, domestic_2015)
data_shaper(date_2015, domestic_2015, arrest_2015)