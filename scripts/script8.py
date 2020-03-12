# вывод самой дорогой модели:
items = ["Lenovo A5; 1234UAH", "Lenovo B8; 1834UAH", "Lenovo C9; 1134UAH"]

def get_price(s):
    s1 = ""
    for i in s:
        if i.isdigit() == True:
            s1 += i
        else:
            break
    if len(s1) == 0:
        return 0
    else:
        return int(s1)

max_price = 0

for item in items:
    a = item.split(";")
    price = a[1].strip()
    name = a[0]
    c = get_price(price)
    if c > max_price:
        max_price = c
        max_name = name
print(max_name, max_price)