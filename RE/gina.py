
#from playsound import playsound
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


def lession_learn(path):
    ''' path 用 list 儲放，合併成 string'''
    text = get_content(''.join(path))
    maxnumber = len(text['english'])
    i = 0
    step = 10
    while i < maxnumber:
        os.system('cls')
        if i+step < maxnumber:
            print("<< status is ( %2d->%2d / %02d ) >>\n" %
                  (i+1, step, maxnumber))
            for j in range(i, i+step):
                print('{:<20s}  {:<20s} '.format(
                    text['english'][j], text['mylanguage'][j]))
                get_voice(path, j)
        else:
            print("<< status is ( %2d->%2d / %2d ) >>\n" %
                  (i+1, maxnumber, maxnumber))
            for j in range(i, maxnumber):
                print('{:<20s}  {:<20s} '.format(
                      text['english'][j], text['mylanguage'][j]))
                get_voice(path, j)
        print("\n 再聽一次請按 a ，任意鍵繼續")
        again = input("> ").lower()
        if again != "a":
            i += step


def lession_quiz(path, quiztype=1):
    ''' path 用 list 儲放，合併成 string'''
    text = get_content(''.join(path))

    maxnumber = len(text['english'])
    quiz = list(range(0, maxnumber))
    if quiztype == 1:
        ques = ['mylanguage', 'english']
    elif quiztype == 2:
        ques = ['english', "mylanguage"]
    else:
        ques = ['mylanguage', 'english']
    print("Quiz start:")
    while len(quiz) > 0:
        i = random.choice(quiz)
        print("\n[[ %2d question left ]]\n" % len(quiz))
        if quiztype != 3:
            print("%s" % text[ques[0]][i])
            ans = input("ans: ").lower().strip()
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
    pre_text = '2ku'+'u'.join(pre[1:])+'w'
    filename = '%s%s%02d.mp3' % (path_dir, pre_text, filenum+1)
    playsound(filename)


if __name__ == "__main__":
    e_class = 'unit-15-1'
    path = ['e:/2000/', e_class, '/']
    status = 0
    while status != 3:
        print("請選擇活動：[ 1:課程學習  2:測試  3:結束 ]")
        status = int(input("> "))
        if status not in [1, 2, 3]:
            continue
        if status == 1:
            lession_learn(path)
        if status == 2:
            # get_voice(path, 2)
            print("請輸入測試方式： 1 英文作答  2 中文作答 3 聽力測試，英文作答")
            quiztype = int(input(":"))
            os.system('cls')
            lession_quiz(path, quiztype)
