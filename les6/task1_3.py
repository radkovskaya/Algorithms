# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
import sys

def func_var3(x):
    x = str(x)
    y = x[::-1]
    return locals()

spam = func_var3(1551).values()
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

# Получаем, что в третьем варианте памяти потрачено меньше всего (106) по сравнению, с 156 в первом и втором варианте.
# Версия python - 3.7, 64-ти разрядная ОС.