def get_formatted_name(first_name, last_name, middle_name=' '):
    if middle_name :
         full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()  # 返回值full_name


music = get_formatted_name('tom', 'simth', 'cc')  # 定义music，返回值储存在music
print(music)
music = get_formatted_name('aa','bb')
print(music)