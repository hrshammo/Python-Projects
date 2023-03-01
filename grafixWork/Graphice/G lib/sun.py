from graphics import *
def main():
    win = GraphWin("CSE 342", 500, 500)
    win.setBackground(color_rgb(255,255,255))

    #circle
    pt1 = Point(200, 200)
    cir = Circle(pt1, 80)
    cir.setFill(color_rgb(255,220,0))
    cir.setOutline(color_rgb(255,220,0))
    cir.draw(win)

    #line1
    ln1 = Line(Point(80, 200), Point(120, 200))
    ln1.draw(win)
    #line2
    ln2 = Line(Point(200, 80), Point(200, 120))
    ln2.draw(win)
    #line3
    ln3 = Line(Point(280, 200), Point(320, 200))
    ln3.draw(win)
    #line4
    ln4 = Line(Point(200, 280), Point(200, 320))
    ln4.draw(win)
    #line5
    ln5 = Line(Point(80, 120), Point(120, 150))
    ln5.draw(win)
    #line6
    ln6 = Line(Point(280, 150), Point(320, 120))
    ln6.draw(win)
    # Upper Part Done
    #line7
    ln7 = Line(Point(280, 260), Point(320, 280))
    ln7.draw(win)
    #line6
    ln8 = Line(Point(80, 280), Point(120, 260))
    ln8.draw(win)

    win.getMouse()
    win.close()
main()