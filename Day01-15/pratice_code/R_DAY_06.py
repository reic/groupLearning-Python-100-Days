'''
計算 C 的 m 取 n
m=7 n=3
'''

# m=int(input("m = "))
# n=int(input("n = "))
# fm=1
# fn=1
# fm_n=1
# for num in range(1,m+1):
#     fm*=num
# for num in range(1,n+1):
#     fn*=num
# for num in range(1,m-n+1):
#     fm_n*=num
# print(fm//fn//fm_n)

# '''
# 運用函數，完成上面的例子
# '''

# def fac(num):
#     # facterial 求階乘
#     result=1
#     for i in range(1,num+1):
#         result*=i
#     return result
# m=7
# n=3
# print(fac(m)//fac(n)//fac(m-n))

'''
課程的 functioin 範列 
'''
# from random import randint
# def roll_dice(n=2):
#     # 搖骰子
#     total=0
#     for _ in range(n):
#         total+=randint(1,6)
#     return total

# def add(a=0,b=0,c=0):
#     return a+b+c

# print(roll_dice())
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3,7,8,2))
# 傳遞參數時可以不按照設定的順序進行傳遞
# print(add(c=50, a=100, b=200))

# def add(*num):
#     total=0
#     for i in num:
#         total+=i
#     return total

'''
函數重複定義，會執行最後定義的函數
'''
# def foo():
#     print("hello")
# def foo():
#     print("goodbye")
# foo()

'''
透過 模組，解決 同名數定義的 偵錯問題
'''
# from R_DAY_06_m1 import foo
# foo()
# from R_DAY_06_m2 import foo
# foo()

'''
透過 import .. as 
用別名區分函數
'''
# import R_DAY_06_m1 as mr1
# import R_DAY_06_m2 as mr2
# mr1.foo()
# mr2.foo()

# import R_DAY_06_m3

'''
最大公因數(gcd)/最小公倍數(lcm)的函數
'''
# def gcd(x,y):
#     (x,y)=(y,x) if x>y else (x,y)
#     for facter in range(x,0,-1):
#         if x%facter==0 and y%facter==0:
#             return facter
# def lcm(x,y):
#     return x*y/gcd(x,y)

'''
撰寫回文數 11 121 1221
12345 , 54321
# '''
# def is_palindrome(num):
#     temp=num
#     total=0
#     while temp>0:
#         total=total*10+temp%10
#         temp//=10
#     return total==num

'''
撰寫質數函數
'''
# def is_prime(num):
#     for facter in range(2,int(num**0.5)+1):
#         if num%facter==0:
#             return False
#     return True if num!=1 else False

'''
判斷是否為回文、質數
透過 __name__="__main__" 的判斷，是為了讓這一個 py 裡面撰寫的函數，可以被其它的程式使用
但是 py 程式的主要工作或執行的程式碼，不會因 import 的時候執行
'''
# if __name__ =='__main__':
#     num=int(input("請輸入正整數： "))
#     if is_palindrome(num) and is_prime(num):
#         print(" %d 是回文質數 " % num)
#     else:
#         print("%d 不是回文質數"%num)

'''
變數的作用範圍
'''
# def foo():
#     b = 'hello'
#     # Python中可以在函数内部再定义函数
#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)
#     bar()
#     # print(c)  # NameError: name 'c' is not defined
# if __name__ == '__main__':
#     a = 100
#     # print(b)  # NameError: name 'b' is not defined
#     foo()

# def foo():
#     a = 200
#     print(a)  # 200
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 100

# def foo():
#     global a # 將變數 a 升絡為全域
#     a = 200
#     print(a)  # 200


# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 200

# def a():
#     i = 1
#     def b():
#         i = 2
#         def c():
#             nonlocal i
#             i = 3

#         c()
#         print('b:', i)

#     b()
#     print('a:', i)

# if __name__=='__main__':
#     a()

'''
開始執行 python 的程式
'''
def main():
    # Todo: Add your code here
    pass # 一個占位用。先定義一個函數，但是沒有內容，在 python 2 必要， python 3 可以省略

if __name__=="__main__":
    main()