import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# print(pd.pandas.set_option('display.max_columns', None))

dataset = pd.read_csv(
    r"D:\Complete Programming\AI Eng\python\House Price Prediction\train.csv"
)

# rows * columns
# print(dataset.shape)

#top 5 rows
# print(dataset.head())

'''
What we are gonna do in this project?
1) Missing values
2) All the Numerical variables
3) Distribution of the numerical variables
4) Categorical variables
5) Cardinality of categorical variables
6) Outliers
7) Relationship between independent and dependent feature(SalePrice)
'''



# ==========================================
#             MISSING VALUES
# ==========================================

#here we'll check the percentage of non values present in each feature
#  step 1: make the list of features which has missing values
features_with_na=[features for features in dataset.columns if dataset[features].isnull().sum()>1]

# step 2: print the feature name and the percentage of missing values
for feature in features_with_na:
    print(feature, np.round(dataset[feature].isnull().mean(), 4), '% missing values')
