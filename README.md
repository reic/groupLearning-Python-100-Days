# 群體的 Python 100 天學習記錄

這一個專案使用的教材是由骆昊發表在 Github 的 [Python - 100天从新手到大师](https://github.com/jackfrued/Python-100-Days)。

# How-To

透過 Github 的機制，協作提醒自己學習，並將學習的成果或回饋，也分享於 Github。至於如何透過 Github 完成監督呢？目前的想法是在完成學習後，依據課程文件的內容撰寫自己的學習感受，若是可以，也可以試著提供一些範例檔，透過出題的方式，增加自己的理解。

## 如何參與計畫

如果想要參與這一個活動的，請註冊 Github 帳號，再寄 email 給 [reic](mailto:reic.wang@gmail.com) 告訴我你的 github 帳號或是註冊 github 的 email。

## 參與者簽名

reic(R), Zarro(HY)

# 參與學習計畫的前置工作

學習計畫，需要準備可以練習 python 環境和可以提交進度的 git 設定，本文將會依序介紹。

## 運用 Winpython 建立學習 Python 的環境

在學習教材已經有介紹不同平台的工具，但是那些都太複雜了。多數參與學習計畫的人是在 Windows 的平台，建議一開始不需要耗費太多的時間去建置使用的環境，直接下載 [WinPython](https://winpython.github.io/) 的 [WinPython64-3.7.7.0cod](https://github.com/winpython/winpython/releases/download/2.3.20200319/Winpython64-3.7.7.0cod.exe) = Python 3.7 64bit + PyQt5 + Spyder + VSCode 套件組。解壓縮，即完成了初始環境的建置。

解壓縮後，裡面已經有兩個推薦使用的練習軟體 Jupyter Notebook.exe 和 VS Code.exe。參與學習計畫的人，

* VS Code.exe 即是由 Microsfot 推出的免費版本的編輯器。(Reic 比較推薦這一套，可以結合 Git 使用)
* Jupyter Notebook.exe 執行後，透過網頁開始練習。(這一套在做範例的時候比較方便，但是不利於此專案繳交作業)

## 如何使用 Git 在 VS Code 提交進度

需要下載 git 和修改 Winpython 的 script ，實現目的。

###  準備 GIT　的環境

首先至 [GIT 官網](https://git-scm.com/) 下載 [Windows GIT 軟體](https://git-scm.com/download/win)。 WinPython 為 Microsfot Windwos 的可攜軟體(portable)方案，因此建議下載 Git for Windows Portable，並解壓縮即可。

### 整合 GIT 和 VSCODE

假設將 WinPython 和 GIT 都解壓縮在使用者(Tom)的下載，在下載應該會有

* PortableGit ： 位置應該是 C:\Users\Tom\Downloads\PortableGit
* WPy64-3770 ： 位置應該是 C:\Users\hcwang\Downloads\WPy64-3770, 其中 3770 代表 WinPython 的版本，不同的版本應該會有不同的號碼，本次介紹以 3770 版介紹。

為了完成環境的建置，需要修改 WPy64-3770/scripts/winvscode.bat ，讓 VSCode 編輯器不修改設計，即可使用 GIT。

透過記事本(notepad)開啟 winvscode.bat，並將前幾行更改為

```Batch
@echo off
rem launcher for VScode
call "%~dp0env_for_icons.bat"
cd/D "%WINPYWORKDIR%"
set GITENV=C:\Users\Tom\Downloads\PortableGit\cmd
set PATH=%PATH%;%GITENV%
```

完成設定後，執行 C:\Users\hcwang\Downloads\WPy64-3770\VS Code.exe 就可開始練習 Python 了。
