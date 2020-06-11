
'''
Item : Python 100 days
Time : 202005 27/28

函數和模組

'''
# 輸入M和N ,計算C(M,N), 計算解決方案---------------------------------------------------------

#%%

m = int(input('m =  '))   
n = int(input('n =  '))

fm = 1
for num in range ( 1, m + 1 ) :
    fm *= num                       # *= 相乘的運算符兩側的值 (fm * num)

fn = 1
for num in range(1, n + 1 ) :
    fn *= num

fm_n = 1
for num in range( 1, m - n + 1) :
    fm_n *= num

print(fm // fn // fm_n)


# 自行定義函數"def:" ,避免重覆代碼 ---------------------------------------------------------------
# %%
# 自訂函數名稱 abc 

def abc(num) : # 求
    result = 1
    for i in range( 1, num + 1) :
        result *= i
    return result

# 直接調用已經定義好的函數

m = abc(int(input(" ")))
n = abc(int(input(" ")))

print( m , n)

# 函數運用--------------------------------------------------------------------------------------

# %%

from random import randint

def roll ( n = 2) : # 內定值為2個骰子
    total = 0 
    for _ in range(n): # TODO
        total += randint(1,6)  # 骰子6面,隨機(1~6)
    return total

# 內定值
print(roll())
# 3個骰子 
print(roll(3))


# 三個變數, 相加-----------------------------
# %%

def add ( a=0, b=0, c=0 ):
    return a + b + c

# a,b,c 內定值
print(add())

# a,b 兩個變數
print(add(3,5))

# a,b,c 三個變數
print(add(5,7,9))


# 模組管理----------------------------------
# %%

'''
指定執行函式

__name__   # 有被定義模組的名字 , __'main'__ #  直接執行該模組

'''

if __name__ == '__main__':
 
# %%
import HY_module1 as m1

print(foo())







    
# %%

