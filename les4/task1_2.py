# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

def func_var2(x):
    x = str(x)
    y = ""
    for i in x:
        y = i + y
    return y

#100 loops, best of 5: 1.94 usec per loop -


#100 loops, best of 5: 631 nsec per loop - Трехзначное число
#100 loops, best of 5: 804 nsec per loop - Шестизначное число
#100 loops, best of 5: 1.17 usec per loop - Десятизначное число
#100 loops, best of 5: 1.94 usec per loop - Двадцатизначное число

# Линейный алгоритм, сложность алгоритма возрастает пропорционально количеству цифр в числе.

