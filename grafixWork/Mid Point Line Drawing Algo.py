import matplotlib
import matplotlib.pyplot as plt
def MP(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    d = dy - (dx / 2)
    xlist=[x0]
    ylist=[y0]
    while (x0<x1):
      x0=x0+1
      if (d < 0):
            d=d+dy
      else:
            d=d+dy-dx
            y0=y0+1
            xlist.append(round(x0, 1))
            ylist.append(round(y0, 1))
      print("x= ", round(x0, 0), end=" , ")
      print("y= ", round(y0, 0), end="\n")
    plt.plot(xlist, ylist, linestyle="--", marker="*")
    plt.show()
# main function
x0 = int(input("Enter x0 :"))
y0 = int(input("Enter y0 :"))
x1 = int(input("Enter x1 :"))
y1 = int(input("Enter y1 :"))
MP(x0, y0, x1, y1)
