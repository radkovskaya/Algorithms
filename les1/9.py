# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))

if a < b < c or c < b < a:
    print(f"Среднее число {b}")
elif b < a < c or c < a < b:
    print(f"Среднее число {a}")
else:
    print(f"Среднее число {c}")