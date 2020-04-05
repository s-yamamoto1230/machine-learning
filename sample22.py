#データの前処理

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("./train.csv")  #訓練用データ
test = pd.read_csv("./test.csv")    #テスト用
data = [train,test]                 #train,testを一つのリストに格納

#データを加工して意味のある特徴を作る [名前(Name)の加工]
#処理①  名前は敬称だけ抜き取る
import re
def get_title(name):
    title_search = re.search('([A-Za-z]+)\.',name)  #正規表現を用いて抽出するパターンを定義
    if title_search:
        return title_search.group(1)
    return ""
#処理②  Titleという列を作り、その中に全員分の敬称を収録
for df in [train,test]:
    df['Title'] = df['Name'].apply(get_title)   #apply() 指定されたデータ列に関数を適用し適用結果を列にして返す

print("trainのTitle列の各要素の個数")
print(train["Title"].value_counts())
print()
print("testのTitle列の各要素の個数")
print(test["Title"].value_counts())

#件数が少ない敬称は置き換えてまとめる
for df in data:
    df['Title'] = df['Title'].replace(["Mlle","Ms","Mme"],"Miss")   #"Mlle","Ms","Mme"は"Miss"に置き換え
    df["Title"] = df['Title'].replace(['Lady','Countess','Capt','Col','Don','Major','Dr','Rev','Sir','Jonkheer','Dona'],'Others')    #その他はOthersへ
print()
print("置き換え後のtrainのTitle列の各要素の個数")
print(train["Title"].value_counts())
print()
print("置き換え後testのTitle列の各要素の個数")
print(test["Title"].value_counts())

#欠損値確認  欠損値の多いものは使わない
print()
print("trainの欠損値数")
print(train.isnull().sum())
print()
print("testの欠損値数")
print(test.isnull().sum())

#Embarkedの欠損部分を埋める
train.Embarked = train.Embarked.fillna("S")     #一番確率が高そうなSで補完

#Ageの欠損部分を埋める       平均でとると全体の平均となってしまい正確さに欠ける
print()
print("敬称別にAge平均を取る")
print(train.groupby("Title")["Age"].mean())    #敬称(Title)別に平均を取る

for dr in data:
    mean = df.groupby("Title")["Age"].mean()                            #敬称列で集計して敬称毎に年齢の平均を出す
    for title in mean.keys():                                           #敬称毎に欠損値の穴埋め処理を行う
        df.loc[(df.Age.isnull())&(df.Title==title),"Age"]=mean[title]
