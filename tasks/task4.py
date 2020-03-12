smartphone_models_list = ["Lenovo A98; 1748UAH; screen: 5''; ram: 1GB; ROM : 16GB; qnty : 2; camera: 8MPx", "Lenovo A300; 1244UAH; screen: 4''; ram: 2GB; ROM : 8GB; qnty : 16; camera: 2MPx", "Lenovo A15; 2748UAH; screen: 3''; ram: 4GB; ROM : 8GB; qnty : 3; camera: 4MPx", "Lenovo    A918; 1556UAH; screen: 6''; ram: 2GB; ROM : 4GB; qnty : 8; camera: 8MPx", "Lenovo G398;2148UAH; screen: 5''; ram: 4GB; ROM : 16GB; qnty : 21; camera: 4MPx", "Lenovo   S498;1045UAH; screen: 5''; ram: 1GB; ROM : 4GB; qnty : 1; camera: 4MPx", "Lenovo   Bt58; 1267UAH; screen: 3''; ram: 1GB; ROM : 2GB; qnty : 0; camera: 2MPx", "Lenovo  N98 ;  1433UAH; screen: 4''; ram: 2GB; ROM : 2GB; qnty : 4; camera: 16MPx", "Lenovo   M98;   1115UAH; screen: 5''; ram: 4GB; ROM : 4GB; qnty : 15; camera: 8MPx", "Lenovo       M8798; 1978UAH; screen: 6''; ram: 2GB; ROM : 1GB; qnty : 1; camera: 4MPx", "Lenovo H98;  1228UAH; screen: 4''; ram: 4GB; ROM : 2GB; qnty : 0; camera: 2MPx", "Lenovo A122 ; 1005UAH; screen: 4''; ram: 1GB; ROM : 1GB; qnty : 2; camera: 2MPx", "Lenovo A98; 1683UAH; screen: 5''; ram: 2GB; ROM : 4GB; qnty : 19", "Lenovo   M5   ; 2054UAH; screen: 5''; ram: 1GB; ROM : 0GB; qnty : 3; camera: 8MPx", "Lenovo A9 ; 1999UAH; screen: 6''; ram: 3GB; ROM : 16GB; qnty : 0; camera: 4MPx", "Lenovo A  ; 1074UAH; screen: 3''; ram: 2GB; ROM : 2GB; qnty : 0", "Lenovo A98;1648UAH; screen: 5''; ram: 3GB; ROM : 8GB; qnty : 2; camera: 2MPx", "Lenovo X10; 2099UAH; screen: 4''; ram: 4GB; ROM : 1GB; qnty : 21; camera: 1MPx", "Lenovo  C33 ; 1367UAH; screen: 5''; ram: 1GB; ROM : 0GB; qnty : 9", "Lenovo K6; 1845UAH; screen: 3''; ram: 2GB; ROM : 16GB; qnty : 17; camera: 8MPx", "Lenovo G7 ; 1409UAH; screen: 5''; ram: 1GB; ROM : 4GB; qnty : 10", "Lenovo N1  ; 1220UAH; screen: 4''; ram: 4GB; ROM : 4GB; qnty : 1; camera: 4MPx", "Lenovo X0  ; 1848UAH; screen: 4''; ram: 2GB; ROM : 2GB; qnty : 0; camera: 2MPx", "Lenovo F3; 1748UAH; screen: 5''; ram: 1GB; ROM : 8GB; qnty : 16"]

# находит смартфон с максимальным объёмом ОЗУ:
def get_max_memory(smartphone_memory_string):
    digits_string = ""
    for character in smartphone_memory_string:
        if character.isdigit():
            digits_string += character
        else:
            break
    if digits_string:
        return int(digits_string)
    return 0


max_memory = 0

for smartphone_model in smartphone_models_list:
    x = smartphone_model.split(";")

    smartphone_model_name = x[0]

    x_ram = x[3].strip()
    smartphone_model_memory = x_ram[5:-2]

    memory = get_max_memory(smartphone_model_memory)

    if memory > max_memory:
        max_memory = memory
        max_name = smartphone_model_name

print(max_name, max_memory)

# находит смартфон с минимальным объёмом ОЗУ:
def get_max_memory(smartphone_memory_string):
    digits_string = ""
    for character in smartphone_memory_string:
        if character.isdigit():
            digits_string += character
        else:
            break
    if digits_string:
        return int(digits_string)
    return 0


random_memory = 4

for smartphone_model in smartphone_models_list:
    x = smartphone_model.split(";")

    smartphone_model_name = x[0]

    x_ram = x[3].strip()
    smartphone_model_memory = x_ram[5:-2]

    memory = get_max_memory(smartphone_model_memory)

    if memory < random_memory:
        random_memory = memory
        max_name = smartphone_model_name

print(max_name, random_memory)

# сортировка по возрастанию/убыванию ОЗУ:
def get_memory(smartphone_model_string):
    x = smartphone_model_string.split(";")
    x_ram = x[3].strip()
    smartphone_model_memory = int(x_ram[5:-2])
    return int(smartphone_model_memory)

new_smartphone_models_list_increase = sorted(smartphone_models_list, key=get_memory)
new_smartphone_models_list_decrease = sorted(smartphone_models_list, key=get_memory, reverse=True)

print(new_smartphone_models_list_increase, "\n", new_smartphone_models_list_decrease)