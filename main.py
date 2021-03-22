'''
03/22/2021
Introduction to Turtle
# 1. Import turtle library import turtle

# 2. Create a pen/turtle
variable=turtle.Turtle()

# 3. Create a paper/screen
variable2 = turtle.Screen()

# 4. Movements

    a. Move forward
    variable1.forward(DISTANCE)
    variable1.fd(DISTANCE)

    b. Move backward
    variable1.backward(DISTANCE)
    variable1.bk(DISTANCE)

    c. Turn right
    variable1.right(ANGLE)
    
    d. Turn left
    variable1.left(ANGLE)

    e. Pen up
    variable1.penup()

    f. Pen down
    variable1.pendown()

    g. Go to home(origin 0,0)
    variable1.home()
    
    h. Go to a specific point
    variable1.goto(X,Y)
'''
'''
import turtle

pen = turtle.Turtle() #Origin (0,0)
pen.forward(100)      #(100,0)
pen.backward(200)     #(-100,0)

pen.left(90)
pen.right(180)
pen.left(1800)

#DRAW a Window

------------------------------
|               |             |
|               |             |                |
|               |             |
|               |             |
|               |             |
|               |             |
------------------------------
'''
'''
import turtle

pen = turtle.Turtle()
pen.forward(300)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(150)
pen.left(180)
#pen.backward(150)
pen.forward(150)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(150)
'''
#DRAW a house
import turtle

pen = turtle.Turtle()
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(45)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(135)
pen.forward(142)
#pen.left(180)
pen.backward(145)


pen.right(90)
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(70)
pen.right(90)
pen.forward(40)
pen.right(90)
pen.forward(70)
pen.penup()
pen.backward(70)
pen.left(90)
pen.forward(30)

#pen.penup()
pen.pendown()

pen.right(45)
pen.forward(25)
pen.right(90)
pen.forward(25)
pen.right(90)
pen.forward(25)
pen.right(90)
pen.forward(25)

#pen.penup()
#pen.goto(0,0)
#pen.home()
