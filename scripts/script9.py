# убрать лишние пробелы без цикла:
s = " Lenovo      A5"
x = s.strip()
x2 = x.split(" ")
print(x2[0] + " " + x2[len(x2)-1])
# сортировка по возрастанию:
a = [8, 3, 15, 2, 7, 4]
a1 = a.sort() # изменяет первоначальный список
print(a)

a2 = sorted(a) # создаёт новый список
print(a2)

for j in range(len(a)):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
        print(a) # убрать a1 = a.sort() для корректного отображения пошаговой сортировки


# находит смартфон с максимальным объёмом ОЗУ:
smartphone_models_list = ["Lenovo A98; 1748UAH; screen: 5''; ram: 1GB; ROM : 16GB; qnty : 2; camera: 8MPx", "Lenovo A300; 1244UAH; screen: 4''; ram: 2GB; ROM : 8GB; qnty : 16; camera: 2MPx", "Lenovo A15; 2748UAH; screen: 3''; ram: 4GB; ROM : 8GB; qnty : 3; camera: 4MPx", "Lenovo    A918; 1556UAH; screen: 6''; ram: 2GB; ROM : 4GB; qnty : 8; camera: 8MPx", "Lenovo G398;2148UAH; screen: 5''; ram: 4GB; ROM : 16GB; qnty : 21; camera: 4MPx", "Lenovo   S498;1045UAH; screen: 5''; ram: 1GB; ROM : 4GB; qnty : 1; camera: 4MPx", "Lenovo   Bt58; 1267UAH; screen: 3''; ram: 1GB; ROM : 2GB; qnty : 0; camera: 2MPx", "Lenovo  N98 ;  1433UAH; screen: 4''; ram: 2GB; ROM : 2GB; qnty : 4; camera: 16MPx", "Lenovo   M98;   1115UAH; screen: 5''; ram: 4GB; ROM : 4GB; qnty : 15; camera: 8MPx", "Lenovo       M8798; 1978UAH; screen: 6''; ram: 2GB; ROM : 1GB; qnty : 1; camera: 4MPx", "Lenovo H98;  1228UAH; screen: 4''; ram: 4GB; ROM : 2GB; qnty : 0; camera: 2MPx", "Lenovo A122 ; 1005UAH; screen: 4''; ram: 1GB; ROM : 1GB; qnty : 2; camera: 2MPx", "Lenovo A98; 1683UAH; screen: 5''; ram: 2GB; ROM : 4GB; qnty : 19", "Lenovo   M5   ; 2054UAH; screen: 5''; ram: 1GB; ROM : 0GB; qnty : 3; camera: 8MPx", "Lenovo A9 ; 1999UAH; screen: 6''; ram: 3GB; ROM : 16GB; qnty : 0; camera: 4MPx", "Lenovo A  ; 1074UAH; screen: 3''; ram: 2GB; ROM : 2GB; qnty : 0", "Lenovo A98;1648UAH; screen: 5''; ram: 3GB; ROM : 8GB; qnty : 2; camera: 2MPx", "Lenovo X10; 2099UAH; screen: 4''; ram: 4GB; ROM : 1GB; qnty : 21; camera: 1MPx", "Lenovo  C33 ; 1367UAH; screen: 5''; ram: 1GB; ROM : 0GB; qnty : 9", "Lenovo K6; 1845UAH; screen: 3''; ram: 2GB; ROM : 16GB; qnty : 17; camera: 8MPx", "Lenovo G7 ; 1409UAH; screen: 5''; ram: 1GB; ROM : 4GB; qnty : 10", "Lenovo N1  ; 1220UAH; screen: 4''; ram: 4GB; ROM : 4GB; qnty : 1; camera: 4MPx", "Lenovo X0  ; 1848UAH; screen: 4''; ram: 2GB; ROM : 2GB; qnty : 0; camera: 2MPx", "Lenovo F3; 1748UAH; screen: 5''; ram: 1GB; ROM : 8GB; qnty : 16"]
max_memory = 0
max_name = ''

for smartphone_model in smartphone_models_list:
    smartphone_specs = smartphone_model.split(";")

    smartphone_ram = smartphone_specs[3].strip()
    smartphone_ram = smartphone_ram[5:-2]
    memory = int(smartphone_ram)

    if memory > max_memory:
        max_memory = memory
        max_name = smartphone_specs[0]

print(max_name, max_memory)