def divisors(num):
        divisors = [i for i in range(1, num+1) if num % i == 0]
        return divisors
def run():
    try:
        num = int(input('Write a number: \n'))
        if num <= 0:
            raise ValueError
        print(divisors(num))
        print('Program has ended')
    except (ValueError, TypeError):
        print('Enter a valid number!')

if __name__ == '__main__':
    run()