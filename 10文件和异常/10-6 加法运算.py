print("请给我两个数字，我将告诉你结果：")
a = input("请输入第一个数字：")
b = input("请输入第二个数字： ")
c = int(a) +int(b)
print(c)
print("\n请给我两个数字，我将告诉你结果：")
try:
    a = input("请输入第一个数字：")
    b = input("请输入第二个数字： ")
    c = int(a) +int(b)
except ValueError:
    print("对不起请输入数字")
else:
    print(c)
