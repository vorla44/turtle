from turtle import *


# production X->-YF+XFX+FY-, Y->+XF-YFY-FX+
# Y:n ja X:n ero on siinä, että kulma vaihtuu
def hilbert(level, angle, step):
    # Input Parameters are numeric
    # Return Value: None
    if level == 0:
        return

    left(angle)
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
    right(angle)
    hilbert(level - 1, angle, step)
    # eteenpäin ja vasemmalle ja piirretään 1. tason kuvio
    forward(step)
    hilbert(level - 1, angle, step)
    # eteenpäin ja piirretään 1 tason kuvio
    right(angle)
    forward(step)
    hilbert(level - 1, -angle, step)
    # vasemmalle, eteenpäin ja piirretään 1. tason kuvio, siten, etttä kulma on -90
    left(angle)
    # käännytään oikealle


# axiom

def main():
    # level = int(input())
    level = 2
    size = 200
    penup()
    goto(-size / 2.0, size / 2.0)
    pendown()

    # For positioning turtle
    # koon kanssa pitää olla tarkkana 0. vaiteessa sivu jaetaan 0 osaan 2**level-1 = 0
    # 1 vaiheessa 2**level - 1 3 osaan jne
    hilbert(level, 90, size / (2 ** level - 1))
    done()


if __name__ == '__main__':
    main()