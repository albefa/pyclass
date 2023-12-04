filename='guest.txt'

users=input("请输入您的用户名：")

with open(filename,'a') as f:
    f.write(users+"\n")