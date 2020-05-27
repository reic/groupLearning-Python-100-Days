
'''

Item : Python 100 days
Time : 20200527

函數和模組

'''
# 輸入M和N ,計算C(M,N), 計算解決方案---------------------------------------------------------

#%%

m = int(input('m =  '))   # 有
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


# 定義函數"def:" ,避免重覆代碼 ---------------------------------------------------------------

# %%


# %%
