#pandas演算
import pandas as pd
import numpy as np

df = pd.DataFrame({'Age':[12,14,12,18],
                    'Gender':["M","M","F","F"],
                    'Height':[150,160,150,175],
                    'Weight':[35,50,36,60]})

#最大値  max()
print(df.loc[:,'Weight'].max())

#中央値  median()
print(df.loc[:,'Weight'].median())

#最小値  min()
print(df.loc[:,'Weight'].min())

#基本統計をまとめて出す  describe()
print(df.loc[:,'Weight'].describe())

#取り出したものに全て1を足して更新
print(df)
df[:,'Age'] += 1
print(df)
