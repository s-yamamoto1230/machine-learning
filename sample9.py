#Numpy配列に対する数学的演算
import numpy as np
a = np.array([0,1,2,3,9])
b = np.array([2,4,6,0,np.inf])    #infは無限大
#足し算(+,np.add(a,b))
print(a + b)    #要素ごとの足し算。要素の個数が等しくないと計算できない
print(a + 3)    #全ての要素に3を足す
#引き算(-,np.subtract(a,b))
print(a - b)
print(a - 3)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
#同じ要素番号同士の掛け算
print(A * B)
#行列の掛け算
print(A.dot(B))

c = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(c.sum())  #aの総和
print(c.mean()) #aの平均
#axis   0は行方向、1は列方向
print(c.sum(axis = 0))  #行方向の和
print(c.mean(axis = 1)) #列方向の平均

#------------------------------------------------
a = np.arange(1,11)
print(a)
b = a.reshape(2,5)
print(b)
b0 = np.arange(1,6)
b1 = np.arange(6,11)
print(b0 + b1)
print(b0 - b1)
print(b0 * b1)
print(b0 / b1)
