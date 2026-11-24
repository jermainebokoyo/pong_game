# learing how to make a pong game with python 3
# by jermaine
# part 1

import time
import turtle

wn = turtle.Screen()
wn.title("pong by Jae")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paaddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("gray")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Pen (scoring)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def show_score():
    pen.clear()
    pen.write(
        "Player A: {}  Player B: {}".format(score_a, score_b),
        align="center",
        font=("Courier", 24, "normal"),
    )

def keep_on_screen(paddle, y):
    # Stay under the score line. The paddle is 100px tall.
    if y > 200:
        return 200
    if y < -250:
        return -250
    return y

# Function for paddle a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(keep_on_screen(paddle_a, y))

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(keep_on_screen(paddle_a, y))

# Function for paddle b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(keep_on_screen(paddle_b, y))

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(keep_on_screen(paddle_b, y))

# Keyboard binding for paddle a
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# Keyboard binding for paddle b
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    time.sleep(0.01)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        show_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        show_score()

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
