"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""
from math import sqrt

def prod_of_pythagorean_triple(n: int = 1000):
    """Calculate the product of the pythagorean triple that sums to n.

    Args:
        n (int, optional): What should the pythagorean triple sum to? Defaults to 1000.

    Returns:
        int: Product of pythagorean triple.
    """
    for a in range(1, 500):
        for b in range(1, 500):
            c = sqrt((a**2) + (b**2))
            if c == int(c) and a + b + c == 1000:
                return int(a *b * c)

if __name__ == '__main__':
    print(prod_of_pythagorean_triple())