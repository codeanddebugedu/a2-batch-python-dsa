# Make a function named checkOddEven which takes an integer as a argument
# If even, rint EVEN, else print ODD


def checkOddEven(num: int) -> None:
    if num % 2 == 0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")


n = 56
checkOddEven(n)
checkOddEven(10)
checkOddEven(9)
