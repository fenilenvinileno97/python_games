"""
Program for check divisibility 
"""
from multiprocessing.sharedctypes import Value


def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors #after for cycle, divisors is appended

def run():
    try:
        num = int(input('Enter a number: '))
        print(divisors(num))
        print('Program has ended')
    except ValueError:
        print('Enter a valid number!')
if __name__ == '__main__':
    run()