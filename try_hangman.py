import random
import os

def read_data(filepath = './files/data.txt'):
    words = []
    with open(filepath, 'r', encoding = 'utf-8') as f:
        for line in f:
            words.append(line.strip().upper())
    return words

def normalize(s): # It removes the accents of a string
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

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
    
        letter = normalize(input('Enter a letter: ').strip().upper())
        assert letter.isalpha(), 'Just can enter letters!'
    
        if letter in chosen_word_list:
            for index in letter_index_dict[letter]:
                chosen_word_list_underscores[index] = letter
                
        underscores = ' '.join(map(str, chosen_word_list_underscores))
        print(underscores)
        print('\n')
        
        remaining_underscore = '_'
        if not remaining_underscore in chosen_word_list_underscores:
            os.system('clear')
            print('You have won!, correct word was', chosen_word)
            break
        
        
    
if __name__ == '__main__':
    run()