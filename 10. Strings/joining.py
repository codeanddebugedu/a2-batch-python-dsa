"""
String -> List
List -> String (Joining)
"""

# my_string = "python is great    6 6 3"
# r = list(my_string)
# print(r)
# my_list = [2, 5, 1, 8, 9, 8]  # 251898
my_list = ["aaaa", "dasdy", "dwad", "dwadwa"]

result = "".join(str(i) for i in my_list)
# result = "".join(my_list)
print(result)
print(type(result))
