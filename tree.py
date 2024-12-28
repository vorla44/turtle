import turtle
def draw_tree():
    draw_trunk()
    draw_leafs()

def draw_trunk(turt, width, height):
    turt.color('brown')
    turt.begin_fill()
    turt.setheading(0) # head to right
    turt.forward(width)
    turt.right(90)
    turt.forward(height)
    turt.right(90)
    turt.forward(width)
    turt.right(90)
    turt.forward(height)
    turt.end_fill()

def draw_leafs(turt, width, height, triangles=3):
    #draw 3 triangles
    for i in range(triangles):
        draw_triangle(turt, width, height)
        height_increase = height/2
        turt.sety(turt.ycor() + height_increase)


def draw_triangle(turt, width, height):
    branch_overhang = height #length branches overhang from draw_trunk
    triangle_height = 2*height #a single triangle is two times as tall as the draw_trunk

    turt.begin_fill()
    x_init, y_init = (turt.xcor(), turt.ycor())
    x_middle = x_init + width/2.0
    x_bottom_left = x_init - branch_overhang
    x_bottom_right = x_init + width + branch_overhang
    y_top = y_init + triangle_height

    turt.goto(x_bottom_left, y_init)
    turt.goto(x_middle, y_top)
    turt.goto(x_bottom_right, y_init)
    turt.goto(x_init, y_init)
    turt.end_fill()

width = 100
height = 200

turt = turtle.Turtle()
draw_trunk(turt, 100, 200)
draw_leafs(turt, 100, 200)


turtle.done()