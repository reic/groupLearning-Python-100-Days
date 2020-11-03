from bs4 import BeautifulSoup
import requests
import pandas as pd

'''
BeautifulSoup 是一套協助解析網頁結構的模組
requests 取得網頁內容的程式
'''

# 中油公司歷史油價網址
url = "https://vipmember.tmtd.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"


html = requests.get(url).text
# sp = BeautifulSoup(html, 'html.parser')
sp = BeautifulSoup(html, 'lxml')

'''
使用萬字元的方法

data=sp.find_all('span',{'id': lambda L: L and L.startswith('MyGridView')})

此方法需要再 import re
data=sp.find_all('span',{'id':re.compile('MyGridView.*')})
'''
data = sp.find_all('table', {"id": "MyGridView"})
date_prices = data[0].find_all("tr")
price_list = []

# 取得 columns 名稱
row = date_prices[0]
cols = row.find_all('th')
'''
只取 '調價日期', '無鉛汽油92', '無鉛汽油95', '無鉛汽油98' 四個欄位
cols[0].text :調價日期,
cols[1].text :無鉛汽油92
cols[2].text :無鉛汽油95
cols[3].text :無鉛汽油98
用生成式完成
'''
columns = [cols[i].text for i in range(4)]

for row in date_prices[1:]:
    #     print(row)
    cols = row.find_all('span')
    if len(cols[1].text) < 1:
        continue
    item = [cols[i].text for i in range(4)]
    price_list.append(item)

oil_price_table = pd.DataFrame(price_list, columns=columns)
print(oil_price_table.head())
