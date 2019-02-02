# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
import sys

def func_var1(x):
    n = x
    count = 0
    z = 0
    while n > 0:
        n = n // 10
        count += 1
    while count > 0:
        a = x % 10
        y = a * 10 ** (count - 1)
        z += y
        x = x // 10
        count -= 1
    return locals()

print(func_var1(1551))
spam = func_var1(1551).values()
print(spam)

def show_size(x, level=0, i=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
                i += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                i += sys.getsizeof(item)
    return i
print(show_size(spam))

