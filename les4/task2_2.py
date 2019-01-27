# Алгоритм поиска простых чисел

def find_nth_prime(n):
    primes = []
    num = 2

    while len(primes) < n:
        is_prime = True
        for divisor in primes:
            if num % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

        num += 1

    return primes[n-1]

#100 loops, best of 5: 8.56 usec per loop - 10
#100 loops, best of 5: 358 usec per loop - 100
#100 loops, best of 5: 7.55 msec per loop - 500
#100 loops, best of 5: 29.8 msec per loop - 1000

# Алгоритм не линейный. Но работает быстрее, чем решето. Оценка по сложности сверху О(n^^2)







