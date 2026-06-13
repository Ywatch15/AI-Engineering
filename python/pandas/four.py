# READ JSON to CSV

import pandas as pd
import numpy as np
from io import StringIO



Data='{"emp_name":"James", "email":"james@example.com", "job_profile":[{"title1":"Data Analyst", "title2":"Data Scientist"}], "age":30}'
df1=pd.read_json(Data) #read the JSON data and create a dataframe

print(df1.to_json(orient='records')) #convert the dataframe to JSON format with 'records' orientation and print it


df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None) #read the csv file from the given URL and create a dataframe
print(df.head()) #print the dataframe

df.to_csv('wine.csv', index=False) #save the dataframe to a csv file named 'wine.csv'


