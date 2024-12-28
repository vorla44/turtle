from turtle import *


# production
def hilbert(level, angle, step):
    # Input Parameters are numeric
    # Return Value: None
    if level == 0:
        return

    right(angle)
    hilbert(level - 1, -angle, step)
    # 1. taso
    # turtle 90 oikealle ja eteenpäin
    # vasemmalle 90 ja eteenpäin
    # vasemmalle 90 ja eteenpäin
    # turtle 90 oikealle eli alkup. asentoon
    # 2. taso katso ohjesivulta pages/hilbert.docx tai kuvaus_muut.html millaisia kuvioita tulee kun kulmat vaihtuvat
    # turtle 90 oikealle
    # piirretään 1. tason kuvio siten että kulma on -90 eli kuvio pyörähtää 90 astetta vastapäivään ja samalla lyhennetään janaa
    forward(step)
    left(angle)
    hilbert(level - 1, angle, step)
    # eteenpäin ja vasemmalle ja piirretään 1. tason kuvio
    forward(step)
    hilbert(level - 1, angle, step)
    # eteenpäin ja piirretään 1 tason kuvio
    left(angle)
    forward(step)
    hilbert(level - 1, -angle, step)
    # vasemmalle, eteenpäin ja piirretään 1. tason kuvio, siten, etttä kulma on -90
    right(angle)
    # käännytään oikealle


def main():
    # level = int(input())
    level = 3
    size = 200
    penup()
    goto(-size / 2.0, size / 2.0)
    pendown()

    # For positioning turtle
    hilbert(level, 90, size / (2 ** level - 1))
    done()


if __name__ == '__main__':
    main()