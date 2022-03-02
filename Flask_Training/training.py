from flask import Flask

app = Flask(__name__) #__name__代表目前執行模組。__name__是內建的py變數，會儲存這個程式在哪個模組下執行，如果程式被當成主程式來執行，__name__會被當成__main__，所以才有 if __name__ == __main__的用法，但假如這支程式被拿來當成模組來運行，則此時__name__ 會變成是這支程式的名字。

@app.route("/") #函式的裝飾 (Decorator): 以下方函式為基礎，提供附加的功能。
def home():
    return "Hello Flask 2" #回給瀏覽器

@app.route("/haha")
def test():
    return "this is a fucking test!"

if __name__ == "__main__": #如果以主程式執行
    app.run(host="127.0.0.1", port=8080) #則立刻啟動伺服器 #run是Flask的Function，後面可以接host跟port。

