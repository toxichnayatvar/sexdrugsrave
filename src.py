import turtle

def square(a):
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
square(100)

def red_circle(radius):
    turtle.fillcolor('#ff0000') #red color
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

red_circle(100)

def blue_square(a):
    turtle.fillcolor('#0000ff') # blue color
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.end_fill()

blue_square(100)


turtle.done()