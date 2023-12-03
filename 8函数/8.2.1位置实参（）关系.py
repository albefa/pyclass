def desccribe_pet(anmal_type, pet_name):
    """动物类型及名字"""
    print("\nI have a "+anmal_type+".")
    print("My "+anmal_type+" name is "+pet_name+".")
desccribe_pet('dog','tudou')
desccribe_pet('hamster','harry')
# 关键字实参
desccribe_pet(pet_name='cc',anmal_type='cat')