# width = int(input('Please enter width: '))
# price_width = 10
# item_width = width - price_width
# header_fmt ='{{:{}}}{{:>{}}}'.format(item_width, price_width)
# fmt        ='{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
# print('=' * width)
# print(header_fmt.format('Ttem','Price'))
# print('-' * width)
# print(fmt.format('Apple', 0.4))
# print(fmt.format('Pear', 0.55))
# print(fmt.format('Cantaloupes', 1.93))
# print(fmt.format('Dried Apricots(16 oz.)', 8.02))
# print(fmt.format('Pruns (4lbs)', 12.06))
# print('=' * width)

# name = input('what is your name')
# if name.endswith('Gumby'):
#     print('hello,Mr.Gumby')
# else:
#     print('hello, stranger')
# d = {'x': 1, 'y': 2, 'z': 3}
# for key in d:
#     print(key, 'corresponds to', d[key])

# from math import sqrt

# for n in range(99, 0, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break

# result =[]
# for x in range(3):
#     for y in range(3):
#         result.append((x,y))

# girls =['alice','bernice','clarice']
# boys =['chris','arnold','bob']
# letterGirls ={}
# for girl in girls:
#     letterGirls.setdefault(girl[0],[]).append(girl)
# print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

#斐波那契数
# fibs = [0,1]
# for i in range(8):
#     fibs.append(fibs[-2] + fibs[-1])
# print(fibs)

#自定义函数
def fibs(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
print(fibs(10))
print(fibs(18))

#抽象函数的关键在于隐藏所有细节。数据化结构的函数，最后的键排列顺序不是固定的，
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
storage ={}
init(storage)
print(storage)

#先编写获取函数，再编写储存函数

#关键字参数
def hello_1(greeting, name):
    print('{}, {}!'.format(greeting, name))
def hello_2(name, greeting):
    print('{}, {}!'.format(name, greeting))
def hello_3(greeting='Hello',name='world'):
    print('{},{}!'.format(greeting,name))
