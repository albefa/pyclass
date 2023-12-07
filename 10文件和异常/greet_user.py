import json

username = input("what is your name ?")
filename = 'username.json'
with open('filename', 'w') as f:
    json.dump(username, f)
    print("We'll rember you when you come back, " + username + '!')

import json
filename='username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("welcome back, "+ str(username) +"!")