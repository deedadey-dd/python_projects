from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECre+Key'

bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # return '<h2>The email is {}. The password is {}.'.format(login_form.email.data, login_form.password.data)
        if login_form.email.data == "admin@email.com" and login_form.password.data == '12345678':
            return render_template('success.html')
        elif login_form.email.data == "admin@email.com" and login_form.password != '12345678':
            return render_template('denied.html')

    return render_template('new_base.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
