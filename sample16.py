#オブジェクト指向インターフェース
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,20)
print(x)
y = x**2
z = (x-1)**3
w = ((x-2)*(x-4))**2

#①plt.add_subplot
fig = plt.figure(figsize=(3,3))     #空のfigureを作り、figと名付ける
ax = fig.add_subplot(1,1,1)         #1行1列のaxesをfigの中に作成。1番目のaxesをaxと名付ける
ax.plot(x,y,label="y=x^2")
ax.plot(x,z,label="z=(x-1)^3")
ax.plot(x,w,label="w=((x-2)(x-4))^2")
ax.set_xlim(0,10)
ax.legend()
plt.show()

#②plt.subplots
fig,ax = plt.subplots(1,1,figsize=(3,3))     #figureとaxesを同時に生成。
ax.plot(x,y,label="y=x^2")
ax.plot(x,z,label="z=(x-1)^3")
ax.plot(x,w,label="w=((x-2)(x-4))^2")
ax.legend()
ax.set_title("tgree curves")
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
plt.show()

#グラフを分割
fig,ax = plt.subplots(1,3,figsize=(14,4))   #1行3列に区切った横14inch 縦4inch のグラフ
print(ax)   #axがarrayであることを確認
ax[0].plot(x,y,label="y=x^2")
ax[1].plot(x,z,label="z=(x-1)^3")
ax[2].plot(x,w,label="w=((x-2)(x-4))^2")
for i in range(3):
    ax[i].legend()
    ax[i].set_xlabel("x axis")
    ax[i].set_ylabel("y axis")
plt.tight_layout()
plt.show()

#2行2列のグラフ
fig,ax = plt.subplots(2,2,)
ax[0,0].plot(x,y,label="y=x^2")
ax[0,0].legend()
ax[0,1].plot(x,z,label="z=(x-1)^3")
ax[0,1].legend()
ax[1,0].plot(x,w,label="w=((x-2)(x-4))^2")
ax[1,0].legend()
plt.show()

#------------------------------------------------
fig,ax = plt.subplots(3,1,figsize=(8,6))    #3行1列のグラフ縦8inch 横6inch
x = np.linspace(-1*np.pi,np.pi,100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
ax[0].plot(x,y1,label="sin(x)",color="red")     #赤のグラフ
ax[1].plot(x,y2,label="cos(x)",color="blue")    #青のグラフ
ax[2].plot(x,y1,label="tan(x)",color="green")   #緑のグラフ
for i in range(3):
    ax[i].set_xlabel("x")
    ax[i].set_ylabel("y")
    ax[i].legend()
plt.tight_layout()
plt.show()
