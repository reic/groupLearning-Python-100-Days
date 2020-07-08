from contextlib import contextmanager
from time import perf_counter


def select_sort(origin_items):
    '''
    簡單排序法
    '''
    # list copy ，不指向同一記憶體區塊
    items = origin_items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    '''
    bubble sort
    '''
    # 透過下述的方法，可以將
    items = origin_items[:]
    for i in range(len(origin_items)-1):
        swapped = False
        # for j in range(len(items)-1-i):
        for j in range(len(items)-i-1):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            break
    return items


def buble_sort_upgrade(origin_items, comp=lambda x, y: x > y):
    '''
    buble sort upgrade version
    '''
    items = origin_items[:]
    range_set = len(items)
    for i in range(range_set-1):
        swapped = False
        for j in range(i, range_set-1-i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(range_set-2-i, i, -1):
                if comp(items[j-1], items[j]):
                    items[j], items[j-1] = items[j-1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


'''
進階排序法
'''
'''
-----------------------------------------
merge sort - O(n * log_2 n) - 高级排序算法
35, 97, 12, 68, 55, 73, 81, 40
[35, 97, 12, 68], [55, 73, 81, 40]
[35, 97], [12, 68], [55, 73], [81, 40]
[35], [97], [12], [68], [55], [73], [81], [40]
[35, 97], [12, 68], [55, 73], [40, 81]
[12, 35, 68, 97], [40, 55, 73, 81]
[12, 35, 40, 55, 68, 73, 81, 97]
-----------------------------------------
'''


def merge_sort(items, comp=lambda x, y: x <= y):
    if len(items) < 2:
        return items
    mid = len(items)//2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(iteml, itemr, comp):
    items = []
    index1, index2 = 0, 0
    while index1 < len(iteml) and index2 < len(itemr):
        if comp(iteml[index1], itemr[index2]):
            items.append(iteml[index1])
            index1 += 1
        else:
            items.append(itemr[index2])
            index2 += 1
    items += iteml[index1:]
    items += itemr[index2:]
    return items


'''
-----------------------------------------
快速排序 - 以枢轴为界将列表中的元素划分为两个部分，左边都比枢轴小，右边都比枢轴大
35, 97, 12, 68, 55, 73, 81, 40
35, 12, [40], 68, 55, 73, 81, 97
[12], 35, [40], 68, 55, 73, 81, [97]
[12], 35, [40], 55, [68], 73, 81, [97]
[12], 35, [40], 55, [68], 73, [81], [97]
-----------------------------------------
'''


def quick_sort(origin_items, comp=lambda x, y: x <= y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items)-1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos-1, comp)
        _quick_sort(items, pos+1, end, comp)


def _partition(items, start, end, comp):
 # 將資料分割成左右邊
    pivot = items[end]  # 取最後一個元素來分割
    i = start-1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i+1], items[end] = items[end], items[i+1]
    return i+1


class Person(object):
    # 人
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}:{self.age}'

    def __repr__(self):
        return self.__str__()


def sequence_search(items, key):

    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def bin_search(items, key):
    start, end = 0, len(items)-1
    while start <= end:
        mid = (start+end)//2
        if key > items[mid]:
            start = mid+1
        elif key < items[mid]:
            end = mid-1
        else:
            return mid
    return -1


def main2():
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    # print(select_sort(items)) # 7次迴圈
    # print(items)
    # print(bubble_sort(items)) # 5 次迴卷
    # print(buble_sort_upgrade(items)) # 3 次迴卷
    # print(merge_sort(items))  # 一直切分矩陣，直到最小單位，再比較，逐步合併
    print(quick_sort(items))
    items2 = [Person('Wang', 25), Person("Luo", 39),
              Person('Zhang', 50), Person('He', 20)]
    # print(quick_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    print(merge_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    items3 = ['apple', 'orange', 'watermelon', 'durian', 'pear']
    # print(bubble_sort(items3))
    # print(merge_sort(items3))
    print(quick_sort(items3))
    print(sequence_search(items, 73))
    print(sequence_search(items, 63))
    data = quick_sort(items)
    print(data)
    print(bin_search(data, 37))
    print(bin_search(data, 55))
    # print(bin_search(quick_sort(items3), 'banana'))


'''
百元百雞
窮舉法
'''

'''
公雞5元，母雞3元，小雞 1 元 3 隻
用 100 元買 100隻雞， 公雞、母雞、小雞
'''


def quiz1():
    for x in range(20):
        for y in range(33):
            z = 100-x-y
            if 5*x + 3*y + z//3 == 100 and z % 3 == 0:
                print(x, y, z)


'''
A、B、C、D、E五人在某天夜裡合夥捕魚 最後疲憊不堪各自睡覺
第二天A第一個醒來 他將魚分為5份 扔掉多餘的1條 拿走自己的一份
B第二個醒來 也將魚分為5份 扔掉多餘的1條 拿走自己的一份
然後C、D、E依次醒來也按同樣的方式分魚 問他們至少捕了多少條魚
'''


def quiz2():
    fish = 6
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total-1) % 5 == 0:
                total = (total-1) // 5*4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5
    #     print(fish)


'''
     價錢 重
電腦 200, 20
收音機  20, 4
鐘 175, 10
花瓶 50, 2
書  10, 1
油畫 90, 9
背包只能裝 20 kg
'''


class Thing(object):
    '''物品'''

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def values(self):
        return self.price/self.weight


def input_thing():
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def chief_quiz():
    # max_weight, num_of_things = map(int, input("請輸入2個數字, 用空白間隔：").split())
    max_weight = 20
    # print(max_weight, num_of_things)
    things = [["電腦", 200, 20], ["收音機", 20, 4], [
        "鐘", 175, 10], ["花瓶", 50, 2], ["書", 10, 1], ["油畫", 90, 9]]
    all_things = [Thing(*item) for item in things]
    print([item.name for item in all_things])
    all_things.sort(key=lambda x: x.values, reverse=True)
    print([item.name for item in all_things])
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'總價值: {total_price}美元')


'''
階乘
n!
f(n)=f(n-1)+f(n-2)
1 1 2 3 5 8
'''


def fac(num):
    assert num >= 0
    if num in (0, 1):
        return 1
    return num * fac(num-1)


def fib2(num):
    a, b = 1, 1
    for _ in range(num-1):
        a, b = b, a+b
    return a


def fib3(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a+b
        yield a


def func1():
    print(fac(3))
    print(fib2(1))

    print([fib2(i) for i in range(1, 6)])
    print(*fib3(6))
    # for item in fib3(6):
    #     print(item)


def fib(num, results={}):
    assert num > 0
    if num in (1, 2
        return 1
    try:
        return results[num]
    except KeyError:
        results[num]=fib(num-1)+fib(num-2)
        return results[num]


@contextmanager
def timer():
    try:
        start=perf_counter()
        yield
    finally:
        end=perf_counter()
        print(f'{end - start}秒')


def main():
    for num in range(1, 15):
        # with timer():
        print(f'{num}: {fib(num)}')

    print(*fib(14))


if __name__ == "__main__":

    main()
    # quiz2()
