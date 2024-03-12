from typing import Dict


def countChar(string: str) -> Dict:
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


print(countChar("delhi delhi"))
