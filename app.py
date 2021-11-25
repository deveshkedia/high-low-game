from flask import Flask
from random import randint

app = Flask(__name__)
random_number: int


@app.route('/')
def index():
    global random_number
    random_number = randint(0, 9)
    return "<h1>Guess a number between 0 and 9</h1>"\
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route('/<int:number>')
def guess_number(number):
    try:
        if number == random_number:
            return "<h1>You found Me</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
        elif number < random_number:
            return "<h1 style='color:red'>Too low,try again!</h1><br/><img src=' https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
        else:
            return "<h1 style='color:purple'>Too high,try again!</h1><br/><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    except NameError:
        return "Go to the main page first"


if __name__ == '__main__':
    app.run(debug=True)
