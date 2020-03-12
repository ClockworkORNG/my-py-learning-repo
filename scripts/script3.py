for i in range(10, 101, 5):
    print(i)
s = "Hello world"
i = 0

while i < len(s):
    print(s[i])
    i += 1

for i in s:
    print(i)

for i in range(len(s)):
    print(s[i])

x = s[1:5]
y = s[1:10:2]
z = s[1: :1]
# :: - взять всю строку
print(x)