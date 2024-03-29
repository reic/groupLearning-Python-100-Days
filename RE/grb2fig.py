import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import concurrent.futures


def grb_aggr(files, grb_xlsFileName):
    dft = []
    for file in files:
        dft.append(pd.read_excel(file))
    df = pd.concat(dft, ignore_index=True)
    # 輸出合併檔
    df.to_excel(grb_xlsFileName, index=False)
    return df


def year_fig(df, category, grb_figdata, figout=0):
    dft = pd.DataFrame(pd.pivot_table(df, index=category, values=[
                       '本期經費(千元)'], aggfunc={'本期經費(千元)': ["sum", "count"]}).to_records())
    dft.rename(columns={"('本期經費(千元)', 'count')": "件數",
                        "('本期經費(千元)', 'sum')": "經費(千元)"}, inplace=True)
    if isinstance(category, list):
        index_name = category[0]
        df2 = dft.pivot_table(index=index_name, columns="計畫年度", values=[
            "件數", "經費(千元)"], fill_value=0)
        # df2.columns.name = None
        df2 = df2.reset_index()
        df2.to_excel(
            "{}/{}_件數_經費.xlsx".format(grb_figdata, category))
        df2.to_excel(
            "{}/{}_件數_經費.xlsx".format(grb_figdata, category))
        return
    dft.to_excel("{}/{}_件數_經費.xlsx".format(grb_figdata, category), index=False)
    if figout:
        year_fig2(dft[category], dft["件數"], category, "件數")
        year_fig2(dft[category], dft["經費(千元)"], category, "經費(千元)")


def data_count(df, category):
    dft = pd.DataFrame(pd.pivot_table(df, index=category, values=[
                       '本期經費(千元)'], aggfunc={'本期經費(千元)': ["sum", "count"]}).to_records())
    dft.rename(columns={"('本期經費(千元)', 'count')": "件數",
                        "('本期經費(千元)', 'sum')": "經費(千元)"}, inplace=True)
    return dft


def year_fig2(xdata, ydata, xlab, ylab, grb_figdata):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.plot(xdata, ydata)
    plt.xlabel(xlab, fontsize=14)
    plt.ylabel(ylab, fontsize=14)
    plt.savefig("{}/{}_{}.png".format(grb_figdata, xlab, ylab))
    plt.show()


def columnlinechart(writer, sheet_name, maxrow):
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    # Create a chart object.
    chart = workbook.add_chart({'type': 'column'})

    # Configure the series of the chart from the dataframe data.
    chart.add_series({'name': f"={sheet_name}!C1", 'values': f"={sheet_name}!$C$2:$C${maxrow}",
                      "categories": f"={sheet_name}!$A$2:$A${maxrow}",
                      'fill': {'color': '#808080'}, 'data_labels': {'value': True}, 'gap': 15})

    # 'type': 'column' 即為圖表類別為 line chart
    line_chart = workbook.add_chart({'type': 'line'})
    line_chart.add_series({'name': f"={sheet_name}!B1", "categories": f"={sheet_name}!$A$2:$A${maxrow}", 'values': f"={sheet_name}!$B$2:$B${maxrow}", 'data_labels': {'value': True, "position": "above"},
                           'y2_axis': True, "marker": {"type": "circle", "size": "9", "fill": {"color": "white"}}})  # 'y2_axis': 表示是否增加 secondary y-axis
    chart.combine(line_chart)  # 將兩張圖 (bar chart & line chart) 組合在一起

    chart.set_legend({'position': 'top'})  # legend 位置於圖表下方
    chart.set_x_axis({'major_gridlines': {'visible': False}})
    chart.set_y_axis({'major_gridlines': {'visible': False}})
    # Turn off chart legend. It is on by default in Excel.
    # chart.set_legend({'position': 'none'})
    chart.set_size({'width': 800, 'height': 500})
    # Insert the chart into the worksheet.
    worksheet.insert_chart('F2', chart)


def barchart(writer, sheet_name, maxrow, maxcolumn):
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    # Create a chart object.
    chart = workbook.add_chart({'type': 'bar', 'subtype': 'percent_stacked'})
    for itm in range(1, maxcolumn):
        colname = chr(65+itm)
        chart.add_series({"name": f"='{sheet_name}'!${colname}$1",
                          'categories': f"='{sheet_name}'!$A$2:$A${maxrow}",
                          "values": f"='{sheet_name}'!${colname}$2:${colname}${maxrow}"
                          })
    chart.set_legend({'position': 'top'})  # legend 位置於圖表下方
    chart.set_style(13)
    chart.set_y_axis({'major_gridlines': {'visible': False}})
    chart.set_x_axis({'major_gridlines': {'visible': False}})
    chart.set_size({'width': 800, 'height': 500})
    worksheet.insert_chart("F2", chart)


def piechart(writer, sheet_name, maxrow):
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    chart = workbook.add_chart({"type": "pie"})
    chart.add_series({'categories': f"='{sheet_name}'!$A$2:$A${maxrow}",
                      "values": f"='{sheet_name}'!$C$2:$C${maxrow}",
                      'data_labels': {'category': True, 'percentage': True},
                      })
    chart.set_legend({'position': 'left'})  # legend 位置於圖表下方
    chart.set_style(13)
    chart.set_size({'width': 800, 'height': 500})
    worksheet.insert_chart("F2", chart)


