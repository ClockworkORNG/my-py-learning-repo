# заполнить список 100 нулями, кроме первого и последнего элементов, которые должны быть равны 1:
# первый вариант:
list0 = [0] * 100
list0[0] = list0[-1] = 1
print(list0)
# второй вариант:
print([1]+[0]*98+[1])

# сформировать возрастающий список из чётных чисел (количество элементов 45):
list1 = [i for i in range(2, 92, 2)]
print(list1)

# пользователь вводит число, определить, содержит ли список данное число:
list2 = [0, 1, 2]
num0 = int(input("Enter any number: "))
if num0 in list2:
    print("Yes, the number in the list!")

# найдите сумму и произведение элементов списка, результаты вывести на экран:
# первый вариант:
list3 = [1, 2, 3, 4, 5]
sum = list3[0] + list3[1] + list3[2] + list3[3] + list3[4]
mult = list3[0] * list3[1] * list3[2] * list3[3] * list3[4]
print(sum, mult)
# второй вариант:
same_list3 = [1, 2, 3, 4, 5]
same_sum = 0
same_mult = 1
for i in same_list3:
    same_sum += i
print(same_sum)
for i in same_list3:
    same_mult *= i
print(same_mult)

# найти наибольший элемент списка и вывести его на экран:
# первый вариант:
list4 = [10, 20, 30, 40, 50]
print(max(list4))
# второй вариант:
same_list4 = [10, 20, 30, 40, 50]
max_same_list4 = same_list4[4]
for i in same_list4:
    if i > max_same_list4:
        max_same_list4 = i
print(max_same_list4)

# определите, есть ли в списке определяющиеся элементы, если да, то вывести на экран это значение:
# первый вариант:
list5 = [1, 2, 3, 2, 1]
for i in list5:
    if list5.count(i) >= 2:
        print(i)
# второй вариант:
new_list5 = [i for i in list5 if list5.count(i) >= 2]
print(new_list5)

# в списке все элементы различны, поменяйте местами минимальный и максимальный элемент этого списка:
list6 = [100, 200, 300, 400, 500]
new_list6 = list(list6)
new_list6[list6.index(min(list6))] = max(list6)
new_list6[list6.index(max(list6))] = min(list6)
print(new_list6)