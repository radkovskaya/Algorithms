# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

min_item = 2
max_item = 99
min_mult = 2
max_mult = 9
array = [i for i in range(min_item, max_item)]
array_answ = [0 for i in range(0, max_mult+1)]

for i in array:
    for j in range(min_mult, max_mult+1):
        if i % j == 0:
            array_answ[j] += 1

for item in range(min_mult, max_mult+1):
    print(f"В исходном массиве содержится {array_answ[item]} чисел, которые кратны {item} ")
