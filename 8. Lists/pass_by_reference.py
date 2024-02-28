def display(lst: list):
    lst[0] = 100
    print(id(lst))
    print(lst)


my_list = [45, 33, 22, 11, 91]
print(id(my_list))
display(my_list)
print(my_list)
