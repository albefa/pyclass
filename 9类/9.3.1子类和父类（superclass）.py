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


class ElectricCar(Car):
    """大类Car，小类ECar"""

    def __index__(self, make, model, year):
        """
        初始化父类属性
        再初始化电动车的属性
        """
        super().__init__(make, model, year)  # 父类（Superclass）



my_tesla = ElectricCar('tesla', 'model3', 2018)
print(my_tesla.get_decriptive_name())

my_car = ElectricCar('BMw', 'x3', '2018')
print(my_car.get_decriptive_name())

