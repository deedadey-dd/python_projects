from flask import Flask, render_template, request, redirect
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECr3+Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


# all_books = []


@app.route('/')
def home():
    all_books = Book.query.all()
    number_of_books = len(all_books)
    print(all_books)

    return render_template('index.html', book_num=number_of_books, books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():

    # book_data = {
    #     'name': request.form.get('name'),
    #     'author': request.form.get('author'),
    #     'rating': request.form.get('rating')
    # }
    # print(book_data)
    # print(type(book_data))
    # all_books.append(book_data)
    if request.method == 'POST':
        name = request.form.get('name')
        author = request.form.get('author')
        rating = request.form.get('rating')

        # print(f'title: {name}\nauthor: {author}\nrating: {rating}')
        new_book = Book(title=f'{name}', author=f'{author}', rating=f'{rating}')

        with app.app_context():
            db.session.add(new_book)
            db.session.commit()

        return redirect('/')
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # this is declared here in order to send the the value
    book_to_edit = Book.query.get(id)

    if request.method == 'POST':
        with app.app_context():
            # this is repeated because the query and the update should happen within the same app_context
            # else update will not take effect
            book_to_edit = Book.query.get(id)
            new_rating = request.form.get('new_rating')
            print(new_rating)
            book_to_edit.rating = new_rating

            db.session.commit()

        return redirect('/')
    return render_template('edit.html', book=book_to_edit)


@app.route('/delete/<int:id>')
def delete(id):
    with app.app_context():
        book_to_delete = Book.query.get(id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
