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

i = min_index + 1
summ = 0

while i < max_index:
    summ += array[i]
    i += 1

print(f"Исходный массив: {array}")
print(f"Сумма элементов между максимальным и минимальным элементами: {summ}")
