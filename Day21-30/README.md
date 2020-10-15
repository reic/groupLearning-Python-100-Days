# Python 套件使用練習練習

## Day 21 作業系統套件

內件套件 os、shutil 的使用練習。

首先，建立操作練習的範例檔。在工作環境的資料夾下面，建立一個 sample 的資料夾，並於 sample 資料夾中建立 sample/00 ~ 09 等 10 個資料夾，每一個資料夾下面，建立和子資料夾同名的 .dat 檔案

```python
import os

def make_sample_file(path, num=10):
    # 建立檔案處理的範例檔
    for filename in range(num):
        # 建立 sample/00/00.dat ~ sample/09/09.dat 的檔案
        subpath = "./%s/%02d" % (path, filename)
        if not os.path.exists(subpath):
            os.mkdir(subpath)
        with open("./%s/%02d/%02d.dat" % (path, filename, filename), "w", encoding="utf-8") as f:
            f.write("This is the %02d file" % filename)


def main():
    sample_path = "sample"
    if not os.path.exists(sample_path):
        os.mkdir(sample_path)
    make_sample_file(sample_path)


if __name__ == '__main__':
    main()
    pass
```

## Day 21 文字檔的應用

製作氣象局的年均溫查詢資料，使用到 pandas, numpy 協作完成相關的工作。[範例檔 R_Day_22.py]()
