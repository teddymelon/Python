def sayHello():
    print("Hello")

def say(msg):
    print(msg)
    return #函式回傳None

def add(n1,n2): #這個add的函式只知道n1、n2(多個參數)在這裡是什麼，呼叫的時候必須要逗點隔開
    result=n1+n2
    return result

sayHello()

say("Hello Function")
say("Hello Python")

add(10,20)

#呼叫函式，取得回傳值
value=say("Hello Function")
say("good")
print(value) #印出None

value=add(3,4)
add(3,4)
print(value)
'''
'''
#定義函式
def multiply(n1,n2):
    print(n1*n2)
    return n1*n2

#呼叫函式
#multiply(2,3)
#multiply(5,10)

#回傳值
value=multiply(5,4)+multiply(10,10)
print(value)

#程式的包裝 類似的工作一直做，很適合使用def
def calculate(max):
    sum=0
    for i in range(1,max+1):
        sum=sum+i
    print(sum)
     
for i in range(5):   
    num1=int(input("最大值:"))
    calculate(num1)

