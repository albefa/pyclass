import json


def get_stord_username():
    """如果储存了用户名就获取 """
    filename = "username3.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名    """
    username = input("what is your name? ")
    filename = 'username3.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出姓名  """
    username = get_stord_username()
    if username:
        correct = input("Are you " + username + "?(y/n)")
        if correct == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you came back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you came back, " + username + "!")


greet_user()
