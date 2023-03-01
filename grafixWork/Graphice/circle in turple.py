import turtle

def draw_circle(center_x, center_y, radius):
    turtle.penup()
    turtle.goto(center_x, center_y - radius)
    turtle.pendown()

    x = 0
    y = radius
    p = 1 - radius

    while x <= y:
        turtle.goto(center_x + x, center_y + y)
        turtle.goto(center_x + x, center_y - y)
        turtle.goto(center_x - x, center_y + y)
        turtle.goto(center_x - x, center_y - y)
        turtle.goto(center_x + y, center_y + x)
        turtle.goto(center_x + y, center_y - x)
        turtle.goto(center_x - y, center_y + x)
        turtle.goto(center_x - y, center_y - x)

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

# Example usage
draw_circle(0, 0, 100)
turtle.done()
