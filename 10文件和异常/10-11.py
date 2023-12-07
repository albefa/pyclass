import json

num = input("请输入的你喜欢的数字：")
filename ='likenum.json'
with open(filename,'w') as f:
    json.dump(num,f)

with open(filename) as f:
    numbers =json.load(f)
    print("你喜欢的数字是："+numbers)