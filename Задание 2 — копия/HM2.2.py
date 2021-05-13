hm_list = input('Введите числа с пробелами - ').split()
i = 0
print(f'Исходник{hm_list}')
while i + 1 < len(hm_list):
    if i % 2 == 0:
        hm_list.insert(i, hm_list.pop(i + 1))
    i += 1
print(f'Итог {hm_list}')