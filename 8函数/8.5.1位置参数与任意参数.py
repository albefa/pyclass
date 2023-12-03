def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print(
        "\nMaking a " + str(size) + "-inch pizza with the following topping: ")
    for topping in toppings:
        print("- " + topping)


make_pizza(22, 'peacheni')
make_pizza(36, 'mushroom', 'apple', 'extra cheese')
