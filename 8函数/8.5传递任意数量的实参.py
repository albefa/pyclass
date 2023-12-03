def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following topping: ")
    for topping in toppings:
        print("- " + topping)


make_pizza('apple')
make_pizza('mushroom', 'greenpeppers', 'extro cheere')
