words = input("Введите слова через пробелы - ").split()
for i, word in enumerate(words, 1):
    print(f'{i}, {word[:10]}')