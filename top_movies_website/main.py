from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIE_URL = 'https://api.themoviedb.org/3/search/movie'
MOVIE_API = '7c61aa5a3aa9d5bd335f8d0981bfc7f4'
ACCESS_TOKEN = ('eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YzYxYWE1YTNhYTlkNWJkMzM1ZjhkMDk4MWJmYzdmNCIsInN1YiI6IjY1NzVmM2M4YTFk'
                'MzMyMDEzOGVhNGVmOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lEAUe4rZl5HT9GhPm9y69oKwYJpouyz1L'
                'OvAXXn4s70')
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YzYxYWE1YTNhYTlkNWJkMzM1ZjhkMDk4MWJmYzdmNCIsInN1YiI6IjY"
                     "1NzVmM2M4YTFkMzMyMDEzOGVhNGVmOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lEAUe4rZl5HT9Gh"
                     "Pm9y69oKwYJpouyz1LOvAXXn4s70"
}

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(300), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


class MovieEditForm(FlaskForm):
    new_rating = StringField("Your Rating Out of 10 e.g. 7.6")
    new_review = StringField("Your Review")
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    movie_title = StringField("Movie Title")
    submit = SubmitField("Add Movie")


new_movie_data = None

# # initial movie added for testing
#
# title = "Phone Booth"
# year = 2002
# description = ("Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an "
#                "extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's "
#                "negotiation with the caller leads to a jaw-dropping climax.")
# rating = 7.3
# ranking = 10
# review = "My favourite character was the caller."
# img_url = "https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#
#
#


@app.route("/")
def home():
    all_movies = Movie.query.all()
    num_movies = len(all_movies)
    # print(all_movies)

    # result = db.session.execute(db.select(Movie))
    # all_movie = result.scalars()
    # print(all_movie)

    return render_template("index.html", movies=all_movies, num=num_movies)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # The declaration below is done in order to send the movie into the form for fetching its id.
    movie_to_edit = Movie.query.get(id)

    # This is using FlaskForms and flask-bootstrap

    form = MovieEditForm()
    if form.validate_on_submit():
        with app.app_context():
            movie_to_edit = Movie.query.get(id)
            movie_to_edit.rating = float(form.new_rating.data)
            movie_to_edit.review = form.new_review.data

            db.session.commit()
        return redirect('/')

    # if request.method == 'POST':
    #     new_rating = request.form.get('rating')
    #     new_review = request.form.get('review')
    #
    #     with app.app_context():
    #         movie_to_edit = Movie.query.get(id)
    #         movie_to_edit.rating = new_rating
    #         movie_to_edit.review = new_review
    #
    #         db.session.commit()
    #     return redirect('/')

    return render_template('edit.html', movie=movie_to_edit, form=form)


@app.route('/delete/<int:id>')
def delete(id):
    with app.app_context():
        movie_to_delete = Movie.query.get(id)
        db.session.delete(movie_to_delete)
        db.session.commit()

    return redirect('/')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    global new_movie_data
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        print(movie_title)
        parameters = {
            'query': movie_title
        }
        response = requests.get(MOVIE_URL, headers=headers, params=parameters)
        new_movie_data = response.json()
        num_of_results = len(new_movie_data['results'])
        print(f'new_movie_data = {new_movie_data}')

        return render_template('select.html', data=new_movie_data, results=num_of_results)

    return render_template('add.html', form=form)


@app.route('/select/<int:num>')
def adding(num):
    global new_movie_data
    print(new_movie_data)
    title = new_movie_data['results'][num]['original_title']
    year = int(new_movie_data['results'][num]['release_date'][:4])
    description = new_movie_data['results'][num]['overview']
    img_url = new_movie_data['results'][num]['backdrop_path']

    with app.app_context():
        existing_movie = Movie.query.filter_by(title=title).first()
        if existing_movie:
            if existing_movie.title == title and existing_movie.year == year:
                print("Movie already Exists")

        else:
            new_movie = Movie(title=title, year=year, description=description, rating=None, ranking=None,
                              review='', img_url=img_url)
            print("Movie Added")
            db.session.add(new_movie)
            db.session.commit()

    unrated_movie = Movie.query.filter_by(title=title).first()
    unrated_id = unrated_movie.id
    return render_template('edit.html', movie=unrated_movie, form=MovieEditForm())

    # return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
