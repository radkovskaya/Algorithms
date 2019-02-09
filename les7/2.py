# 2  Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def merge(lst1, lst2):
    array = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            array.append(lst1[i])
            i += 1
        else:
            array.append(lst2[j])
            j += 1
    for i in range(i, len(lst1)):
        array.append(lst1[i])
    for j in range(j, len(lst2)):
        array.append(lst2[j])
    return array

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        return merge(merge_sort(lst[mid:]), merge_sort(lst[:mid]))

array = [random.uniform(0,50) for i in range(10)]
print(f'Исходный массив {array}')
print(f'Отсортированный массив {merge_sort(array)}')
