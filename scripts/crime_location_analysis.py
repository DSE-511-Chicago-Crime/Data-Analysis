
import pandas as pd
import numpy as np

data_file_2019 = pd.read_csv("../data/2019_crime.csv")
print(data_file_2019.head())
all_columns= data_file_2019.columns.values.tolist()
print(all_columns)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.float_format', '{:20,.2f}'.format)
pd.set_option('display.max_colwidth', None)
data_file_2019['arrest']=data_file_2019['arrest'].astype('category').cat.codes
data_file_2019['primary_type']=data_file_2019['primary_type'].astype('category').cat.codes
#print(data_file_2019)
print(data_file_2019.corr())