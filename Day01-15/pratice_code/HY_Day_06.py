
'''
Item : Python 100 days
Time : 202005 27/28, 06/10


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


# 參數有默認值, 相加-----------------------------
# %%

def add ( a=0, b=0, c=0 ):
    return a + b + c

# a,b,c 內定值
print(add())

# a,b 兩個變數
print(add(3,5))

# a,b,c 三個變數
print(add(5,7,9))

# 可變參數
# %%

# 參數前面的* 表示 args 為可變參數

def add (*args) :   
    total = 0
    for val in args :
        total += val
    return total

# 調用 add 函數可傳入0 個以上(多個)參數

print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4))



# 模組管理----------------------------------

'''
模組:
1. 管理相同名稱的函數，避免執行時造成衝突
相同名稱的函數要存在不同的模組中，
方式: from 模組名稱 import 函數名稱(指定模組中的函數)

2. 指定函數進行執行代的動作
在 if 條件下的代碼並不會被執行的，只會直接執行"__main__"。的模組
__name__ 也是一種變數，定義模組的名字 , __'main'__ #  直接執行該模組

'''

# 引入函數-方法1
# %%
from HY_module1 import foo
foo()


from HY_module2 import foo
foo()


# 方法1相同，僅出現後面函數結果
# %%

from HY_module1 import foo
from HY_module2 import foo

foo()


# 引入函數-方法2，兩個函數的值皆能返回
# %%

import HY_module1 as m1
import HY_module2 as m2 

m1.bar()
m2.bar()



# 在模組內執行代碼 # NOTE
# %%

import HY_module3

#不會執行模塊中if條件成立時的代碼,
# 因為模組的名字是module3 而不是__main__




# 練習1 - 求最大公約數
# %%

def gcd(x,y) : 
    ( x , y ) = ( y, x ) if x > y else ( x , y )
    for factor in range ( x , 0 , -1):
        if x % factor == 0 and y % factor ==0:
            return factor



# 求最小公倍數
def lcm( x ,y ):
    return x*y // gcd (x,y)


# 變量應用-函數內的函數
# %%

'''
# 全局變量
在if中定義了一個變量a，這是一個全局變量（global variable），屬於全局作用域，因為它沒有定義在任何一個函數中。

# 局部變量
foo函數中我們定義了變量b，這是一個定義在函數中的局部變量（local variable），屬於局部作用域，
foo函數內部的bar函數來說，變量b屬於嵌套作用域，在bar函數中我們是可以訪問到它的。

c 為局部作用域，在bar函數之外是無法訪問的
'''

# 局部變量
def foo_1():
    b = "hello"
    
    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    bar()

# 全域變量
if __name__ == '__main__' : 
    a = 100
    foo()



# %%

def main():
    pass

if __name__ == '__main__' :
    main()

# %%
