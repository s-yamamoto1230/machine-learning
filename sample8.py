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
