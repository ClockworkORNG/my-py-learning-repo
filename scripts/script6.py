a = [1, 2, 4, 8, 2, 1, 8, 2, 2]
x = a[1]
a[1] = 28
print(x)
# считает кол-во 2, при этом а[1] = 28
c = 0
for i in a:
    if i == 2:
        c += 1
print(c)
b = ["Lenovo A5", "Samsung A6"]
c = b
d = b.copy()
b[0] = 25
print(c)