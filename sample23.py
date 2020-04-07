#機械学習モデルの構築と評価
import numpy as np
import pandas as pd

#pickleをデータフレームに復元
train = pd.read_pickle("titanic_train.pkl")     #答えのあるデータ
test = pd.read_pickle("titanic_test.pkl")       #答えのない予測したいデータ
data = [train,test]

#------------------------------------------------------------------------------
#データ分割(未知のデータに対する評価が出来ないので分割する) ホールドアウト検証
#------------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
#random_state=1234は振り分けを固定するための値
tr_train,tr_test = train_test_split(train,test_size=0.3,random_state=1234)  #trainデータをtr_train:tr_test=7:3に分割

#訓練(学習)用の説明変数
tr_train_X = tr_train[train.columns[1:]]
#訓練(学習)用の目的変数
tr_train_Y = tr_train[train.columns[0]]
#評価用の説明変数
tr_test_X = tr_test[train.columns[1:]]
#評価用の目的変数
tr_test_Y = tr_test[train.columns[0]]

#--------------------------------
#scikit-learnによる決定木の実装
#--------------------------------
from sklearn import tree
model = tree.DecisionTreeClassifier()   #作成
model.fit(tr_train_X,tr_train_Y)        #学習     fit(説明変数,目的変数)
predict = model.predict(tr_test_X)      #予測     predict(説明変数)予測したいモノを渡す
from sklearn import metrics             #精度確認
print('判別率',metrics.accuracy_score(predict,tr_test_Y))

#-------------------------------------------
#scikit-learnによるランダムフォレストの実装
#-------------------------------------------
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)   #作成(100のモデルを用意)
model.fit(tr_train_X,tr_train_Y)        #学習     fit(説明変数,目的変数)
predict = model.predict(tr_test_X)      #予測     predict(説明変数)予測したいモノを渡す
from sklearn import metrics             #精度確認
print('判別率',metrics.accuracy_score(predict,tr_test_Y))

#------------------------------------------------------------------------------
#データ分割(未知のデータに対する評価が出来ないので分割する) K-分割交差検証
#------------------------------------------------------------------------------
from sklearn.model_selection import KFold,cross_val_score,cross_val_predict
#K分割交差検証の設定(n_splitsが分割の個数K)
kf = KFold(n_splits=5,random_state=30,shuffle=True) #K分割のKの値を決めるのが、KFoldの引数n_splits
#交差検証を行い結果を評価する
x = train[train.columns[1:]]                        #説明変数として、trainのコラムが1以降のものを設定
y = train["Survived"]                               #目的変数として、trainのSurvividを設定
#クロスバリデーションで得られるスコアを代入        ・cross_val_scoreの分割法を決めるのが引数cv
cv_resrlt = cross_val_score(model,x,y,cv=kf)        #予測に使うモデル,説明変数,目的変数,及び作成したKFoldのパラメータ引数に与える
print(cv_resrlt)
print("平均精度:{}".format(cv_resrlt.mean()))       #分割数の分だけ精度が得られるので、平均値を取れば全体の精度が確認可能
