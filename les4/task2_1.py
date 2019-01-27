# Решето Эратосфена

def func_sieve(num):

    n = num ** 2
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result[num-1]

#100 loops, best of 5: 29.5 usec per loop - 10
#100 loops, best of 5: 3.53 msec per loop - 100
#100 loops, best of 5: 554 msec per loop - 1000

#Алгоритм не линейный. Сложность алгоритма, согласно информации из википедии O(n\log(\log n)). Работает медленее, чем придуманный алгоритм.





