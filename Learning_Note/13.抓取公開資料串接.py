import urllib.request
'''
src = "https://www.ntu.edu.tw/"
with  urllib.request.urlopen(src) as response:
    data = response.read().decode("utf-8")
#print(data)
#取得台大網站的首頁原始碼
#with open("cool.txt", mode = "w", encoding = "utf-8") as file:
#    file.write(data)
'''

#如何串接擷取公開資料?
import urllib.request
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with  urllib.request.urlopen(src) as response:
    data = json.load(response) #利用json模組處理json資料格式
print(data)


#如何解讀資料?接下來來解讀資料，將公司名稱列表出來
clist = data["result"]["results"]
#print(clist)
for company in clist:
    print(company["公司名稱"]+"\n")

'''
#使用for迴圈列印出公司名稱，並且加進data.txt裡面。
with open("data.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
'''