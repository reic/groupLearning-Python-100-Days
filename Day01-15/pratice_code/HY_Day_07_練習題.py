
# 練習1-跑馬燈


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











