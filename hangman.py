import random
import os

def read(filepath='./files/data.txt'):
    words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip().upper()) #strip is a method used removing spaces between strings
    print(words)
def run():
    read()
if __name__ == '__main__':
    run()