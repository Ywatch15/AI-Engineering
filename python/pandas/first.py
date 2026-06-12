import pandas as pd #import pandas library
import numpy as np #import numpy library

df = pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=['Column1','Column2','Column3','Column4']) #create a dataframe with 5 rows and 4 columns
'''
print(df) #print the dataframe

# print(df.head()) #print the first 5 rows of the dataframe

df.to_csv('first.csv') #save the dataframe to a csv file named 'first.csv'

print(df.loc['Row1']) #print the first row of the dataframe using loc

print(type(df.loc['Row1'])) #print the type of the first row, which is a pandas Series

print(df.iloc[0:3,0:2]) #print the first 3 rows and the first 2 columns of the dataframe using iloc
print(type(df.iloc[0:3,0:2]))
'''



print(df.iloc[:,1:].values) #print all rows and columns from the second column onwards, and get the values as a numpy array
print(df.iloc[:,1:].values.shape) #print the shape of the values, which is (5, 3)
print(type(df.iloc[:,1:].values)) #print the type of the values, which is a numpy array

print(df[['Column1','Column2']]) #print the columns 'Column1' and 'Column2' of the dataframe