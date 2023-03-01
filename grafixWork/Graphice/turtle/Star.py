import turtle
import time
screen=turtle.Screen()
trtl=turtle.Turtle()
screen.setup(420,320)
screen.bgcolor('black')
clr=['red','green','blue','yellow','purple']
trtl.pensize(4)
trtl.penup()
trtl.setpos(-90,30)
trtl.pendown()
for i in range(5):
     trtl.pencolor(clr[i])
     trtl.forward(200)
     trtl.right(144)
trtl.penup()
trtl.setpos(80,-140)
trtl.pendown()
trtl.pencolor('olive')
trtl.write('Vivax Solutions',font=("Arial", 12, "normal"))
trtl.ht()