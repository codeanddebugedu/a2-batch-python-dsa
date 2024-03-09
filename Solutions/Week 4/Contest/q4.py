"""
Ask a sentence from user. Then ask a integer k from user. 
Print all the words which are greater or equal to k.
"""


def printWords(sentence, k):
    words = sentence.split()
    for word in words:
        if len(word) >= k:
            print(word, end=" ")


sentence = input("Enter a sentence: ")
k = int(input("Enter an integer k: "))

printWords(sentence, k)
