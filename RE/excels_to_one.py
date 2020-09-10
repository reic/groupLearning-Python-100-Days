import pandas as pd
import numpy as np
import os
# data_df = pd.read_excel("成績中位數.xlsx", sheet_name=["107下", '108上'])
# # data_df['109上']['成績中位數']


def getFileList(filepath):
    allfilelists = os.listdir(filepath)
    return allfilelists


def main():
    filepath = r'data'
    filelists = getFileList(filepath)

    impact_dict = {}
    for filename in filelists[:1]:
    ''' 讀取 A 欄，建立國家名稱'''
    data_df = pd.read_excel(filepath+"/"+filename, usecols=[0], header=None)
    impact_dict.update({"國家": data_df[0][8:].values})

    for filename in filelists:
    ''' 將不同的 xlsx 檔，整理成一個 excel '''
    data_df = pd.read_excel(filepath+"/"+filename, usecols=[1], header=None)
    dic_index = data_df[1][1]
    impact_dict.update({dic_index: data_df[1][8:].values})

    toexcel = pd.DataFrame(impact_dict)
    toexcel.to_excel("output.xlsx")


if __name__ == "__main__":
    main()
    pass
