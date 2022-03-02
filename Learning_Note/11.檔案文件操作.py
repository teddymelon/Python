#儲存檔案 #利用變數來操作檔案物件
file = open("data.txt", mode="w", encoding="utf-8") #開啟 #編碼 encoding
file.write("嗨文件\nSecond Line") #操作 #用中文出現亂碼，怎麼辦?
file.close() #關閉

#最佳實務，做跟上面一樣的事情
with open("data2.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n4\n3\n2\n1")

#讀取檔案
with open("data2.txt", mode="r", encoding="utf-8") as file:
    data=file.read()
print(data)

#注意，讀寫要分開撰寫，不然會不能正常執行！

#讀取=r / 寫入=w / 讀寫=r+
#讀取檔案，且將每一行的數字加起來 (要轉為int)，要一行一行的處理

sum=0
with open("data2.txt", mode="r", encoding="utf-8") as file:
    for i in file:
        sum+=int(i)
print(sum)


#處理JSON檔案
#從檔案中讀取 JSON的資料，放入變數data裡面
import json
with open("Python\config.json", mode="r") as file:
    data=json.load(file)

print(data) #字典
print("name:", data["name"])
print("version:", data["version"])

data["name"]="New Name"
data.setdefault("Meow","Kitty") #修改變數中的資料 
data.update({"meow":"Bad Meow"}) #updata、setdefault都可以新增但也可以如下新增
data["cool"]="cool chow"
#del data["girl"]

#字典操作:https://kk665403.pixnet.net/blog/post/403711283-%5Bpython%5D-python-dict%E5%AD%97%E5%85%B8%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C%E6%95%99%E5%AD%B8%28%E6%96%B0%E5%A2%9E-%E4%BF%AE%E6%94%B9-

#把最新的資料複寫回檔案中，透過修改變數的資料來達成修改文件內容的目的

with open("Python\config.json", mode="w") as file:
    json.dump(data, file) #dump資料進去