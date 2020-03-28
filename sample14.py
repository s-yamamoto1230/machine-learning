import pandas as pd
import numpy as np

df_titanic = pd.read_csv('titanic_train.csv')   #ファイル読み込み
print(df_titanic.head(5))
print(df_titanic.info())

print(df_titanic.sort_values('Age',ascending = False))
print(df_titanic[(df_titanic['Age'] < 40) & (df_titanic['Sex'] == 'male')])

print(df_titanic.loc[:,'Age'].describe())
df_titanic.loc[:,'Age'] += 20
print(df_titanic)
print(df_titanic.loc[:,'Survived'].sum())

print(df_titanic.isnull().sum())
df_titanic_drop = df_titanic.dropna()
print(df_titanic_drop)
