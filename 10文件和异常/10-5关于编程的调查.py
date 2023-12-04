filename = 'reason.txt'
print("———调查喜欢编程的原因，按（q）退出！———")
while True:
    reason = input("请问您为什么喜欢编程：")
    if reason == 'q':
        break
    else:
        with open(filename, 'a') as f:
            f.write(reason + "\n")
