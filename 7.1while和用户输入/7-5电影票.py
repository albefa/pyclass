# 不到3岁免票，3~12半价，超过12全价
cou = "请输入您的年龄： "
while True:
    age = input(cou)
    if age == 'quit':  # 区分字符与数字，str和int。 先写quit的条件。
        break
    elif 0 < int(age) < 3:
        print("票价免费")
    elif 3 <= int(age) < 12:
        print("您的票价是10美元")
    elif 12 <= int(age):
        print("您的票价是15美元")
