#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

Enterprise = namedtuple("Enterprise", "name profit_1q profit_2q profit_3q profit_4q")

def read_ent():
        name = input("Введите название предприятия ")
        p1 = int(input("Введите прибыль предприятия за первый квартал "))
        p2 = int(input("Введите прибыль предприятия за второй квартал "))
        p3 = int(input("Введите прибыль предприятия за третий квартал "))
        p4 = int(input("Введите прибыль предприятия за четвертый квартал "))
        ent = Enterprise(name, p1, p2, p3, p4)
        return ent

def mid_profit_one(lst_ent):
    mid_ent = [((ent.profit_1q + ent.profit_2q + ent.profit_3q + ent.profit_4q)) for i, ent in enumerate(lst_ent)]
    return mid_ent

def mid_profit_all(mid_p, num_ent):
    summ = 0
    for p in mid_p:
        summ = summ + p
    midle = summ/num_ent
    return midle

def main():
    num_ent = int(input("Введиите количество предприятий "))
    lst_ent = [read_ent() for i in range(num_ent)]
    mid_p = mid_profit_one(lst_ent)
    mid_all = mid_profit_all(mid_p, num_ent)
    print(f"Средняя прибыль по всем предприятиям: {mid_all}")
    lst_ent_small = []
    lst_ent_big = []
    for i, p in enumerate(mid_p):
        if p < mid_all:
            lst_ent_small.append(lst_ent[i])
        elif p > mid_all:
            lst_ent_big.append(lst_ent[i])
        else:
            continue
    print("Предприятия, у которых прибыль больше средней")
    for ent in lst_ent_big:
        print(ent.name)
    print("Предприятия, у которых прибыль меньше средней")
    for ent in lst_ent_small:
        print(ent.name)
main()
