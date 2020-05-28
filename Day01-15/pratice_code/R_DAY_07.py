# s1='hello world!'
# s2="hello world!"
# s3="""
# hello,
# world!
# """
# print(s1,s2,s3,end="")
# print()

# '''
# 跳脫符號說明
# '''
# s1='\'hello world\''
# s2='\n\\hello world!\\\n'
# print(s1,s2,end='')


# '''
# 8進位、16進位制、 Unicode 編碼
# '''
# s1='\141\142\143\x61\x62\x63'
# s2='\u9a86\u660a'
# print(s1,s2)

# '''
# 在字串 最前面加上 r ，讓 \ 不轉譯
# '''
# s1=r'\'hello, world!\''
# s2=r'\n\\hello, world!\\\n'
# print(s1,s2)

# '''
# python 的特殊用法
# '''
# s1='hello ' *3
# print(s1)
# s2='world'
# s1+=s2
# print(s1)
# print('ll' in s1)
# print('good' in s1)

# str2='abc123456'
# #從字串取出指定位置的
# print(str2[2]) # c
# print(str2[2:5]) # c12
# print(str2[2:]) # c123456
# print(str2[2::2]) # c246
# print(str2[::2]) #ac246
# print(str2[::-1]) #654321cba
# print(str2[-3:-1]) #45

# '''
# python 的字串處理
# '''
# str1='hello, world!'
# print(len(str1)) #len 計算文字的長度
# print(str1.capitalize()) # 字串首字大寫
# #字串每個單字字母大寫
# print(str1.title())
# # 所有單字字母大
# print(str1.upper())
# # 找到 字串的位置
# print(str1.find('or'))
# print(str1.find('shit')) # 當找不到，會出現 -1 or False
# # index 和 find 相似，但找不到會出現 error
# # print(str1.index('or'))
# # print(str1.index('shit'))
# # startswith, endswith 檢查開頭或結尾
# print(str1.startswith("He"))
# print(str1.startswith("he"))
# print(str1.endswith("!"))

# # 字元填空
# print(str1.center(50,"*"))
# print(str1.rjust(50,' '))

# # 檢查是字串組成
# # isdigit 是否為數字
# # isaplpha 是否為文字
# # isalnum 是否為數字或文字
# # strip 修剪左右空白
# str2='abc123456'
# print(str2.isdigit())
# print(str2.isalpha())
# print(str2.isalnum())
# str3='   reic@123.com'
# print(str3)
# print(str3.strip())

# '''
# print 格式化輸出
# '''
# a,b=5,10
# print("%d * %d = %d"%(a,b,a*b))
# print('{0} * {1} = {2}'.format(a,b,a*b))
# #python 3.6 以後的新用法
# print(f'{a} * {b} = {a*b}')

'''
list 的介紹
enumerate: for index,item in enumerate(list)
'''
# list1 = [1, 3, 5, 7, 100]
# print(list1) # [1, 3, 5, 7, 100]
# # 乘号表示列表元素的重复
# list2 = ['hello'] * 3
# print(list2) # ['hello', 'hello', 'hello']
# # 计算列表长度(元素个数)
# print(len(list1)) # 5
# # 下标(索引)运算
# print(list1[0]) # 1
# print(list1[4]) # 100
# # print(list1[5])  # IndexError: list index out of range
# print(list1[-1]) # 100
# print(list1[-3]) # 5
# list1[2] = 300
# print(list1) # [1, 3, 300, 7, 100]
# # 通过循环用下标遍历列表元素
# for index in range(len(list1)):
#     print(list1[index])
# # 通过for循环遍历列表元素
# for elem in list1:
#     print(elem)
# # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
# for index, elem in enumerate(list1):
#     print(index, elem)

'''
list 的元素添加和移除
'''
# list1 = [1, 3, 5, 7, 100]
# # 添加元素
# list1.append(200) # 添加在最後面
# list1.insert(1, 400) # 在指定的位置，添加一筆資料
# # 合并两个列表
# # list1.extend([1000, 2000])
# list1 += [1000, 2000]
# print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
# print(len(list1)) # 9
# # 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
# if 3 in list1:
# 	list1.remove(3)
# if 1234 in list1:
#     list1.remove(1234)
# print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# # 从指定的位置删除元素
# # pop() 不代任何輸入時，預設刪除最後一筆
# list1.pop(0)
# list1.pop(len(list1) - 1)
# print(list1) # [400, 5, 7, 100, 200, 1000]
# # 清空列表元素
# list1.clear()
# print(list1) # []

# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# # sorted函数返回列表排序后的拷贝不会修改传入的列表
# # 函数的设计就应该像sorted函数一样尽可能不产生副作用
# list3 = sorted(list1, reverse=True)
# # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
# list4 = sorted(list1, key=len)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# # 给列表对象发出排序消息直接在列表对象上进行排序
# list1.sort(reverse=True)
# print(list1)

'''
生成式和生成器
'''
# f=[ x for x in range (1,10)]
# print(f)
# f=[x+y for x in "ABCDE" for y in'12345']
# print(f)

# 透過列表儲生成器
# import sys
# f=[x**2 for x in range(1,1000)]
# print(sys.getsizeof(f))
# print(f) # 生成式
# # 下列為 code 創造，儲存的代碼，而不是值
# # 但是每次在取用的時候，需要執行 1
# # 可以節省儲存的空間，但是需要花費額外的時間
# f=(x**2 for x in range(1,1000)) #生成器
# print(sys.getsizeof(f))
# print(f)
# for val in f:
#     print(val)

# '''
# 通過 yield 關鍵字，將一個階通函數改為生成器函數
# '''
# def fib(n):
#     a,b=0,1
#     for _ in range(n):
#         a,b=b,a+b
#         yield a
# def main():
#     for val in fib(10):
#         print(val)

# if __name__=="__main__":
#     main()

# '''
# 元組 和 列表
# '''
# # 定义元组
# t = ('骆昊', 38, True, '四川成都')
# print(t)
# # 获取元组中的元素
# print(t[0])
# print(t[3])
# # 遍历元组中的值
# for member in t:
#     print(member)
# # 重新给元组赋值
# # t[0] = '王大锤'  # TypeError
# # 变量t重新引用了新的元组原来的元组将被垃圾回收
# t = ('王大锤', 20, True, '云南昆明')
# print(t)
# # 将元组转换成列表
# person = list(t)
# print(person)
# # 列表是可以修改它的元素的
# person[0] = '李小龙'
# person[1] = 25
# print(person)
# # 将列表转换成元组
# fruits_list = ['apple', 'banana', 'orange']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)

# '''
# 集合  { }，裡面的元素是唯一
# 創建的方法 = { } or var=set(元組, list, 集合)
# { 可以用成生器 } = { num for num in range(1,100) if num%3==0 or num%5==0}
# 集合的方法 add
# '''
# # 创建集合的字面量语法
# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
# print('Length =', len(set1))
# # 创建集合的构造器语法(面向对象部分会进行详细讲解)
# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 2, 1))
# print(set2, set3)
# # 创建集合的推导式语法(推导式也可以用于推导集合)
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)
# set1.add(4)
# set1.add(5)
# set2.update({11, 12})
# set2.discard(5)
# if 4 in set2:
#     set2.remove(4)
# print(set1, set2)
# # print(set3)
# set3.pop()
# print(set3)
# print()

# # 集合的交集、并集、差集、对称差运算
# print(set1 & set2)
# # print(set1.intersection(set2))
# print(set1 | set2)
# # print(set1.union(set2))
# print(set1 - set2)
# # print(set1.difference(set2))
# print(set1 ^ set2)
# # print(set1.symmetric_difference(set2))
# # 判断子集和超集
# print(set2 <= set1)
# # print(set2.issubset(set1))
# print(set3 <= set1)
# # print(set3.issubset(set1))
# print(set1 >= set2)
# # print(set1.issuperset(set2))
# print(set1 >= set3)
# # print(set1.issuperset(set3))

'''
字典
'''
# # 创建字典的字面量语法
# scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# print(scores)
# # 创建字典的构造器语法
# items1 = dict(one=1, two=2, three=3, four=4)
# # 通过zip函数将两个序列压成字典
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# # 创建字典的推导式语法
# items3 = {num: num ** 2 for num in range(1, 10)}
# print(items1, items2, items3)
# # 通过键可以获取字典中对应的值
# print(scores['骆昊'])
# print(scores['狄仁杰'])
# # 对字典中所有键值对进行遍历
# for key in scores:
#     print(f'{key}: {scores[key]}')
# # 更新字典中的元素
# scores['白元芳'] = 65
# scores['诸葛王朗'] = 71
# scores.update(冷面=67, 方启鹤=85)
# print(scores)
# if '武则天' in scores:
#     print(scores['武则天'])
# print(scores.get('武则天'))
# # get方法也是通过键获取对应的值但是可以设置默认值
# print(scores.get('武则天', 60))
# # 删除字典中的元素
# print(scores.popitem())
# print(scores)
# print(scores.popitem())
# print(scores)
# print(scores.pop('骆昊'))
# print(scores)
# # 清空字典
# scores.clear()
# print(scores)

