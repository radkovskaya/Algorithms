# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

size = 10
min_item = -100
max_item = 100
array = [random.randint(-100, max_item) for i in range(size)]
max_minus = min_item

for item in array:
    if item < 0:
        if item > max_minus:
            max_minus = item

print(f"Исходный массив: {array}")
print(f"Максимальный отрицательный элемент: {max_minus}")


