
from flask import g


def say(msg="Hello"):
    print(msg)

say("Hello Function") #印出Hello Function
say() #印出預設資料


def dif(a=4, b=5):
    print(a,b)
#呼叫函式,以參數名稱對應資料
dif(b=2,a=3)

def infinite(*message):
    for i in message:
        print(i)

infinite("Hello","Cool","Girl")

def power(base,exp=0): #給預設值
    print(base**exp)

power(3,2) 
power(4) #若上面exp不給預設值，會產生錯誤

def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=2,n1=4)

def avg(*ns): #不管哪種呼叫方式，呼叫三個、四個、五個數字，使用不定參數 「*」
    sum = 0
    for i in ns:
        sum+=i
    print(sum/len(ns))

avg(3,4)

#不定參數 * ，印出來的東西會是Tuple
def test(*info):
    print(info)

test("a","b","c","d","e","f","g")
