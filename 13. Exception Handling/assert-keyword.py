# Assert
try:
    age = int(input("Enter your age = "))
    assert age > 18, "You should be atleast 18 age"

    vote_id = int(input("Enter voting ID = "))
    vote_id = input("Enter party to vote = ")
except AssertionError as e:
    print(e)
except:
    print("Some error occurred")
