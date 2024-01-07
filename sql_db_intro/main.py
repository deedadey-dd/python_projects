import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
#
# # Create a table with the following fields or columns id, title, author, rating
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, "
# #                "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# # Enter an entry into the table
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///all_books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, unique=True, nullable=False)


# This is optional and allow each book object to be identified by its title when printed
def __repr__(self):
    return f'<Book {self.title}>'


# Create the Database
# without the app context, there will be an error.
with app.app_context():
    db.create_all()
    # Create a Record
    new_book = Book(id=1, title='Harry Potter', author='J. K. Rowling', rating=8.3)
    db.session.add(new_book)

with app.app_context():
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
