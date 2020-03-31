#データの可視化  Seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv("./tips.csv")

#棒グラフ（個数）  countplot()
sns.countplot(tips.day)
plt.show()
#棒グラフ（平均）  barplot()
sns.barplot(tips.day,tips.total_bill)
plt.show()

#ヒストグラム  distplot()
sns.distplot(tips.total_bill,bins=20)
plt.show()

#線形回帰プロット  regplot()
sns.regplot(tips.total_bill,tips.tip)
plt.show()      #直線、95%信頼区間が自動で描かれる。

#グラフを並べて書く場合
fig,ax = plt.subplots(1,2,figsize=(10,5))
sns.countplot(tips.day,ax=ax[0])                #どこに描写するのか書く。axの0番目
sns.regplot(tips.total_bill,tips.tip,ax=ax[1])  #axの1番目
plt.show()

#-----------------------------------------------------------
#喫煙してる人、してない人の数→棒グラフ
#チップの額の分布→ヒストグラム
#注文総額とチップの額の関係性→散布図
fig,ax = plt.subplots(1,3,figsize=(15,5))
sns.countplot(tips.smoker,ax=ax[0])
sns.distplot(tips.tip,bins=20,kde=False,ax=ax[1])               #kdeで曲線の有無指定
sns.regplot(tips.total_bill,tips.tip,fit_reg=False,ax=ax[2])    #fit_regで直線の有無指定
plt.show()
