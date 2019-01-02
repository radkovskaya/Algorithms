# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = 10
max_item = 10
array = [random.randint(0, max_item) for i in range(size)]

min_el = max_item
max_el = 0
max_index = 0
min_index = 0

for index, value in enumerate(array):
    if value > max_el:
        max_el = value
        max_index = index
    if value < min_el:
        min_el = value
        min_index = index

print(f"Массив до замены элементов: {array}")
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f"Массив после замены элементов: {array}")
