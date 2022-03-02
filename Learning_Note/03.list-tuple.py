
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
print(a[0])