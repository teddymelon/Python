import random
#從列表中隨機選取資料
random.choice([0,1,5,8])

#從列表中選取特定個數的資料，本次示範選擇3個
random.sample([0,1,5,8,9],3)

#調換順序，將列表的資料「就地」隨機調換順序，會對列表本身做修改
data=[0,1,5,8]
print(data)
random.shuffle(data)
print(data)

#取得亂數 0.0 ~ 10.0 之間的隨機亂數
print(random.random())
print(random.uniform(0, 10)) #代表0-10之間的隨機亂數，且機率相同

#取得平均數100、標準差10的常態分配亂數，也就是取得的數字會在(平均數是在100，然後加減一個標準差的)，是以常態分配來分配。
#就是那個經典的錐形圖
print(random.normalvariate(100, 10))

import statistics

#計算平均數
num1=statistics.mean([1,4,6,9])
print(num1)

#計算中位數
num2=statistics.mean([1,2,3,4,5])
print(num2)

#計算標準差，來計算資料的分散狀況
num3=statistics.stdev([1,4,6,9])
print(num3)

#-------------------------------------------分割
data = random.uniform(0.0,10.0)
print(data)