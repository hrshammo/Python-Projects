from graphics import *
# Create a window with a title
win = GraphWin("Animated Scenario", 800, 600)
# Create background objects
sky = Rectangle(Point(0, 0), Point(800, 400))
sky.setFill(color_rgb(79, 166, 255))
sky.draw(win)

sun = Circle(Point(700, 100), 70)
sun.setFill("yellow")
sun.draw(win)

cloud1 = Circle(Point(100, 100), 30)
cloud1.setFill("white")
cloud1.draw(win)

cloud2 = Circle(Point(200, 150), 40)
cloud2.setFill("white")
cloud2.draw(win)

city = Rectangle(Point(600, 200), Point(800, 600))
city.setFill(color_rgb(64, 67, 105))
city.draw(win)
city2 = Rectangle(Point(300, 350), Point(600, 600))
city2.setFill(color_rgb(62, 95, 112))
city2.draw(win)

road = Rectangle(Point(0, 500), Point(800, 800))
road.setFill("black")
road.draw(win)

# Create car object
car_body = Rectangle(Point(100, 450), Point(300, 500))
car_body.setFill(color_rgb(62, 69, 156))
car_body.draw(win)

car_window = Rectangle(Point(170, 460), Point(230, 490))
car_window.setFill("white")
car_window.draw(win)

car_wheel1 = Circle(Point(120, 510), 20)
car_wheel1.setFill(color_rgb(57, 57, 59))
car_wheel1.draw(win)

car_wheel2 = Circle(Point(280, 510), 20)
car_wheel2.setFill(color_rgb(57, 57, 59))
car_wheel2.draw(win)

# Move the objects
dx = 5
while True:
    # Move the background objects
    sun.move(-dx / 2, 0)
    cloud1.move(dx / 3, 0)
    cloud2.move(dx / 4, 0)
    city.move(-dx, 0)
    city2.move(-dx, 0)
    # Wrap the background objects around the screen
    if sun.getCenter().getX() < -50:
        sun.move(900, 0)
    if cloud1.getCenter().getX() > 850:
        cloud1.move(-1000, 0)
    if cloud2.getCenter().getX() > 850:
        cloud2.move(-1000, 0)
    if city.getP2().getX() < 0:
        city.move(1600, 0)
    if city2.getP2().getX() < 0:
        city2.move(1500, 0)
    # Move the car
    car_body.move(dx, 0)
    car_window.move(dx, 0)
    car_wheel1.move(dx, 0)
    car_wheel2.move(dx, 0)

    # Wrap the car around the screen
    if car_body.getP2().getX() < 0:
        car_body.move(800, 0)
        car_window.move(800, 0)
        car_wheel1.move(800, 0)
        car_wheel2.move(800, 0)

    # Pause for a moment
    time.sleep(0.02)

    # Update the window
    win.update()

# Close the window when done
win.close()
