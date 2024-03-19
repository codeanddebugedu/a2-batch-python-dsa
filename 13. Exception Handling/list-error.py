try:
    my_list = [34, 55, 63, 78, 94, 0]
    # print(my_list + "abc")
    # print(my_list[99])
    # print(my_list[0] / my_list[-1])
except ZeroDivisionError:
    print("Cannot divide by zero, please check the values again")
except IndexError:
    print("Index is out of range")
except Exception as e:
    print(type(e).__name__)
    print(e)
    print("Some unknown error occurred")
# else:
#     print("Everything works fine")
# finally:
#     print("This is a finally clause")
