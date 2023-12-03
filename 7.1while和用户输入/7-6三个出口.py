# 三种方法结束循环；第一种while中条件结束寻循环（7-4pizza）
promt = "1请输入一种配料： "
name = ""
while name != 'quit':
    name = input(promt)
    print("我们会在披萨中添加" + name + "这种配料")

# active
promt = "2请输入一种配料： "
active = True
while active:
    name = input(promt)
    if name == 'quit':
        active = False
    else:
        print("我们会在披萨中添加" + name + "这种配料")

# break
promt = "3请输入一种配料： "
while True:
    name = input(promt)
    if name == 'quit':
        break
    else:
        print("我们会在披萨中添加" + name + "这种配料")