def yeardiv(dfyears, period):
    # dfyears 為 df["year"].values 的值
    years = list(set(dfyears))
    start = min(years)
    grouplabel = [f"{itm}~{itm+period-1}" for itm in years[::period]]
    groupyear = []
    for itm in dfyears:
        groupyear.append(grouplabel[(itm-start)//period])
    return groupyear


def checkdict(context, wordDict):
    if context in wordDict:
        wordDict[context] += 1
    else:
        wordDict[context] = 1


def main(grb_dir):
    print(grb_dir)
    grb_xlsFileName = f"{grb_dir[:6]}_grb.xlsx"
    outputfilename = f"{grb_dir[:6]}_output.xlsx"
    # 取得下載 xlsx 所有檔案名稱
    files = ["{}/{}".format(grb_dir, i) for i in os.listdir(grb_dir)]

    # 執行 xslx 合併檔案
    df = grb_aggr(files, grb_xlsFileName)
    # df = pd.read_excel("D:/grb.xlsx")

    # 資料處理的工作
    # 僅取出 國科會、科技部的計畫
    filterlist = ["行政院國家科學委員會", "科技部"]
    df1 = df[df["計畫主管機關"].isin(filterlist)][['計畫中文名稱', '執行單位名稱', '計畫年度', '計畫主管機關', '研究性質', '研究領域', '本期期間(起)', '本期期間(訖)', '本期經費(千元)',
                                             '計畫主持人', '共同/協同主持人', '中文關鍵詞', '英文關鍵詞']]
    # 研究領域，僅取出第一個研究領域 分析
    df1["主研究領域"] = [itm[0] for itm in df1["研究領域"].str.split(";").values]
    # 執行機構名稱的清理
    df1["執行單位_new"] = [str(itm[1]).replace("台灣", "臺灣") for itm in df1["執行單位名稱"].str.extract(
        r'(國立|.*法人|行政院)?(.*大學|.*學院|.*研究院|.*學會|.*學校|原子能委員會|食品工業發展研究所|國家同步輻射研究中心|林業試驗所|中醫藥研究所)').values]
    # 輸出整理過的檔案
    df1.to_excel("{}_MOST_整理.xlsx".format(
        grb_xlsFileName[:grb_xlsFileName.rfind(".")]), index=False)
    df1 = pd.read_excel("{}_MOST_整理.xlsx".format(
        grb_xlsFileName[:grb_xlsFileName.rfind(".")]))
    with pd.ExcelWriter(outputfilename, engine='xlsxwriter') as writer:
        tmp = data_count(df1, "計畫年度")
        maxrow = len(tmp)+1
        tmp.to_excel(writer, sheet_name="計畫年度", index=False)
        columnlinechart(writer, "計畫年度", maxrow)

        tmp = data_count(df, ["研究性質", "計畫年度"])
        mask = tmp["研究性質"] == "其他"
        tmp[~mask].to_excel(writer, sheet_name="研究性質with年度", index=False)

        tmp = data_count(df1, ["研究性質", "計畫年度"])
        mask = tmp["研究性質"] == "其他"
        tmp = tmp[~mask]
        tmp.to_excel(writer, sheet_name="MOST 研究性質with年度", index=False)
        for j in [4, 3, 2]:
            yearlen = len(set(tmp["計畫年度"].values))
            if yearlen % j == 0:
                divdat = yearlen//j
                break

        groupyear = yeardiv(tmp["計畫年度"].values, divdat)
        tmp["計畫年度"] = groupyear
        tmp = pd.DataFrame(pd.pivot_table(tmp, index="研究性質",
                                          values="經費(千元)", columns=["計畫年度"]).to_records())
        sindex = tmp.index.to_list()
        sindex[0] = 4
        tmp.index = sindex
        tmp.sort_index(inplace=True)
        tmp.to_excel(writer, sheet_name="MOST 研究性質 with 年度區間", index=False)
        maxrow = len(tmp)+1
        maxcolumn = len(tmp.columns)
        barchart(writer, "MOST 研究性質 with 年度區間", maxrow, maxcolumn)

        tmp = data_count(df1, "主研究領域")
        tmp.sort_values("經費(千元)", ascending=False, inplace=True)
        maxrow = len(tmp)+1
        tmp.to_excel(writer, "主研究領域", index=False)
        if maxrow > 13:
            maxrow = 13
        piechart(writer, "主研究領域", maxrow)

        sheetname = "執行單位_new"
        tmp = data_count(df1, sheetname)
        tmp.sort_values("經費(千元)", ascending=False, inplace=True)
        maxrow = len(tmp)+1
        tmp.to_excel(writer, sheet_name=sheetname, index=False)
        if maxrow > 25:
            maxrow = 25
        piechart(writer, sheetname, maxrow)


if __name__ == "__main__":
    # 定義區
    # 設定工作目錄
    working_dir = r"g:\6g"
    txt_data = "txt"
    os.chdir(working_dir)
    grb_dirs = ["6g"]

    # # 做圖用的 xlsx 分檔的輸出位置
    grb_figdata = "data2fig"

    # # 建立 xlsx 輸出檔的存放目錄
    try:
        os.mkdir(txt_data)
    except FileExistsError:
        print("%s 的目標已存在" % txt_data)

    try:
        os.mkdir(grb_figdata)
    except FileExistsError:
        print("%s 的目標已存在" % grb_figdata)
    main(grb_dirs[0])
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    #     executor.map(main, grb_dirs)
