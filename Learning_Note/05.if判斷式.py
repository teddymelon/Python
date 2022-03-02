#IF運算
'''
x = int(input("輸入數字："))

if x > 200:
    print("大於200")
elif x == 200:
    print("等於200")
elif x > 100:
    print("大於100，小於200")
elif x == 100:
    print("等於100")
else:
    print("小於100")
'''

n1=int(input("Num1: "))
n2=int(input("Num2: "))
op=input("請輸入運算:+, -, *, /: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")
