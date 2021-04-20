from pprint import pprint


def read():
    cook_book = {}
    with open('receipt.txt', encoding='utf-8') as file:
        for line in file:
            dish_name = line.lower().strip()
            count = int(file.readline())
            ingredients = []
            for i in range(count):
                ingredient_name, quantity, measure = file.readline().lower().strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure,
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            file.readline()

    return cook_book


def get_shop_list_by_dishes(dish, count):
    cook_book = read()
    for i in dish:
        if i in cook_book:
            shop_list = {}
            for element in cook_book[i]:
                element['quantity'] *= count
                shop_element = {
                        'measure': element['measure'], 'quantity': element['quantity']
                    }
                shop_list[element['ingredient_name']] = shop_element
            pprint(shop_list)


pprint(read(), width=100)
print()
get_shop_list_by_dishes(['запеченный картофель', 'омлет'], 2)
