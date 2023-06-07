import turtle
from random import randint
import time

drawing_board =turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch The Turtle")
drawing_board.setup(width=600, height=600)

tur = turtle.Turtle()
tur.shape('turtle')
tur.color("green")
tur.penup()

tur.write("asdasd")




def showHideTurtle():
    tur.hideturtle()
    tur.goto(randint(-250, 250), randint(-200, 200)) # deqiqleshdirilmeli
    tur.showturtle()


for i in range(10):
    showHideTurtle()
    time.sleep(1)



turtle.done()