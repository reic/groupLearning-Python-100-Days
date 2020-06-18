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


def merge(items1, items2, comp=lambda x, y: x < y):
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    '''歸併排序'''
    if len(items) < 2:
        return items
    mid = len(items)//2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def main():
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    # print(select_sort(items)) # 7次迴圈
    print(items)
    # print(bubble_sort(items)) # 5 次迴卷
    # print(buble_sort_upgrade(items)) # 3 次迴卷
    print(merge_sort(items))


if __name__ == "__main__":
    main()
