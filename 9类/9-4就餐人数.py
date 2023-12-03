class Restaurant:
    """餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 6

    def describe_restaurant(self):
        """指出餐馆名字及开业状态"""
        print("餐馆名：" + self.restaurant_name.title() + " .")
        print("餐馆规模： " + self.cuisine_type + " .")

    def open_restaurant(self):
        """指出餐馆正在开业"""
        print(self.restaurant_name.title() + "餐馆正在营业！")

    def read_number(self):
        """打印就餐人数"""
        print("有" + str(self.number_served) + "正在用餐")

    def set_number_served(self, in_number):
        """设置餐馆人数"""
        self.number_served = in_number

    def increment_number_served(self,moment_number):
        """就餐人数递增"""
        self.number_served += moment_number

r_restaurant = Restaurant('beihj', 'mid')
r_restaurant.describe_restaurant()
r_restaurant.open_restaurant()
r_restaurant.read_number()

# 添加set_number_serverd
e_restaurant =Restaurant('AAAA','mix')
e_restaurant.describe_restaurant()
e_restaurant.open_restaurant()
e_restaurant.set_number_served(22)
e_restaurant.read_number()
print("就餐人数增加后顾客人数： ")
e_restaurant.increment_number_served(20)
e_restaurant.read_number()