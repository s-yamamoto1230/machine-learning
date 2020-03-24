#データ参照
import numpy as np
a = np.array(["あ","い","う","え","お"])
print(a[2])     #先頭から参照する場合は0スタート
print(a[-3])    #末尾からスタートする場合は-1スタート
print(a[[0,2]]) #0番目と2番目の要素を取り出す
print(a[1:4])    #1から3番目までの要素を取り出す[始:終]
print(a[0:4:2]) #0から4番目までで2つ間隔で取り出す[始:終:間隔]

#二次元の場合
b = np.array([[1,2,3],[4,5,6]])
print(b[1,2])   #1行目2列目を取り出す
print(b[:,2])   #2列目を取り出す。:は任意の意味
print(b[:,[0,2]])   #行は任意。列は0列目と2列目を取り出す
c = np.array([[0,1,2,3,4],[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]])
print(c[-1])    #-1列目全てを取り出す
print(c[range(5),range(5)]) #0,1,2,3,4の行列で重なる部分を取り出す

#条件に合った要素の抜き出し  .where(<条件文>,<真の時の値>,<偽の時の値>)
d = np.arange(20).reshape((4,5))    #1から19までで4行5列の配列
e = np.where((d>0) & (d%3 == 0),1,0)    #0より大きくてかつ3で割って余りが0のものに1を返す
print(e)

#------------------------------------------------------------
array = np.arange(1,26).reshape((5,5))
print(array)
print(array[1:3,1:3])   #(1,2)行(1,2)列の交差を出力