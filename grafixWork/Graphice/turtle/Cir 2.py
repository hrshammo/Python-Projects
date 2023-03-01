import turtle    # importing the module
trtl = turtle.Turtle()    #making a turtle object of Turtle class for drawing
screen=turtle.Screen()    #making a canvas for drawing
screen.setup(420,320)    #choosing the screen size
trtl.pencolor('red')    #making colour of the pen red
trtl.pensize(4)    #choosing the size of pen nib
trtl.shape('turtle')   #choosing the shape of pen nib
n=0
while n<7:   #loop for 7 circles
    n=n+1
    trtl.penup()
    trtl.setpos(0,-n*20)
    trtl.pendown()
    trtl.circle(20*n)