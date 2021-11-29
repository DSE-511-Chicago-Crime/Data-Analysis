#will not be part of final script 
#just exists to cut out data reading step for speed
import pandas
import numpy

df = pandas.read_csv('./data/combineddata.csv')

df['date'] = pandas.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S+00:00')
dates = df['date'].to_numpy()
numpy.save('arrests/dates.npy', dates)

arrests = df['arrest'].to_numpy()
numpy.save('arrests/arrests.npy', arrests)