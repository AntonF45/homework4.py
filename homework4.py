# 1. Организуйте программу:
# Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
# Вывести количество символов введённого текста
# 2. Работа с методами строк:
# Используя методы строк, выполните следующие действия:
# Выведите строку my_string в верхнем регистре.
# Выведите строку my_string в нижнем регистре.
# Измените строку my_string, удалив все пробелы.
# Выведите первый символ строки my_string.
# Выведите последний символ строки my_string.

my_string = input('Как Ваши дела? ')  # Создайте переменную my_string и присвойте ей значение строки с произвольным
# текстом (функция input()).
print(len(my_string))  # Вывести количество символов введённого текста
print(my_string.upper())  # Выведите строку my_string в верхнем регистре.
print(my_string.lower())  # Выведите строку my_string в нижнем регистре.
print(my_string.replace(' ', ''))  # Измените строку my_string, удалив все пробелы.
print(my_string[0])  # Выведите первый символ строки my_string.
print(my_string[-1])  # Выведите последний символ строки my_string.
