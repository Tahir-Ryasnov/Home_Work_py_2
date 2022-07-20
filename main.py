#from pprint import pprint
import os


with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredient_list = []
        for item in range(int(file.readline())):
            ingredient_dict = {}
            name, quantity, measure = file.readline().split(" |")
            ingredient_dict['ingredient_name'] = name.strip(' \n')
            ingredient_dict['quantity'] = int(quantity.strip(' \n'))
            ingredient_dict['measure'] = measure.strip(' \n')
            ingredient_list.append(ingredient_dict)
        cook_book[dish] = ingredient_list
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for items in dishes:
        for keys, values in cook_book.items():
            if keys in items:
                for value in values:
                    value['quantity'] *= person_count
                    shop_list[value.pop('ingredient_name')] = value
    return shop_list


directory = r'C:\Users\Артем\PycharmProjects\HomeWork_2\sorted'
files = os.listdir(directory)
texts = filter(lambda x: x.endswith('.txt'), files)
dict = {}
for file in files:
    print(os.path.abspath(file))
    n = os.path.abspath(file)
    with open(n) as text:
        print(n)
print(dict)


#pprint(cook_book)
#pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Баарш'], 3))
