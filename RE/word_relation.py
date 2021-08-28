import os
os.chdir("d:/")

filename = "keyword.txt"
with open(filename, "r", encoding="utf-8") as f:
    keywords = f.read().splitlines()

content = []
for itm in keywords[:4]:
    if len(itm.strip()) == 0:
        continue
    if "；" in itm:
        tmpArray = [context for context in itm.split(
            "；") if len(context.strip()) > 0]
        if len(tmpArray) > 1:
            print(tmpArray)
    if ";" in itm:
        tmpArray = [context for context in itm.split(
            ";") if len(context.strip()) > 0]
        if len(tmpArray) > 1:
            print(tmpArray)


# # 確保至少有 2 個關鍵詞
# content = [sorted(itm.split("\t"))
#            for itm in keywords if len(itm.split('\t')) > 1]


# def checkdict(context):
#     if context in wordDict:
#         wordDict[context] += 1
#     else:
#         wordDict[context] = 1


# def pairwords(arr):
#     if len(arr) == 2:
#         context = "\t".join(arr)
#         checkdict(context)
#         # return arr
#     tmp = []
#     maxlen = len(arr)
#     for i in range(maxlen-1):
#         for j in range(i+1, maxlen):
#             context = "\t".join([arr[i], arr[j]])
#             checkdict(context)


# wordDict = {}
# # print(wordDict)
# for itm in content:
#     pairwords(itm)

# outputArry = []
# for key, value in wordDict.items():
#     outputArry.append([key, value])
# outputArry.sort(key=lambda x: x[1], reverse=True)
# outputArry = [f"{itm[0]}\t{itm[1]}" for itm in outputArry]
# with open("{}_{}".format("Ouput", filename), "w", encoding="utf-8") as f:
#     f.write("\n".join(outputArry))
