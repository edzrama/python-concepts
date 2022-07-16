# save this as app.py
from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper


def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper



@app.route("/")
def hello():
    # return "Hello, World!"
    return '<h1 style="text-align: center">Hello, World! </h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://c.tenor.com/ZhfMGWrmCTcAAAAM/cute-kitty-best-kitty.gif"> '


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "bye!"


@app.route("/username/<name>")
# @app.route("/username/<name>/<int:num>")
def greet(name):
    return f"hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)