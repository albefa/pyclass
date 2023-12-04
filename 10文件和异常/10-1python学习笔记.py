# 打开并打印
file_name = 'learning_python.txt'  # 文本中出现字母和数字组合数字会报错

print("读取文本并打印")
with open(file_name) as file_object:
    result = file_object.read()
    print(result)

print("\n读取文本并逐行打印")
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n储存在一个列表中后再打印")
with open(file_name) as file_object:
    lines =file_object.readlines()

for line in lines:
    print(line.rstrip())