#交通信号灯？？
promt = "\nTell me something,and I will repeat it back to you: "
promt += "\nEnter 'quit' to end the program."
active = True
while active:
    massage = input(promt)
    if massage =='quit':  #信号quit的标志当massage是quit时，active是false，循环停止
        active = False
    else:
        print(massage)
