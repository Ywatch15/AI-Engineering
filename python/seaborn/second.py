import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df=sns.load_dataset("tips")

'''
# this is the distribution plot of the data as count of the tips 
sns.countplot(x='sex', data=df)
plt.show()

sns.countplot(y='sex', data=df)
plt.show()
'''

'''
# this is the bar plot of the data 
sns.barplot(x='sex',y='tip', data=df)
plt.show()
sns.barplot(y='sex',x='tip', data=df)
plt.show()
'''


'''
# this is the box plot of the data
sns.boxplot(x='day',y='total_bill', data=df)
plt.show()
sns.boxplot(data=df, orient='v')
plt.show()
'''


sns.violinplot(x='total_bill',y='day', data=df, palette='rainbow')
plt.show()