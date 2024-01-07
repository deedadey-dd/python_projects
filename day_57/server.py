from flask import Flask, render_template
import random
import datetime
import requests

agify_url = 'https://api.agify.io'
gender_url = 'https://api.genderize.io'


app = Flask(__name__)

# parameters = {
#     'name': 'dennis',
# }
# age_response = requests.get(agify_url, params=parameters)
# age = age_response.json()['age']
# gender_response = requests.get(gender_url, params=parameters)
# gender = gender_response.json()['gender']
# print(parameters['name'].title())
# print(age)
# print(gender)

@app.route('/')
def home_page():
    random_number = random.randint(0, 10)
    this_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=this_year)


@app.route('/<name>')
def guessed_page(name):
    parameters = {
        'name': name,
    }
    age_response = requests.get(agify_url, params=parameters)
    age = age_response.json()['age']
    gender_response = requests.get(gender_url, params=parameters)
    gender = gender_response.json()['gender']

    named = name.title()

    this_year = datetime.datetime.now().year
    return render_template('guessed.html', name=named, age=age, gender=gender, year=this_year)


if __name__ == "__main__":
    app.run(debug=True)
