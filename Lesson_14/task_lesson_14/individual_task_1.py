# Задача №1 (lesson_13_1)

"""
Необходимо создать матрицу (двухмерный список) М х N. M и N задаёт пользователь
с клавиатуры.

Обязательные условия:

 1. матрица создаётся при помощи list comprehension. При создании, список
    заполняется случайными числами (используйте генератор случайных чисел)
 2. необходимо посчитать сумму значений каждой строки (функцию sum()
    использовать НЕЛЬЗЯ). Сумма выводится напротив соответствующих строк
 3. необходимо посчитать сумму значений каждой колонки (функцию sum()
    использовать НЕЛЬЗЯ). Сумма выводится под соответствующей колонкой
 4. Можно использовать ТОЛЬКО ОДИН, одномерный, дополнительный список
 5. Можно использовать ТОЛЬКО ОДНУ дополнительную переменную
 6. Вывод программы ДОЛЖЕН соответствовать примеру ниже (для форматирования
    вывода, Вам понадобится функция format())
 7. задача считается выполненной ТОЛЬКО при строгом выполнении всех условий.
"""

from random import randint

N = int(input('Введите кол - во строк: '))
M = int(input('Введите кол - во столбцов: '))

matrix = [[randint(10, 51) for j in range(M)] for i in range(N)]

suma_list = [0] * M
suma = 0

for i in range(N):
    for j in range(M):
        print('', matrix[i][j], end=' ')
        suma += matrix[i][j]
        suma_list[j] += matrix[i][j]
    print('|', suma)
    suma = 0

print('--- ' * M)

for i in range(len(suma_list)):
    print(' ' * (3 - len(str(suma_list[i]))) + str(suma_list[i]) + ' ', end='')
