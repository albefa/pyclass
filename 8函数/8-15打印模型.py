import printing_functions as pf


def show_completed_modles(completed_modles):
    """显示打印好的模型"""
    print("\n下列都是打印完成的：")
    for completed_modle in completed_modles:
         print(completed_modle)

unprinted_designs = ['phone back', 'robot pendent', 'carmodle']
completed_models = []

# 参数的对应性
pf.print_modles(unprinted_designs, completed_models)
show_completed_modles(completed_models)