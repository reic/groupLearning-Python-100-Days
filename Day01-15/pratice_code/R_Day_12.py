'''
valid email, password rules
'''

import re


def re1():
    # username = input('請輸入帳號(只能為大小寫英文、數字，6-20碼) username：')
    password = input('請輸入包含大小英文、數字、符號，至少8碼：')

    # m1 = re.match(r'^[0-9A-Za-z]{6,20}$', username)
    # if not m1:
    #     print('無效的使用者名稱')
    m2 = re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', password)
    if not m2:
        print("無效的密碼")
    # if m1 and m2:
    #     print("登入成功")
    else:
        print("創新密碼")


def re2():
    # 創建正則表達式對象 使用了前瞻和回顧來保證手機號前後不應該出現數字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情說8130123456789遍，我的手機號是13512346789這個靚號，
    不是15600998765，也是110或119，王大錘的手機號才是15600998765。
    '''
    # 查找所有匹配並保存到一個列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------華麗的分隔線--------')
    # 通過迭代器取出匹配對象並獲得匹配的內容
    for temp in pattern.finditer(sentence):
        # print(temp.group())
        print(temp.group())
    print('--------華麗的分隔線--------')
    # 通過search函數指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


def mobile_numbers():
    sentence = '''我的手機是 0958001925，辦公室的電話是 0227377888，
    其它的人手機有 0937216314，0921123456，
    高公局熱鍵 1968'''
    pattern = re.compile(r'(?<=\D)(09\d{8})(?=\D)')
    mylist = re.findall(pattern, sentence)
    print(mylist)
    for match in re.finditer(pattern, sentence):
        sStart = match.start()
        sEnd = match.end()
        # complete match
        sGroup = match.group()
        print("Match %s found at [%s,%s]" % (sGroup, sStart, sEnd))
    m = pattern.search(sentence)
    while m:
        print(m.group(), m.end())
        m = pattern.search(sentence, m.end())


def word_filter():
    sentence = "你是個北七啊。幹什麼東西吃，Fuck is a action."
    avoid_word = '北七|fuck|shit|幹|你娘'
    filter_sentence = re.sub(avoid_word, "*", sentence, flags=re.I)
    print(filter_sentence)


def slip_sentence():
    poem = '窗前明月光，疑是地上霜。舉頭望明月，低頭思故鄉。'
    sentence_list = re.split(r'[，。,.]', poem)
    if ''in sentence_list:
        sentence_list.remove("")
    print(sentence_list)


if __name__ == "__main__":
    # slip_sentence()
    # string = "Hello"
    # print(string[1:]+string[0:1])
    # print(''.join(string[index] for index in range(len(string)-1, -1, -1)))
    mobile_numbers()
