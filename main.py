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

# turtle random gelmesi
for i in range(10):
    tur.hideturtle()
    tur.goto(randint(-250, 250), randint(-200, 200))  # deqiqleshdirilmeli
    time.sleep(0.5)
    tur.showturtle()
    time.sleep(1)




# timer_text.clear()
# timer_text.write(i, font=("Courier", 30))



timer_text = turtle.Turtle('circle', visible=False)
timer_text.penup()



turtle.done()