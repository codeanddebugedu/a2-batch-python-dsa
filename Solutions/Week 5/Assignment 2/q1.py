"""
Write a Python function that takes a dictionary as input where the values are lists. 
The function should return a new list containing all the elements from
all the lists in the dictionary.
It should have at least 3-4 keys and any amount of elements can be in a list.
"""

from typing import Dict, List


def mergeList(dictionary: Dict) -> List:
    result = []
    for v in dictionary.values():
        # result.extend(v) # Method 1
        # result = result + v  # Method 2
        for i in v:
            result.append(i)

    return result


print(mergeList({"A": [1, 2, 3], "B": [4, 5, 6]}))
