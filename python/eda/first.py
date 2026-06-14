import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns

train=pd.read_csv('titanic_train.csv')
# print(train.head())

# print(train.isnull())


# sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# plt.show()

# sns.set_style('whitegrid')
# sns.countplot(x='Survived',data=train)
# plt.show()


# sns.set_style('whitegrid')
# sns.countplot(x='Survived',hue='Sex',data=train,palette='RdBu_r')
# plt.show()

print(train.info())
