#pandas (１つ１つに何か下に意味があるデータに有効。アプリログ、アンケート結果など)
import pandas as pd
import numpy as np

df = pd.DataFrame({'Age':[12,14,12,18],
                    'Gender':["M","M","F","F"],
                    'Height':[150,160,150,175],
                    'Weight':[35,50,36,60]})
print(df.info())    #データフレーム概要出力
print(df.head(2))   #dfのindex前から2つを表示
print(df.tail(2))   #dfのindex後ろから2つを表示
print(df.columns)   #全ての列の名前を出す
print(df.index)     #全てのindexを出す

#---------------------------------------------
df_titanic = pd.read_csv('titanic_train.csv')   #ファイル読み込み
print(df_titanic.head(5))
print(df_titanic.info())
