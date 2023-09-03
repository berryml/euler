"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from problem_3 import is_prime

def sum_primes_below_n(n: int = 10):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return sum(primes)
    
if __name__ == '__main__':
    print(sum_primes_below_n(2000000))