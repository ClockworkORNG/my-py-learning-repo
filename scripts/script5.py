# строку, в котрой между словами стоит 2-3 символа пробел, преобразовать так, чтобы между словами осталось по одному символу пробела:
s = "hello     world!"
s1 = ""
c = 0
for i in s:
    if i != " ":
        c = 0
        s1 = s1 + i
    elif c == 0:
        c = 1
        s1 = s1 + i
print(s1)