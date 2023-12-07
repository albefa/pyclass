filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileExistsError:
    msg = "Sorry, the file " + filename + " doesnt exist."
    print(msg)
else:
    # 计算文本多少字数
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words")
