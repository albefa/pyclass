def get_formatted_name(first_name, last_name):
    """返回简洁的名字"""
    full_name = first_name + ' ' + last_name
    return full_name.title()  # 返回值full_name


while True:
    print("\nPlease Tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last_name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
