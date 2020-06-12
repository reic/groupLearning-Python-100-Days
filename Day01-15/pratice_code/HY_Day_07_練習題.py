
# 練習1-跑馬燈
# %%

import os
import time

def main():
    content = "文字跑馬燈...."
    # 迴圈
    while True: # 檢查迴圈是否為True
        # 清理螢幕上的輸出
        os.system('cls') 
        print(content)
        # 休眠 100 sec
        time.sleep(0.1)
        #從下一個字開始)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()


# %%

def generate_code(code_len=4):
    import random
    # 產生 code_table
    code_table="".join([chr(65+i) for i in range(26)]) #產生 A-Z
    code_table+="".join([chr(97+i) for i in range(26)]) #產生 a-z
    code_table+="".join([str(i) for i in range(10)])     #產生 0-9
    last_pos=len(code_table)-1
    code=''
    for _ in range(code_len):
        code+=code_table[random.randint(0,last_pos)]
    return code

print(generate_code(5))







# %%

def generate_code1(code_len=4):
    import random
    code=''
    for _ in range(code_len):
        type_char=random.randint(1,3) # 1 數字， 2 大寫, 3 小寫
        if type_char==1:
            code+=str(random.randint(0,9))
        elif type_char==2:
            code+=chr(64+random.randint(1,26)) #char(65) 為 A
        else:
            code+=chr(96+random.randint(1,26)) #char(97) 為 a
    return code


print(generate_code1(5))
