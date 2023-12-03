# 三明治点餐一个形参
def order_list(*tastlist):
    """输出所有配料"""
    print("\n顾客的点餐的三明治是：")
    print(tastlist)


order_list('applemeat')
order_list('beaf', 'extro cheese', 'furt')
order_list('meat', 'banana', 'vagetable', 'organe')
