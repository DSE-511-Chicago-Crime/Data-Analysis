#don't run this script - the data should already be in the folder
import pandas

df2019 = pandas.read_csv('./data/2019_crime.csv')
df2020 = pandas.read_csv('./data/2020_crime.csv')
df2021 = pandas.read_csv('./data/2021_crime.csv')

df = pandas.concat([df2019, df2020, df2021])

df.to_csv('./data/combineddata.csv')