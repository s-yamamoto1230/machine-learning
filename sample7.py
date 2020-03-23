#外部ライブラリ import
import time
import math
for count in range(1,4):
    time.sleep(1)
    print(f"{count}")
print(math.log(100))

#------------------------------------
for count1 in range(1,13):
    time.sleep(1)
    if count1%3 == 0:
        print("3の倍数です!!")
    else:
        print(f"{count1}秒経過")
