import turtle
turtle.speed(0.5)
turtle.hideturtle()
screen = turtle.Screen()
screen.bgcolor('black')
turtle.color('white')

for i in range(5,13):
    turtle.right(45)
    for i in range(1,15):
        turtle.circle(2*i+80)
        turtle.up()
        turtle.goto(0,0)
        turtle.down()


    
    
    

turtle.done()