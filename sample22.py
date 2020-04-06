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

#-------------
#欠損値処理
#-------------

#Embarkedの欠損部分を埋める
train.Embarked = train.Embarked.fillna("S")     #一番確率が高そうなSで補完

#Ageの欠損部分を埋める       平均でとると全体の平均となってしまい正確さに欠ける
print()
print("敬称別にAge平均を取る")
print(train.groupby("Title")["Age"].mean())    #敬称(Title)別に平均を取る

for df in data:
    mean = df.groupby("Title")["Age"].mean()                            #敬称列で集計して敬称毎に年齢の平均を出す
    for title in mean.keys():                                           #敬称毎に欠損値の穴埋め処理を行う
        df.loc[(df.Age.isnull())&(df.Title==title),"Age"]=mean[title]

#Fareの欠損部分を埋める      一か所だけなので中央値で埋める
test.Fare = test.Fare.fillna(test.Fare.median())

#Cabinは欠損値が多く、あまり製紙の分類に役に立たなさそうなので後で削除

#処理後の欠損値確認
print()
print("trainの処理後欠損値数")
print(train.isnull().sum())
print()
print("testの処理後欠損値数")
print(test.isnull().sum())

#--------------------------------------
#数値データのカテゴライズ化
#--------------------------------------
sns.boxplot(df["Age"])
plt.show()

#pd.cut(分割するデータ,分割基準リスト,分割後に割り当てるカテゴリの値,境界値をどちらに含めるか(Trueなら小さいほう。Falseなら大きいほう。))
for df in data:
    df['Age_band']  = pd.cut(df["Age"],[0,22,30,37,59,100],labels=range(5),right=False)
print()
print("Ageを5つのグループにカテゴリ分け")
print(train['Age_band'].head())     #0~22歳、23~30歳、31~37歳、38~59歳、60歳以上の5つのグループに分けた。

sns.boxplot(df["Fare"])
plt.show()

#Fareも5分割して、Fare_band列を作る
for df in data:
    df['Fare_band'] = pd.cut(df["Fare"],[0,8,15,31,66,520],labels=range(5),right=False)
print()
print("Fareを5つのグループにカテゴリ分け")
print(train['Fare_band'].head())

#カテゴライズした要素を切り口としてグラフ化
sns.barplot(train["Age_band"],train["Survived"])
plt.show()
sns.barplot(train["Fare_band"],train["Survived"])
plt.show()
sns.barplot(train["Title"],train["Survived"])
plt.show()

#---------------------
#不要データの削除
#----------------------
#Passengerld    あまり生死と関係がなさそう
#Name           Title列を作ったので用済み
#Ticket         規則性が見いだせず扱いに困る
#Cabin          欠損値が多すぎ
#Age            Age_band列を作ったので用済み
#Fare           Fare_band列を作ったので用済み
drop_columns = ['PassengerId','Name','Ticket','Cabin','Age','Fare']     #削除する列名をリストに格納
train = train.drop(drop_columns,axis=1)                                 #trainから削除
test = test.drop(drop_columns,axis=1)                                   #testから削除
data = [train,test]                                                     #dataに再代入

#-------------------------------
#文字列データの数値への置き換え
#-------------------------------
for df in data:
    # 性別を数字でおきかえ
    df.loc[df['Sex']=="female", "Sex"]=0
    df.loc[df['Sex']=='male','Sex']=1
    # 敬称を数字で置き換え
    df.loc[df['Title']=='Mr', 'Title']=0
    df.loc[df['Title']=='Miss', 'Title']=1
    df.loc[df['Title']=='Mrs', 'Title']=2
    df.loc[df['Title']=='Master', 'Title']=3
    df.loc[df['Title']=='Others', 'Title']=4
    # 乗船した港３種類を数字でおきかえ
    df.loc[df['Embarked']=='S', 'Embarked']=0
    df.loc[df['Embarked']=='C', 'Embarked']=1
    df.loc[df['Embarked']=='Q', 'Embarked']=2

#------------------------
#前処理してデータの保存
#------------------------
#pickle():Pythonにおけるオブジェクトの読み書きが可能なデータ形式
data[0].to_pickle("./titanic_train.pkl")    #pickle形式でtrainを保存
data[1].to_pickle("./titanic_test.pkl")     #pickle形式でtestを保存
