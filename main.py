from flask import Flask, render_template
from datetime import datetime
from crawl import crawl_stocks, crawl_pm25

# print(__name__)

app = Flask(__name__)
books = {
    1: {
        "name": "Python book",
        "price": 299,
        "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
    },
    2: {
        "name": "Java book",
        "price": 399,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
    },
    3: {
        "name": "C# book",
        "price": 499,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
    },
}


@app.route("/pm25")
def get_pm25():
    today = datetime.now()
    columns, values = crawl_pm25()
    datas = {
        "columns": columns,
        "values": values,
        "today": today.strftime("%y/%m/%d %H:%M:%S"),
    }
    return render_template("pm25.html", datas=datas)


@app.route("/stocks")
def get_stocks():
    datas = crawl_stocks()
    return render_template("stocks.html", stocks=datas)


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
    name = "Leo"
    # 等號左邊是前端的變數，右邊是後端的
    return render_template("index.html", date=today, name=name)


@app.route("/books")
# 取用dic的元素，在網頁中以JSON顯示
def show_books():
    for key in books:
        print(books[key])
    return render_template("books.html", books=books)


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
