import pandas as pd
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re
import sys
import os
import string


def convert_pdf_2_text(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    with open(path, "rb") as fp:

        #         for page in PDFPage.get_pages(fp, set()):
        counter = 0
        maxpages = 3
        for page in PDFPage.get_pages(fp, set(), maxpages=maxpages):
            interpreter.process_page(page)
        text = retstr.getvalue()
    device.close()
    retstr.close()
    return text


def getFileList(filepath):
    allfilelists = os.listdir(filepath)
    allfilelists = [itm for itm in allfilelists if itm.endswith(".pdf")]
    return allfilelists


def charReplace(txt):
    # / 有兩種不同的字碼， chr(8725), chr(47)
    chrlist = [chr(8725), chr(47), chr(8208)]
    return txt.replace(chrlist[0], "_").replace(chrlist[1], "_").replace(chrlist[2], "-")


def change_names_from_excel():

    year = 108
    df = pd.read_excel(
        "e:/0911.xlsx", usecols=["系統編號", "年度", "審議編號", "計畫完整中文名稱"])
    dfa = df[(df["年度"] == year) & (df["審議編號"].notna())
             ][["系統編號", "計畫完整中文名稱", "審議編號"]]
    dfa["計畫完整中文名稱"] = dfa["計畫完整中文名稱"].str.replace("/", "_")
    path = "e:/"+str(year)+"/"
    with open(path+"output.bat", "w", encoding='utf-8') as f:
        f.write("")
    with open(path+"output.bat", "a", encoding='utf-8') as f:
        for itm in dfa.values:
            print(itm[1])
            output_content = 'move "{}.pdf" "./ok/{}_{}.pdf"\n'.format(
                itm[0], itm[2], itm[1])
            f.write(output_content)


def main():
    year = 107

    path = 'e:/%s/' % (str(year))
    files = getFileList(path)
    end = 30
    counter = 1
    with open(path+"/output.bat", "w", encoding='utf-8') as f:
        f.write('')

    with open(path+"output.bat", "a", encoding='utf-8') as f:

        for itm in files:
            print(counter, itm)
            counter += 1
            text = convert_pdf_2_text(path+itm)

            patten = r'審議編號：(.*)\n'
            result = re.findall(patten, text)
            if len(result) == 0:
                output = 'move "%s" "./old/%s"\n' % (itm, itm)
                f.write(output)
                continue

            result = [itm.strip() for itm in result]

            if len(result[0]) == 0:
                output = 'move "%s" "./old/%s"\n' % (itm, itm)
                f.write(output)
                continue

            output = ('move "%s" "./ok/%s.pdf"\n' %
                      (itm, charReplace(result[0])))
            f.write(output)
