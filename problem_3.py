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

def get_prime_factors(n, set_of_prime_factors):
    
    if n == 1:
        set_of_prime_factors.add(n)
    elif n % 2 == 0:
        set_of_prime_factors.add(2)
        get_prime_factors(n / 2, set_of_prime_factors)
    else:
        divisible = False
        for divisor in range(3, 1 + int(sqrt(n))):
            if n % divisor == 0:
                divisible = True
                if is_prime(divisor):
                    set_of_prime_factors.add(divisor)
                get_prime_factors(n / divisor, set_of_prime_factors)
            else:
                pass
        if not divisible:
            set_of_prime_factors.add(int(n))

if __name__ == '__main__':
    get_prime_factors(600851475143, prime_factors)            
