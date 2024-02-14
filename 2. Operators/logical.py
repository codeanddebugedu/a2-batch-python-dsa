"""
Logical Operators (To compare 2 or more conditions) (Always in BOOL)
AND
C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T

OR
C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T

NOT (reverses the result)
"""

physics = 16
chemistry = 20
maths = 66
print(physics > 33 and chemistry > 33 and maths > 33)
# print(physics > 33 and chemistry > 33)
# print(physics > 33 or chemistry > 33)
# print(not (physics > 33 or chemistry > 33))
print(physics > 33 and not chemistry > 33)
# F and T -> F
print(not physics > 33)
