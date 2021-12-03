#don't run this script - the data should already be in the folder
import pandas
import pickle

df2015 = pandas.read_csv('./data/2015_crime.csv')
df2016 = pandas.read_csv('./data/2016_crime.csv')
df2017 = pandas.read_csv('./data/2017_crime.csv')
df2018 = pandas.read_csv('./data/2018_crime.csv')
df2019 = pandas.read_csv('./data/2019_crime.csv')
df2020 = pandas.read_csv('./data/2020_crime.csv')
df2021 = pandas.read_csv('./data/2021_crime.csv')

#combine the dataframes
df = pandas.concat([df2019, df2020, df2021])

#csv in case anyone can't work with pickle
df.to_csv('./data/combineddata.csv')

#pickle
df.to_pickle('./data/combineddata.pickle')