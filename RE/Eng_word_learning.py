from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
import re


def get_words_old(data):
    words = []
    word = ''  # get word in content
    patten = re.compile(r'[a-zA-Z-\'"]')
    for c in data:
        if re.match(patten, c):
            word += c.lower()
        else:
            if word:
                words.append(word)
                word = ''
    return words


def get_words(data, pattern=r'[a-zA-Z]+'):
    words = re.findall(pattern, data)
    return words


class Wordobj(object):
    def __init__(self, word, counter=1):
        self.counter = counter
        self.word = word

    def __str__(self):
        return " %s \t %d " % (self.word, self.counter)


def word_count(words):
    stems = {}
    ps = PorterStemmer()
    for word in words:
        word = word.lower()
        index = ps.stem(word)
        if index not in stems:
            stems[index] = Wordobj(word)
        else:
            stems[index].counter += 1
            len_word = len(word)
            len_stem_word = len(stems[index].word)
            if len_word < len_stem_word:
                stems[index].word = word
            if len_word == len_stem_word and word != stems[index].word:
                stems[index].word = word
    return stems


def main():
    with open('English.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    stops_word = ['in', 'of', 'at', 'to']
    words_list = get_words(text)
    stems = word_count(words_list)
    output_list = [[item.word, item.counter]
                   for item in stems.values() if item.counter >= 4 and item.word not in stops_word]
    output_list.sort(key=lambda x: x[1], reverse=True)
    print(output_list)


if __name__ == "__main__":
    main()
