# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
#一个简单的数据库

#一个将人名用作键的字典。每个人都用一个字典表示，字典包含键’phone‘和’addr‘，它们分别与电话号码和地址相关联。
people = {
    'Alice' :{
        'phone':'2356',
        'addr':'Foo bridge 89'
    },

    'Beth' :{
        'phone' :'9305',
        'addr' :'Bar str 58'
    },
    'Cecil' :{
        'phone' :'5648',
        'addr' :'Baz avenue 90'
    }
}
# # #电话号码和地址的描述性标签，共打印输出时使用
# # labels = {
# #     'phone' : 'phone number',
# #     'addr' : 'address'
# }

# name = input ('Name:  ')
#
# #要查找电话号码还是地址？
# request = input ('Phone number (p) or address (a)')
# #使用正确的键
# if request == 'p': key ='phone'
# if request == 'a': key ='addr'
# #仅当名字是字典包含的键时才打印信息
# if name in people: print("{}'s {} is {}.".format(name,labels[key],people[name][key]))

#一个使用get（）的简单数据库
#在这里插入代码清-单中的数据（字典people）
labels = {
    'phone':'phone number',
    'addr':'address'
}
name =input('Name: ')

#要查找电话号码还是地址？
request = input('Phone number (p) or address (a) ?')
#使用正确的键：
key = request #request既不是‘p'也不是’a'
if request == 'p':key == 'phone'
if request == 'a':key == 'addr'
#使用get提供默认值
person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not available')
print("{}'s {} is {}.".format(name,label,result))