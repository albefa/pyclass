# 将类的一部分作为一个独立的类提取出来
class Car:
    """模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_readings = 0

    def get_decriptive_name(self):
        """返回信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印里程"""
        print("这辆车行驶了 " + str(self.odometer_readings))

    def update_odometer(self, milage):
        """
        将里程表读书设置为指定的值
        禁止里程回溯，
        """
        if milage >= self.odometer_readings:
            self.odometer_readings = milage
        else:
            print("不可回调里程")

    def increment_odometer(self, miles):
        """将里程数表读数增加指定的量"""
        self.odometer_readings += miles


class Battery:
    """"
    将电池作为一个单独的类
    模拟电动汽车电瓶的简单尝试
    """

    def __init__(self, battery_size=70):
        """初始化电池属性"""
        self.battery_size = battery_size

    def descibe_battery(self):
        """输出一条描述电瓶容量的信息"""
        print("THis car has a " + str(self.battery_size) + "-km battery .")

    def get_rang(self):
        """打印一条消息，指出电动车的里程数"""
        if self.battery_size == 70:
            range = 240

        elif self.battery_size == 85:

            range = 270
        message = "this car can go approximataly " + str(range)
        message += " miles on full charge"
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性，再初始化电动车特有属性"""
        super().__init__(make, model, year)
        self.battery = Battery()  # 调用battery属性


my_tesla = ElectricCar('telsa', 'model3', 2019)

print(my_tesla.get_decriptive_name())
my_tesla.battery.descibe_battery()
my_tesla.battery.get_rang()
