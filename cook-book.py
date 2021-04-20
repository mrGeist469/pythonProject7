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
                i += 1
            ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book


print(read())


