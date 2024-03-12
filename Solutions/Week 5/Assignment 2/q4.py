"""
Write a Python function that takes two dictionaries as input, 
where the values are lists. The function should merge the lists 
corresponding to the same keys in both dictionaries into a 
single list and return a new dictionary with these merged lists.
"""


def mergeDictionary(dictionary1, dictionary2):
    merged_dictionary = {}

    # We do this for dictionary1
    for key in dictionary1:
        if key in dictionary2:
            merged_dictionary[key] = dictionary1[key] + dictionary2[key]
        else:
            merged_dictionary[key] = dictionary1[key]

    # Now we do for keys in dictionary2 not present in dictionary1
    for key in dictionary2:
        if key not in dictionary1:
            merged_dictionary[key] = dictionary2[key]

    return merged_dictionary


dict1 = {"x": [1, 2, 3], "y": [4, 5, 6]}
dict2 = {"x": [7, 8, 9], "y": [10, 11, 12], "z": [99, 100, 111]}
result = mergeDictionary(dict1, dict2)
print(result)
