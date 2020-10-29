# You are given two strings, str_1 and str_2, where str_2 is generated by randomly shuffling str_1 and then adding one letter at a random position.

# Write a function that returns the letter that was added to str_2.

# Examples:

# csFindAddedLetter(str_1 = "bcde", str_2 = "bcdef") -> "f"
# csFindAddedLetter(str_1 = "", str_2 = "z") -> "z"
# csFindAddedLetter(str_1 = "b", str_2 = "bb") -> "b"


def csFindAddedLetter(str_1, str_2):
        
    sorted_str_1 = sorted(str_1)
    sorted_str_2 = sorted(str_2)
    
    sorted_list_1 = list(sorted_str_1)
    sorted_list_2 = list(sorted_str_2)
    print('sorted_list_1', sorted_list_1)
    print('sorted_list_2', sorted_list_2)

    unique_chars = []
    unique_char_string = ''
    last_char = sorted_list_2[len(sorted_list_1)]

    for i in range(0, len(sorted_list_1)):
        if sorted_list_2[i] != sorted_list_1[i]:
            unique_chars.append(sorted_list_2[i])
            
            return unique_char_string.join(unique_chars)
    else:
        return sorted_str_2[len(sorted_list_1)]


print(csFindAddedLetter('xqmxtheyvpdqounqmfyaqdqxwe', 'xqmxtheyvpdqounqmfyaqxdqxwe'))
print(csFindAddedLetter('bcde', 'bcdfe'))
print(csFindAddedLetter('bcde', 'bcdde'))
print(csFindAddedLetter('bf', 'bfb'))

# str_1: "xqmxtheyvpdqounqmfyaqdqxwe"
# str_2: "xqmxtheyvpdqounqmfyaqxdqxwe"