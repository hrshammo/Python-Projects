import matplotlib
import matplotlib.pyplot as plt
def DDA(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    m = dy / dx
    steps = max(dx, dy)
    xlist = []
    ylist = []
    for i in range(steps):
        if m < 1:
            x0 = x0 + 1
            y0 = y0 + m
        elif m == 1:
            x0 = x0 + 1
            y0 = y0 + 1
        elif m > 1:
            x0 = x0 + 1 / m
            y0 = y0 + 1

        print("x= ", round(x0, 1), end=",")
        print("y= ", round(y0, 0), end="\n")
        xlist.append(round(x0, 1))
        ylist.append(round(y0, 1))
    plt.plot(xlist, ylist, linestyle="--", marker="*")
    plt.show
# main func
x0 = int(input("Enter x0 :"))
y0 = int(input("Enter y0 :"))
x1 = int(input("Enter x1 :"))
y1 = int(input("Enter y1 :"))
DDA(x0, y0, x1, y1)
