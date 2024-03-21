"""
Aditi has used a text editing software to type some text. 
After saving the article as WORDS.TXT, she realized that she has 
wrongly typed alphabet J in place of alphabet I everywhere in the article.

Write a function definition for JTOI() in Python that would display 
the corrected version of entire content of the file WORDS.TXT 
with all the alphabets "J" to be displayed as an alphabet "I" on screen.

Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.
Example:
If Aditi has stored the following content in the file WORDS.TXT:
WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A SENTENCE

The function JTOI() should display the following content:
WELL, THIS IS A WORD BY ITSELF. YOU COULD STRETCH THIS TO BE A SENTENCE
"""


def JTOI(filename):
    try:
        file = open(filename, "r")
        data = file.read()
        corrected_data = data.replace("J", "I")
        print(corrected_data)
        file.close()
    except FileNotFoundError:
        print("File not found!")


JTOI("hello.TXT")
