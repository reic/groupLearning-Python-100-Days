'''
Item : Python 100Dsays
Time : 20200522

分支結構，if 結構
＃ 縮進層次
＃ 4個空格

'''

# 練習 1-肩平化結構, 分段函數求值, (較優) -------------------------------------

x = float(input("x =  "))
if x > 1 :
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

print( "f (%.2f) = %.2f " % ( x , y ))


# 練習 2 - 嵌套結構 ------------------------------------------------
# 嵌套 : if , elif, else 的內部都可以再出一支分支結構

x = int(input( "x =  "))
if x > 1 :
    y = 3 * x - 5
else :
    if x > -1 :
        y = y + 2
    else :
        y = 5 * x + 3
print( "f (%.2f) = %.2f " % ( x, y))

# 練習 3 - 單位互換-----------------------------------------------------

value = int(input("輸入尺寸: "))
unit = input(" 輸入單位 (in OR cm ): ")

if unit =='in' :
    print(" %f 英吋 = %f 公分" % ( value ,value * 2.54))
elif unit == 'cm' :
    print( "%f 公分 = %f 英吋" % ( value, value / 2.54))

else:
    print("errrr...")


# 練習 4 -數字轉類別 -----------------------------------------------------

score = int(input( " 輸入數字 : "))
if score >= 90 :
    grade = "A"
elif score >= 80 : 
    grade = "B"
elif score >= 70 :
    grade = "C"
elif score >= 


