#NumPy  (複数のデータが集まって１つの意味を成すものに有効。写真、音声など)
import numpy as np  #今後npで呼び出せる
#１次元配列生成
a = np.array([1,2,3])
#２次元配列生成
b = np.array([[1,2,3],[4,5,6]])
print(f"aは{a.ndim}次元です")
print(f"aの要素数は{a.size}個です")
print(f"aは{a.shape}行列です")
print(f"aの型は{a.dtype}")
print(f"bは{b.ndim}次元です")
print(f"bの要素数は{b.size}個です")
print(f"bは{b.shape}行列です")
print(f"bの型は{b.dtype}")

#ゼロ行列
zeros2x3 = np.zeros((2,3))  #オール0の二行三列配列を作る
print(zeros2x3)
#イチ行列
ones2x3 = np.ones((2,3))
print(ones2x3)

#arange関数
print(np.arange(10))    #0から始まる連続する10の整数配列
#np.arange(始,終,間隔) 終わりの値を含まない
print(np.arange(10,30,5))
print(np.arange(0,2,0.3))
#等間隔な数列を生成(始,終,個数) 終わりの値を含む
print(np.linspace(0,np.pi,10))

#reshape関数  形を変えて値の順番はそのまま
array = np.array([1,2,3,4,5,6]) #6要素の配列を生成
arr2x3 = array.reshape(2,3)     #arrayを(2,3)行列に変形
print(arr2x3)
arry2x4 = array.reshape(2,3)    #割り切れない値ではreshape不可。エラーになる。

#ravel関数
a = arr2x3.ravel()      #行列を一次元にほどく
print(a)

#Tまたはtranspose関数    形も順番も変更する
arr2x3_T = arr2x3.T     #転置行列。行と列を入れ替える。二行三列なら三行二列になる。
arr2x3_transpose = arr2x3.transpose()   #上と同じ
print(arr2x3_T)
print(arr2x3_transpose)

#---------------------------------------------------------
a = np.arange(15)
print(a)
b = a.reshape(3,5)
print(b)
print(f"aは{a.shape}行")
print(f"bは{b.shape}行列")
