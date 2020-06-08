import multiprocessing as mp
import tkinter
import tkinter.messagebox
from threading import Thread, Lock
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print("開始下載 %s" % filename)
    time_to_download = randint(1, 5)
    sleep(time_to_download)
    print("下載 %s 完成，並耗時 %s 秒" % (filename, time_to_download))


def mdownload_task(filename):
    print("啟動下載程序， Process_id[%d]. " % getpid())
    print("開始下載 %s" % filename)
    time_to_download = randint(1, 5)
    sleep(time_to_download)
    print("下載 %s 完成，並耗時 %s 秒" % (filename, time_to_download))


def main_processing():
    start = time()
    p1 = Process(target=mdownload_task, args=("超速學習.pdf",))
    p1.start()
    p2 = Process(target=mdownload_task, args=("Python 學習手冊.pdf",))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("總耗時 %s 秒" % (end-start))


counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


def main2():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()


def main_thread1():
    start = time()
    t1 = Thread(target=download_task, args=("超速學習.pdf",))
    t1.start()
    t2 = Thread(target=download_task, args=("Python 學習手冊.pdf",))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("總耗時 %s 秒" % (end-start))


'''
thread Class 是可以繼承，透過 run() methon 設定要執行的工作
'''


class DownloadTrack(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("開始下載 %s" % self._filename)
        time_to_download = randint(1, 5)
        sleep(time_to_download)
        print("下載 %s 完成，並耗時 %s 秒" % (self._filename, time_to_download))


def main_thread_ineritance():
    start = time()
    t1 = DownloadTrack("超速學習.pdf")
    t1.start()
    t2 = DownloadTrack("pythond 學習手冊.pdf")
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("總耗時 %s 秒" % (end-start))


'''
Thread 採用共用記憶體， Processing 是獨立記憶體。
所以在用Thread 的時候要小心資源的使用是否適當，以避免程式 Crash
多執行緖，同時向一個帳號 轉帳 的問的
'''


class Account(object):
    def __init__(self):
        self._balance = 0
        # 多執行緒關鍵資源 鎖定
        self._lock = Lock()

    def deposit(self, money):
        # 取得關鍵資料
        self._lock.acquire()
        try:
            new_balance = self._balance+money
            sleep(0.05)
            self._balance = new_balance
        finally:
            # 釋放關鍵資源
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def bank_deposit():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("帳號餘額為： %d 元" % account.balance)


def download_singleThread():
    sleep(randint(1, 5))
    tkinter.messagebox.showinfo("提示", "下載完成")


def main_download_handler():
    def show_about():
        tkinter.messagebox.showinfo("關於", "作者：小白")

    class DownloadTrackHandler(Thread):
        def run(self):
            sleep(5)
            tkinter.messagebox.showinfo("提示", "下載完成")
            button1.config(state=tkinter.NORMAL)

    def download():
        button1.config(state=tkinter.DISABLED)
        DownloadTrackHandler(daemon=True).start()

    top = tkinter.Tk()
    top.title = "單線程"
    top.geometry('200x200')
    top.wm_attributes('-topmost', True)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text="下載", command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text="關於", command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()


def org_count():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    end = time()
    print("Excution time: %3f" % (end-start))


def task_handler(curr_list, result_quene):
    total = 0
    for number in curr_list:
        total += number
    result_quene.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    start = time()
    result_queue = mp.Queue()
    index = 0
    for _ in range(8):
        p = mp.Process(target=task_handler, args=(
            number_list[index:index+12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print("Excution Time:", end-start, sep='')


if __name__ == "__main__":
    org_count()
    main()
