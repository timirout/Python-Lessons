# # Задача №2 (lesson_13)

"""
Написать функцию сортировки двухмерного списка МхМ (матрицы)
Значение М - задаётся пользователем, с клавиатуры. Может быть любым
целым, положительным числом, больше 5.

Функция должна:

 1. найти сумму элементов столбцов и отсортировать столбцы по
    возрастанию этих сумм
 2. отсортировать каждый нечётный столбец по возрастанию значений снизу
    вверх, а каждый чётный столбец по возрастанию значений сверху вниз.

 Так же, ваша программа должна иметь функцию вывода данного списка
 на экран. При выводе, внизу каждого столбца должна выводиться сумма
 элементов этого столбца.

Что можно использовать:

 1. для создания списка использовать ТОЛЬКО 'list comprehension' и
    генератор случайных чисел. Диапазон случайных чисел для заполнения
    списка от 1 до 50. Список должен создаваться однострочным
    выражением.
 2. Можно использовать ТОЛЬКО ДВА списка. Первый это двухмерный список
    размером МхМ, второй, вспомогательный, одномерный список размером
    М. Использование других списков (или коллекций) НЕДОПУСТИМО.
 3. Можно использовать ТОЛЬКО ОДНУ переменную М для хранения размера
    списка, плюс переменные циклов for.
 4. Для сортировки можно использовать алгоритм пузырьковой сортировки.
    Использование встроенных функций сортировки - НЕДОПУСТИМО (да и не
    получится их использовать)!
 5. Решение должно включать ТОЛЬКО ДВЕ функции: функцию сортировки (по
    правилам описанным выше) и функцию вывода на экран.
    Задача считается решённой верно при условии соблюдения всех требований.

Аккуратный вывод на экран - приветствуется.
"""

from random import randint


def sort_list(lis, len_lis, suma_lis):
    # ПЛЮСУЮ СУММУ КАЖДОГО ЭЛЕММЕНТА СТОЛБЦА
    for i in range(len_lis):
        for j in range(len_lis):
            suma_lis[j] += lis[i][j]

    #  СОРТИРУЮ СУММУ СТОЛБЦОВ И ИХ СТОЛБЦЫ ПО ВОЗРАСТАНИЮ
    for i in range(len(suma_lis)):
        flag = True
        for j in range(len(suma_lis) - i - 1):
            if suma_lis[j] > suma_lis[j + 1]:
                suma_lis[j], suma_lis[j + 1] = suma_lis[j + 1], suma_lis[j]
                flag = False
                for s in range(len(lis)):
                    lis[s][j], lis[s][j + 1] = lis[s][j + 1], lis[s][j]
        if flag:
            break

    # СОРТИРУЕМ СТОЛБЦЫ ЧЁТНЫЕ - СНИЗУ ВВЕРХ, НЕЧЁТНЫЕ - СВЕРХУ ВНИЗ
    for j in range(len(lis)):
        for i in range(len(lis) - 1):
            flag = True
            for s in range(len(lis) - 1 - i):
                if lis[s][j] > lis[s + 1][j] if j % 2 else lis[s][j] < lis[s + 1][j]:
                    lis[s][j], lis[s + 1][j] = lis[s + 1][j], lis[s][j]
                    flag = False
            if flag:
                break


def output_on_display(lis, len_lis, suma_lis):
    # ВЫВОЖУ КОНЕЧНЫЙ РЕЗУЛЬТАТ ЧЕРЕЗ ВТОРУЮ ФУНКЦИЮ
    for i in range(len_lis):
        for j in range(len_lis):
            print(' ' * (3 - len(str(lis[i][j]))) + str(lis[i][j]) + ' ', end='')
        print()

    print('--- ' * len_lis)

    for i in range(len_lis):
        print(' ' * (3 - len(str(suma_lis[i]))) + str(suma_lis[i]) + ' ', end='')


while True:
    lening = int(input('Введите кол - во строк и столбцов (больше 5): '))
    if lening <= 5:
        print('!!!КОЛ - ВО СТРОК И СТОЛБЦОВ В ВАШЕЙ МАТРИЦЕ НЕ БОЛЬШЕ 5!!!')
        continue
    else:
        break

matrix = [[randint(1, 51) for j in range(lening)] for i in range(lening)]

# МОЖНО УКАЗАТЬ ВМЕСТО -len(matrix)- ПЕРЕМЕННУЮ -lening-
len_list = len(matrix)
suma_list = [0] * len_list
# а
sort_list(matrix, len_list, suma_list)
output_on_display(matrix, len_list, suma_list)
