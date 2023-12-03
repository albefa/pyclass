#一人多个喜欢的数字，并打印
favorite_num ={'bob':[1,2,3],
               'alice':[33,44,55],
               'tom':[666,777,888],
               }
for name, numbers in favorite_num.items():
    print("\n" + name.title())
    for number in numbers:
        print("\t"+str(number))