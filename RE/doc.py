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
    text = ", "+', '.join([item.word for item in data.values()])
    with open('./'+filename, "a", encoding='utf-8') as f:
        f.write(text)


def main():
    # 從 word 檔讀取文字， 不認識的字  double underline (ctrl - alt - d) 的字
    wordall, unknowns = get_doc_words('test.docx')
    stemlist = word_count(wordall)
    unknown_stemlist = word_count(unknowns)
    counter = 0
    for item in unknown_stemlist:
        counter += stemlist[item].counter
        unknown_stemlist[item].word = stemlist[item].word
    accident_rate = counter/len(wordall)*100
    print(counter, len(wordall))
    print("意外率 %.2f " % accident_rate)

    # 將新的單字寫入檔案
    unknownwords_to_file('wordlearn.txt', unknown_stemlist)


if __name__ == "__main__":
    main()
