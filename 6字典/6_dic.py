#6-1字典ren
relation ={'firsr_name':'zhang',
           'last_name':'san',
           'age':'20',
           'city':'shanghai'
           }
print(relation)
print("\n")
#6-2 喜欢的数字
like_num ={'zhangsan':'6',
           'lisi':'5',
           'wangwu':'25',
           'liliu':'18',
           'sunqi':'221'}
print(like_num)
print("\n")
#6-3词汇表
cihuibiao ={'int':'数字模式',
            'str':'文本',
            'if':'条件',
            'in':'判断条件',
            'append':'增加'}

print(*cihuibiao.keys(),*cihuibiao.values())
print(*cihuibiao.keys(),sep='\n')
# for key, value in cihuibiao.item():
#key 定义出现问题？
#     print(value +":"+ key)
glossary = {
    'print': '打印',
    'title': '首字母大写',
    'lower': '全部小写',
    'upper': '全部大写',
    'str': '字符串',
    }

# 打印
print(f"print: {glossary['print']}")
print(f"title: {glossary['title']}")
print(f"lower: {glossary['lower']}")
print(f"upper: {glossary['upper']}")
print(f"str: {glossary['str']}")