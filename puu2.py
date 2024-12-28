import turtle

pituus = 100
vr = turtle.Turtle()
vr.getscreen().bgcolor('#994444')
vr.width(2)  # valitse kynän paksuus
vr.left(90)
vr.color("red", "white")  # valitse värit, kynän väri punainen
vr.penup()
vr.goto((0, -100))
vr.pendown()


def puu_haara(turtle, pituus):
    if pituus < 5:
        return

    turtle.fd(pituus)
    turtle.left(20)

    turtle.fd(pituus)
    puu_haara(turtle, pituus * 0.5)
    turtle.pu
    turtle.bk(pituus)
    turtle.pd
    turtle.right(45)
    turtle.fd(pituus)
    puu_haara(turtle, pituus * 0.5)
    turtle.pu
    turtle.bk(pituus)
    turtle.left(25)
    turtle.bk(pituus)
    turtle.pd

    return (pituus)


def main():
    # reset() #poista kaikki vanhat eli aloita tyhjästä ikkunasta

    puu_haara(vr, pituus)
    vr.ht()  # piilota turtle (hide turtle) eli kursoria ei näy
    # return "Done"  #kuvio on valmis eli lopeta
    turtle.done()


if __name__ == '__main__':
    main()

    vr.mainloop()