# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random

def median(lst):
    while len(lst) != 1:
        lst.remove(max(lst))
        lst.remove(min(lst))
    return lst

lst = [i for i in range(9)]
random.shuffle(lst)
print(f' Медиана: {median(lst)}')