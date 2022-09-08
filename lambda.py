"""Anonymous functions doesn't have name, in Python just have one code line
def run():
    def palindrome(string):
        string = string.lower()
        string = string.replace(' ', '')
        return string == string[::-1]

    print(palindrome('Anita lava la Tina'))

if __name__ == '__main__':
    run()"""

palindrome = lambda string : string.replace(' ', '').lower() == string.replace(' ', '').lower()[::-1]
print(palindrome('Anita Lava La Tina'))