from flask import Flask, request
import random

app = Flask(__name__)
secret_num = random.randint(0, 9)
print(secret_num)


@app.route('/')
def home_page():
    return ('<h1>Guess a number...</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route('/<int:num>')
def check_number(num):

    if num == secret_num:
        return ('<h1>You found me!!!</h1>'
                '<img src="https://media.giphy.com/media/xUOrwiqZxXUiJewDrq/giphy.gif">')
    elif num < secret_num:
        return ('<h1>Too low, Try Again...</h1>'
                '<img src="https://media.giphy.com/media/wdh1SvEn0E06I/giphy.gif">')
    else:
        return ('<h1>Too high, Try Again...</h1>'
                '<img src="https://media.giphy.com/media/79eQOjPPrisR9B2zy6/giphy.gif">')


if __name__ == '__main__':
    app.run(debug=True)
