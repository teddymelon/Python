#類別是Py裡面的語法結構，可以把變數 or 函式封裝起來，這些封裝起來的東西，被稱作「類別的屬性」
#要先定義(建立)類別，然後才能使用類別中的屬性

#如何定義類別?

#class 類別名稱:
#    定義封裝的變數
#    定義封裝的函式

class Test:
    x = 3 #定義變數
    def say(word):
        return print(word)

#如何使用?
#類別名稱.屬性名稱

print(Test.x + 3)
Test.say("Hello")

class IO:
    supportedSrcs = ["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read From", src)

print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")