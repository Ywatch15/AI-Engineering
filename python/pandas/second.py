import pandas as pd #import pandas library
import numpy as np #import numpy library

# CSV = Comma Separated Values
df=pd.read_csv('mercedesebenz.csv') #read the csv file named 'mercedesebenz.csv' and create a dataframe
print(df) #print the dataframe

# print(df.info())
# print(df.describe())

# print(df['year'].value_counts()) #print the value counts of the column 'year' in the dataframe
# print(df[df['year']>2019]) #print the rows of the dataframe where the value of the column 'year' is greater than 2019

print(df.corr()) #print the correlation matrix of the dataframe