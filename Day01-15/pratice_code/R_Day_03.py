'''
使用者驗證
'''
username=input('請輸入使用者名稱:')
password=input('請輸入密碼:')
# username=admin password=123456 則成功
if username=='admin' and password =='123456':
    print("登入")
else:
    print('帳號/密碼錯誤')

"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
# # 如何列印出，題目呢？
# # # 分段函數求值
x=float(input('x = ')) 
if x>1:
    y=3*x-5
else:
    if x>=-1:
        y=x+2
    else:
        y=5*x+3


# # 扁平化的時候，比較難理解
x=float(input('x = ')) 
if x>1:
    y=3*x-5
    equ='3x-5'
elif x>=-1:
    y=x+2
    equ='x+2'
else:
    y=5*x+3
    equ='5x+3'

# print('f(%.2f)=%s= %.2f' %(x,equ,y))

# #  inch and cm 轉換
# # 撰寫程式說明檔
unit=input('請輸入單位 cm / in :')
value=float(input("請輸入長度："))
if unit=='in':
    print('%f 英寸 = %f 公分' % (value, value*2.54))
elif unit=='cm' or unit=='公分':
    print('%f 公分 = %f 英寸' % (value, value/2.54))
else:
    print("請輸入有效單位")

# 百分制成績 換成等鈒制
'''
90 以上 A
80 =< score < 90 => B
70 =< score < 80 => C
60 =< score < 70 => D
score < 60=>E
'''
score=int(input('請輸入成續： '))
if score >=90:
    grade ='a'
elif score >=80:
    grade='b'
elif score >=70:
    grade='c'
elif score >=60:
    grade='d'
else:
    grade='e'

# print('%d 對應的等級為 %s' %(score,grade))

"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

知道三個邊， 海龍公式：  s=周長/2  面積= sqrt(s*(s-a)*(s-b)*(s-c))
"""
print("請輸入三角形的 a, b, c 三個邊")
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
if a+b>c and b+c>a and c+a>b:
    print("周長： %f" % (a+b+c))
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("面積： %f" % (area))
else:
    print("這三個邊不能構成三角型")