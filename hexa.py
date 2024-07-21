import turtle

for i in range(1,5):
    turtle.forward(100)
    turtle.right(90)

turtle.penup()
turtle.goto(-25,-50)
turtle.pendown()

turtle.left(45)
for i in range(1,5):
    turtle.forward(100)
    turtle.right(90)

turtle.done()