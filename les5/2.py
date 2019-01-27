#2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict


dict = {"0" : 0, "1": 1, "2": 2, "3" : 3, "4": 4, "5":5, "6": 6, "7": 7, "8":8, "9":9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15 }
dict_reverse = {0 : "0", 1: "1", 2: "2", 3 : "3", 4: "4", 5: "5", 6: "6", 7: "7", 8:"8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14 : "E", 15: "F" }


def list_to_dict(lst):
    num = defaultdict(int)
    for i, el in enumerate(lst):
        num[i] = el
    return num


def hex_to_dec(lst):
    lst_dec = [dict[num] for i, num in enumerate(lst)]
    return lst_dec


def dec_to_hex(lst):
    lst_hex = [dict_reverse[num] for i, num in enumerate(lst)]
    return lst_hex


def summ(num1, num2):
    return (num1 + num2) % 16, (num1 + num2) // 16


def read_number(prompt):
    lst1 = list(input(prompt))
    lst1.reverse()
    lst1_dec = hex_to_dec(lst1)
    num1 = list_to_dict(lst1_dec)
    return num1


def sum_numbers(num1, num2):
    i = 0
    overflow = 0
    sum_dec = defaultdict(int)
    while (i < max(len(num1), len(num2))) or (overflow > 0):
        tmp = summ(num1[i], num2[i])
        sum_dec[i] = tmp[0] + overflow
        overflow = 0
        overflow = tmp[1]
        if sum_dec[i] > 15:
            overflow += sum_dec[i] // 16
            sum_dec[i] = sum_dec[i] % 16
        i += 1

    sum_dec = [v for k, v in sorted(sum_dec.items())]
    sum_dec.reverse()
    return sum_dec


def mul_numbers(num1, num2):
    multi = defaultdict(int)

    for i in range(len(num1)):
        for j in range(len(num2)):
            multi[i + j] += num1[i] * num2[j]

    multi = [v for k, v in sorted(multi.items())]

    R = 0
    for i, num in enumerate(multi):
        R += num * (16 ** i)

    multi_16 = defaultdict(int)
    i = 0
    while R > 0:
        multi_16[i] = R % 16
        R = R // 16
        i += 1

    multi_16 = list(multi_16.values())
    multi_16.reverse()

    return multi_16


num1 = read_number("Введите первое число ")
num2 = read_number("Введите второе число ")
print("Сумма введенных чисел равна {}".format(dec_to_hex(sum_numbers(num1, num2))))
print("Произведение введенных чисел равно {}".format(dec_to_hex(mul_numbers(num1, num2))))

