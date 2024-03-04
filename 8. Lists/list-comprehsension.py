# List Comprehension

# 1 to 10

# my_list = [i for i in range(1, 101, 5)]
# my_list = [i for i in range(-10, -1, -1)]
# my_list = [i for i in range(10, -1, -1)]
# my_list = [f"{i}-even" if i % 2 == 0 else f"{i}-odd" for i in range(1, 11)]
# my_list = [i for i in range(1, 11) if i % 2 == 0]
my_list = [i for i in range(1, 51) if i % 5 == 0 and i % 4 == 0]
print(my_list)
