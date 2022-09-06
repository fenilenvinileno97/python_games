#create a squared-number list from 1 to 100
def run():
    list_comprehension = [i**2 for i in range(1,101) if i % 3 != 0]
    print(list_comprehension)
if __name__ == '__main__':
    run() 