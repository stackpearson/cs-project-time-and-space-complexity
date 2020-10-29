# Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

# Examples:

# csFirstUniqueChar(input_str = "lambdaschool") -> 2
# csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
# csFirstUniqueChar(input_str = "vvv") -> -1
# Notes:

# input_str will only contain lowercase alpha characters.

def csFirstUniqueChar(input_str):
    # determine uniqe chars

    unique_char = []
    char_order = []
    counts = {}
    first_unique = ''

    for char in input_str:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            char_order.append(char)
            
    for char in char_order:
        if counts[char] == 1:
            unique_char.append(char)
            first_unique = ''.join(unique_char)
            return input_str.index(first_unique)
    return -1
            
print(csFirstUniqueChar('lambdaschool'))
print(csFirstUniqueChar('vvv'))