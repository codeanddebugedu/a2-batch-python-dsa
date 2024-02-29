# Membership Operator (IN / NOT IN)

a = [43, 67, 11, 89, 54]

num: int = int(input("Enter a number = "))  # 54

# if a.count(num) > 0:
#     print("YEs")
# else:
#     print("No")

if num in a:
    print("YEs")
else:
    print("NO")