'''
在營幕顯示跑馬燈文字
顯示文字：群體的 Python 100 天學習記錄......
'''

def prac1():
   import os
   import time
   content="群體的 Python 100 天學習記錄......" 
   while True:
       os.system('cls') # clear console
       print(content.center(150))
       content=content[1:]+content[0]
       time.sleep(0.2) #sleep 的變數為秒數

'''
設計一個由數字和文字組成的 驗證碼，可以指定驗證碼長度
'''
def generate_code(code_len=4):
    import random
    # 產生 code_table
    code_table="".join([chr(65+i) for i in range(26)]) #產生 A-Z
    code_table+="".join([chr(97+i) for i in range(26)]) #產生 a-z
    code_table+="".join([str(i) for i in range(10)])     #產生 0-9
    last_pos=len(code_table)-1
    code=''
    for _ in range(code_len):
        code+=code_table[random.randint(0,last_pos)]
    return code
def generate_code1(code_len=4):
    import random
    code=''
    for _ in range(code_len):
        type_char=random.randint(1,3) # 1 數字， 2 大寫, 3 小寫
        if type_char==1:
            code+=str(random.randint(0,9))
        elif type_char==2:
            code+=chr(64+random.randint(1,26)) #char(65) 為 A
        else:
            code+=chr(96+random.randint(1,26)) #char(97) 為 a
    return code

'''
設定一個取得 檔案附檔名的函數
'''
def get_suffix(filename, has_dot=False):
    # has_dot 表 return 是否需要帶 .
    pos=filename.rfind(".")
    if pos==-1:
        return ''
    index= pos if has_dot else pos+1
    return filename[index:]

'''
取得數列中最大的兩個數
'''
def get_max2(x):
    m1,m2=x[0],x[1] 
    for itm in x:
        if itm > m1:
            m1,m2=itm,m1
        elif itm > m2:
            m2=itm
    return m1,m2

'''
計算 輸入年月日，是一年的第幾天
'''
def days_in_year(year=2020,month=1,day=1):
    def is_leap_year(year):
        return (year%4==0 and year%100 !=100) or year%400 ==0
    days_in_month= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days=day
    for i in range(month-1):
        days+=days_in_month[i]
    if is_leap_year(year) and month >2:
        days+=1
    return days
'''
範列程式
'''
def which_day(year, month, date):
    def is_leap_year(year):
        return (year%4==0 and year%100 !=100) or year%400 ==0
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

'''
計算 巴斯卡三角型
   1
  1 1
 1 2 1
1 3 3 1
'''
def pascal():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [1] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

'''
案例1：大樂透 1-49 號，開獎。  6 個數字 + 特別號
randint, sample
'''

'''
案例 2：約瑟夫環
《幸運的基督徒》
有15個基督徒和15個非基督徒在海上遇險，為了能讓一部分人活下來不得不將其中15個人扔到海裡面去，有個人想了個辦法就是大家圍成一個圈，由某個人開始從1報數，報到9的人就扔到海裡面，他後面的人接著從1開始報數，報到9的人繼續扔到海裡面，直到扔掉15個人。由於上帝的保佑，15個基督徒都倖免於難，問這些人最開始是怎麼站的，哪些位置是基督徒哪些位置是非基督徒。
'''

if __name__=="__main__":
    pass
    # main()
    # prac1()
    # print(generate_code())
    # print(generate_code1(5))
    # print(get_suffix("test.bat","a"))
    # print(get_suffix("test.bat"))
    # max1,max2=get_max2([1,-3,5,2,11,7,9,23])
    # print(max1,max2)
    # print(days_in_year(2000, 11, 28))
    # print(which_day(2000, 11, 28))
    # print()
    # print(days_in_year(1981, 12, 31))
    # print(which_day(1981, 12, 31))
    # pascal()
    # print([[]]*4)
