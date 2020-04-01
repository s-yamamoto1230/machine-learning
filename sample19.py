#Seabornの便利な可視化
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv("./tips.csv")

#散布図行列  pairplot()
sns.pairplot(tips)      #全ての量的変数に対して、ヒストグラムと散布図を表示。
plt.show()

#相関係数(2つの変数の関係の値)    #heatmap()
#pandasの場合
print(tips.corr())     #相関係数を出す
tips.corr().style.background_gradient("summer_r")    #相関の情報に色を付ける
#seabornの場合
sns.heatmap(tips.corr(),cmap="summer_r")
plt.show()

#カテゴリごとにデータの分布を表示  swarmplot()
sns.swarmplot("day","total_bill",data=tips)     #day列に含まれるカテゴリごとにtotal_bill列の分布を可視化
plt.show()      #横に膨らんでいる所ほどデータが密集している。
sns.swarmplot("day","total_bill",data=tips,hue="sex",dodge=True)    #hue→可視化の切り口をさらに追加。dodge→追加した切り口を重ねるかどうか。Trueで重ねない。
plt.show()

#カテゴリごとにデータの分布を表示  boxplot()
sns.boxplot(tips.day,tips.tip,hue=tips.sex)
plt.show()      #箱の中央線は中央値。黒店は外れ値。

#---------------------------------------------------
#支払総額とチップ額のヒストグラム及び散布図を可視化。
sns.pairplot(tips[["total_bill","tip"]])
plt.show()
#性別毎のチップの総額の分布をboxplotし、さらに曜日の色相も追加
sns.boxplot(tips.sex,tips.tip,hue=tips.day)
plt.show()
