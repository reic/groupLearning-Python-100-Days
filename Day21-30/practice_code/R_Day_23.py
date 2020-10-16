import sqlite3


def disp_menu():
    print("學生資料編輯")
    print("".center(50, "-"))
    options = ["1.新增", "2.編輯", "3.刪除", "4.顯示所有學生", "0.結束"]
    for i in options:
        print("{:<s} {:<2s}".format(i, ''), end='')
    print()
    print("".center(50, "-"))


def append_data():
    while True:
        no = int(input("請輸入學生座號(-1停止輸入)："))
        if no == -1:
            break
        name = input("請輸入學生姓名：")
        sqlstr = "select * from students where stdno = {};".format(no)
        cursor = conn.execute(sqlstr)
        if len(cursor.fetchall()) > 0:
            print("輸入的座號已存在。")
        else:
            sqlstr = "insert into students values({},'{}');".format(no, name)
            conn.execute(sqlstr)
            conn.commit()


def edit_data():
    no = int(input("請輸入學生座號："))
    sqlstr = "select * from students where stdno = {};".format(no)
    cursor = conn.execute(sqlstr)
    rows = cursor.fetchall()
    if len(rows) > 0:
        print("目前學生的姓名: {}".format(rows[0][1]))
        name = input("請輸入學生姓名：")
        sqlstr = "update students set name='{}' where stdno={};".format(
            name, no)
        conn.execute(sqlstr)
        conn.commit()
    else:
        print("找不到學生的座號！")


def del_data():
    no = int(input("請輸入學生座號："))
    sqlstr = "select * from students where stdno = {};".format(no)
    cursor = conn.execute(sqlstr)
    rows = cursor.fetchall()
    if len(rows) > 0:
        print("你目前要刪除是座號 {} 的 {}".format(rows[0][0], rows[0][1]))
        answer = input("確定要刪除(y/n)? ").lower()
        if answer == "y":
            sqlstr = "delete from students where stdno={};".format(no)
            conn.execute(sqlstr)
            conn.commit()
            print("已刪除指定的學生....")
    else:
        print("找不到指定的學生！")


def disp_data():
    cursor = conn.execute("select * from students;")
    for row in cursor:
        print("NO {}: {}".format(row[0], row[1]))


def main():

    while True:
        disp_menu()
        choice = int(input("請輸入你的選擇："))
        if choice == 0:
            break
        if choice == 1:
            append_data()
        elif choice == 2:
            edit_data()
        elif choice == 3:
            del_data()
        elif choice == 4:
            disp_data()
        else:
            break
        input("請按 Enter 回主選單")


if __name__ == "__main__":
    database_at = "./Day21-30/data/scores.sqlite"
    conn = sqlite3.connect(database_at)
    main()
    conn.close()
    pass
