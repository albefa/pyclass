promt = "\nTell me something,and I will repeat it back to you: "
promt += "\nEnter 'quit' to end the program."
massage = ""
while massage != 'quit':   #不等于quit循环
    massage = input(promt)

    if massage !='quit':  #不打印quit
        print(massage)