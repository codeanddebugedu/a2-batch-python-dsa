my_list = [["Anirudh", 76], ["Vandana", 23], ["Akul", 67], ["Sanjay", 92]]
# my_list = [[76, "Anirudh"], [23, "Vandana"], [67, "Akul"], [92, "Sanjay"]]

# print(my_list[0][0])
# print(my_list[2][1])
# print(my_list[3][-1])
# print(my_list[-4][0])

# my_list.sort()
# x = sorted(my_list)
# print(my_list)
# print(x)
x = sorted(my_list, key=lambda x: x[1])
print(x)
# my_list.sort(key=lambda x: x[1], reverse=True)
# print(my_list)
