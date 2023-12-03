class Restaurant:
    """餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """指出餐馆名字及开业状态"""
        print("餐馆名：" + self.restaurant_name.title() + ".")
        print("餐馆规模： " + self.cuisine_type + ".")

    def open_restaurant(self):
        """指出餐馆正在开业"""
        print(self.restaurant_name.title() + "餐馆正在营业！")


north_restaurant = Restaurant('big house', 'huge')
print("\n餐馆信息：")
north_restaurant.describe_restaurant()
north_restaurant.open_restaurant()
