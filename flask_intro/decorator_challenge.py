from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        result = function()
        return f"<b>{result}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        result = function()
        return f'<em>{result}</em>'
    return wrapper


def make_underlined(function):
    def wrapper():
        result = function()
        return f'<u>{result}</u>'
    return wrapper


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def welcome():
    return ('You are Welcome to the Home Page!'
            '<input type="text" id="uname"><br><br>')


results = welcome()
print(results)

if __name__ == '__main__':
    app.run(debug=True)


