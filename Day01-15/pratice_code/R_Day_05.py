'''
尋找水仙花數： 一個 3 位數，每一位數 的數字的立方和，等於自己
'''
for i in range(100,1000):
    min=i%10
    mid=(i//10)%10
    high=i//100 #得商數
    if i == min**3+mid**3+high**3:
        print(i)


'''
反轉輸入數字
'''
num=int(input("請輸入一個整數： "))

reversed_num=0
while num>0:
    reversed_num=reversed_num*10+num%10
    num //= 10
print(reversed_num)


'''
百錢百雞問題
公雞5元一隻，母雞3元一隻，小雞1元三隻，
用100塊錢買一百隻雞，問公雞、母雞、小雞各有多少隻？
'''
price={"公雞":5,"母雞":3,"小雞":1/3}

imax=int(100 / price["公雞"])
for i in range(imax):
    jmax=(100-price["公雞"]*i)//price["母雞"]
    for j in range(jmax):
        k=int((100-price["公雞"]*i-price["母雞"]*j)/price["小雞"])
        if i+j+k==100:
            print("公雞 %d, 母雞 %d, 小雞 %d"%(i,j,k))


'''
CRAPS 賭博遊戲
兩粒骰子
first： 
  7, 11 點，玩家贏
  2, 3, 12 莊家贏
then:
  玩家： 第一次的點數，玩家贏
  7 點：莊家贏
 '''

from random import randint
money=1000
while money > 0:
    print("剩下資金：", money)
    go_on=False
    while True:
        debt=int(input("請下注："))
        if 0 < debt <=money:
            break
    first=randint(1,6)+randint(1,6)
    print("玩家擲出 %d 點" % first)
    if  first in [7,11]:
        print("玩家贏")
        money+=debt
    elif first in [2,3,12]:
        print("莊家贏")
        money-=debt
    else:
        go_on=True
    gameplay=[]
    while go_on:
        go_on=False
        current=randint(1,6)+randint(1,6)
        
        gameplay.append(current)
        if current==first:
            print("丟出了",gameplay)
            print("玩家贏")
            money+=debt
        elif current==7:
            print("丟出了",gameplay)
            print("莊家贏")
            money-=debt
        else:
            go_on=True
print("你破產了")


'''
生成 黃生數列 的前 20 個數字 
1,1,2,3,5,8
'''
first,second=1, 1
gold_list=[1,1]
i=2
while i<20:
   first,second=second,first+second
   gold_list.append(second)
   i+=1

print(gold_list)

'''
列出 1000 以內的完美數
6=1+2+3，所有因子的總和 = 自己
未活用  因數的特性， 造成太多的遞迴
'''
for i in range(1,10000):
    sum=0
    jmax=i-1
    for j in range(1,jmax):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i,end=" ")
print()


'''
列出質數
'''
import math
for i in range(2,100):
    is_prime=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i,end=" ")
    

