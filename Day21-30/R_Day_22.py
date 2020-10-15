import pandas as pd


def get_clipboard():
    # 從 中央氣象局取得區域的月均溫
    # https://www.cwb.gov.tw/V8/C/C/Statistics/monthlymean.html

    # 因為取得的資料是一列的資料，透過 numpy 的 reshape ，轉換為正確的欄位
    data = pd.read_clipboard(header=None).values.reshape(-1, 16)
    # 整理取得的資料，並形成 csv 檔
    filename = "./Day21-30/data/climate.csv"
    # 新的資料最後 2 欄為平均溫的統計區間，因為用不到，所以就不儲至 csv 檔
    pd.DataFrame(data[:, :-2]).to_csv(filename, header=None, index=None)
    tmp = data[:, :-2]
    climate_data = list(tmp)
    return climate_data


def disp_area(data):
    i = 0
    for a in data:
        print("{:>2}:{:<3}\t".format(i, a[0]), end="")
        i += 1
        if not(i % 5):
            print()
    print()


def disp_temp(data):
    print("顯示區域：", data[0])
    print("".center(50, "-"))
    for i in range(1, 13):
        print("{:>3}月均溫：{:>.1f}度".format(i, float(data[i])))
    print("".center(50, "-"))
    print("{:>3}年均溫：{:>.1f}度".format("", float(data[13])))


def main():
    # get from clipbboard()
    # climate_data=get_clipboard()
    filename = "./Day21-30/data/climate.csv"
    climate_data = pd.read_csv(filename, header=None).values
    # print(climate_data)
    while True:
        disp_area(climate_data)
        area = int(input("請輸入你要查詢平均溫度的地區(-1 結束)"))
        if area == -1:
            break
        disp_temp(climate_data[area])
        input("請按 Enter 回主選單")


if __name__ == "__main__":
    main()
    pass
