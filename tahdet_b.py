import turtle, math

vr = turtle.Turtle()
vr.getscreen().bgcolor('#994444')

vr.penup()
vr.goto((-200, 100))
vr.pendown()


def star(turtle, size, level):
    if level == 0:
        return
    else:
        # turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            turtle.left(216)

            star(turtle, size / 3, level - 1)  # tämä pois niin toimii ilman rekursiota

        # turtle.end_fill()


def main():
    star(vr, 400, 1)
    # vr.done() tekee, mutta poistuu kun valmis
    # return "Done!" tekee, mutta poistuu
    turtle.done()  # toimii oikein


if __name__ == "__main__":
    main()

# 216*5 = 1080 /3 = 360 eli osoitin kääntyy 3 täyttä kierrosta
# syntyy 5-kulmainen tähti, jokainen kulma 36 astetta
# jokainen kulma on 36 astetta
# tässä tehdään kolme kierrosta 200/3=66 66/3=22 22/3 < 10
# size/21 < 10, vain yksi kierros eli tähti
# kokeilin 7-kulmiota range(7), Jokainen kulma on 180/7 ja left
# 180+kulma ja toimii. Parillisilla ei toimi.
# säännölliset monikulmiot on helppo toteuttaa samalla periaatteella