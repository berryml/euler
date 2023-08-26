"""Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89
By considering the terms in the Fibonacci sequence whose values do not exceed four
million, find the sum of
the even-valued terms.
"""
fibs = []
def fib(n1, n2, upper_limit):
    n = n1 + n2
    if n <= upper_limit:
        fibs.append(n)
        fib(n2, n, upper_limit)
    else:
        pass

        
fibs.append(1)
fibs.append(2)
fib(1, 2, 4000000)

even_fibs = [f for f in fibs if f%2 == 0]
print(sum(even_fibs))