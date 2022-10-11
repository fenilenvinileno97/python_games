from functools import reduce
import random
import os

def read_data(filepath = './files/data.txt'):
    words = []
    with open(filepath, 'r', encoding = 'utf-8') as f:
        for line in f:
            words.append(line.strip().upper())
    return words

# def check_true(iterable):
#     for item in iterable:
#         if not item:
#             return False
#         return True
        

def run():
    
    data = read_data(filepath = './files/data.txt')
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ['_'] * len(chosen_word_list)
    letter_index_dict = {}
    
    for index, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(index)

    while True:
    
        letter = input('Enter a letter: ').strip().upper()
        assert letter.isalpha(), 'Just can enter letters!'
    
        if letter in chosen_word_list:
            for index in letter_index_dict[letter]:
                chosen_word_list_underscores[index] = letter
                
        underscores = ' '.join(map(str, chosen_word_list_underscores))
        print(underscores)
        print('\n')
    
        for item in underscores:
            if not item == '_':
                return False
        

        #we should create a cycle for finding '_' remaining in chosen_word_list_underscores and if this value is false, program is ended
        #afterwards, os library functions should be implemented.
    
if __name__ == '__main__':
    run()