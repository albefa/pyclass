print("\n请给我两个数字，我将告诉你结果：")
print("---输入（q）退出---")
while True:
    a = input("请输入第一个数字：")
    b = input("请输入第二个数字：")

    if a == 'q' or b =='q':
        break
    else:
        try:
            c = int(a) + int(b)
        except ValueError:
            print("对不起请输入数字")
        else:
            print(c)
