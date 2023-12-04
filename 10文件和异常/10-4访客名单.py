filename ='guest_book.txt'

print("输入（q）退出！")
while True:
    user=input("请输入访客名字：")
    if user=='q':
        break
    else:
        with open(filename,'a') as f:
            f.write(user+"\n")
        print(user+"您好，已加入顾客名单！")