import json

def greet_user():
    """问候用户，并指出名字"""

    filename = 'username.json'
    path =r"H:\pyclass\10文件和异常\username.json"
    try:
        with open('filename') as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("what is your name? ")
        with open(filename,'w') as f:
            json.dump(username,f)
            print("We'll remember you when you when you come back ,,"+username+" !")
    else:
        print("Welcomback, "+username+"!")


greet_user()