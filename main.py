from flask import Flask, render_template
from datetime import datetime

# print(__name__)

app = Flask(__name__)
books = {1: "python book", 2: "java book", 3: "flask book"}


@app.route("/bmi/name=<name>&height=<h>&weight=<w>")
# 使用GET方式傳遞
def getBmi(name, h, w):
    try:
        bmi = round(eval(w) / (eval(h) / 100) ** 2, 2)
        return f"{name} BMI:{bmi}"
    except Exception as e:
        print(e)
    return "<h1>參數錯誤</h1>"


@app.route("/sum/x=<x>&y=<y>")
def my_sum(x, y):
    # 參數不正確，輸出參數錯誤(try +except)
    try:
        total = eval(x) + eval(y)
        return f"{x}+{y}={total}"
    except Exception as e:
        print(e)
    return "<h1>參數錯誤</h1>"


@app.route("/")
def index():
    today = datetime.now()
    # print(today)
    # return f"<h1>hello flask<br>{today}</h1>"
    return render_template("index.html", date=today)


@app.route("/books")
# 取用dic的元素，在網頁中以JSON顯示
def show_books():
    return books


# @app.route("/book")
# def show_book():
#    return books[1]


@app.route("/book/<int:id>")
def show_book(id):
    # 輸出 有書<h1>第一本書:XXX</h1>
    # 無此編號
    if id not in books:
        return f"<h1 style='color:red'>無此編號:{id}</h1>"

    return f"<h1>第{id}本書:{books[id]}</h1>"


app.run(debug=True)
