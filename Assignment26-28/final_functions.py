def min_max_sum(a, b, c):
    return (min(a, b, c), max(a, b, c), a + b + c)

def primes_sieve(limit):
    limitn = limit + 1
    primes = list(range(2, limitn))

    for i in primes:
        if i:
            for f in range(i * i, limitn, i):
                primes[f - 2] = 0 
    return [x for x in primes if x]

def min_max_sum_fixed(a, b, c):  # Renamed to avoid conflict with the first min_max_sum
    return (min(a, b, c), max(a, b, c), a + b + c)
