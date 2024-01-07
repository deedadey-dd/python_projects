import datetime

from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


# # Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# #CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# #CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# #WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # body = StringField("Blog Content", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post", render_kw={'class': 'btn btn-primary', 'type': 'submit'})


def title_exists(new_title):
    article = BlogPost.query.filter_by(title=new_title).first()
    return article is not None

def format_date():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime('%B %d, %Y')
    return formatted_date


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.get(index)
    # for blog_post in posts:
    #     if blog_post["id"] == index:
    #         requested_post = blog_post
    # print(requested_post.body)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/edit/<int:index>", methods=['POST', 'GET', 'DELETE'])
def edit_post(index):
    post = BlogPost.query.get(index)

    form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body
    )

    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        author = form.author.data
        body = form.body.data
        img_url = form.img_url.data
        # date = post.date
        #
        # with app.app_context():
        #     # do we have to delete only some portions of the post object
        #     # or we delete the entire post and use
        #     db.session.delete(post)
        #     db.session.commit()
        #
        # if title_exists(title):
        #     return 'Title already exists'
        # else:
        #     with app.app_context():
        #         # # do we have to delete only some portions of the post object
        #         # # or we delete the entire post and use
        #         # db.session.delete(post)
        #         # db.session.commit()
        #
        #         payload = BlogPost(title=title, date=date, subtitle=subtitle, author=author, body=body,
        #                            img_url=img_url)
        #         db.session.add(payload)
        #         db.session.commit()

        with app.app_context():
            post.title = title
            post.subtitle = subtitle
            post.author = author
            post.body = body
            post.img_url = img_url
            db.session.commit()

        new_post = BlogPost.query.get(index)
        return render_template('post.html', post=new_post)

    return render_template('make-post.html', form=form, job='Edit Post')


@app.route("/new_post", methods=['POST', 'GET'])
def new_post():
    form = CreatePostForm()

    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        author = form.author.data
        body = form.body.data
        img_url = form.img_url.data

        if title_exists(title):
            return 'Title already exists'
        else:
            with app.app_context():
                payload = BlogPost(title=title, date=format_date(), subtitle=subtitle, author=author, body=body, img_url=img_url)
                db.session.add(payload)
                db.session.commit()
            return redirect(url_for('get_all_posts'))

    return render_template('make-post.html', form=form, job='New Post')


@app.route('/delete/<int:index>')
def delete(index):
    post_to_delete = BlogPost.query.get(index)
    with app.app_context():
        db.session.delete(post_to_delete)
        db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
