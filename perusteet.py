from turtle import *


def kuvio(radius, color1, color2):
    width(2)
    color(color1, color2)
    begin_fill()
    circle(radius / 2., 180)
    circle(radius / 2., 180)

    end_fill()


def main():
    reset()
    kuvio(200, "black", "green")
    ht()
    return "Done"


if __name__ == '__main__':
    main()
