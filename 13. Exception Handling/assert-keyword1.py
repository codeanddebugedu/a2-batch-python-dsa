try:
    my_list = [54, 65, 78, 2, 123, 45, 65, 7, 11]
    index = int(input("Enter index number = "))
    assert index >= 0 and index < len(my_list), "Index is out of range"
    print(my_list[index])
except AssertionError as ae:
    print(ae)
except:
    print("Some unknown error occurred")
