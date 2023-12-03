num = "可以判断输入的数是不是10的整倍数"
num += "\n请输入数字："
number =input(num)
number =int(number)
if number %10 ==0:
    print(str(number) + "是10的倍数")
else:
    print(str(number) + "不是10的倍数")