from matplotlib import pyplot as plt
def midPointCircle(x0, y0, r):
    x = 0
    y = r
    xlist = [0]
    ylist = [y]
    Octa1x = [x + x0]
    Octa1y = [y + y0]
    Octa2x = [y + y0]
    Octa2y = [x + x0]
    Octa3x = [y + y0]
    Octa3y = [-(x + x0)]
    Octa4x = [x + x0]
    Octa4y = [-(y + y0)]
    Octa5x = [-(x + x0)]
    Octa5y = [-(y + y0)]
    Octa6x = [-(y + y0)]
    Octa6y = [-(x + x0)]
    Octa7x = [-(y + y0)]
    Octa7y = [x + x0]
    Octa8x = [-(x + x0)]
    Octa8y = [y + y0]
    d = 1 - r
    # print("d0",d)
    print("X= ", x + x0, end=" ")
    print("y= ", y + y0, end="\n")
    while (x < y):
        if (d < 0):
            # print("E")
            d = d + 2 * x + 3
            x = x + 1
        else:
            # print("SE")
            d = d + (2 * x) + 5 - (2 * y)
            y = y - 1
            x = x + 1
    xlist.append(x)
    ylist.append(y)
    Octa1x.append(x + x0)
    Octa1y.append(y + y0)
    Octa2x.insert(0, y + y0)
    Octa2y.insert(0, x + x0)
    Octa3x.insert(0, y + y0)
    Octa3y.insert(0, -(x + x0))
    Octa4x.append(x + x0)
    Octa4y.append(-(y + y0))
    Octa5x.append(-(x + x0))
    Octa5y.append(-(y + y0))
    Octa6x.insert(0, -(y + y0))
    Octa6y.insert(0, -(x + x0))
    Octa7x.insert(0, -(y + y0))
    Octa7y.insert(0, x + x0)
    Octa8x.append(-(x + x0))
    Octa8y.append(y + y0)
    # plt.plot(xlist, ylist, linestyle="--", marker="+", color="blue")
    plt.plot(Octa1x, Octa1y, linestyle="--", marker="+", color="blue")
    plt.plot(Octa2x, Octa2y, linestyle="--", marker="+", color="black")
    plt.plot(Octa3x, Octa3y, linestyle="--", marker="+", color="yellow")
    plt.plot(Octa4x, Octa4y, linestyle="--", marker="+", color="orange")
    plt.plot(Octa5x, Octa5y, linestyle="--", marker="+", color="olive")
    plt.plot(Octa6x, Octa6y, linestyle="--", marker="+", color="green")
    plt.plot(Octa7x, Octa7y, linestyle="--", marker="+", color="navy")
    plt.plot(Octa8x, Octa8y, linestyle="--", marker="+", color="red")
    plt.show()
# main
print("Enter circle 1st point:")
x0 = int(input())
print("Enter circle 2nd point:")
y0 = int(input())
print("Enter radius of circle:")
r = int(input())
midPointCircle(x0, y0, r)