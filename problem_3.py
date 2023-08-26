"""The prime factors of 13195 are 5, 7, 13, and 29.
What is the largest prime factor of the number 600851475143?
"""
from math import sqrt

prime_factors = set()

def is_prime(n):
    prime = True
    for x in range(2, 1 + int(sqrt(n))):
        if n % x == 0:
            prime = False
    return prime

def get_prime_factors(n):
    
    if n == 1:
        prime_factors.add(n)
    elif n % 2 == 0:
        prime_factors.add(2)
        get_prime_factors(n / 2)
    else:
        divisible = False
        for divisor in range(3, 1 + int(sqrt(n))):
            if n % divisor == 0:
                divisible = True
                if is_prime(divisor):
                    prime_factors.add(divisor)
                get_prime_factors(n / divisor)
            else:
                pass
        if not divisible:
            prime_factors.add(int(n))

get_prime_factors(600851475143)            
print(prime_factors)

