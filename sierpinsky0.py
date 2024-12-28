import turtle
def draw_sierpinski(length,depth):
    if depth==0:
        t.fd(length)
        t.left(120)
        t.fd(length)
        t.left(120)
        t.fd(length)
        t.left(120)

    else:

        draw_sierpinski(length/2,depth-1)
        t.fd(length/2)
        draw_sierpinski(length / 2, depth - 1)
        t.left(120)
        t.fd(length/2)
        t.right(120)
        draw_sierpinski(length/2,depth-1)
        t.left(60)
        t.back(length/2)
        t.right(60)


window = turtle.Screen()
t = turtle.Turtle()
draw_sierpinski(100,3)
window.exitonclick()