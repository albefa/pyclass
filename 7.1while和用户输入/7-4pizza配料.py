promt = "请输入一种配料： "
while True:
    name = input(promt)
    if name == 'quit':
        break
    else:
        print("我们会在披萨中添加" + name + "这种配料")
