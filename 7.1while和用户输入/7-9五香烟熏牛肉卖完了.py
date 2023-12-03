# 卖完了,pastrami
print("\n店里的五香烟熏牛肉卖完了")
sandwich_orders = ['pastrami', 'apple', 'peache','pastrami', 'jirou', 'peigen','pastrami']
print(sandwich_orders)
# 删除'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
