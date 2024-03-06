"""
Ask a string from user.
Replace all vowels with z.

aeroplane

list

join

zzrzplznz
"""

str = "aeroplane"
str2 = ""
for ch in str:
    if ch in "aeiou":
        str2 += "z"
    else:
        str2 += ch


print(str2)
