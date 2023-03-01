from matplotlib import pyplot as plt


def midPoint(x, y, x1, y1):
    dx = x1 - x
    dy = y1 - y
    d = dy - (dx / 2)
    xlist = [x]
    ylist = [y]
    while (x < x1):
        x = x + 1
        if (d < 0):
            d = d + dy
        else:
            d = d + dy - dx
            y = y + 1
        xlist.append(x)
        ylist.append(y)
        print("x=", x, end=", ")
        print("y=", y, end="\n ")
    plt.plot(xlist, ylist, linestyle="--", marker="+")
    plt.show()


# main Function
print("Enter Initial Point: ")
x = int(input())
y = int(input())

print("Enter Finishing Point: ")
x1 = int(input())
y1 = int(input())
midPoint(x, y, x1, y1)