def divisors(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    return divisors #after for cycle, divisors is appended

def run():
    num = (input('Enter a number: '))
    assert num.isnumeric(), 'You should enter a valid quantity'
    print(divisors(int(num)))
    print('Program has ended')
if __name__ == '__main__':
    run()