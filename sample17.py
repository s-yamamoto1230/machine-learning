#Matplotlibによる可視化
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv("./tips.csv")
print(tips.head(5))
print(tips.isnull().sum())

#棒グラフによる可視化  plt.bar()
left = range(4)
day = tips.day.value_counts().keys()
height = tips.day.value_counts().values
plt.bar(left,height,tick_label=day)     #tick_labelでleftで振られた数字を文字列に置き換える
plt.show()

#円グラフによる可視化  plt.pie()
plt.pie(tips.day.value_counts(),autopct="%.1f%%",labels=tips.day.value_counts().keys()) #autopctはフォーマット指定。割合を%で表示
plt.show()

#ヒストグラムで可視化  plt.hist()
plt.hist(tips.total_bill,bins=20,color="green")     #binsはグループの数
plt.xlabel("total_bill")
plt.ylabel("counts")
plt.title("histogram of total_bill")
plt.show()

#散布図で可視化  plt.scatter()
plt.scatter(x=tips["total_bill"],y=tips["tip"])
#plt.scatter("total_bill","tip",data=tips)  この書き方でも可
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.show()

#---------------------------------------------------------
#性別ごとのチップの額と支払総額の関係性を調べる
fig,ax = plt.subplots(2,1,figsize=(8,8))

tips_male = tips[tips["sex"] == "Male"][["total_bill","tip"]]       #男性データ
tips_female = tips[tips["sex"] == "Female"][["total_bill","tip"]]   #女性データ

ax[0].scatter(x=tips_male["total_bill"],y=tips_male["tip"],label="Male",color="blue")
ax[1].scatter(x=tips_female["total_bill"],y=tips_female["tip"],label="Female",color="red")

for i in range(2):
    ax[i].set_xlabel("total_bill")
    ax[i].set_ylabel("tip")
    ax[i].legend()
plt.show()
