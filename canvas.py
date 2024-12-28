from turtle import TurtleScreen, RawTurtle, TK


def main():
    peacecolors = ("red3", "orange", "yellow",
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4")
    root = TK.Tk()
    cv1 = TK.Canvas(root, width=300, height=200, bg="#ddffff")
    cv2 = TK.Canvas(root, width=300, height=200, bg="#ffeeee")
    cv1.pack()
    s1 = TurtleScreen(cv1)
    s1.bgcolor(peacecolors[1])  # canvas tausta
    s2 = TurtleScreen(cv2)
    s2.bgcolor(peacecolors[2])
    cv2.pack()

    p = RawTurtle(s1)  # turtle
    q = RawTurtle(s1)

    p.color(peacecolors[0], peacecolors[1])  # reuna, sisus
    p.width(3)
    q.color("blue", (0.85, 0.85, 1))
    q.width(3)

    for t in p, q:
        t.shape("turtle")
        t.lt(36)

    q.lt(180)

    for t in p, q:
        t.begin_fill()
    for i in range(5):
        for t in p, q:
            t.circle(50)
            t.lt(72)
    for t in p, q:
        t.end_fill()
        t.lt(54)
        t.pu()
        t.bk(50)

    return "EVENTLOOP"


if __name__ == '__main__':
    main()
    TK.mainloop()  # keep window open until user closes it