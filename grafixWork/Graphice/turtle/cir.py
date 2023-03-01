import turtle    # importing the module
trtl = turtle.Turtle()    #making a turtle object of Turtle class for drawing
screen=turtle.Screen()    #making a canvas for drawing
screen.setup(420,320)    #choosing the screen size
trtl.pencolor('red')    #making colour of the pen red
trtl.pensize(4)    #choosing the size of pen nib
trtl.shape('turtle')   #choosing the shape of pen nib
trtl.penup()   #moving the pen up
trtl.setpos(0,-60)   #setting new position
trtl.pendown()   #moving the pen down
trtl.circle(60)   #drawing circle with radius 60 pixels