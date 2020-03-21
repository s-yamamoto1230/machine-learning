str = "Hello,World"
print(str)

num = 10 + 20 + 30 + 40
print(num)

#途中改行
num1 = 10 + 20 + 30 + 40 + \
      50 + 60 + 70 + 80
print(num1)

#一行書き
num2 = 10; num3 = 8; num4 = 12
print (num2 + num3 + num4)

#三連引用符
msg = """¥
こんにちは。
今日のミーティングですが"予定通り"の時間に行います。
何か変更があれば連絡してください。"""
print(msg)

#繰り返し
str = "abc"
print(str * 4)

#インデックス
str1 = "Hello"
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])

str2 = "こんにちは"
print(str2[-5])
print(str2[-4])
print(str2[-3])
print(str2[-2])
print(str2[-1])

#指定範囲取得
str = "愛知県名古屋市中村区"
print(str[0:7])
print(str[:3])
print(str[3:])
print(str[0:8:2])
