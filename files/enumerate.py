import os
import random

def read_data():
    with open('./files/data.txt', 'r', encoding='utf-8') as data:
        for elem in data:
            pass

def run():
    read_data()

if __name__ == '__main__':
    run()