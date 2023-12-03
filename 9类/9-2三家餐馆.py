class Restaurant:
    """餐馆的类"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """指出餐馆名字及开业状态"""
        print("餐馆名："+self.restaurant_name.title()+".")
        print("餐馆规模： "+self.cuisine_type+".")


    def open_restaurant(self):
        """指出餐馆正在开业"""
        print(self.restaurant_name.title()+"餐馆正在营业！")

n_r =Restaurant('house','huge')
l_r =Restaurant('apple','mid')
w_r =Restaurant('huawei','mix')
print("\n餐馆信息")
n_r.describe_restaurant()
n_r.open_restaurant()
l_r.open_restaurant()
l_r.describe_restaurant()
w_r.describe_restaurant()
w_r.open_restaurant()