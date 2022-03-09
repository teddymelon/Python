
#有序可變動列表 List
'''
grades=[12,60,15,70,90]
grades[1:4]=[] #刪除的作法
grades=grades+[12,33]
length=len(grades)
print(length)
'''

#巢狀列表
'''
data=[[3,4,5],[6,7,8]]
#data[0][0:]=[3,3,3,3,3,3,3,3,3]
print(data[0])
del data[0]
print(data[0])
print(data)
'''
#代表第一層的第二個元素，可以通過這個方法來拆解巢狀列表


#有序不可變動列表 Tuple
'''
grades=[12,60,15]
grades=grades+[11,33]
print(grades)
'''


data=(3,4,5)
print(data[0:2])
#data=[0]=5 #錯誤：Tuple的資料不可變動
#tuple 與串列主要有三點不同：

#1.使用的符號不同
#tuple ，用小括號表示 。
#例如 (‘a’, ‘b’)。

#2.串列，用中括號表示 。
#例如 [‘a’, ‘b’]。
#tuple屬於不可變的資料型態
#不可變（Immutable）是什麼意思？
#就是你不可以修改、增減tuple的值。
#也因為 tuple 不可變的特性，所以沒有append()、remove()、pop()等會更動值的操作。
#只含有一個項目時，要加上逗點
#當你要建立只有一個項目的 tuple，千萬要記得加上逗號，否則不會建立 tuple。

'-----------------------------------------------------------------------------------'

#列表學習

a = [1,2,3]
b = [1 , 'abc' , 2.0 , ['a', 'b' , 'c']]

print(a)
print(b)
print(b[3][0], a[0], end = "\n", sep = "-") #按下control然後再按print，會看到print的function，end後面預設是接"/n"；然後sep是分割符號，預設是空白。

c = b[1:3]

print(c, type(c))

s = 'abcdef'

print(s[1:3], s[-1])

print(b[-1])  #-1代表的是最後一個數字，index都從0開始。

'-----------------------------------------------------------------------------------'

#list的操作

list_1 = [9, -1, -4, 3, 7, 11, 3]

print("List_1的長度=", len(list_1)) #List的長度

print("List的最大值=", max(list_1)) #找最大值

print("List裡的最小值=", min(list_1)) #找最小值

print("List裡'3'這個元素出現過{}次".format(list_1.count(3)))
print(f"List裡'3'這個元素出現過{list_1.count(3)}次") #兩種字串格式化的方法，都是透過 list.count(x) 來作計數

#List的改動
list_2 = ["a",'b',"c","d"]

#給List結尾加一個新元素
list_2.append("e")
print("list_2=", list_2)

#在list2的a、c加入一個b元素，在某個index"前"面插入某個參數
list_2.insert(1,'b')
print("list_2=", list_2)

#刪除列表裡的某個參數
list_2.remove("b")
print("list_2=", list_2)  #如果有重複參數需要刪除，可以使用while迴圈如下
"----------------------------------------------"
target = 'dog'
list = ['cat', 'dog', 'dog', 'pig', 'dog']
while(target in list):
    list.remove(target)
"----------------------------------------------"

list_2.pop(1) #刪除特定index位置的元素，或者使用del list[x]
print(list_2)

del list_2[0:2] #代表刪除從 0,1 index的資料，2的index元素則不會影響。
print(list_2)


#修改index所代表的值
list_2[0] = "1"
print(list_2)

#如果是字串，沒有辦法跟列表一樣進行修改，只能整組替換
#a = '123'
#a[0] = 'a' 會跳錯
#a = 'abc'

#列表翻轉

list_3 = [1,2,3]
list_3.reverse() #排序反轉
print(list_3)


list_4 = [9, -1, -4, 3, 7, 11, 3]
list_4.sort(reverse = False,key = int) #排序，如果加reverse也可以，若為True則由大到小，False則由小到大。
print(list_4)

list_5 = [1,0,-5,-7]
list_5.sort()
print(list_5)

"---------------------------------------------------------------"
#Tuple 元組

a = (1,2,3)   #Tuple的寫法
b = 1,        #Tuple的寫法
print(type(a))
print(type(b))

print(a[1])
print(a[1:])
print(a[-1])


#Tuple的改變?
tuple1 = ('a','b','c')
#tuple1[0] = 2   無法操作，代表排序、翻轉、抽換都不行

print(tuple1.index('b')) #去找在Tuple內的值，是第幾個Index。

#List v.s Tuple
'Tuple是不可變的Python的對象，只需要固定的內存，immutable的'

'List是可變的，mutable，python對象，需要兩個內存空間，一個用來儲存實際的列表數據，一塊是可變動的空間用於擴展。'
#Tuple創建和訪問要比列表還要快，但是不如列表靈活。

#若數據量小，使用List或者Tuple都無所謂，但若是絕對不允許改變，則可以使用Tuple。
