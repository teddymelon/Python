'''
#裝飾器是一個函式

def 裝飾器名稱(回呼函式名稱) #回呼函式
    def 內部函式名稱():
        #裝飾器內部的程式碼
        回呼函式名稱()
    return 內部函式名稱
#按照上述的規則結構，產出的稱為裝飾器

#如何使用裝飾器?

@裝飾器名稱   # @是所謂的程式設計語法糖，對功能沒有影響，但是能夠讓程式更加簡潔。
def 函式名稱():
    #函式內部的程式碼

#上述這包，就是包含了裝飾器函式
#裝飾器:
#1.也是函式
#2.可以接受函式做為參數，並且返回函式
#3.在不改變原有函式結構的情況下增加新功能
#4.

函式名稱() #呼叫帶有裝飾器的函式。
'''

#def testDecorator(callback):
#    def innerFunc():
#        print("裝飾器函式")
#        callback()
#    return innerFunc

#@testDecorator
#def decoratedFunc():
#    print("普通函式")

#有了裝飾器後，我們怎麼運用函式來工作？

from tkinter import N


def testDecorator(callback):
    def innerFunc(inner_data):
        print("裝飾器函式")
        print(inner_data)
        callback("裡面的程式碼")    #callback才是真正對應到下方decorated，所以下方函式想要帶參數，就要放在這邊的Callback
    return innerFunc

@testDecorator
def decoratedFunc(data):
    print("普通函式"+"加上", data)

decoratedFunc("Inner_Func的資料")  #一般來說，一般函式我們要加個參數(Parameter)進去，我們直接在decoratedFunc裡面加參數就好。若要使用裝飾器，就必須先呼叫Callback，

#如果不用@這類型的語法糖，就要撰寫如下方:
#testDecorator(decoratedFunc)("Inner_Func的資料")

#重要!裝飾器其實是為了避免重複勞動，因為當有類似的功能要執行的時候，不必每次都寫一次。
#此外，請注意，testDecorator這個裝飾器函式，裡面包的inner函式，才是我們要執行的。

#也就是說，testDecorator(decoratedFunc)，實質上會先把decoratedFunc(做為callback)丟進testDecorator，接著被整併進innerFunc，然後整個testDecorator會回給你一個把decoratedFunc包進去的整包函式(也就是innerFunc)，接著記得再用一個()，因為函式回傳的是另一個函式。


def calculate(callback):
    def run():                #----------------
        result = 0
        for n in range(51):   #這是我們想讓裝飾器作的事情。
            result += n
        print (result)        #----------------
        callback()            #我們下方的主要函式
    return run

@calculate
def show():
    print("普通函式的程式碼")

#實際應用，我想重複運用1加到50的運算功能，我就可以用裝飾器。
def calculate(callback):
    def run():
        #裝飾器想要執行的程式碼
        result = 0
        for n in range(51):
            result += n
        #把計算結果透過參數傳到被裝飾的普通函式中。
        callback(result)
    return run

@calculate
def show(n):
    print("計算結果是", n)

@calculate
def showEnglish(n):
    print("Result is", n)

show()
showEnglish()