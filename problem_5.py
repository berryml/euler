# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from
# 1 to 20?


def get_smallest_multiples(n: int = 10):
    values = [value for value in range(1, n + 1)]
    if values:
        n  = max(values)
        m = n
        values.remove(n)
        while any(n % value for value in values):
            n += m
        return n
    return 0


if __name__ == '__main__':
    print(get_smallest_multiples(20))