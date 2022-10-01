import random
import os

def read_data(filepath = './files/data.txt'):
    words = []
    with open(filepath, 'r', encoding = 'utf-8') as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def run():
    data = read_data(filepath = './files/data.txt')
    chosen_word = random.choice(data)
    chosen_word_spaces = ['_']*len(chosen_word)
    chosen_word_list_underscores = ['_'] * len(chosen_word_spaces)
    print(chosen_word)
    letter_index_dict = {key for key in chosen_word}
    print(letter_index_dict)
    spaces = ' '.join([str(item) for item in chosen_word_list_underscores])
    print(spaces)

if __name__ == '__main__':
    run()