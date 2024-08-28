from flask import Flask
import random

number = random.randint(0, 9)
print(number)

app = Flask(__name__)


@app.route("/")
def main_page():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://i.giphy.com/media/v1"
            ".Y2lkPTc5MGI3NjExZmt5dWZkN2dsbjZqYTIwMzJjdmJubW0ycXQ3OTFzcjNraGg0NWc1eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2Pum9csX8vN3a7COmS/giphy.gif'/>")


@app.route("/<int:num>")
def check_guess(num):
    if num < number:
        return ("<h1 style='color: red'>It's too low, Try Again</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />")
    elif num > number:
        return ("<h1 style='color: purple'>It's too High, Try Again</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />")
    else:
        return ("<h1 style='color: green'>You found Me!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />")


if __name__ == "__main__":
    app.run(debug=True)
