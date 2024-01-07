from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps', validators=[DataRequired(), URL()])
    opening = StringField('Opening Time e.g. 8:00AM', validators=[DataRequired()])
    closing = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    Coffee_Rating = SelectField('Coffee Rating', validators=[DataRequired()], choices=['☕️', '☕️☕️',
                                                                            '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi_strength = SelectField('WiFi Strength Rating', validators=[DataRequired()], choices=['✘', '💪',
                                                                    '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power_available = SelectField('Power Socket Availability', validators=[DataRequired()], choices=['✘',
                                                    '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, Wi-Fi rating, power outlet rating fields
# make coffee/Wi-Fi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit() and request.method == 'POST':
        # print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        new_cafe = (f'\n{form.cafe.data},{form.location.data},{form.opening.data},{form.closing.data},'
                f'{form.Coffee_Rating.data},{form.wifi_strength.data},{form.power_available.data}')
        # print(new_cafe)
        with open('cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
            csv_file.write(new_cafe)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file)
        list_of_rows = []

        for row in csv_data:
            list_of_rows.append(row)
        # print(list_of_rows)
        number_of_rows = len(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, rows=number_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
