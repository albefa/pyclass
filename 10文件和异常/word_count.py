def count_words(filename):
    """计算一个文本有多少字数 """
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
        print(
            "The file " + filename + " has about " + str(num_words) + " words")

filename ='alice.txt'
count_words(filename)

filename ='programming.txt' # 中文显示字数不对
count_words(filename)