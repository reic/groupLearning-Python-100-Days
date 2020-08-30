# 用來計算不同級分的人數
def main(fname):
    with open(fname, 'r', encoding='utf-8') as f:
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
    with open(fname[:-4]+"_output.txt", "w", encoding='utf-8') as f:
        f.write(strings)


if __name__ == "__main__":
    filenames = ['1072.txt', '1081.txt', '1082.txt']
    for fname in filenames:
        main(fname)

    # a = [None] * 15
    # a[0] = int(a[0] or 0) + 1
    # print(a)
    pass
