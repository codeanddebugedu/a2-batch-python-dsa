my_string: str = "delhi is clean city"


result = "".join([ch if ch != "i" else "z" for ch in list(my_string)])
print(result)
