from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_func():
        val = function()
        return f"<b>{val}</b>"
    return wrapper_func


def make_emphasis(function):
    def wrapper_func():
        val = function()
        return f"<em>{val}</em>"
    return wrapper_func


def make_underline(function):
    def wrapper_func():
        val = function()
        return f"<u>{val}</u>"
    return wrapper_func


@app.route("/")
def hello_world():
    return ("<h1  style='text-align: center'>Hello, World!</h1>"
            "<p>This is paragraph</p>"
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDkxeHVuN21oNmh5aHl0N241ODkzZGl4dzBtcXo0NG1hcDVtbXVvciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yFQ0ywscgobJK/giphy.gif'/>")


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye!"


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}. You are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
