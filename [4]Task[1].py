import string
def open_file():
    fin = open('word')
    for line in fin:
        word = line.strip().lower().replace(' ', '')
        for c in string.punctuation:
            word = word.replace(c, '')
        print(word)
open_file()