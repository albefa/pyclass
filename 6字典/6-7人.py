#创建一个people空列表
people =[]
#将三个字典加入people列表
person1 ={'first_name':'erci',
         'last_name':'metion',
         'age':45,
         'city':'sitka',
         }
people.append(person1)

person2 ={'first_name':'bob',
         'last_name':'Tai',
         'age':55,
         'city':'praris',
         }
people.append(person2)

person3 ={'first_name':'chang',
         'last_name':'wang',
         'age':10,
         'city':'toyr',
         }
people.append(person3)
print(people)
# full_name = person['fist_name'] + " " +person['last_name']
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

# print("\tFullname"+ full_name)
# print("\tCity:"+ s_city)
# print("\tName" + s_name)
# print("\tAge: " + str(s_age))
#print 位置重要，否则不加入for循环
    print(f"{name}, of {city}, is {age} years old.")
for i in people:
    print(i)
