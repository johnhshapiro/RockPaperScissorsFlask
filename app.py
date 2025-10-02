from flask import Flask, render_template, request, redirect
from enum import Enum
import random

app  = Flask(__name__)

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(Enum):
    WIN = 1
    LOSS = 2
    DRAW = 3

def evaluate_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return Result.DRAW
    elif player_choice == Choice.ROCK and computer_choice == Choice.PAPER:
        return Result.LOSS
    elif player_choice == Choice.PAPER and computer_choice == Choice.SCISSORS:
        return Result.LOSS
    elif player_choice == Choice.SCISSORS and computer_choice == Choice.ROCK:
        return Result.LOSS
    elif player_choice == Choice.ROCK and computer_choice == Choice.SCISSORS:
        return Result.WIN
    elif player_choice == Choice.SCISSORS and computer_choice == Choice.PAPER:
        return Result.WIN
    elif player_choice == Choice.PAPER and computer_choice == Choice.ROCK:
        return Result.WIN

def play(player_choice):
    computer_choice = random.choice(list(Choice))
    result = evaluate_result(player_choice, computer_choice)
    return render_template('results.html', result=result, player_choice=player_choice, computer_choice=computer_choice)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rock/')
def rock():
    return play(Choice.ROCK)

@app.route('/paper/')
def paper():
    return play(Choice.PAPER)

@app.route('/scissors/')
def scissors():
    return play(Choice.SCISSORS)

if __name__ == "__main__":
    app.run(debug=True)
