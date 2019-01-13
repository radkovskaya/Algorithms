# 4. Определить, какое число в массиве встречается чаще всего.

import random

size = 100
max_item = 10
array = [random.randint(0, max_item) for i in range(size)]
lst = [0 for i in range(max_item+1)]
max_el = 0

for item in array:
    lst[item] += 1
print(f"Массив-счетчик повторений элементов: {lst}")

for index, item in enumerate(lst):
    if item > max_el:
        max_el = item
        max_index = index

print(f"Исходный массив: {array}")
print(f"Чаще всего в массиве встречается элемент: {max_index}")

