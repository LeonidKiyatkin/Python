"""
Задание 5. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""


list = input(
    'Введите строку из нескольких слов, разделённых пробелами: ').split()
j = 1
for i in list:
    print(f'{j}. {i[:10]}')
    j += 1
