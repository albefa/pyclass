print("give me two number ,and I'll divide them")
print("Enter 'q' to quit.")

while True:
    firstnumber =input("\nFist number: ")
    if firstnumber =='q':
        break
    secondnumber =input("seond number: ")
    try:
        answer = int(firstnumber)/int(secondnumber)
    except ZeroDivisionError:
        print("You cant divide by 0")
    else:
        print(answer)