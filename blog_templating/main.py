from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def post(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()

    return render_template('post.html', blog_index=num, posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)
