
from playsound import playsound
from time import sleep
import re
import random
import os


def get_content(path):
    pattern = r'=(.*)\n'
    files = ["english.txt", 'mylanguage.txt', 'syllable.txt']
    data = {}
    for filename in files:
        with open(path+filename, 'r', encoding='utf_16_le') as f:
            data[filename[:-4]] = re.findall(pattern, f.read())
    return data


# def get_unit_data(path, quiztype=1, numtest=10):
def get_unit_data(path, quiztype=1):
    ''' path 用 list 儲放，合併成 string'''
    text = get_content(''.join(path))

    maxnumber = len(text['english'])
    # for i in range(maxnumber):
    #     print(" %20s  %20s \t %s" %
    #           (text['english'][i], text['syllable'][i], text['mylanguage'][i]))
    # quiz = random.sample(range(0, maxnumber), numtest)
    quiz = list(range(0, maxnumber))
    if quiztype == 1:
        ques = ['mylanguage', 'english']
    elif quiztype == 2:
        ques = ['english', "mylanguage"]
    else:
        ques = ['mylanguage', 'english']
    print("Quiz start:")
    # for i in quiz:
    while len(quiz) > 0:
        i = random.choice(quiz)
        # if ans == text[ques[1]][i]:
        if quiztype != 3:
            print("%s" % text[ques[0]][i])
            ans = input("ans: ").lower().strip()
            # if ans in text[ques[1]][i]:
            if answer_check(ans, text[ques[1]][i], quiztype):
                if quiztype != 1:
                    print("%5s答對了。 %s" % ('', text[ques[1]][i]))
                else:
                    print("%5s答對了。" % (''))
                    get_voice(path, i)
                quiz.remove(i)
            else:
                print("%5sError： Answer is: %s " % ('', text[ques[1]][i]))
                sleep(1.5)
        else:
            while 1:
                get_voice(path, i)
                ans = input("再聽一次，請輸入 y ：").lower()
                if ans != "y":
                    # if ans == text[ques[1]][i]:
                    if answer_check(ans, text[ques[1]][i], quiztype):
                        print("%5s答對了， %s " % ('', text[ques[0]][i]))
                        quiz.remove(i)
                    else:
                        print("%5sError: %s %s" %
                              ('', text[ques[1]][i], text[ques[0]][i]))
                        sleep(1.5)
                    break
        sleep(1.5)
        os.system('cls')


def answer_check(ans, ques_ans, quiztype):
    ''' 檢查不同 quiztype 答案是否正確 '''
    if quiztype == 2:
        # '''中文 unicode 範圍 '''
        ch_ans = re.findall(u"[\u4e00-\u9fa5]+", ques_ans)
        return ans in ch_ans
    else:
        return ans == ques_ans


def get_voice(path, filenum):
    path_dir = ''.join(path)
    pre = path[1].split('-')
    # pre_text = '2ku%d' % int(pre[1])
    # if len(pre) > 2:
    #     pre_text += 'u%d' % int(pre[2])
    # pre_text += 'w'
    pre_text = '2ku'+'u'.join(pre[1:])+'w'
    # voicelist = random.sample(range(36), 4)
    # for i in voicelist:
    filename = '%s%s%02d.mp3' % (path_dir, pre_text, filenum+1)
    playsound(filename)


if __name__ == "__main__":
    e_class = 'unit-15-1'
    path = ['e:/2000/', e_class, '/']
    # get_voice(path, 2)
    print("請輸入測試方式： 1 英文作答  2 中文作答 3 聽力測試，英文作答")
    quiztype = int(input(":"))
    os.system('cls')
    get_unit_data(path, quiztype)
