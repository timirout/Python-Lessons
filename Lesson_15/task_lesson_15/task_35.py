#  Задача №35 (Цифровой счётчик)

"""
Реализовать класс цифрового счетчика. Обеспечьте возможность установки максимального
и минимального значений, увеличения счетчика на 1, возвращения текущего значения.
"""


class Counter:

    # УСТАНАВЛИВАЕТ МИНИМАЛЬНОЕ И МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ ДЛЯ НАШЕГО СЧЁЧИКА
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def increase(self):
        # ЕСЛИ МИНИМАЛЬНОЕ ЗНАЧЕНИЕ МЕНЬШЕ МАКСИМАЛЬНОГО, ТО ОН УВЕЛИЧИТСЯ НА ОДНУ ЕДИНИЦУ
        if self.start < self.end:
            self.start += 1
            return self.start
        # ЕСЛИ ЖЕ МИНИМАЛЬНОЕ ЗНАЧЕНИЕ БОЛЬШЕ МАКСИМАЛЬНОГО ТО НАШ СЧЁЧИК ЗАКАНЧИВАЕТСЯ
        else:
            return 'У вашего счётчика закончились значения!'


my_counter = Counter(start=0, end=2)
print(my_counter.increase())    # Увеличился на 1   0(1)
print(my_counter.increase())    # Увеличился на 1   1(2)
print(my_counter.increase())    # 'У вашего счётчика закончились значения!'
