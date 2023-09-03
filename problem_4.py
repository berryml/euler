"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 * 99. Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    return str(n)[:] == str(n)[::-1]

def get_palindrome_product(max_num = 999, min_num=99):
    all_products = sorted(list(set([x * y for x in range(100, 1000) for y in range(100, 1000)])), reverse=True)
    for ap in all_products:
        if is_palindrome(ap):
            return ap
        else:
            pass
            
            
get_palindrome_product()