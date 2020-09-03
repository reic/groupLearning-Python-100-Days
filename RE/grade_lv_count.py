# 用來計算不同級分的人數
def main():
    with open("1.txt", 'r', encoding='utf-8') as f:
        content = f.read().split("\n")
    if content[-1] == '':
        content.pop()
    min_value = min(content)
    max_value = max(content)
    # div_count = int((float(max_value)-float(min_value))//0.3)+1
    div_count = int((float(max_value)-0.0)//0.3)+1
    print(div_count)
    nums = [0 for _ in range(div_count)]
    print(len(nums))
    for itm in content:
        index = int((float(itm)-0.0)//0.3)
        nums[index] += 1
    print("min= %s, max=%s" % (min_value, max_value))
    rangenum = 0.0
    strings = ''
    for itm in nums:
        strings += "{:.1f}~{:.1f} \t {}\n".format(rangenum, rangenum+0.3, itm)
        rangenum += 0.3
    with open("2.txt", "w", encoding='utf-8') as f:
        f.write(strings)


def xlsx():
    import pandas as pd
    import numpy as np
    sheet_name = ['107下', '108上', '108下']
    file_read = pd.read_excel("成績中位數.xlsx", sheet_name=sheet_name)
    divides = 10
    columns = []
    for i in range(divides):
        if i == 0:
            text = "0.0 ~ 1.6"
        else:
            text = "%.1f ~ %.1f" % (i*0.3+1.3, i*0.3+0.3+1.3)
        columns.append(text)
    output = []
    for itm in sheet_name:
        distrubs = ([0]*int(divides))
        df = file_read[itm]
        data_1 = df[df['是否同意公布單科成績分布圖'] == "Y"]["成績中位數"]
        for i in data_1:
            if i <= 1.6:
                distrubs[0] += 1
            else:
                index = (i-1.6)//0.3
                if not np.isclose((i-1.6) % 0.3, 0):
                    index += 1
                distrubs[int(index)] += 1

        output.append(distrubs)

    output = pd.DataFrame(output, index=sheet_name, columns=columns)
    ot = output.transpose()

    writer = pd.ExcelWriter('output.xlsx')

    ot.to_excel(writer, sheet_name="同意公布成績")
    # writer.save()
    output = []
    for itm in sheet_name:
        distrubs = ([0]*int(divides))
        df = file_read[itm]
        data_1 = df[df['是否同意公布單科成績分布圖'] != "Y"]["成績中位數"]
        for i in data_1:
            if i <= 1.6:
                distrubs[0] += 1
            else:
                index = (i-1.6)//0.3
                if not np.isclose((i-1.6) % 0.3, 0):
                    index += 1
                distrubs[int(index)] += 1

        output.append(distrubs)

    output = pd.DataFrame(output, index=sheet_name, columns=columns)
    ot = output.transpose()
    # writer=pd.ExcelFile('output.xlsx')
    ot.to_excel(writer, sheet_name="不公布成績")
    writer.save()
    writer.close()


if __name__ == "__main__":
    main()
    # a = [None] * 15
    # a[0] = int(a[0] or 0) + 1
    # print(a)
    pass
