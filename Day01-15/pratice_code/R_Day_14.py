from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
from time import time
from threading import Thread
import requests


class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/')+1:]
        res = requests.get(self.url)
        with open('./Day01-15/pratice_code/'+filename, 'wb') as f:
            f.write(res.content)


def main1():
    # requests get api, then multi thread to download the files
    # 取得圖片的 api ，不一定要透過這一個網站
    # 可以試著去抓取其它的網頁，用其它的方法實現
    res = requests.get(
        'http://api.tianapi.com/meinv/?key=bdf0c2468a47ae42669911101865e9c9&num=10')
    data_model = res.json()
    for item in data_model['newslist']:
        url = item['picUrl']
        DownloadHandler(url).start()


def main2():
    # 錯誤無法成功
    sender = '0608412@narlabs.org.tw'
    receivers = ['hcwang@narlabs.org.tw', 'reic.wang@gmail.com']
    message = MIMEText('用 Python 發送郵件測試.', 'plain', 'utf-8')
    message['From'] = Header("Reic")
    message['To'] = Header('HC')
    message['Subject'] = Header("python sendder", 'utf-8')
    smtper = SMTP_SSL('mail.narlabs.org.tw')
    smtper.login(sender, "password")
    smtper.sendmail(sender, receivers, message.as_string())
    print("送件完成")


if __name__ == "__main__":
    pass
