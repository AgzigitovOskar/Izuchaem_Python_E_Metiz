# Передача произвольного набора аргументов

# def make_pizza(*toppings):
#     """Выводит описание пиццы."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# make_pizza('mushrooms', 'green peppers', 'extra cheese', '1', '2', '3')



# Позиционные аргументы с произвольными наборами аргументов
def make_pizza(size, *toppings):
    """Выводит описание пиццы."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')