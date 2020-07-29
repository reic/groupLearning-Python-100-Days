from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
import re
import os
from datetime import datetime


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


def english_words_left(words_list, output_list, word_learn=6):
    ps = PorterStemmer()
    learn_list = [ps.stem(i[0]) for i in output_list[0:word_learn]]

    content = list(filter(lambda item: ps.stem(
        item) not in learn_list, words_list))
    return content


def main():
    filename = 'English.txt'
    # get English Word tank
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    words_list = get_words(text, r'[a-zA-Z-\'"]+')
    # get English word_new
    filename_learn = "English_from_doc.txt"
    with open(filename_learn, 'r', encoding='utf-8') as f:
        text = f.read()
        words_list.extend(get_words(text, r'[a-zA-Z-\'"]+'))

    stops_word = ['in', 'of', 'at', 'to']
    stems = word_count(words_list)
    output_list = [[item.word, item.counter]
                   for item in stems.values() if item.counter >= 4 and item.word not in stops_word]
    output_list.sort(key=lambda x: x[1], reverse=True)
    counter = 0
    text = ''
    for i in output_list[:6]:
        counter += i[1]
        text += i[0]+"\n"

    with open("English_need_learn.txt", 'w', encoding='utf-8') as f:
        f.write(text)

    print(counter)
    words_left = english_words_left(words_list, output_list)
    print("原始字數: {:5d}, 移除學習中字數: {:5d}".format(
        len(words_list), len(words_left)))
    os.system('copy %s %s_%s.txt' %
              (filename, filename[:-4], datetime.now().strftime("%Y%m%d")))
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(', '.join(words_left))


if __name__ == "__main__":
    main()
