"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random


def question(num, user_count):
	user_answer = round(int(input('Введите число: ')))
	if user_answer == num or user_count == 0:
		print('Загаданное число:', num, '')
	else:
		user_count -= 1
		if user_answer > num:
			print('Ваше число БОЛЬШЕ нужного')
		else:
			print('Ваше число МЕНЬШЕ нужного')
		print('Попыток осталось:', user_count, '\n')
		question(num, user_count)


answer = random.randint(0, 100)
question(answer, 10)

# u_cnt = 0
# while u_cnt < 10:
# 	user_answer = round(int(input('Введите число')))
# 	u_cnt += 1
# 	if user_answer > answer:
# 		print('Ваше число БОЛЬШЕ нужного')
# 	elif user_answer < answer:
# 		print('Ваше число МЕНЬШЕ нужного')
# 	elif user_answer == answer:
# 		print('Вы угадали!!! Подравляю!!!\n Загаданное число: ', answer)
# 		u_cnt += 10
# 	else:
# 		print('Вы не угадали.\n Загаданное число: ', answer)
