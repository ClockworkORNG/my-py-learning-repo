# найти наименьший и наибольший элемент списка и вывести его на экран:
num0 = [1, 4, 8, 16, 2, 4]
max = 0
min = 1e38
for i in num0:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)

# пример использования своей функции:
def my_max(x, y):
    if x > y:
        return x
    else:
        return y
z = my_max(15, 8)
print(z)

# вывод цены, без названия валюты:
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

for item in items:
    a = item.split(";")
    price = a[1].strip()
    c = get_price(price)
print(c)