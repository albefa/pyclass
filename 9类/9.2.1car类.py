# 类中，给属性指定默认值
class Car:
    """模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_readings = 18668

    def get_decriptive_name(self):
        """返回信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印里程"""
        print("这辆车行驶了 "+str(self.odometer_readings))


my_new_car = Car('audi', 'A4', 2016)
print(my_new_car.get_decriptive_name())

my_new_car = Car('BMW','5seis',2018)
print(my_new_car.get_decriptive_name())
my_new_car.read_odometer()

# 修改属性
my_new_car.odometer_readings = 500
my_new_car.read_odometer()
