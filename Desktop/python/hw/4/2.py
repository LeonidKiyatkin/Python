"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""
user_name = input('Введите имя: ')
user_last_name = input('Введите фамилию: ')
user_year = int(input('Введите год рождения: '))
user_city = input('Введите город проживания: ')
user_email = input('Введите email: ')
user_tel = input('Введите телефон: ')


def user_info(name, last_name, year, city, email, tel):
    print(f'{name} {last_name} {year} года рождения, проживает в городе {city}, email: {email}, телефон: {tel}')


user_info(name=user_name, last_name=user_last_name, year=user_year,
          city=user_city, email=user_email, tel=user_tel)
