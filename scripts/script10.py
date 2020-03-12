f = open("C:/tmp/data2.txt", "r")
f.seek(0, 0)
print(f.tell())
r = f.read(6)# 65535 байт = 64 килобайта
print(r)
s = f.split("\r\n")
print(s)

lambda a: a * 2