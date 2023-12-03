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

class IceCramStand(Restaurant):
    """继承Resturant类"""
    def __init__(self,restaurant_name, cuisine_type='冰淇淋店'):
        """重置属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def ReadStand(self):
        """返回冰淇淋站信息口味"""
        for flavor in self.flavors:
            print("甜品店有下列的口味："+flavor)


OcIceCreamStand = IceCramStand('DQ','huge')
OcIceCreamStand.flavors=['apple','草莓','香草','原味']
OcIceCreamStand.open_restaurant()
OcIceCreamStand.ReadStand()
