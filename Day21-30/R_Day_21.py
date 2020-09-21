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


def create_batch(base_dir, target_dir, batchfilename):
    if os.path.isfile(batchfilename):
        os.remove(batchfilename)
    with open(batchfilename, 'a+', encoding='utf=8') as f:
        f.write('if not exist output\\ mkdir output\n')
        for itm in os.walk(base_dir):
            midtext = ''
            if len(itm[2]) == 0:
                continue
            if len(itm[1]) != 0:
                midtext = "%s_" % itm[1][0]
            for filename in itm[2]:
                f.write('move "%s\\%s" "%s\\%s%s"\n' %
                        (itm[0], filename, target_dir, midtext, filename))
    pass


def main():
    sample_path = "sample"  # 檔案的位置
    target_path = 'output'  # 將檔案移動到的目標區域
    batchfilename = 'output.bat'  # batchfilename 在 cmd 下執行的
    if not os.path.exists(sample_path):
        os.mkdir(sample_path)
    # make_sample_file(sample_path)
    # 建立 batch file in UTF-8
    create_batch(sample_path, target_path, batchfilename)
    # 若是檔案名稱有中文，建議再用 notepad 將 batch file 轉成 ANSI 的編碼


if __name__ == '__main__':
    main()
    # sh.rmtree("sample")
    pass
