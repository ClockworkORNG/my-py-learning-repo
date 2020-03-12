s = "simple string"
c = 0
# количество букв S
for i in s:
    if i == "s":
        c += 1
print(c)
# позиция S
for i in range(len(s)):
    if s[i] == "s":
        print(i)
s1 = ""
for i in s:
    if i != " ":
        s1 = s1 + i
    else:
        s1 = s1 + "_"
print(s1)
# перевод в верхний регистр
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s3 = "abcdefghijklnoprstuvwxyz"
s4 = "simple string"
for i in s4:
    for j in range(len(s)):
        if s3[j] == i:
            # print(j)
            print(s2[j])