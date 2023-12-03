cars =['bmw','audi','subra','vlolo','vm']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())
#5-1
car ='audi'
print("Is car =='subra'? I predict Ture.")
print(car =='subra')
print("\nIs car =='audi'? I predict False.")
print(car =='audi')
#5-2
print("\n")
food ='Miantiao'
print(food =='mifan')
print(food.lower()=='miantiao')
print("\n比大小")
age_0 =20
age_1 =25
print(age_0 < age_1)
print(age_0 >  age_1)
print(age_0 <= age_1)
print(age_0 >= age_1)
print(age_0 == age_1)
print('\n关键字and-or')
print(age_0 >15 and age_1 >22)
print(age_0 > 20 or age_1 >23)
print('\n测试包含——不包含')
num_1 =['12','14','15','18']
print('15' in num_1)
print('36' in num_1)
print('68'not in num_1)

print("\n")
#5-3try alien_color
alien_colors =['green', 'yellow', 'red']
for alien_color in alien_colors[0:3]:
    print(alien_color.lower())
    if alien_color == 'green':
         print("玩家获得5分")
    if alien_color not in ['green']:
        print("玩家获得10分")
#5-4else
print("\n")
alien_colors =['green', 'yellow', 'red']
for alien_color in alien_colors[0:3]:
    print(alien_color.lower())
    if alien_color =='green':
        print('玩家得到6')
    else:
        print('player got 10 point')
#5-5if_elif_else
print("\n")
alien_colors =['green', 'yellow', 'red']
for alien_color in alien_colors[0:3]:
    print(alien_color.lower())
    if alien_color =='green':
        print('player got 5 points')
    elif alien_color =='yellow':
        print('Player got 10 points')
    else:
       print('Plater got 15 points')

print("\n")
alien_colors =['green', 'yellow', 'red']
for alien_color in alien_colors[0:3]:
    print(alien_color.lower())
    if alien_color =='green':
        print("玩家得到5分")
    if alien_color =='yellow':
        print("玩家得到10分")
    if alien_color =='red':
        print("玩家得到20分")

print("\n")
alien_colors =['green', 'yellow', 'red']
for alien_color in alien_colors[0:3]:
    print(alien_color.lower())
    if alien_color =='green':
        print('got 5')
    elif alien_color =='yellow':
        print('got 10')
    elif alien_color =='red':
        print('got 15')

#5-6人生的不同阶段
age = 4
print("\n")
print("人生阶段：")
if 0 < age < 2:
    print('婴儿')
if 2<= age < 4:
    print("蹒跚学步")
if 4<= age <13:
    print('儿童')
if 13<= age <20:
    print('青少年')
if 20<= age <65:
    print('成年人')
if 65<= age:
    print('老年人')

#5-7喜欢的水果
print('\n')
favorite_fruits =['apple','banana','peach']
if 'apple' in favorite_fruits:
    print('1You realiy like apple')
if 'banana' in favorite_fruits:
    print('2you realy like banana')
if 'peach' in favorite_fruits:
    print('3you realy like peach')
if 'boluo' in favorite_fruits:
    print('4you realt like it')
else:
    print('you dont like it ')