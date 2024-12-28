#!/usr/bin/env python3
"""       turtle-example-suite:

              tdemo_peace.py

A simple drawing suitable as a beginner's
programming example. Aside from the
peacecolors assignment and the for loop,
it only uses turtle commands.
"""

from turtle import *

def main():
    peacecolors = ("red3",  "orange", "yellow",
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4")

    reset()
    Screen() #640*540 (0,0) keskellä
    up()
    goto(-320,-195) #vasen reuna, 75p alareunan yläpuolella eli viivassa x-vasen, y-vasenylä
    width(70)

    for pcolor in peacecolors:
        color(pcolor)
        down()
        forward(640)
        up()
        backward(640)
        left(90)
        forward(66) # viivat vähän päällekkäin
        right(90)

    width(25)
    color("white")
    goto(0,-170) #x keskellä, y-170 keskikohdan alaluolella
    down()

    circle(170) #ympyrä, säde 170
    left(90)
    forward(340) #pystyhalkaisija
    up()
    left(180)
    forward(170) #keskikohta
    right(45)
    down()
    forward(170) # vasen haara
    up()
    backward(170) #keskikohta
    left(90)
    down()
    forward(170) #oikea haara
    up()

    goto(0,300) # vanish if hideturtle() is not available ;-)
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()