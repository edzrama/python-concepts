from flask import Flask, render_template
from requests import get
from datetime import datetime


app = Flask(__name__)
posts = get("https://api.npoint.io/452f406e60db7aba52ff").json()


@app.route('/')
def home():
    year = datetime.now().year
    return render_template("index.html", posts=posts, year=year)


@app.route('/post/<int:post_id>')
def post(post_id):
    for blog_post in posts:
        if blog_post['id'] == post_id:
            return render_template("post.html", post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
