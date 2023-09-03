"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
"""

from problem_3 import is_prime

def nth_prime(n: int = 6):
    """Calculate the nth prime number.

    Args:
        n (int, optional): The nth prime number to find. Defaults to 6.

    Returns:
        int: nth prime number
    """
    primes = []
    i = 1
    while len(primes) < n + 1:
        if is_prime(i):
            primes.append(i)
        else:
            pass
        i += 1
    return primes[-1]

if __name__ == '__main__':
    print(nth_prime(10001))