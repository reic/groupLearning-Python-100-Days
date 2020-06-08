from math import sqrt
from time import sleep


class Student(object):
    # __init__ 是一個特殊的方法，用在建立物件的初使用操作
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s 正在學習 %s" % (self.name, course_name))

    # 變數的命名
    # PEP 8要求標識符的名字用全小寫多個單詞用下劃線連接
    # 但是部分程序員和公司更傾向於使用駝峰命名法(駝峰標識)
    def watch_movie(self):
        if self.age < 18:
            print("%s 只能看熊出沒！" % self.name)
        else:
            print("%s 正在看島國愛情大電影！" % self.name)


class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def pract1():
    stu1 = Student("瑞課", 38)
    stu1.study(" Python 100 天實作挑戰!")
    stu1.watch_movie()
    stu2 = Student("王大錘", 18)
    stu2.study("生活倫理")
    stu2.watch_movie()


def prac2():
    # private value, method 的說明
    test = Test("hello")
    # AttributeError: Test object has no attribute
    # test.__bar()
    # print(test.__foo)

    # 但是 Python 沒有嚴格保證 private value, method，只是增加了 取用的難度
    test._Test__bar()
    print(test._Test__foo)


'''
練習 1  定義一個數字時鐘

'''


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                self._hour %= 24

    def show(self):
        return "%2d:%2d:%2d" % \
            (self._hour, self._minute, self._second)


def exe1():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


'''
練習2：定義一個類描述平面上的點並提供移動點和計算到另一個點距離的方法。
'''


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2+dy**2)

    def __str__(self):
        return "( %s, %s )" % (str(self.x), str(self.y))


def exe2():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    # p2.move_to(-1, -1)
    print(p1.distance_to(p2))


if __name__ == "__main__":
    exe2()
