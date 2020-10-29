# Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

# Examples:

# csFirstUniqueChar(input_str = "lambdaschool") -> 2
# csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
# csFirstUniqueChar(input_str = "vvv") -> -1
# Notes:

# input_str will only contain lowercase alpha characters.

def csFirstUniqueChar(input_str):
    # determine uniqe chars
    unique_chars_set = set(input_str)
    # unique_chars = ''.join(unique_chars_set)
    # print(unique_chars)
    # loop over input_str  checking for characters that match
    for i in unique_chars_set:
        if i in input_str:
            print(unique_chars_set[])
            
    
    

print(csFirstUniqueChar('lambdaschool'))