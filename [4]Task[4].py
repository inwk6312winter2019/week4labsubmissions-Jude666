import string
def open_file():
    word_list = []
    fin = open('pg58773.txt')
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

def word_list():
    wordInlist = []
    fin = open('word')
    for line in fin:
        word = line.strip().lower().replace(' ', '')
        wordInlist.append(word)
    return wordInlist

def compare():
    word_in_book = open_file()
    word_in_list = word_list()
    count = 0
    for c in word_in_book:
        if c not in word_in_list:
            print(c)
            count += 1
    print("The number of words in the book but not in the list is", count)

print("The total number of words is", len(open_file()))
print("The number of times each word is used", different_word())
print("The number of different words is", len(different_word()))
print("The 20 most frequently used words are", frequently_used())
compare()