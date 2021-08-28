import os


def single_word():
    tmp = []
    for itm in keywords:
        if len(itm.strip()) == 0:
            continue
        if "；" in itm:
            tmpArray = [context.strip() for context in itm.split("；")
                        if len(context.strip()) > 0]
            tmp.extend(tmpArray)
            continue
        if "；" in itm:
            tmpArray = [context.strip() for context in itm.split("；")
                        if len(context.strip()) > 0]
            tmp.extend(tmpArray)
            continue
        if "、" in itm:
            tmpArray = [context.strip() for context in itm.split("、")
                        if len(context.strip()) > 0]
            tmp.extend(tmpArray)
            continue
        tmp.append(itm)
    return tmp


def pair_data():
    for itm in keywords:
        if len(itm.strip()) == 0:
            continue
        if "；" in itm:
            tmpArray = [context.strip() for context in itm.split(
                "；") if len(context.strip()) > 0]
            if len(tmpArray) < 2:
                continue
            content.append(sorted(tmpArray))
        if ";" in itm:
            tmpArray = [context.strip() for context in itm.split(
                ";") if len(context.strip()) > 0]
            if len(tmpArray) < 1:
                continue
            content.append(sorted(tmpArray))
        if "、" in itm:
            tmpArray = [context.strip() for context in itm.split(
                "、") if len(context.strip()) > 0]
            if len(tmpArray) < 1:
                continue
            content.append(sorted(tmpArray))


def checkdict(context):
    if context in wordDict:
        wordDict[context] += 1
    else:
        wordDict[context] = 1


def pairwords(arr):
    if len(arr) == 2:
        context = "\t".join(arr)
        checkdict(context)
        pairword_list.append(context)
        # return arr
    tmp = []
    maxlen = len(arr)
    for i in range(maxlen-1):
        for j in range(i+1, maxlen):
            context = "\t".join([arr[i], arr[j]])
            checkdict(context)
            pairword_list.append(context)


def main():
    # print(wordDict)
    pair_data()
    for itm in content:
        pairwords(itm)

    outputArry = []
    for key, value in wordDict.items():
        outputArry.append([key, value])
    outputArry.sort(key=lambda x: x[1], reverse=True)
    gephi = []
    corelation_value = 3
    for itm in outputArry:
        if itm[1] < corelation_value:
            break
        for _ in range(itm[1]-corelation_value):
            gephi.append(itm[0])
    outputArry = [f"{itm[0]}\t{itm[1]}" for itm in outputArry]

    with open("{}_{}".format("Ouput", filename), "w", encoding="utf-8") as f:
        f.write("\n".join(outputArry))
    # with open("{}_{}.csv".format("Gephi", filename[:-4]), "w", encoding="utf-8") as f:
    #     f.write("\n".join(pairword_list))
    with open("{}_{}.csv".format("Gephi", filename[:-4]), "w", encoding="utf-8") as f:
        f.write("\n".join(gephi))


def main2():
    words = single_word()
    print(len(words))
    for itm in words:
        if itm in singleDict:
            singleDict[itm] += 1
        else:
            singleDict[itm] = 1
    outputArry = []
    for key, value in singleDict.items():
        outputArry.append([key, value])
    outputArry.sort(key=lambda x: x[1], reverse=True)
    outputArry = [f"{itm[1]}\t{itm[0]}" for itm in outputArry]
    with open("{}_{}".format("output_wordcloud", filename), "w", encoding="utf-8") as f:
        f.write("\n".join(outputArry))


if __name__ == "__main__":
    os.chdir("d:/")

    filename = "keyword.txt"
    with open(filename, "r", encoding="utf-8") as f:
        keywords = f.read().splitlines()

    content = []
    wordDict = {}
    pairword_list = []
    singleDict = {}
    wordcloud = []
    main()
    main2()
