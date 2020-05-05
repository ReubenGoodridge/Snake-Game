# Imports
from turtle import Turtle, Screen
import time
import random
import winsound

# Define Globals
delay = 0.1
score = 0
hscore = 0

# Screen setup
wn = Screen()
wn.title('Snake')
wn.bgcolor('green')
wn.bgpic('background.gif')
wn.setup(600, 600)
wn.tracer(0)

# Register Images
wn.register_shape('apple.gif')
wn.register_shape('head.gif')
wn.register_shape('headd.gif')
wn.register_shape('headl.gif')
wn.register_shape('headr.gif')
wn.register_shape('segmentu.gif')
wn.register_shape('segmentd.gif')
wn.register_shape('segmentl.gif')
wn.register_shape('segmentr.gif')

# Player
p = Turtle()
p.shape('head.gif')
p.color('black')
p.speed(10)
p.penup()
p.goto(0, 0)
p.direction = 'stop'

# Body Growth
bs = []

# Food
f = Turtle()
f.shape('apple.gif')
f.color('red')
f.speed(10)
f.penup()
f.goto(0, 100)

# Pen
pen = Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.ht()
pen.goto(0, 260)
pen.write('Score: {} Highscore: {}'.format(score, hscore), align='center', font=('Courier', 24, 'normal'))


# Functions


def gu():
    if p.direction != 'down':
        p.direction = 'up'
        p.shape('head.gif')
        winsound.PlaySound('grass.wav', winsound.SND_ASYNC)


def gd():
    if p.direction != 'up':
        p.direction = 'down'
        p.shape('headd.gif')
        winsound.PlaySound('grass.wav', winsound.SND_ASYNC)


def gl():
    if p.direction != 'right':
        p.direction = 'left'
        p.shape('headl.gif')
        winsound.PlaySound('grass.wav', winsound.SND_ASYNC)


def gr():
    if p.direction != 'left':
        p.direction = 'right'
        p.shape('headr.gif')
        winsound.PlaySound('grass.wav', winsound.SND_ASYNC)


def move():
    if p.direction == 'up':
        y = p.ycor()
        p.sety(y + 20)

    if p.direction == 'down':
        y = p.ycor()
        p.sety(y - 20)

    if p.direction == 'left':
        x = p.xcor()
        p.setx(x - 20)

    if p.direction == 'right':
        x = p.xcor()
        p.setx(x + 20)


wn.listen()
wn.onkeypress(gu, 'w')
wn.onkeypress(gd, 's')
wn.onkeypress(gl, 'a')
wn.onkeypress(gr, 'd')

# Main Game Loop
while True:
    wn.update()

    # Border Collisions
    if p.ycor() > 290 or p.ycor() < -290 or p.xcor() > 290 or p.xcor() < -290:
        time.sleep(1)
        p.goto(0, 0)
        p.direction = 'stop'
        for s in bs:
            s.goto(10000, 10000)
        bs.clear()
        score = 0
        pen.clear()
        pen.write('Score: {} Highscore: {}'.format(score, hscore), align='center', font=('Courier', 24, 'normal'))

    # Food Collisions
    if p.distance(f) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        f.goto(x, y)
        score += 10
        if score > hscore:
            hscore = score
        pen.clear()
        pen.write('Score: {} Highscore: {}'.format(score, hscore), align='center', font=('Courier', 24, 'normal'))
        # Add new segment
        ns = Turtle()
        ns.speed(0)
        if p.direction == 'up':
            ns.shape('segmentu.gif')
        if p.direction == 'down':
            ns.shape('segmentd.gif')
        if p.direction == 'left':
            ns.shape('segmentl.gif')
        if p.direction == 'right':
            ns.shape('segmentr.gif')
        ns.color('black')
        ns.penup()
        bs.append(ns)
        winsound.PlaySound('munch.wav', winsound.SND_ASYNC)

    for index in range(len(bs)-1, 0, -1):
        x = bs[index-1].xcor()
        y = bs[index-1].ycor()
        bs[index].goto(x, y)

    if len(bs) > 0:
        x = p.xcor()
        y = p.ycor()
        bs[0].goto(x, y)

    move()

    # Body Collisions
    for s in bs:
        if s.distance(p) < 20:
            time.sleep(1)
            p.goto(0, 0)
            p.direction = 'stop'
            for segments in bs:
                segments.goto(10000, 10000)
            bs.clear()
            score = 0
            p.direction = 'stop'
            pen.clear()
            pen.write('Score: {} Highscore: {}'.format(score, hscore), align='center', font=('Courier', 24, 'normal'))

    for ns in bs:
        if p.direction == 'up':
            ns.shape('segmentu.gif')
        if p.direction == 'down':
            ns.shape('segmentd.gif')
        if p.direction == 'left':
            ns.shape('segmentl.gif')
        if p.direction == 'right':
            ns.shape('segmentr.gif')

    time.sleep(delay)

wn.mainloop()