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


count = 0

timer_text = turtle.Turtle('circle', visible=False)
timer_text.penup()
# timer_text.clear()
timer_text.write('Score: 0', move=False, font=("Courier", 30))
# timer_text.setpos(-250,250)
timer_text.goto(-75, 270)
def clickTurtle(x,y):
    global count
    count = count + 1
    timer_text.clear()
    timer_text.goto(-75, 270)
    timer_text.write(f'Score: {count}', font=("Courier", 16))



tur.onclick(clickTurtle)


# turtle random gelmesi
for i in range(2):
    tur.hideturtle()
    tur.goto(randint(-250, 250), randint(-200, 200))  # deqiqleshdirilmeli
    time.sleep(0.5)
    tur.showturtle()
    time.sleep(5)



turtle.done()