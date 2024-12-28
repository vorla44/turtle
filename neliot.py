from turtle import *

colormode(255)
import math


def piirra_nelio(sivu, x, y):
    begin_fill()
    if sivu == 100:
        up()
        goto(x - sivu, y + sivu)
        color("red")
        down()


    elif sivu == 40:
        up()
        goto(x, y)
        color("red")
        down()

    elif sivu == 80:
        up()
        goto(x - sivu, y)
        color("blue")
        down()
    elif sivu == 60:
        up()
        goto(x, y + sivu)
        color("blue")
        down()
    for i in range(4):
        begin_fill()
        forward(sivu)
        right(90)

    end_fill()
    lt(180)
    pu()
    goto(0, 0)


piirra_nelio(40, -100, 100)
piirra_nelio(60, 100, -100)
piirra_nelio(100, -50, -20)
piirra_nelio(80, 90, 30)
done()
