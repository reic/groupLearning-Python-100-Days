def foo():
    pass


def bar():
    pass


# __name__是Python中一個隱含的變量它代表了模塊的名字
# 只有被Python解釋器直接執行的模塊的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()