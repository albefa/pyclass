# 创建一个people空列表
people = []
# 将三个字典加入people列表
person1 = {'first_name': 'erci',
           'last_name': 'metion',
           'age': 45,
           'city': 'sitka',
           }
people.append(person1)

person2 = {'first_name': 'bob',
           'last_name': 'Tai',
           'age': 55,
           'city': 'praris',
           }
people.append(person2)

person3 = {'first_name': 'chang',
           'last_name': 'wang',
           'age': 10,
           'city': 'toyr',
           }
people.append(person3)
for person in people:
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    s_city = person['city']
    s_age = person['age']
    print("\nFullname: " + full_name)
    print("City: " + s_city)
    print("Age: " + str(s_age))
