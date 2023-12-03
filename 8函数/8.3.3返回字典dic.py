def build_person(first_name, last_name, age=' '):
    """返回一个字典，其中包含有关一个人信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


music = build_person('jimi', 'hendix', age = 27)
print(music)
music = build_person('tom','AAAA')
print(music)
