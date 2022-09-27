def read():
    numbers = []
    with open("./files/numbers.txt", "r", endcoding= "utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    pass

def run():
    pass

if __name__ == '__main__':
    run()