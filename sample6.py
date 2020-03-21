#クラス
'''
_init_ ・コンストラクタ
       ・クラスが持つフィールドを定義する
 selt  ・クラスに属しているということを明示するためにつける
       ・フィールドの先頭と関数の第一引数にはselfをつける
       ・クラス内からフィールドへアクセスする場合にはselfが必要
'''

class ModelA:
    def __ini_t_(self):
        self.gas = 100
    def run(self):
        self.gas = self.gas - 5
        print("10Km走りました")
    def charge(self,supply_amount):
        self.gas = self.gas + supply_amount
        print(f"現在のガソリンは{self.gas}リットルです")

class ModelA_2:
    def __init__(self,gas):   #_init_の引数にgasを追加
        self.gas = gas      #gasの値がself.gasの初期値になる
    def run(self):
        self.gas = self.gas - 5
        print("10Km走りました")
    def charge(self,supply_amount):
        self.gas = self.gas + supply_amount
        print(f"現在のガソリンは{self.gas}リットルです")

#------------------------------------------------------
class Human:
    def __init__(self):
        print("initialized")
        self.health = 100   #インスタンスが持つhealthを100に初期化
        self.time = 10      #インスタンスが持つtimeを100に初期化
        self.achieve = 0    #インスタンスが持つachieveを100に初期化
    def work(self):
        print("work")
        self.achieve += 1
        self.time -= 1
        self.health -= 50
    def rest(self):
        print("rest")
        self.time -= 3
        self.health += 50

human1 = Human()    #human1と言う名前のインスタンスを生成
print(f"health:{human1.health}")
print(f"time:{human1.time}")
print(f"achieve:{human1.achieve}")

human1.work()
print(f"health:{human1.health}")
print(f"time:{human1.time}")
print(f"achieve:{human1.achieve}")

human1.rest()
print(f"health:{human1.health}")
print(f"time:{human1.time}")
print(f"achieve:{human1.achieve}")
