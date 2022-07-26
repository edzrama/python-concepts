from flask import Flask, render_template, request
from requests import get
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.now().year
    return render_template("index.html", year=year)


@app.route("/guess", methods=['GET', 'POST'])
def guess():
    name = request.form['name']
    year = datetime.now().year
    gender = get(url=f"https://api.genderize.io?name={name}").json()["gender"]
    age = get(url=f"https://api.agify.io?name={name}").json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age, year=year)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/452f406e60db7aba52ff"
    all_posts = get(blog_url).json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
