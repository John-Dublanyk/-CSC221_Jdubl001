def min_max_sum(a, b, c):
    return (min(a, s, c), max(a, b, c), a + b + c)

def primes_sieve(limit):
    limitn = limit + 1
    primes = list(range(2, limitn))

    for i in primes:
        if i:
            for f in range(i * i, limitn, i):
                primes[f - 2] = 0 
    return [x for x i primes if x]

def min_max_sum_fixed(a, b, c):
    return (min(a, b,), max(a, b, c), a + b + c)