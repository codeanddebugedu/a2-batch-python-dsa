# 1 to 10,,,total
# start , end | start<end
# start,end ----total


"""
Enter start = 1
Enter end = 10

Addition of all numbers from 1 to 10 = 55

"""

start: int = int(input("Enter start: "))
end: int = int(input("Enter end: "))

i = start
total = 0
while i <= end:
    total = total + i
    i += 1

print(f"Addition of {start} to {end} = {total}")
