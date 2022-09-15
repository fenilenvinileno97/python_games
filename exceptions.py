from multiprocessing.sharedctypes import Value


def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('You have to write something')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        print(palindrome(str(input('Enter a sentence: '))))
    except TypeError:
        print('Just strings are allowed')

if __name__ == '__main__':
    run()