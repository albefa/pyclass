# 9-10
# from resturant import Rresturant

# 9-11
# from NewUsers import Users,Privileges,Admin

# 9-13

from random import randint

"""引入基础模块"""


class Die:
    """骰子的类"""

    def __init__(self, sides=6):
        """初始化骰子"""
        self.sides = sides

    def roll_die(self):
        """返回骰子的一个面数"""
        self.result = randint(1, int(self.sides))
        # results=[]
        # results.append(self.result)
        return (self.result)



# 6面骰子
d6 = Die()
results = []
for roll_num in range(10):
    results.append(d6.roll_die())
print("10次投掷六面骰子")
print(results)
#10面骰子
d10 =Die(sides=10)
results = []
for roll_num in range(15):
    results.append(d10.roll_die())
print("10次投掷10面骰子")
print(results)

#20面骰子
d20 =Die(sides=20)
results = []
for roll_num in range(25):
    results.append(d20.roll_die())
print("10次投掷20面骰子")
print(results)
