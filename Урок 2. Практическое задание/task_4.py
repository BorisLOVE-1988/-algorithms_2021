"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Массив в этом задании строить не нужно!
Нужно решить без него!

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def my_mod(num, a):
	"""Функция которая делит единицу на -2 заданное число раз"""
	if num == 0:
		return a
	else:
		num = num-1
		return a + my_mod(num, a/(-2))


user_number = round(int(input('Введите количество элементов: ')))
# my_sum, a = my_mod(num=user_number, 1)
my_sum = my_mod(user_number-1, 1)
print(1, 'Количество элементов: ', user_number, 'их сумма: ', my_sum)
