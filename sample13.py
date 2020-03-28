#欠損値処理  NaN
import pandas as pd
import numpy as np

df = pd.DataFrame({'Age':[12,14,12,18],
                    'Gender':["M","M","F","F"],
                    'Height':[np.nan,160,150,175],
                    'Weight':[35,50,np.nan,60]})
print(df)

#欠損地確認
print(df.isnull())  #欠損部分はtureで出てくる

#欠損値の数を求める
print(df.isnull().sum())    #tureの数を数える

#欠損地のある行を削除(あまり使わない)  dropna()
df_dropna = df.dropna()
print(df_dropna)

#欠損地の書き換え  fillna(maxやmeanなど)
df_fillna = df.fillna(df.mean())    #欠損地を中央値に書き換え
print(df_fillna)
