import json
from math import sqrt
import time


def readfile():
    '''
    當文檔不存在會出現異常
    '''
    # f = open('致橡樹.txt', 'r', encoding='utf-8')
    # print(f.read())
    # f.close()


def readfile2():
    '''
    異常處理的方法
    '''
    f = None
    try:
        f = open('致橡樹.txt', 'r', encoding='utf-8')
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("無法找到指定文件")
    except LookupError:
        print("指定了未知的編碼")
    except UnicodeDecodeError:
        print("讀取文件解碼錯誤")
    finally:
        if f:
            f.close()


def readfile3():
    '''
    透過 with open() as f:
    在完成讀檔時，即釋放資源
    '''
    filename = "Day01-15/pratice_code/致橡樹.txt"
    try:
        # with open(filename, 'r', encoding='utf-8') as f:
        #     print(f.read())
        # with open(filename, 'r', encoding='utf-8') as f:
        #     for line in f:
        #         print(line, end='')
        #         time.sleep(0.5)
        print()
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        lines = [i.strip() for i in lines]
        print(lines)

    except FileNotFoundError:
        print("無法找到指定文件")
    except LookupError:
        print("指定了未知的編碼")
    except UnicodeDecodeError:
        print("讀取文件解碼錯誤")


def is_prime(n):
    '''
    質數判斷
    '''
    assert n > 0
    factor_max = int(sqrt(n)+1)
    for factor in range(2, factor_max):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def write_in_different_files():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number)+'\n')
                elif number < 1000:
                    fs_list[1].write(str(number)+'\n')
                else:
                    fs_list[2].write(str(number)+'\n')
    except IOError as ex:
        print(ex)
        print('文件寫入錯誤')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')


def copy_png():
    import base64
    try:
        with open('award.png', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
            print(base64.b64encode(data))
        with open('copy_award.png', "wb") as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print("無法找到檔案", e)
    except IOError:
        print("讀寫文件錯誤")


def json_write():
    mydict = {
        'name': 'reic',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open("data.json", "w", encoding='utf-8') as fs:
            #  ensure_ascii 不將中文字轉碼
            json.dump(mydict, fs, ensure_ascii=False)
    except IOError as e:
        print(e)
    print("資料已儲")


class Teacher(object):

    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def title(self):
        return self.__title


def json_try():
    import json
    json_str = '{"name": "骆昊", "age": 38, "title": "叫兽"}'
    res = json.loads(json_str)
    print(res)
    print(type(res))
    print(res['name'])
    print(res['age'])

    teacher = Teacher(**res)
    print(teacher)
    print(teacher.name)
    print(teacher.age)
    print(teacher.title)
    filename = "teacher.csv"


def json_dum():
    teacher_dict = {'name': '白元芳', 'age': 25, 'title': '讲师'}
    json_str = json.dumps(teacher_dict, ensure_ascii=False)
    print(json_str)
    print(type(json_str))
    fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
    json_str = json.dumps(fruits_list)
    print(json_str)
    print(type(json_str))


if __name__ == '__main__':
    # main()
    json_dum()
