# Задача №9 (Усовершенствовал)

"""
Программа запрашивает ввод, с клавиатуры, целые числа, пока не будет введён 0.
Как только будет введён 0 (ноль), программа должна посчитать и вывести на экран:

 - Количество введённых чисел (завершающий 0 не считается)
 - Их сумму
 - Среднее арифметическое всех введённых чисел(не считая завершающего числа 0)
 - Определить максимальное и минимальное значение
 - Определить количество чётных и не чётных элементов в последовательности
"""

qnt = 0
suma = 0
arg = 0
mixs = 0
mins = 0
even = 0
n_even = 0
e = 'Четное'
ne = 'Не четное'
a = []

while True:
    # Тут мы вводим строку
    num = input('Введите целое число: ')

    """
    Тут мы проверяем если ли в нашей строке одни лишь цифры.
    Еели в строке находятся только цифры тогда
    оно записывается как 'int', а если нет тогда цикл
    начинается заново пока мы не введём именно цифру.
    """
    if num.isdigit():
        num = int(num)
    else:
        continue

    if not num:
        break

    qnt += 1
    suma += num
    arg = suma / qnt

    if mixs == 0:
        mixs, mins = num, num

    if num > mixs:
        mixs = num
    if num < mins:
        mins = num

    """
    Тут я добавил список что бы
    записать последовательность
    чётных или не чётных чисел.
    """
    if not num % 2:
        even += 1
        a += [e]
    if num % 2:
        n_even += 1
        a += [ne]
    """
    Можно упростить вычесление не чётных чисел.
    В Print(е) после завершение цикла можно записать как (qnt - even).
    Это и будет количесво не чётных чисел.
    """

print('Количество введённых чисел:', qnt)
print('Сумма всех чисел:', suma)
print('Среднее арифметическое всех чисел:', arg)
print('Минимальное число:', mins)
print('Максимальное число:', mixs)
print('Количесво чётных числе: ', even)
print('Количесво не чётных числе: ', n_even)
print('Последовательность чётных и не чётных чисел:\n', a, sep='')