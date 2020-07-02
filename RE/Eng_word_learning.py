from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize

with open('English.txt', 'r', encoding='utf-8') as f:
    new_word = f.read()


class Stemer(object):
    def __init__(self, word, counter=1):
        self.counter = counter
        self.word = word

    def __str__(self):
        return " %s: %d " % (self.word, self.counter)


ps = PorterStemmer()
words = new_word.split(", ")
stems = {}
for w in words:
    index = ps.stem(w.lower())

    if index not in stems:
        stems[index] = Stemer(w)
    else:
        stems[index].counter += 1
        if len(w) < len(stems[index].word):
            stems[index].word = w.lower()
        if len(w) == len(stems[index].word) and w.lower() != stems[index].word:
            stems[index].word = w.lower()
for stem in stems.values():
    if stem.counter > 4:
        print(stem.word, stem.counter)
# for stem in stems:
#     print(stem)
