with open('pi_digits.txt') as file_object:
    lines = file_object.read()

pi_string=''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

file_name='pi_30_digits.txt'
with open(file_name) as file_object:
    lines =file_object.read()
pi_string=''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))



file_name='pi_30_digits.txt'
with open(file_name) as file_object:
    lines =file_object.read()
pi_string=''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

file_name='pi_million_digits.txt'
with open(file_name) as file_object:
    lines =file_object.read()
pi_string=''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52]+"...")
print(len(pi_string))
# 你的生日是否包含在pi中
file_name='pi_million_digits.txt'
with open(file_name) as file_object:
    lines =file_object.read()
pi_string=''
for line in lines:
    pi_string += line.strip()

birthday=input("输入你的生日（mmddyy）: ")
if birthday in pi_string:
    print("您的生日在百万数的pi中")
else:
    print("您的生日不在百万数pi中")