# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

x = int(input("Введите число "))
n = x
count = 0
z = 0
while n > 0:
    n = n // 10
    count += 1
while count > 0:
    a = x % 10
    y = a * 10 ** (count - 1)
    z += y
    x = x // 10
    count -= 1
print(f"Обратное число {z}")