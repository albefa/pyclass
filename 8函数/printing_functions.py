def print_modles(unprinted_designs, completed_models):
    """模拟打印每个设计，直到全部打印完为止，将每个打印后的转移到另外列表"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)