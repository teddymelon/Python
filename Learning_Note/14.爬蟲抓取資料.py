#爬蟲，必須要盡可能地讓程式模仿一個普通使用者的樣子
#如果抓Json格式，可以用內建的json模組來處理
#如果是HTML，用第三方套件 Beautifulsoup 來做資料解析。

#安裝python的時候，就一起安裝了PIP套件管理工具，來安裝Beautifulsoup4

# 抓取 PTT 電影版的網頁原始碼(HTML)

# 解析原始碼，取得每篇文章的標題
'''
import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"
with  req.urlopen(url) as response:
    data = response.read()
print(data)
'''
#如果只是這樣就會失敗，因為沒有附上Request Header。


import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"
#建立一個Request物件, 附加Request Headers的資訊。
request = req.Request(url, headers={
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
})

with  req.urlopen(request) as response:
    data = response.read().decode("utf-8")

#解析原始碼，取得每篇文章的標題

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
#print(root.title.string)

#從網頁中尋找標籤
titles=root.find_all("div", class_="title") #尋找 class="title"的div標籤
#print(titles)

#find_all 是列表的方式呈現出來

for title in titles:
    if title.a != None:
        print(title.a.string)

