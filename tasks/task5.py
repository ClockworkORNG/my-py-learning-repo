# открыть файл data2.txt и прочитать его содержимое:
list_file = open("D:/tmp/data2.txt", "r")
list_of_strings = list_file.read()

# разбить его по строкам (по товарам):
smartphone_models_list = list_of_strings.split("\n")

smartphone_models_list_data = list()

# каждый товар разбить на составляющие для формирования словаря:
for smartphone_model in smartphone_models_list:
    smartphone_specs = smartphone_model.split(";")

    try:
        smartphone_camera = smartphone_specs[6]
    except IndexError:
        smartphone_camera = ""

# словари (описание товаров) добавить в список товаров:
    smartphone_models_list_data.append({
        "smartphone_name": smartphone_specs[0],
        "smartphone_price": smartphone_specs[1],
        "smartphone_screen": smartphone_specs[2],
        "smartphone_ram": smartphone_specs[3],
        "smartphone_rom": smartphone_specs[4],
        "smartphone_qnty": smartphone_specs[5],
        "smartphone_camera": smartphone_camera
    })

#print([smartphone_models_dict["smartphone_name"] for smartphone_models_dict in smartphone_models_list_data])
print(smartphone_models_list_data)

# храня описание товаров в виде списка словарей, подключить код сортировки и поиска макс/мин параметра:

# находит смартфон с максимальным значением цены:
max_price = 0
max_name = ''

for smartphone_model in smartphone_models_list_data:

    smartphone_price = smartphone_model["smartphone_price"].strip()
    smartphone_price = smartphone_price[:-3]
    price = int(smartphone_price)

    if price > max_price:
        max_price = price
        max_name = smartphone_model["smartphone_name"].strip()

print(max_name, max_price)

# находит смартфон с минимальным значением цены:
random_price = 2748
min_name = ''

for smartphone_model in smartphone_models_list_data:

    smartphone_price = smartphone_model["smartphone_price"].strip()
    smartphone_price = smartphone_price[:-3]
    price = int(smartphone_price)

    if price < random_price:
        random_price = price
        min_name = smartphone_model["smartphone_name"].strip()

print(min_name, random_price)

# сортирует список словарей со смартфонами по возрастанию/убыванию цены:
def get_price(smartphone_model):
    x = smartphone_model["smartphone_price"].strip()
    x_price = x[:-3]
    smartphone_model_price = int(x_price)
    return smartphone_model_price

new_smartphone_models_list_increase = sorted(smartphone_models_list_data, key=get_price)
new_smartphone_models_list_decrease = sorted(smartphone_models_list_data, key=get_price, reverse=True)

print(new_smartphone_models_list_increase, "\n", new_smartphone_models_list_decrease)

list_file.close()