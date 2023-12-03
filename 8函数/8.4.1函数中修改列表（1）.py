# 不用函数
# 首先一个待打印的列表和一个完成空列表
unprinted_designs =['phone back','robot pendent','carmodle']
completed_designs =[]

#打印后移动到完成打印的列表中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #模拟根据设计制作的3D打印的过程
    print("正在打印： "+ current_design)
    completed_designs.append(current_design)

#显示打印完成的数据
print("\n下列都已完成打印")
for completed_design in completed_designs:
    print(completed_design)
