import json

numbers = [1, 2, 568646568]
filename = 'numbers.json'
with open('filename', 'a') as f_obj:
    json.dump(numbers, f_obj)
