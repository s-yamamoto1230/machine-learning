#for文
for i in [1,2,3]:
    print(i)

#while文
count = 1
while count <= 3: #countが３以下の時、繰り返し処理
    print(count)
    count = count + 1

#if文 and(かつ)　or(または)
score = 65
if score >= 90: #90点以上
    print("優")
elif 90 > score and score >= 70: #90点未満70点以上
    print("良")
elif 70 > score and score >= 60: #70点未満60点以上
    print("可")
else:
    print("不可")

#条件が来るまでループ
count = 0
while True:
    count = count + 1
    if count == 5:
        break
    print(count)

#-----------------------------------------------------
x = 2**10
print(x)

ans = 1
for j in[1,2,3,4,5,6,7,8,9,10]:
    ans = ans * 2
print(ans)

y = 1
ans = 1
while y <= 10:
    ans = ans * 2
    y = y + 1
print(ans)
