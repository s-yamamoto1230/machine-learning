#データの可視化  Matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(4,4))   #横4inch x 縦4inch のグラフを描く宣言
plt.plot([0,2,4,6,8],[0,6,12,24,48],label="graph")  #[xの値],[yの値],label="線の名前"
plt.xlabel("x axis")    #横軸名前
plt.ylabel("y axis")    #縦軸名前
plt.title("title")      #グラフの名前
plt.legend()            #labelを表示するための宣言
plt.show()              #グラフ呼び出し

x = np.linspace(0,10,20)
print(x)
y = x**2
z = ((x-2)*(x-4))**2
plt.plot(x,y,label="y=x^2")
plt.plot(x,y,label="z=(x-1)^3")
plt.plot(x,y,label="w=((x-2)(x-4))^2")
plt.legend()
plt.show()
