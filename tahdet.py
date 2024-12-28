import turtle, math
vr = turtle.Turtle()
vr.getscreen().bgcolor('#994444')

vr.penup()
vr.goto((-200, 100))
vr.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        #turtle.begin_fill()
        for i in range(5): #5-kulmio
            turtle.forward(size)
            star(turtle, size/10) #tämä pois niin toimii ilman rekursiota, size/jakaja <=10 määrää rekursiokierrosten määrän
            turtle.left(216)
        #turtle.end_fill()
star(vr, 200)

turtle.done()
#kulman suuruus = 180/kulmat + 180 eli vasemmalle ensin 180 astetta + kulma, toimii kun pariton kulmamäärä
#parillisissa pitää varmaan tehdä niin, että laitetaan esim. kaksi kolmiota päällekkäin
