import turtle
s = turtle.Screen()
t = turtle.Turtle()

#huruf R
t.pensize(5)
t.penup()
t.goto(-100,-100)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.right(-180)
t.forward(50)
t.right(130)
t.forward(60)
t.left(35)
t.penup()
t.forward(50)

#angka 8
t.pencolor('blue')
t.pendown()
t.circle(30)
t.right(-90)
t.penup()
t.forward(60)
t.right(90)
t.pendown()
t.circle(30)
t.penup()

#angka 3
t.forward 100
