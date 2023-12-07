from name_function import get_formatted_name

print("输入'q'退出")
while True:
    first =input("\nPlease give me a first name: ")
    if first =='q':
        break
    last =input("Please give me a last name: ")
    if last =='q':
        break

    formatter_name = get_formatted_name(first,last)
    print("\tNearly formatted name: "+ formatter_name+'.')