#1 Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n += 1
        print(array)

lst = [i for i in range(-100,100)]
random.shuffle(lst)
bubble_sort(lst)
