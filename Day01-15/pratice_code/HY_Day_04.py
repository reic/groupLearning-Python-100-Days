
# //TODO

'''

Item : Python 100Ds days
Time : 20200525

循環結構:
    1. for...in..: 用在確定執行次數、對容器進行迭代
    2. while : 用在不確定執行次數 , 搭配布林運算, True = go , False = pass

'''

''' 
# range 寫法 #
range (101) : 0~100
range ( 1, 101 ): 1~100
range ( 1, 101 ,2 ) : 1~100, ,奇數, 每 2 個一次, 順向
range ( 100, 0, -2 ) : 100~0, 偶數, 每 2 個一次, 逆向

'''

# 練習 1 -- 計算1～100 ----------------------------------------------

sum = 0 # 起始值
for i in range(101):  # 計算100次
    sum += i          # 每計算一次疊加一次
print(sum)


# 練習 2-- 偶數求和 ----------------------------------------------------

sum = 0 
for i in range ( 2, 101, 2 ) :  # 起始 2, 終止 101 , 每 2 次計算
    sum += i 
print(sum)

# 加入分支結構 if 

sum = 0 
for j in range ( 1, 101):
    if j % 2 == 0 :  # if j/2 = 0 就跳過
        sum += j
print(sum)


# 練習 3 ---# 1~200 之間,隨機數字------------------------------------------------------------
# break, 中止,跳出循環
# coutinue, 放棄, 繼續另一循環 

# import random

# # 隨機數字答案
# answer = random.randint(1,200)

# # 計算猜測的次數
# counter = 0

# while True:
#     counter += 1 # 當判斷為True 時, 加計一次
#     number = int(input(" 輸入數字 "))
#     if number < answer :
#         print (" 大一點 ")
#     elif number > answer : 
#         print (" 小一點 " )
#     else:
#         print (" 正確 ")
#         break # 跳出迴圈
# # 計算次數
# print(" 總共猜 %d 次 " % counter)

#-練習 4 --九九乘法表（循環 + 嵌套）--------------------------------------------------------
# %d 整數
# end "\t": 在結尾不換行,加入 tab

for i in range( 1 , 10 ):
    for j in range( 1, i + 1 ) : 
        print( " %d * %d = %d " % ( i , j, i*j ) ,end = "\t") 
    print() # 列印 i 循環的結果 
    
# 練習 5--循環控制-----------------------------------------------   
# 同一循環後才換行

for i in range(10):
    for j in range( i + 1 ):
        print("*" , end = "")
    print()

# 
for i in range(10, 0 , -1) :
    for j in range ( i - 1 ):
        print("*", end = "")
    print()
    
