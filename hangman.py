import random
import os

def read_data(filepath='./files/data.txt'):
    words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip().upper()) #strip is a method used removing spaces between strings
    return words

def run():
    data = read_data(filepath='./files/data.txt')
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word.lower().strip()]
    chosen_word_list_underscores = ['_'] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    while True:
        os.system('clear')
        print('Adivina la palabra!')

        for element in chosen_word_list_underscores:
            print(element + '', end='')
        print('\n')

        letter = input('Ingresa una letra: ').strip().upper()
        assert letter.isalpha()

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        if '_' not in chosen_word_list_underscores:
            os.system('clear')
            print('¡Ganaste! La palabra era', chosen_word)
            break

if __name__ == '__main__':
    run()