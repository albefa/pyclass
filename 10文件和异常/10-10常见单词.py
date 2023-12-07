filename ='bird.txt'

with open(filename) as f:
    contents = f.read()
    #print(contents)
    print(contents.lower().count('the'))