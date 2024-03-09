string = "abc xyz pqr lmn"

# cba zyx rqp nml

words = string.split()
result = [w[::-1] for w in words]
print(" ".join(result))
