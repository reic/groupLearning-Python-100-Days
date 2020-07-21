# pip install python-docx
import docx
import re
from nltk.stem import PorterStemmer
from Eng_word_learning import word_count, get_words


def get_doc_words(filename):
    # read docx
    readfile = docx.Document("./"+filename)
    wordlist, unknowlist = [], []
    for para in readfile.paragraphs:
        wordlist.extend(get_words(para.text.lower()))
        for run in para.runs:
            if run.underline and run.underline != True:
                # unknowlist.append(run.text.lower())
                unknowlist.extend(get_words(run.text.lower()))
    return wordlist, unknowlist


def unknownwords_to_file(filename, data):
    text = ', '.join([item.word for item in data.values()])+"\n"
    with open('./'+filename, "a", encoding='utf-8') as f:
        f.write(text)


def main():
    # 從 word 檔讀取文字， 不認識的字  double underline (ctrl - shift - d) 的字
    wordall, unknowns = get_doc_words('test.docx')
    # print(wordall)
    stemlist = word_count(wordall)
    unknown_stemlist = word_count(unknowns)
    counter = 0
    for item in unknown_stemlist:
        counter += stemlist[item].counter
        unknown_stemlist[item].word = stemlist[item].word
        unknown_stemlist[item].counter = stemlist[item].counter
    accident_rate = counter/len(wordall)*100
    # print(counter, len(wordall))
    # print(counter)
    print({item.word: item.counter for item in unknown_stemlist.values()})
    print("總共單字數 %2d" % len(stemlist))
    print("不熟悉的單字 %2d" % len(unknown_stemlist))
    print("意外率 %.2f %%" % accident_rate)

    filename = "English_from_doc.txt"
    # 將新的單字寫入檔案
    unknownwords_to_file(filename, unknown_stemlist)


if __name__ == "__main__":
    main()
