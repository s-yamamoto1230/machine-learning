#可視化のまとめ練習
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

house = pd.read_csv("./house_data.csv")
print(house)

#横軸(日本円(1ドル100円)に変換した価格)縦軸(リビングの広さ)の散布図
house["price_jp"] = house["price"]*100                                  #日本円に変換
plt.scatter(x=house["price_jp"],y=house["sqft_living"],s=1,color="green")  #sは点のサイズ
plt.xlabel("price")
plt.ylabel("sqft_living")
plt.show()

#家の状態に新しいデータ列を追加。conditionが1~2はbad。3~5はgood。
house["good/bad"] = 0                                   #good/bad列を作成
house.loc[house["condition"]<=2,"good/bad"] = "bad"     #good/bad列のhouse[condition]が2以下のものを取り出しbadを代入
house.loc[house["condition"]>=3,"good/bad"] = "good"    #good/bad列のhouse[condition]が3以上のものを取り出しgoodを代入
print("condition列の要素数を確認")
print(house["condition"].value_counts())                #condition列の要素数を確認
print("good/bad列の要素数を確認")
print(house["good/bad"].value_counts())                 #good/bad列の要素数を確認

#箱ひげ図を作成 横軸(4と5だけの家のグレード) 縦軸(日本円に変換した価格) good/badで色相を分ける
data = house[(house["grade"]>3) & (house["grade"]<6)]   #条件一致する物だけを抽出
x = data["grade"]                                       #grade列を抽出
y = data["price_jp"]                                    #price_jp列を抽出
sns.boxplot(x,y,hue=house["good/bad"])
plt.show()
