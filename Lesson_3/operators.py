'''

'''

# арифметические операторы
"""
    +   сложение                    A + B       'Hello ' + 'World' = 'Hello World'
    -   вычитание                   A - B
    *   умножение                   A * B       'Hello ' * 3 = 'Hello Hello Hello'
    /   деление                     A / B       10 / 3 = 3.33333
    //  целочисленное деление       A // B      10 // 3 = 3.0
    %   остаток от деления          A % B       10 % 3 = 1
        ------------------------------------
    +   унарный плюс                +A
    -   унарный минус               -B
        ------------------------------------
    **  возведение в степень        A ** B      A ** B ** C
"""

# операторы сравнения
"""
    >   больше                      A > B
    <   меньше                      A < B
    >=  больше либо равно           A >= B
    <=  меньше либо равно           A <= B
    !=  не равно                    A != B
    ==  строгое равенство           A == B
"""

# логические операторы
"""
    not логическое НЕ               not A
    and логическое И                A and B
    or  логическое ИЛИ              A or B
        ------------------------------------
    A       B       A and B     A or B      not A
    True    True    True        True        False
    True    False   False       True        False
    False   True    False       True        True
    False   False   False       False       True
"""

# битовые операции
"""
    &   битовое И                   A & B
    |   битовое ИЛИ                 A | B
    ^   битовое исключающее ИЛИ     A ^ B
    ~   битовое НЕ                  ~ A
        ------------------------------------
    A       B       A ^ B
    True    True    False
    True    False   True
    False   True    True
    False   False   False
"""

# операторы сдвига
"""
    >>                              A >> B
    <<                              A << B
"""

a = 2
print(a << 2)

a = 64
print(a >> 2)

# операторы присваивания
"""
    =                               A = B
        ------------------------------------
    A = A + 3                       A += 3
    +                               +=
    -                               -=
    *                               *=
    /                               /=
    //                              //=
    %                               %=
    **                              **=
    >>                              >>=
    <<                              <<=
    &                               &=
    |                               |=
    ^                               ^=
"""

a = 6
b = 5
c = 7

# a and (b or not c)
