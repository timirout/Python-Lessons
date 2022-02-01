# Задача №16 (Удаление элемента списка)

"""
Дан список из чисел и индекс элемента в списке `k`. Удалите из списка элемент с
индексом `k`, сдвинув влево все элементы, стоящие правее элемента с индексом `k`.

  -  Программа получает на вход список (список можно создать и заполнить случайными числами),
   затем число `k`. Программа сдвигает все элементы, а после этого удаляет последний элемент
   списка при помощи метода `pop()` (да, такой метод есть в арсенале списков. Я ошибочно сказал,
   что его нет. pop() без параметра, удаляет последний элемент списка и возвращает его значение)
   без параметров.
  -  Программа должна осуществлять сдвиг непосредственно в списке.
   Также нельзя использовать дополнительный список.
  -  Также не следует использовать метод `pop(k)` с параметром.
  -  Использовать оператор del НЕЛЬЗЯ!
"""

import random


del_num = None

num = int(input('Введите кол-во элементов в списке: '))
lis = [random.randint(1, 1000) for i in range(num)]
print(lis)
while True:
    k = int(input('Введите индекс от 0 до {0}: '.format(len(lis) - 1)))
    if k < 0 or k > len(lis) - 1:
        print('Вы ввели не существующий индекс!')
        continue
    else:
        del_num = lis[k]
        for i in range(k + 1, len(lis)):
            lis[i - 1] = lis[i]
        break
lis.pop()
print(lis)

print('Вы удалили число', del_num, 'из вашего списка!')