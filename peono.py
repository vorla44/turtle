import turtle

aste=90
def draw_peano(length,depth, aste):
    if depth==0:
        t.fd(length)
        t.fd(length)
        t.right(aste)
        t.fd(length)
        t.right(90)
        t.fd(length)
        t.fd(length)
        t.left(90)
        t.fd(length)
        t.left(90)
        t.fd(length)
        t.fd(length)

    else:
        draw_peano(length/2, depth-1, aste)
        t.fd(length/2)
        t.left(aste)
        draw_peano(length/2, depth-1, -aste)



window = turtle.Screen()
t = turtle.Turtle()
draw_peano(100,1, aste)
window.exitonclick()