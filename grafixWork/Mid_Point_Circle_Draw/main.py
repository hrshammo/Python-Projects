from graphics import *
def main():
    win= GraphWin("CSE 341",500,500)
    win.setBackground(color_rgb(158, 151, 222))

#circle
    pt1=Point(250,250)
    cir=Circle(pt1,120)

    cir.setFill(color_rgb(158, 201, 219))
    cir.setOutline(color_rgb(10, 30, 38))
    cir.setWidth(3)
    cir.draw(win)
#line
    ln=Line(Point(250,250),Point(165,165))
    ln.setWidth(3)
    ln.draw(win)
#triangle
    tri=Polygon(Point(250,250),Point(250,370), Point(370,250))
    tri.setWidth(3)
    tri.setFill(color_rgb(165, 214, 194))
    tri.draw(win)


    win.getMouse()
    win.close(win)

main()