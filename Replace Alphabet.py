"""
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
"""

def alphabet_position(text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in text.lower():
        if i in alpha:
            result += str(alpha.index(i) + 1) + " "
    return result[:-1]


print(alphabet_position("...."))

