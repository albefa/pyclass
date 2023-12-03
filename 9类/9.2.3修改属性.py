# update_odometer 修改属性
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


# update_odometer 修改属性

my_new_car = Car('BMW', '5seis', 2018)
print(my_new_car.get_decriptive_name())
my_new_car.update_odometer(2323)
my_new_car.read_odometer()

my_used_car = Car('subra', 'outback', 2000)
print(my_used_car.get_decriptive_name())

my_used_car.update_odometer(265000)
my_used_car.read_odometer()

my_used_car.increment_odometer(333)
my_used_car.read_odometer()
