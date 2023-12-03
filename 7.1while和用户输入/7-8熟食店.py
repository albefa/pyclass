# 列表中含各种三明治名字
sandwich_orders = ['apple', 'peache', 'jirou', 'peigen']
# 空白的完成列表
finished_sandwichs = []
# 便利sandwich_orders,并打印
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made your " + current_order + " sandwich.")
    finished_sandwichs.append(current_order)
# 做好后打印全部
print("\n已经做好了这些三明治：")
for finished_sandwich in finished_sandwichs:
    print(finished_sandwich.upper())