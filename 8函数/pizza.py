def make_pizza(size, *toppings):
    """概述要做的披萨，这是个模块函数  """
    print("\n做一个： " + str(size) +
          " -寸 披萨包含下面的食材：")
    for topping in toppings:
        print("- " + topping)
