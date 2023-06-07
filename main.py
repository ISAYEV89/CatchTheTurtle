import turtle
from random import randint
from threading import Timer

drawing_board =turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch The Turtle")
drawing_board.setup(width=600, height=600)

tur = turtle.Turtle()
tur.shape('turtle')
tur.color("green")
tur.penup()


def showHideTurtle():
    tur.hideturtle()
    tur.goto(randint(-250, 0), randint(0, 200))
    tur.showturtle()


Timer(1, showHideTurtle).start()

turtle.done()