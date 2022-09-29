import random
import os

def read(filepath='./files/data.txt'):
    words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip().lower()) #strip is a method used removing spaces between strings
    return words
    
def run():
    data = read(filepath='./files/data.txt')
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word.lower().strip()]
    print(chosen_word_list)
if __name__ == '__main__':
    run()