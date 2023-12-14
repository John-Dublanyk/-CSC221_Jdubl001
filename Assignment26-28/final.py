from final_functions import min_max_sum_fixed, primes_sieve

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
result_tuple = min_max_sum_fixed(a, b, c)
print("min_max_sum_fixed result:", result_tuple)

print("Primes up to 1000:", primes_sieve(1000))

x = 10
y = 100
z = 1000
result_tuple = min_max_sum_fixed(x, y, z)
print("min_max_sum_fixed result:", result_tuple)