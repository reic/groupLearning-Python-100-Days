'''
用 @property 封裝，用 getter 和 setter 取得資料和修改資料
'''
from abc import ABCMeta, abstractmethod
from time import time, localtime, sleep
from math import sqrt


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter 的作法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改/設置 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self.age <= 16:
            print('%s 正在玩飛行棋.' % self._name)
        else:
            print('%s 正在玩跳棋.' % self._name)


def pra1():
    person = Person("王小明", 12)
    person.play()
    print(person.name)
    person.age = 22
    person.play()


class Person1(object):

    # 限定只能使用下列的屬性
    __slots__ = ("_name", "_age", "_gender")

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飛行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def pra2():
    person = Person1('王小明', 22)
    person.play()
    person._gender = '男'
    # 下列的那一行會產生錯誤，因為使用 限定外的使用。
    # 但若是沒有使用 __slots__ 則正常
    # person._is_gay = True


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod  # self 不見了
    def is_valid(a, b, c):
        return a+b > c and b+c > a and c+a > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter()/2
        return sqrt(half * (half - self._a)*(half-self._b)*(half-self._c))


def pra3():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 可以透過直接呼叫 class.function( )，再將 宣告的類別傳入
        # print(Triangle.perimeter(t))
        print(t.area())
        print(Triangle.area(t))
    else:
        print("無法形成三角形")


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod  # self => cls
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%2s:%2s:%2s' % (self._hour, self._minute, self._second)


def pra4():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


'''
class 繼承多種關係的說明
'''


class Person2(object):
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, age):
        self.__age = age

    def play(self):
        print("%s 正在愉快的玩耍。" % self._name)

    def watch_av(self):
        if self.__age >= 18:
            print("%s 正在觀看愛情動作片" % self._name)
        else:
            print("%s 只能觀看<<熊出沒>>" % self._name)


class Student(Person2):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print("%s 的 %s正在學習 %s" % (self._grade, self._name, course))


class Teacher(Person2):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print("%s %s 正在教授 %s" % (self._title, self._name, course))


def pra5():
    stu = Student("王小明", 15, "國三")
    stu.study("數學")
    stu.watch_av()
    stu.age, stu.grade = 18, "大學"
    stu.study("微積分")
    stu.watch_av()

    t = Teacher("如花", 38, "美容師")
    t.teach("畫妝課")
    t.watch_av()


'''
多態： 
在繼承 上一層的類別後，子類別修改了父類別的方法，覆寫(override)
透過覆寫，讓父類別的方法，在子類別中擁有著不同的作用，當宣告子類別時，不同的子類別會出現不同的行為，則稱為多形(polymorphism)
'''


class Pet(object, metaclass=ABCMeta):
    # 寵物
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        # 發出聲音
        pass


class Dog(Pet):
    def make_voice(self):
        print("%s: 汪汪汪...." % self._nickname)


class Cat(Pet):
    def make_voice(self):
        print("%s: 喵....喵....." % self._nickname)


def main():
    pets = [Dog('旺財'), Cat('凱蒂'), Dog('大黃')]
    for pet in pets:
        pet.make_voice()


if __name__ == "__main__":
    main()
