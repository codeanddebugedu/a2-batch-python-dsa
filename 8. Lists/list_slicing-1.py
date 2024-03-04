# List SLicing
my_list = [45, 31, 76, 54, 11, 32, 100]

# result = my_list[0 : len(my_list)]
# result = my_list[0:6:2]
# result = my_list[0:6:4]  # 45
# result = my_list[::10]
# result = my_list[-4:-1]
# result = my_list[-1:-4]
# result = my_list[::-2]
# result = my_list[-2:-4:-2]
# result = my_list[-2:-4:2]
result = my_list[-5::-2]

print(result)
