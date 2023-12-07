# filecats = 'cats.txt'
# filedogs = 'dogs.txt'
# with open(filedogs) as f_dogs:
#     dogsnames = f_dogs.read()
#     print("狗的名字是")
#     for dogsname in dogsnames:
#         print(dogsname.split())
# with open(filecats) as f_cats:
#     catsnames = f_cats.read()
#     print("猫的名字是：")
#     for catsname in catsnames:
#         print(catsname.split())

filenames =['cats.txt','dogs.txt']

for filename in filenames:
    print("\n REading file:"+filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("!!!sorry,Icant find that file")