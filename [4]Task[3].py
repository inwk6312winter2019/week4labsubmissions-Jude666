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
            dictionary[word] += 1
    dictionary.pop('', None)
    return dictionary

def frequently_used():
    d = different_word()
    d_copy = d
    counter = 0
    frequent_words = []
    while counter < 20:
        frequent_word = max(d_copy, key=d_copy.get)
        frequent_words.append(frequent_word)
        d_copy.pop(frequent_word, None)
        counter += 1
    return frequent_words


print("The total number of words is", len(open_file()))
print("The number of times each word is used", different_word())
print("The number of different words is", len(different_word()))
print("The 20 most frequently used words are", frequently_used())