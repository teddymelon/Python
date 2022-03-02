#break
n=1
while n<5:
    if n==3:
        break
    n+=1

print(n)

n=0
for i in [0,1,2,3]:
    if i%2==0:
        continue #直接進入下一圈，不會跑下面的n+=1
    n+=1
print(n) #原先要加4次，但是因為continue的存在，被跳過兩次

n=1
while n<5:
    n+=1
    print("變數n的資料是:",n)
else:
    print(n)


for c in "Hello":
    print(c)
else:
    print(c)

n=0
while n<5:
    if n==3:
        break
    print(n)
    n+=1
print("最後的n:",n)

n=0
for i in [0,1,2,3]:
    if i%2==0:
        continue
    print(i)
    n+=1
print("最後的n",n)

sum=0
for n in range(11):
    sum+=n
else:
    print(sum)

#綜合範例: 找出整數平方根
#輸入9 得到3
#輸入11 得到沒有整數的平方根

n=int(input("輸入一個正整數:"))
for i in range(n):
    if i*i==n:
        print("整數平方根",i)
        break #用break強制結束迴圈，不會執行else區塊
else:
    print("沒有整數平方根")
