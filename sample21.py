#データの前処理

#目的変数→予測したい変数
#説明変数→目的変数を予測するためにモデルに投入する変数
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("./train.csv")  #訓練用データ
test = pd.read_csv("./test.csv")    #テスト用
data = [train,test]                 #train,testを一つのリストに格納

print("--trainデータ--")
print(train.info())                 #trainのデータ概要確認
print(train.head(5))                #trainの中身を確認(先頭5行)
print(train.tail(5))                #trainの中身を確認(最後5行)
print()
print("--testデータ--")
print(test.info())                  #testのデータ概要確認
print(test.head())                  #testの中身を確認(先頭5行)
print(test.tail(5))                 #testの中身を確認(最後5行)

print()
print("--trainの欠損値確認--")
print(train.isnull().sum())         #notnullにすれば欠損値でない数が出てくる

#外れ値の確認
sns.boxplot(train["Age"])           #箱ひげ図による量的変数Ageの可視化
plt.show()
sns.boxplot(train["Fare"])          #箱ひげ図による量的変数Fareの可視化
plt.show()

#「年齢」列の深堀
sns.distplot(train["Age"],bins=16)
plt.show()
print()
print("年齢の出現回数表示(最後から15行)")
print(train["Age"].value_counts().tail(15))     #グループ化したほうが良い

#「運賃」列の分布の可視化
sns.distplot(train["Fare"],bins=10)
plt.show()

#「運賃」列に存在する各要素の個数を可視化
print()
print("運賃の出現回数表示(最後から15行)")
print(train["Fare"].value_counts().tail(15))    #グループ化したほうが良い

#Surbivedと他の列との関係性を可視化
sns.heatmap(train.corr(),cmap="summer",annot=True)  #annot→ヒートマップの中に値を入れるかどうか
plt.show()

#男女それぞれの生存者数を棒グラフで表示
sum_survived = train.groupby(["Sex"])["Survived"].sum() #trainデータのSurvived列の和を性別毎に求め可視化。
sns.barplot(sum_survived.keys(),sum_survived.values)
plt.show()
