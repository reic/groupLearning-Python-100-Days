import heapq
from math import log2, factorial
from matplotlib import pyplot
import numpy


def dict_comprehesion():
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }

    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)


def grades_bad_function():
    names = ['關羽', '張飛', '趙雲', '馬超', '黃忠']
    courses = ['國文', '數學', '英語']
    # 录入五个学生三门课程的成绩
    # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
    # scores = [[None] * len(courses)] * len(names)
    # 生成一個與 names 對應的成續矩陣
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
            print(scores)


'''
從dict 中找出最大的或最小的 N 個元素
堆結構 (大根堆/小根堆)
headq 模組
head query
'''


def headq_try():
    list1 = [34, 25, 15, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


'''
itertools module
迭代工具模組
'''


def inter_module():
    import itertools
    # for item in itertools.permutations('ABCD'):
    #     print("".join(item))
    for item in itertools.combinations('ABCDE', 3):
        print(item)
    # for item in itertools.product('ABCD', '123'):
    #     print(item)
    # for item in itertools.cycle(('A', 'B', 'C')):
    #     print(item)


'''
collections 模組
有點類似我寫的詞頻計算程式
'''


def collect_try():
    from collections import Counter
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter.most_common(5))


def math_plot():
    '''
    繪圖練習
    '''
    num = 6
    styles = ['r-', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
    legends = ['log2', 'linear', '線性對數',
               'squaur', 'cubic', '3 order', 'factorial']
    x_data = [x for x in range(1, num+1)]
    y_data1 = [log2(y) for y in range(1, num+1)]
    y_data2 = [y for y in range(1, num+1)]
    y_data3 = [y*log2(y) for y in range(1, num+1)]
    y_data4 = [y**2 for y in range(1, num+1)]
    y_data5 = [y**3 for y in range(1, num+1)]
    y_data6 = [3**y for y in range(1, num+1)]
    y_data7 = [factorial(y) for y in range(1, num+1)]
    y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, styles[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(0, 8, step=1))
    pyplot.yticks(numpy.arange(0, 751, step=50))
    pyplot.show()


if __name__ == "__main__":
    # inter_module()
    math_plot()
