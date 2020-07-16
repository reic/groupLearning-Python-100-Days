
from playsound import playsound
from time import sleep
import re
import random


def get_unit_data():
    pattern = r'=(.*)\n'
    files = ["english.txt", 'mylanguage.txt', 'syllable.txt']
    text = {}
    for filename in files:
        with open("/unit-01/"+filename, 'r', encoding='utf_16_le') as f:
            text[filename[:-4]] = re.findall(pattern, f.read())
        # content = [item.strip() for item in english_text.split("&")]
        # content[0] = content[0].strip('\ufeff')

    maxnumber = len(text['english'])
    # for i in range(maxnumber):
    #     print(" %20s  %20s \t %s" %
    #           (text['english'][i], text['syllable'][i], text['mylanguage'][i]))

    quiz = random.sample(range(0, maxnumber), 4)
    print("Quiz start:")
    for i in quiz:
        ans = input(" %s ： " % text['mylanguage'][i]).lower().strip()
        if ans == text['english'][i]:
            print("\t 答對了。")
        else:
            print("\t Error： Answer is: %s " % text['english'][i])


def voice_test():
    path = '/unit-01/'
    pre = '2ku1w'
    voicelist = random.sample(range(36), 4)
    for i in voicelist:
        filename = '%s%s%02d.mp3' % (path, pre, i+1)
        playsound(filename)
        sleep(1)
