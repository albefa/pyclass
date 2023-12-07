import json

filename = 'likenum.json'

try:
    with open(filename) as f:
        numbers = json.load(f)
except FileNotFoundError:
    numbers = input("请输入的你喜欢的数字：")
    with open(filename, 'w') as f:
        json.dump(numbers, f)
    print("Thanks，I rember that.")

else:
    print("你喜欢的数字是：" + numbers)
