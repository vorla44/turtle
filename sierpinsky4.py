from turtle import *
import turtle
t = turtle.Turtle()

Window = turtle.Screen()

Window.bgcolor('white')

t.penup()
t.goto(-200, -200)
t.pendown()
def serp_tri(side, level):
    if level == 1:
        for i in range(3):
            t.color('black')
            #t.ht()
            t.fd(side)
            t.left(120)
            t.speed(100000)

    else:
        #t.ht()
        serp_tri(side/2, level-1)
        t.fd(side/2)
        serp_tri(side/2, level-1)
        t.bk(side/2)
        t.left(60)
        t.fd(side/2)
        t.right(60)
        serp_tri(side/2, level-1)
        t.left(60)
        t.bk(side/2)
        t.right(60)
        t.speed(100000)

def main():
    serp_tri(400, 2)

if __name__ == '__main__':
    main()
    Window.mainloop()