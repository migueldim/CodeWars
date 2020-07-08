"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary
representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""

def count_bits(number):
    bin_number = str(bin(int(number)))
    counter = 0
    for i in bin_number:
        if i == '1':
            counter += 1
    return counter


print(bin(194645646))
print(count_bits(194645646))
