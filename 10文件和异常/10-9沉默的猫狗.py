filenames =['cats.txt','dogs.txt']

for filename in filenames:
    print("\n REading file:"+filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
       pass