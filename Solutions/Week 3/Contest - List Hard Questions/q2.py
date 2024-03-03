"""
Given two sorted lists, write a Python code to merge them into a single sorted list.
"""
from typing import List

a = [1, 4, 6, 7, 8, 12, 14, 22]
b = [34, 56, 78, 99, 100]

i = 0
j = 0

result = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    elif b[j] < a[i]:
        result.append(b[j])
        j += 1
    else:
        result.append(a[i])
        result.append(b[j])
        i += 1
        j += 1

while i < len(a):
    result.append(a[i])
    i += 1

while j < len(b):
    result.append(b[j])
    j += 1

print(result)
