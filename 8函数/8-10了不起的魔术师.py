def show_magicians(names):
    for name in names:
        print("魔术师名字叫做：" + name + "!")


def make_great(unadd_names, add_names):
    """修改列表并加入The Great"""

    while unadd_names:
        current_name = unadd_names.pop()
        add_name = "The Great " + current_name.title()

        add_names.append(add_name)


unadd_names = ['tom', 'able', 'CC', 'bob']
add_names = []
# 容易忽略添加函数
make_great(unadd_names, add_names)
show_magicians(add_names)
