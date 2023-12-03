# 定义汽车函数2行参+关键字实参
def make_car(maker, size, **user_info):
    """制造商，型号，其他关键字实参"""
    builing_cars = {}
    builing_cars['Maker_name: '] = maker
    builing_cars['Size_name: '] = size
    for key, value in user_info.items():
        builing_cars[key] = value
    return builing_cars



msg=make_car('audi', 's3', color='red', sheel='20')
print(msg)
msg =make_car('bence','s600',color='blue',tow_package =True,sheel='22')
print(msg)