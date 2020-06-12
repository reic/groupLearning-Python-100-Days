# print 函數的用法
# range 函數的用法
# import random ，用 random 產生隨機整數
# for in 的循環
# while 的循環

'''
求 1 ~ 100 的和
'''
import random
from math import sqrt


def sum1


sum = 0
# range range(1,101)   1<=x<101
for x in range(0, 101):
    sum += x

print(sum)
for x in range(0, 1):
    print(x)


'''
求 1~100 的偶數合
'''
sum = 0
for x in range(2, 101, 2):
    sum += x
print("運用 range 的 step 實現， sum = %d" % (sum))

for x in range(101):
    if x % 2 == 0:
        sum += x
print("分支結構 + 循環結構實現， sum =%d" % (sum))


'''
猜數字遊戲，
系統隨機給一個 1~100數的整數，玩家輸入自己猜的數字
會提示 數是太大，還是數字太小
如果玩家猜中數字，會告訴使用者猜幾次
'''
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('請猜一個數字： '))
    if number < answer:
        print("大一點")
    elif number > answer:
        print("小一點")
    else:
        print("答案是 %d , 猜對了" % (answer))
        break
print("你共猜了 %d 次" % (counter))
if counter > 7:
    print("你比平常人花更多的次數才成功")


'''
輸出一個 99乘法表
'''
# print 函數的用法
for i in range(2, 10):
    for j in range(2, 10):
        print("%dx%d=%2d" % (i, j, i*j), end="\t")
    print()


'''
輸入一個正整數，判斷是不是質數
'''
num = int(input('請輸入一個正整數： '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print("%d 是質數" % num)
else:
    print("%d 不是質數" % num)


'''
輸入 2 個正整數，計算最大公因數，最小公倍數
'''
x = int(input("x= "))
y = int(input("y= "))
if x > y:
    x, y = y, x  # 變數值交換技術

for facter in range(x, 0, -1):
    if x % facter == 0 and y % facter == 0:
        print('%d 和 %d 的最大公因數為 %d' % (x, y, facter))
        print('%d 和 %d 的最小公倍數為 %d' % (x, y, x*y/facter))
        # 最小公倍數 = 兩個數相乘 / 最大公因數
        break

'''
圖形列印
'''


row = int(input('請輸入行數： '))
for i in range(row):
    for _ in range(i+1):
        print("*", end='')
    print()

row = int(input('請輸入行數： '))
for i in range(row):
    for j in range(row):
        if j < row-i-1:
            print(" ", end='')
        else:
            print("*", end='')
    print()

row = int(input('請輸入行數： '))
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()

# 我撰寫的方法
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")
    print()

for i in range(1, 7):
    for j in range(6, 1, -1):
        if j > i:
            print(" ", end='')
        else:
            print("*", end='')
    print("")

for i in range(1, 6):
    for j in range(1, 6-i):
        print(" ", end='')
    for k in range(1, 2*i):
        print("*", end='')
    print()
