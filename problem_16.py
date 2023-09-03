"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

def power_digit_sum(n: int = 15):
    second_power = [int(x) for x in str(int(2 ** n))]
    return sum(second_power)
    
if __name__ == '__main__':
    print(power_digit_sum(1000))