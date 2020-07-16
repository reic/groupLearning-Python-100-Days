
import re
import random
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
