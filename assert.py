def palindrome(string):
    assert len(string) > 0, "It can't be entered an empty string"
    return string == string[::-1]

print(palindrome(""))