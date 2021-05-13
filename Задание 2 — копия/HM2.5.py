hm_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
new_number = int(input('Введите натуральное число - '))
i = 0

for n in hm_list:
    if new_number <= n:
        i += 1
hm_list.insert(i, int(new_number))
print(hm_list)