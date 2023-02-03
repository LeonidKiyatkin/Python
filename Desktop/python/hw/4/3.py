"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

n1 = int(input('Введите число 1: '))
n2 = int(input('Введите число 2: '))
n3 = int(input('Введите число 3: '))


def my_func1(num1, num2, num3):
    lst = []
    lst.extend([num1, num2, num3])
    lst.sort()
    return lst[-1] + lst[-2]


def my_func2(num1, num2, num3):
    lst = []
    lst.extend([num1, num2, num3])
    max1 = max(lst)
    lst.remove(max1)
    return max1 + max(lst)


print(f'Cумма наибольших двух аргументов (использована функция sort()):',
      my_func1(n1, n2, n3))
print(f'Cумма наибольших двух аргументов (без функции sort()):', my_func2(n1, n2, n3))
