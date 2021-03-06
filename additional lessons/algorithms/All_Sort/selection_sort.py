# ВЫБОРАЧНАЯ СОРТИРОВКА
def selection_sort(lis):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(lis)):
        # Исходно считаем наименьшим первый элемент
        k = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(lis)):
            if lis[j] < lis[k]:
                k = j
        # Самый маленький элемент меняем с первым в списке
        lis[i], lis[k] = lis[k], lis[i]

    return lst


# Проверяем, что оно работает
lst = [6, 4, 9, 8, 1, 5, 3, 0, 2, 7]
print(selection_sort(lst))
