#関数
def calc_hypotenuse(x,y): #関数定義
    ans = (x**2 + y**2)**(1/2)
    return ans

a = calc_hypotenuse(2,3) #関数呼び出し
b = calc_hypotenuse(4,5)
c = calc_hypotenuse(6,7)
print(a)
print(b)
print(c)

#-------------------------------------------
def BMI(height,weight):
    ans = weight / (height**2)  #BMI計算
    return ans

def Degree_of_obesity(height,weight):
    ans = BMI(weight,height)
    if ans < 18:    #18未満
        return "痩せ気味"
    elif ans >= 18 and ans < 25:    #18以上25未満
        return "普通"
    else:
        return "太り気味"

tanaka = {"height":2,"weight":80}
check_BMI = BMI(tanaka["height"],tanaka["weight"])
check_obesity = Degree_of_obesity(tanaka["height"],tanaka["weight"])
print(check_BMI)    #BMI出力
print(check_obesity)    #肥満度出力

#-------------------------------------------------
#renge関数
for i in range(5):  #0～順に4まで
    print(i)
for j in range(2,5):    #2～順に4まで
    print(j)
for k in range(2,5,2):  #2～4まで２刻み
    print(k)

base = 2
for Multiplication_table2 in range(1,10):
    print(f"{base} * {Multiplication_table2} = {base * Multiplication_table2}")

#---------------------------------------------------
#format関数
x = 15
print("xは{:.2f}".format(x)) #15を小数点第2まで出力。fはflortのf
print(f"xは{x:.2f}") #fstringを用いた書き方

name = "taro"
age = 20
print("私の名前は{}です。年齢は{:d}です。".format(name,age))  #format書き方
print(f"私の名前は{name}です。年齢は{age:d}です。")   #fstring書き方
