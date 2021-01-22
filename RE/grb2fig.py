import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


def grb_aggr(files):
    dft = []
    for file in files:
        dft.append(pd.read_excel(file))
    df = pd.concat(dft, ignore_index=True)
    # 輸出合併檔
    df.to_excel(grb_xlsFileName, index=False)
    return df


def year_fig(df, category, figout=0):
    dft = pd.DataFrame(pd.pivot_table(df, index=category, values=[
                       '本期經費(千元)'], aggfunc={'本期經費(千元)': ["sum", "count"]}).to_records())
    dft.rename(columns={"('本期經費(千元)', 'count')": "件數",
                        "('本期經費(千元)', 'sum')": "經費(千元)"}, inplace=True)
    dft.to_excel("{}/{}_件數_經費.xlsx".format(grb_figdata, category), index=False)
    if figout:
        year_fig2(dft[category], dft["件數"], category, "件數")
        year_fig2(dft[category], dft["經費(千元)"], category, "經費(千元)")


def year_fig2(xdata, ydata, xlab, ylab):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.plot(xdata, ydata)
    plt.xlabel(xlab, fontsize=14)
    plt.ylabel(ylab, fontsize=14)
    plt.savefig("{}/{}_{}.png".format(grb_figdata, xlab, ylab))
    plt.show()


# 定義區
# 設定工作目錄
working_dir = "g:/grb/"
# GRB 下載的分檔 excel 在工作目錄下的 子目標位置
grb_dir = "grbdata"
# GRB 分類合併後的檔案名稱，將放在工作目錄
grb_xlsFileName = "grb.xlsx"
# 做圖用的 xlsx 分檔的輸出位置
grb_figdata = "data2fig"

os.chdir(working_dir)
# 取得下載 xlsx 所有檔案名稱
files = ["{}/{}".format(grb_dir, i) for i in os.listdir(grb_dir)]

# 建立 xlsx 輸出檔的存放目錄
try:
    os.mkdir(grb_figdata)
except FileExistsError:
    print("%s 的目標已存在" % grb_figdata)

# 執行 xslx 合併檔案
df = grb_aggr(files)

# 資料處理的工作
# 僅取出 國科會、科技部的計畫
filterlist = ["行政院國家科學委員會", "科技部"]
df = df[df["計畫主管機關"].isin(filterlist)][['計畫中文名稱', '執行單位名稱', '計畫年度', '計畫主管機關', '研究性質', '研究領域', '本期期間(起)', '本期期間(訖)', '本期經費(千元)',
                                        '計畫主持人', '共同/協同主持人', '中文關鍵詞', '英文關鍵詞']]
# 研究領域，僅取出第一個研究領域 分析
df["主研究領域"] = [itm[0] for itm in df["研究領域"].str.split(";").values]
# 執行機構名稱的清理
df["執行單位_new"] = [str(itm[1]).replace("台灣", "臺灣") for itm in df["執行單位名稱"].str.extract(
    r'(國立|.*法人)?(.*大學|.*學院|.*研究院|.*學會|.*學校)').values]
# 輸出整理過的檔案
df.to_excel("{}_整理.xlsx".format(grb_xlsFileName[:-4]), index=False)

# 製作畫圖用的 excel 檔案
year_fig(df, "計畫年度", 1)
year_fig(df, "研究性質", 1)
year_fig(df, ["研究性質", "計畫年度"])
year_fig(df, "研究領域")
year_fig(df, "主研究領域")
year_fig(df, ["主研究領域", "計畫年度"])
year_fig(df, ["研究領域", "計畫年度"])
year_fig(df, "執行單位_new")
