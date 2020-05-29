'''

Item : Python 100 days
Time : 20200526

程式邏輯

'''

# 練習 1 -水仙花數----------------------------------------------------
# 設定三位數, 如, 567=5*100+6*10+7*1,  一個三位數, 各個數之立方和等於該數
# 程式邏輯 :依據數字位置, 取不同的值
# %%
 
for num in range(100,1000) :
    high = num // 100      # 百位數 (// 除法, 取整數)
    mid  = num // 10 % 10  # 十位數 (先// 除法, 再 % 取餘數)
    low  = num % 10        # 個位數 (% 取餘數)
    if num == high ** 3 + mid ** 3 + low ** 3 :  # 水仙花數公式
        print(num)



# 練習 2 -整數/字串反轉-------------------------------------------------------
# 原例 - 正整數反轉,迴圈-while
# %%
num = 123
reversed_num = 0 
while num > 0 :
    reversed_num = reversed_num *10 + num % 10
    num //= 10
print(reversed_num)

# 字串反轉-列表
a = ('大家好')       
b = list(a)  # 轉成 list
b.reverse()    # 反轉函式
b = "".join(b) # 合併字串
print(b)

# 倒序切片 - 直接反轉:[::-1] (相反順序操作)
b = a[::-1]
print(b)

# 結合倒序切片, 合併字串 
c = "".join(i for i in a[::-1])
print(c)

# 字串反轉-反向迴圈
# FIXME:反向迭代

num = ("456")
num_1 = ""

for i in num :
    num_1 = i + num_1
print(num_1)


# 索引法
a = "789"
b = ""
for i in range(1, len(a)+1) :
    b = b + a[-i]
print(b) 

# 練習 3 有幾種解決方案, 窮舉法(暴力搜索法)------------------------------------------------------------------------
# 雞兔同籠, 100元可買幾隻雞? 幾隻兔?
# %%
# FIXME: 計算有幾種方案

for i in range (0, 20) :
    for j in range (0, 50) :
        if 4*i + 2*j == 100 :
            print ( '兔: %d 隻 , 雞: %d 隻' % (i,j))
            




