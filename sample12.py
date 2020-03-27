import pandas as pd
import numpy as np

df_titanic = pd.read_csv('titanic_train.csv')   #ファイル読み込み
print(df_titanic.head(5))
print(df_titanic.info())

print(df_titanic.sort_values('Age',ascending = False))
print(df_titanic[(df_titanic['Age'] < 40) & (df_titanic['Sex'] == 'male')])
