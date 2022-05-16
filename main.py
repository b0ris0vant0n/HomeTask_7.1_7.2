from pprint import pprint

with open('recipes.txt') as file_obj:
    cook_book = {}
    units = ['ingredient_name', 'quantity', 'measure']
    for dishes in file_obj:
        quantity = int(file_obj.readline().strip())
        list_ingredients = []
        for item in range(quantity):
            data = file_obj.readline().strip().split(' | ')
            data[1] = int(data[1])
            dictionary = dict(zip(units, data))
            list_ingredients.append(dictionary)
        cook_book[dishes.strip()] = list_ingredients
        file_obj.readline()
    pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_main = {}
    for dish in dishes:
        for ingridients in cook_book[dish]:
            shop_list = {ingridients['ingredient_name'] : {'measure' : ingridients['measure'], 'quantity' : int(ingridients['quantity'])*person_count}}
            if ingridients['ingredient_name'] in shop_list:
                ingridients['quantity'] += ingridients['quantity']
                shop_list_main.update(shop_list)
            else:
                shop_list_main.update(shop_list)

    pprint(shop_list_main)

get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Омлет'], 1)

