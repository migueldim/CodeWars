""""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that
occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and
 lowercase) and numeric digits.
"""

def duplicate_count(text):
    result = 0
    counters = []
    for i in text.lower():
        if text.count(i) > 1 and i not in counters:
            result += 1
            counters.append(i)

    return result

print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
print(duplicate_count("indivisibility"))