"""
Write a Python code to find the dierence between two lists
(i.e., elements present in the first list but not in the second).
"""
from typing import List


def difference(lst1: List, lst2: List):
    for i in lst1:
        if i not in lst2:
            print(i)


difference([1, 2, 3, 4], [3, 4, 5, 6])
