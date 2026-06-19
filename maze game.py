import turtle


r = turtle.Turtle()
a = turtle.Turtle()
s = turtle.Screen()

s.bgpic("maze.gif")

s.addshape("austronaut.gif")
a.shape("austronaut.gif")
a.penup()
a.goto(-100,290)

s.addshape("rocket.gif")
r.shape("rocket.gif")
r.penup()
r.goto(180,-280)


#movement
def up():
    r.setheading(90)
    r.forward(10)
    r.setheading(0)
def down():
    r.setheading(270)
    r.forward(10)
    r.setheading(0)
def left():
    r.setheading(180)
    r.forward(10)
    r.setheading(0)
def right():
    r.forward(10)

#button click
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()

#congrats
while True:
    s.update()
    if r.distance(a) < 10:
        s.bgpic("congrates.gif")
    
turtle.done()