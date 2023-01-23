from matplotlib import pyplot as plt


def dda(x0, y0, x1, y1):
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

        print("x=", x0, end=", ")
        print("y=", round(y0, 2), end="\n")

        xlist.append(x0)
        ylist.append(y0)

    plt.plot(xlist, ylist, linestyle='--', marker='+')
    plt.show()


print('Insert 1st point:')
x0 = int(input())
y0 = int(input())
print('Insert last point')
x1 = int(input())
y1 = int(input())

dda(x0, y0, x1, y1)