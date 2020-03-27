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

#indexに名前を付ける
df.index = ['Taro','Jiro','Hana','Ayumi']
print(df)
print(df.index)

#特定の列と行だけ名前を変更
df = df.rename(columns={'Gender':'Sex'},index={'Taro':'Goro'})
print(df)

#列の追加
df['city'] = ['Tokyo','Kyoto','Osaka','Hakata']
print(df)

#列の削除
df = df.drop(columns=('city'))
print(df)

#列名を指定してデータを参照
print(df['Age'])    #df.Ageでも可
print(df[['Age','Sex']])   #2列同時に参照

#特定の1つのデータを参照 loc[]
print(df.loc['Goro','Age'])

#特定の複数のデータを参照
print(df.loc[:,['Age','Sex']])

#条件を指定して取り出す
print(df[df['Age']>12])   #Ageが12より大きいモノのみ

#条件指定して必要なものだけ取り出す
print(df.loc[df['Age']>12,["Height","Weight"]])

#データの並び替え  sort_values()
print(df.sort_values('Age',ascending = True))  #ascending=昇順   Falseにすれば降順

#複数のヘッダーを指定して並べ替え
print(df.sort_values(['Sex','Age']))    #性別で並び替えた後性別ごとの年齢で並べ替え

#列内のユニークな値とその出現回数を求める  value_counts()
print(df["Sex"].value_counts())

#データを集計し、演算する  groupby()
print(df.groupby("Sex").mean())     #性別でグループ分け
