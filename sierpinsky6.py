import turtle

def sier(tur, order, size):
    """ Draw Sierpinski triangle """
    if order == 0:
        for _ in range(3):
            tur.forward(size)
            tur.forward(size)
            tur.left(120)
    else:
        step = size / 2
        for t1, m1, t2, m2 in [(0, step, 0, 0),
                               (120, step, -120, 0),
                               (-60, step, 60, -(step))]:
            sier(tur, order - 1, step)
            tur.left(t1)
            tur.forward(m1)
            tur.left(t2)
            tur.forward(m2)


if __name__ == '__main__':
    odr = int(input("Enter the order: "))
    sz = int(input("Enter the size: "))

    root = turtle.Screen()
    root.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color('blue')
    alex.speed(100)

    sier(alex, odr, sz)

    root.mainloop()