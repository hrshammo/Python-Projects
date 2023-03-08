from graphics import *
import time

# create the graphics window
win = GraphWin("My City", 800, 600)

# create the background
sky = Rectangle(Point(0, 0), Point(800, 300))
sky.setFill('sky blue')
sky.draw(win)

sun = Circle(Point(50, 50), 30)
sun.setFill('yellow')
sun.draw(win)

road = Rectangle(Point(0, 300), Point(800, 600))
road.setFill('gray')
road.draw(win)

for i in range(4):
    buildings = Rectangle(Point(100 * i + 50, 300), Point(100 * i + 150, 550))
    buildings.setFill('gray')
    buildings.draw(win)

# create the moving objects
car = Image(Point(50, 450), "car.gif")
car.draw(win)

plane = Image(Point(800, 50), "plane.gif")
plane.draw(win)

# animate the scene
while True:
    car.move(5, 0)
    plane.move(-10, 0)
    time.sleep(0.1)
    if car.getAnchor().getX() > 800:
        car.move(-850, 0)
    if plane.getAnchor().getX() < -100:
        plane.move(900, 0)
