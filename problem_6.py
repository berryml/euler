"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the\
sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square\
of the sum.
"""

def sum_square_difference(n: int = 10):
    """Calculate the sum of squared integers from 1 through n. Calculate the square of summed integers from\
        1 through n. Calculate their difference.

    Args:
        n (int, optional): First n natural numbers. Defaults to 10.

    Returns:
        int: Difference between summed squares and squared sum.
    """
    sum_of_squares = sum([i**2 for i in range(1, n + 1)])
    square_of_sums = sum([i for i in range(1, n + 1)]) ** 2
    return abs(sum_of_squares - square_of_sums)

if __name__ == '__main__':
    print(sum_square_difference(100))