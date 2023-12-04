filename='programming.txt'
with open(filename,'w') as f:
    f.write("我爱programming.")
    f.write("我喜欢Creating new gaming！")
    f.write("我爱programming.\n")
    f.write("我喜欢Creating new gaming！\n")

# 附加模式，打开文件进行添加，不覆盖文件
with open(filename,'a') as f:
    f.write("我喜欢在大数据中寻找meaning.\n")
    f.write("我喜欢创造app！\n")