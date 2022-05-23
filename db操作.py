from flask import Flask, request, jsonify, render_template, url_for, redirect
from usesql.query import name_query

app = Flask(__name__)
app.config["DEBUG"] = True #會啟動Flask的Debug模式
app.config["JSON_AS_ASCII"] = False #解決Flask中文亂碼的問題

@app.route("/")
def home():
    return "<h1>Hello API!</h1>"

@app.route("/query", methods=['POST','GET'])
def query():
    if request.method == 'POST':
        if request.values['send']=='送出到資料庫查詢':
            query_name = request.values['user']
            
            try: #利用try來解決查詢不到東西的狀況
                return render_template("query.html", name=name_query(query_name)[0][1], number=name_query(query_name)[0][0],age=name_query(query_name)[0][2])
            except:
                return render_template("query.html", name="無此資料，請重新查詢", number="無此資料，請重新查詢",age="無此資料，請重新查詢")
        #if request.values['apply']=='註冊':
        #    apply_name = request.values['apply_']
            
    return render_template('query.html', name="尚未查詢", number="尚未查詢", age="尚未查詢")


if __name__ == "__main__":
    app.run(host = '127.0.0.1', port=3000)