
def withdraw_list(students, student_id=3, withdraw=15):
    output, check = [], []
    for item in students:
        if item[0] == "108下":
            continue
        if item[student_id] not in check:
            check.append(item[student_id])
            output.append(item)
            continue
        c_index = check.index(item[student_id])
        if output[c_index][withdraw] < item[withdraw]:
            output[c_index] = item
    return output


def get_students(filename):
    star, appl, exam = [], [], []
    f = open(filename, encoding='utf-8')
    content = [x.split("\t") for x in f.read().split("\n")]
    for item in content:
        if len(item) != 2:
            continue
        if item[1] == "申請":
            appl.append(item[0])
        elif item[1] == "繁星":
            star.append(item[0])
        elif item[1] == "指考":
            exam.append(item[0])
    return [star, appl, exam]


def withdraw_count(filename, withdraw_students, data_index=15):
    # star_c,appl_c,eaxm_c=0,0,0
    count = {"繁星": 0, "申請": 0, "指考": 0}
    [star, appl, exam] = get_students(filename)

    # print(len(star),len(appl),len(exam))
    for item in withdraw_students:
        if item[3] in star:
            count["繁星"] += int(item[data_index])
        elif item[3] in appl:
            count["申請"] += int(item[data_index])
        elif item[3] in exam:
            count["指考"] += int(item[data_index])
    # return [star_c,appl_c,eaxm_c]
    return count


def alldraw_count(filename, withdraw_students):
    count = {"繁星": 0, "申請": 0, "指考": 0}
    [star, appl, exam] = get_students(filename)
    # print("申請: %s,  指考： %s, 繁星: %d" % (len(appl),len(exam),len(star)))
    for item in withdraw_students:
        if item[0] == "108下":
            continue
        if len(item) < 3:
            break
        if item[3] in star:
            # print(item[3],1)
            count["繁星"] += 1
        elif item[3] in appl:
            # print(item[3],2)
            count["申請"] += 1
        elif item[3] in exam:
            # print(item[3],3)
            count["指考"] += 1
    # return [star_c,appl_c,eaxm_c]
    return count


def main1():
    f = open('test.csv', 'r', encoding='utf-8')
    content = [x.split("\t") for x in f.read().split("\n")]
    f.close()
    for item in content[::-1]:
        if len(item) > 3:
            break
        content.remove(item)
    # withdraw_students 休學資料表
    withdraw_students = withdraw_list(content, 3, 15)
    output_string = '\n'.join("\t".join(x) for x in withdraw_students)
    # 整理好的 休學資料表，輸出檔為 output.csv
    f = open("output.csv", "w", encoding="utf-8")
    f.write(output_string)
    f.close()

    filename = ["106.csv", "107.csv", "108.csv"]
    print("休學人次計算")
    for item in filename:
        print(item, withdraw_count(item, withdraw_students))

    f = open('draw.csv', 'r', encoding='utf-8')
    content = [x.split("\t") for x in f.read().split("\n")]
    content.pop()
    f.close()
    print("退學人次計算")
    # for item in filename:
    for item in filename:
        print(item, alldraw_count(item, content))
