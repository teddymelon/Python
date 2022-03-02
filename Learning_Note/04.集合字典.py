
#集合的運算

s1={3,4,5}
print(3 in s1) #有在裡面會出現True
print(10 in s1) #出現False
print(6 not in s1) #出現正確，因為6不在集合中


s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 #交集：取兩個集合中相同的資料
print(s3)

s3=s1|s2 #聯集：取兩個集合中的所有資料，但不重複取
print(s3)

s3=s1-s2 #用集合去做-，叫做差集：從s1中減去s2重疊的部分，有順序性的，s1-s2跟s2-s1是不一樣的。
print(s3)

s3=s1^s2 #反交集：取兩個集合中，不重疊的部分
print(s3)

s=set("Hello") #set(字串)，使用字串拆解成集合，重複的不會算到
print(s)
print("H" in s)


#字典的運算: key-value 配對

dic={"apple":"蘋果","banana":"香蕉"}
print(dic["apple"])
dic["apple"]="小可愛" #取value
print(dic["apple"])

print("apple" in dic) #判斷key是否存在，不會判斷value，而是判斷key。

print(dic)

del dic["apple"] #刪除字典的鍵值對 (Key-value pair)
print(dic)

dic={i:i*2 for i in [3,4,5]} #dic={i:i*2 for i in 列表} 
print(dic)
#用這套邏輯，去撰寫345的鍵值字典

#dic的兩種用法如下

test_1 = dict(test="cool",k=123) #第一種方式，是要用dict加上括弧，然後Key值不需要用""
test_2 = {"test":"cool","k":123} #第二種方式，就直接用大括弧就搞定。

print (test_1["test"])  #存取就直接用中括弧然後存取其中的Key值
print (test_2["k"])

# Python Dict就相當於其他語言的HashMap

#若找尋不在Hashmap裡面，會跳錯，這時候可以用.get語法來操作 語法：test_1.get("你要查找的Key值","你要自定義回傳的訊息") 預設是回傳None

print(test_1.get("haha"))