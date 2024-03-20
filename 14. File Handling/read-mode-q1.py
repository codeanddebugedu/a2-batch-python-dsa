"""
[Hello, World]
This is Anirudh
We are doing python

World Hello 
Anirudh is This
python doing are We

"""

f = open("hello.txt", "r")

lines = f.readlines()

for line in lines:
    words = line.split()
    # words.reverse()
    words = words[::-1]
    print(words)
    print(" ".join(w[::-1] for w in words))


f.close()
