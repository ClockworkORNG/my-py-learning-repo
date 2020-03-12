# находит товар с максимальной ценой:
smartphone_models_list = ["Lenovo A98; 1748UAH", "Lenovo A300; 1244UAH", "Lenovo A15; 2748UAH", "Lenovo    A918; 1556UAH", "Lenovo G398;2148UAH", "Lenovo   S498;1045UAH", "Lenovo   Bt58; 1267UAH", "Lenovo  N98 ;  1433UAH", "Lenovo   M98;   1115UAH", "Lenovo       M8798; 1978UAH", "Lenovo H98;  1228UAH", "Lenovo A122 ; 1005UAH", "Lenovo A98; 1683UAH", "Lenovo   M5   ; 2054UAH", "Lenovo A9 ; 1999UAH", "Lenovo A  ; 1074UAH", "Lenovo A98;1648UAH", "Lenovo X10; 2099UAH", "Lenovo  C33 ; 1367UAH", "Lenovo K6; 1845UAH", "Lenovo G7 ; 1409UAH", "Lenovo N1  ; 1220UAH", "Lenovo X0  ; 1848UAH", "Lenovo F3; 1748UAH"]

def get_max_price(smartphone_price_string):
    digits_string = ""
    for character in smartphone_price_string:
        if character.isdigit():
            digits_string += character
        else:
            break
    if digits_string:
        return int(digits_string)
    return 0

max_price = 0

for smartphone_model in smartphone_models_list:
    smartphone_model_name, smartphone_model_price = smartphone_model.split(";")
    smartphone_model_name = smartphone_model_name.strip()
    smartphone_model_price = smartphone_model_price.strip()

    price = get_max_price(smartphone_model_price)

    if price > max_price:
        max_price = price
        max_name = smartphone_model_name

print(max_name, max_price)

# находит товар с минимальной ценой:
def get_max_price(smartphone_price_string):
    digits_string = ""
    for character in smartphone_price_string:
        if character.isdigit():
            digits_string += character
        else:
            break
    if digits_string:
        return int(digits_string)
    return 0

random_price = 1748

for smartphone_model in smartphone_models_list:
    smartphone_model_name, smartphone_model_price = smartphone_model.split(";")
    laptop_model_name = smartphone_model_name.strip()
    smartphone_model_price = smartphone_model_price.strip()

    price = get_max_price(smartphone_model_price)

    if price < random_price:
        random_price = price
        max_name = smartphone_model_name

print(max_name, random_price)

# сортировка по возрастанию/убыванию цены:
def get_price(smartphone_model_string):
    smartphone_model_name, smartphone_model_price = smartphone_model_string.split(";")
    smartphone_model_price = smartphone_model_price.strip()
    smartphone_model_price = smartphone_model_price[:-3]
    return int(smartphone_model_price)


new_smartphone_models_list_increase = sorted(smartphone_models_list, key=get_price)
new_smartphone_models_list_decrease = sorted(smartphone_models_list, key=get_price, reverse=True)

print(new_smartphone_models_list_increase, "\n", new_smartphone_models_list_decrease)