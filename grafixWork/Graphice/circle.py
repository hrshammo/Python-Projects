import matplotlib.pyplot as plt
def draw_circle(center_x, center_y, radius):
    x = 0
    y = radius
    p = 1 - radius
    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    plt.title('Midpoint Circle Drawing Algorithm')
    # Draw the initial points
    plot_points(ax, center_x, center_y, x, y)
    while x <= y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_points(ax, center_x, center_y, x, y)
    plt.show()
def plot_points(ax, center_x, center_y, x, y):
    ax.plot(center_x + x, center_y + y, 'ro')
    ax.plot(center_x + x, center_y - y, 'ro')
    ax.plot(center_x - x, center_y + y, 'ro')
    ax.plot(center_x - x, center_y - y, 'ro')
    ax.plot(center_x + y, center_y + x, 'ro')
    ax.plot(center_x + y, center_y - x, 'ro')
    ax.plot(center_x - y, center_y + x, 'ro')
    ax.plot(center_x - y, center_y - x, 'ro')
# Example usage
print('Insert Mid Point')
a = int(input())
b = int(input())
print('Insert Redius')
c = int(input())
draw_circle(a, b, c)
