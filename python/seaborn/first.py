import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=sns.load_dataset("tips")
'''
#this is the loading of datasets with some raw data
df=sns.load_dataset("tips")
print(df.head())

#this defines the corelation between the data and the heatmap
print(df.corr(numeric_only=True))

# this is the heatmap of the data with annotations
print(sns.heatmap(df.corr(numeric_only=True), annot=True))
plt.show()
'''

'''
# This is the jointplot of the data with scatter plot
sns.jointplot(x='tip',y='total_bill',data=df, kind='hex')
plt.show()

# This is the jointplot of the data with regression line
sns.jointplot(x='tip',y='total_bill',data=df, kind='reg')
plt.show()
'''

'''
# this is the pairplot of the data with scatter plot
sns.pairplot(df)
plt.show()

#this is the pairplot of the data with scatter plot and hue as sex
sns.pairplot(df, hue='sex')
plt.show()
'''


# print(df['smoker'].value_counts())


# sns.distplot(df['tip'])
# plt.show()

sns.distplot(df['tip'], kde=False, bins=10)
plt.show()