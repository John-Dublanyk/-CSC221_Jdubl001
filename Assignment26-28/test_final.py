from final_functions import min_max_sum_fixed, primes_sieve
import pytest

def test_min_max_sum_fixed():
    assert min_max_sum_fixed(1, 2, 3) == (1, 3, 6)
    assert min_max_sum_fixed(10, 20, 30) == (10, 30, 60)

def test_primes_sieve():
    assert primes_sieve(10) == [2, 3, 5, 7]
    assert primes_sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
