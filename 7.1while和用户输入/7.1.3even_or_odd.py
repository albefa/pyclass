#%表示余数，可分奇数偶数
num = input("Enter a number, and Ill tell you if it's even or add")
num =int(num)
if num % 2 ==0:
    print("\nThe number "+ str(num) + " is even.")
else:
    print("\nTHe number "+ str(num) + " is add.")
