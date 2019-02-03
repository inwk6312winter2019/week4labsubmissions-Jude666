import string, time
def open_file():
    word_list = []
    fin = open('word')
    for line in fin:
        word = line.strip().lower().replace(' ', '')
        for c in string.punctuation:
            word = word.replace(c, '')
        word_list.append(word)
    return word_list

def different_word():
    word_list = open_file()
    dictionary = {}
    for word in word_list:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] =+ 1
    return dictionary


print("The total number of words is", len(open_file()))
print("The number of times each word is used", different_word())
print("The number of different words is", len(different_word()))