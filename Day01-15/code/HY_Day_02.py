'''
Item : Python 100Dsays
Time : 20200521

變量

'''

# 設變數 a, b 進行計算

a = 123
b = 456
c = "hello world"
d = 1 + 5j
e = True

#-計算 --------------------------------------------
print(a + b)  # 579
print(a - b)  # -333
print(a * b)  # 560888
print(a / b)  # 0.269...

# 檢索變量的類型的函數 type -----------------------

print(type(a+b))  # int
print(type(a-b))  # int
print(type(a*b))  # int 
print(type(a/b))  # float
print(type(c))    # str
print(type(d))    # complex
print(type(e))    # bool


# 變數類型轉換函數--------------------------------

print(" int 轉成  str ")
print(type(str(a+b))) #  將指定的對象轉換成字符串形式，可以指定編碼。
print(type(chr(a+b))) #  將整數轉換成該編碼對應的字符串（一個字符）

print(" 字符串轉換成對應的整數")
# print(type(ord (c))) 無法轉換
# print(type(float(c))) 無法轉換

#-輸入輸出函數---------------------------------------------

# input() # 可輸入字符串
# int()   # 轉成整數
# print() # 輸出

# -----------------------------------------------------

# 輸入值轉成整數
x = int(input('a =  '))
y = int(input('b =  '))

# 佔位符, %d 是整數的佔位符，%f 是小數的佔位符，%% 表示百分號
print('%d + %d = %d' % (a, b, a+b))
print('%d - %d = %d' % (a, b, a-b))

# 運算符
'''
[] [:] : 下標? ,切片
** : 指數
~ + - : 取反位
>> 右移 ? , <<左移
＆ 按位與？
^| 按位異或 按位或
!== 不等於
is, is not 身份運算符
in, not in 成員運算符
not or and 邏輯運算符

'''
# -練習1-華氏溫度轉為攝氏溫度----------------------------------------------

# %1f 浮點佔位符
# {f : 1.f}, {c:1.f}, :1.f 為浮點數

f = float(input(" 請輸入華氏溫度 "))
c = (f-32) / 1.8
print( '%.1f 華氏度  = %1f 攝氏度' % (f,c))


#-練習2-圓半徑計算周長和面積, .2f 2位數浮點值
radius = float(input("請輸入圓的半徑"))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius

print('周長: %.2f' % perimeter)
print('面積: %.2f' % area)


#-練習3 判斷是否閏年---------------------------------------

year = int(input(" 請輸入年份 "))
is_leap = year % 4 == 0 and year % 100 != 0 or \
    year % 400 == 0
print(is_leap)

