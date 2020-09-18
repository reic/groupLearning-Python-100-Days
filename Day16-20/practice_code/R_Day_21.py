import os
import shutil as sh


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
    # main()
    # sh.rmtree("sample")
    pass
