def greet_users(names):
    """列表中打印问候每一个成员"""
    for name in names:
        print("你好 " + name.title() + "!")


usernames = ['alb', 'tom', 'saber', 'archer']
greet_users(usernames)
