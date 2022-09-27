def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding = "utf-8") as f: #take care with " " characters
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    pass

def run():
    read()

if __name__ == '__main__':
    run()