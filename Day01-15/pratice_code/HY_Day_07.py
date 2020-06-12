'''
Item : Python 100 days
Time : 2020/06/11

1.字串結構
2.生成器 : 列表和元組
3.集合
4.字典

以'\' 表示轉義，
'''


# %%

s1 = '\'hello, world !\''
s2 = '\n\\hello , world @\\\n'

# r 表示不轉譯
s3 = r'\'hello, world !\''
s4 = r'\n\\hello , world @\\\n'

print( s1,s2, s3,s4 ,end ='' )

# 字串拼接----------------
# %%

s5 = "hello " * 5

# 連接 s1+s5 字串,成為新的 s1 
s1 += s5 


# 從字串中取出特定位置的值--------
# %%

# 檢查特定字串是否存變數中
# 使用 in 和not in 來判斷

print('ho' in s1) 

# 取出第8個字符
print(s1[8])

# 字串切片-取出一串字串
# 0~12的字符
print(s1[:12])

# 2~結束的字符
print(s1[10:])


# 取出固定規律區間位置的字符
# %%

s6='abcd1234'

# 從第2個起,每跳2個
print(s6[2::2])

# 從第初始起,每3個一跳
print(s6[::3])

# 順序反向排列
print(s6[::-1])

# NOTE「-」逆數(開頭+1,從下一個開始)，選取之間的字串
print(s6[-5:-2])

print(s6[5:-1])

print(s6[2:5])

# 字串計算
# %%

# 計算字符長度
print(len(s6))

# 字首字母轉大寫
print(s5.capitalize())

# 每一單字字首轉大寫
print(s5.title())

# 全部轉大寫
print(s5.upper())


# 找字串
# %%
# 只能找出單一位置, 字串重覆出現，則出現-1
print(s6.find('12'))
print(s5.find('EL'))


# 去除字串的左右空白
print(s3.strip())


# 字串格式化----------------------------
# %%
# 設定 a,b 字串變數

a , b = 5 , 10

# 方法1, 以佔位符來指代
print( '%d * %d = %d' %(a, b, a*b) )

# 方法2, 以f及大括孤來指代
print(f'{a} * {b} = {a*b}')


# 列表--------------------------------
# %%

# list 運算 (* 2 次)
list_1 = [ 1,3,5,7,9,20,34,47,89,103] * 3
list_2 = ['hello world' , 'goodbye', 'goodday'] *2

print(list_1)
print(list_2)

# list 指定位置的字符
print(list_1[4])
print(list_2[4])

# list 逆數
print(list_2[-1])
print(list_2[-3])



# 循環偏歷 for 迴圈
# %%

# NOTE 方法1和2的差異?


# 方法1
# range: list_1 的範圍
# len: 遍歷list_1
# 建立索引
for index in range(len(list_1)):
    print(list_1[index])


# 方法2
# for 循環
for elem in list_1:
    print(elem)



# %%
# enumerate函數處理列表之後再遍歷可以同時獲得元素索引和值

for index , elem in enumerate(list_1):
    print(index, elem)



# 修改、增加、刪除列表中的元素
# %%

# 修改列表中第5個位置的數字
list_1[4] = 16

# 增加列表中元素，在尾部
list_1.append(300) # 只能加一個
list_1 += [500, 700] # 加很多個

# 增加列表中元素，在開頭
list_1.insert(1,400)

# 清除元素,-if 判斷式------------------
# %%
# 清除前個數
print(len(list_1))

# 刪除特定字串或數字
if 5 in list_1:
    list_1.remove(5)

# 刪除指定位置
list_1.pop(2)


# 清除列表中所有元素
list_1.clear()
print(list_1)


# 字串列表----------------------------------
# %%

# 增加
list_2 += ['apple' , 'ipad' ,'mac']

# 切片出來的元素, 另成新列表
list_21 = list_2[2:5]

# 反向列表
list_22 = list_2[::-1]

# 元素排序
list_23 = sorted(list_2)

# 依key的原則排序, key = len(字符串長度)
list_24 = sorted(list_2, key =len)
list_24


# 列表生成器/生成式-------------------------------
# %%

# 數字生成式
list_3 = [ x for x in range (1, 21)]
print(list_3)

# 列表器, X 與 y 兩列不等長, 循環
list_4 = [x + y for x in 'ABCDEFG' for y in '1234567890']
print(list_4)  # A0-A9, B0-B9



# 執行效率
# %%
import sys

# 列表形式
list_5 = [ x ** 2 for x in range(1,1000)]
print(sys.getsizeof(list_5)) # 記憶體效率,查看占有的字數
print(len(list_5))

# list_6 的效率比list_5 好

list_6 = (x ** 2 for x in range(1,1000))
print(sys.getsizeof(list_6)) # 生成器不佔用存儲數據的空間
print(list_6)

for val in list_6:
    print(val)

# 生成器函數 yield------------------------
# %%
def fib (n):
    a, b = 2, 4
    for _ in range(n):
        a, b = b, a+b
        yield a 

def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__' :
    main()




# 元組----------------------
# %%
# 元組/不能修改內容, 在多線程使用較佳
# 元組在創建時間和佔用的空間上面都優於列表


a = ('王大明' , 22 , '高中')

# 取出元組
print(a[0])
print(a[2])

# 遍歷
for b in a:
    print(b)

# 轉列表
c = list(a)
c


# 集合-集合內為唯一值,不重覆
# %%

# NOTE 集合的字面量？
set1 = {1,2,3,3,3,3,3,2,2,2,1,1,1}
print('length = ' , len(set1))

# NOTE 集合的構造器？
set2 = set(range(1,10))
set3 = set((1,2,3,3,3,3,2,2,2,1,4,5))
print(set2, set3)

# NOTE 集合推導式?
set4 = {num for num in range(1,100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 增加集合內元素-以下方式皆能新增
set1.add(4)
set1.add(40)
set2.update([11,12])

# 移除集合內指定的元素
set2.discard(5)
if 4 in set2:
    set2.remove(4)

# 移除集合內第一個位置,不管元素
set2.pop()



# 集合運算
# %%
print(set2, set4)

# 交集 intersetion
print(set2 & set4)
print(set2.intersection(set4))

# 聯集 union
print(set2 | set4)
print(set2.union(set4))

# 集合相減 subtracting, set2 減去交集後剩下的集合
print(set2 - set4)
print(set2.difference(set4))

# 集合相加元素減去集合交集元素(symmetric_difference)
print( set2 ^ set4)
print(set2.symmetric_difference(set4))

# 創建字典
# %%

# 字典存儲任意類型對象，由一個鍵和一個值組成的“鍵值對”
# 字典字面量

dic1 = { '王大明' : 24, '白芳方' : 23 , '林威' : 33}

# 字典構造器
dic2 = dict(one = 1, two = 2, three = 3, four = 4)

# NOTE 用 zip 函數, 兩個序列壓成字典
dic3 = dict(zip(['a','b','c'],'12345'))

# 推導式((key值) num : num**2)
dic4 = {num : num ** 2 for num in range(1,10)}

# 從 key 值找出對應值
print(dic1['白芳方'])

# 用遍歷的方式
for key in dic1:
    print(f'{key} : {dic1[key]}')


# 字典更新
# %%
# 新增字典元素
dic1.update(冷面笑匠 = 44, 小叮噹= 88, 小飛俠 = 55)

# 取出指定元素的值
if '小叮噹' in dic1:
    print (dic1['小叮噹'])

print(dic1.get('小叮噹'))

# 刪除字典內元素
print(dic1.popitem()) # 從尾開始刪
print(dic1.pop('白芳方'))

# 清空字典
dic1.clear()
dic1









