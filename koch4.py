# Python program to print complete Koch Curve.
from turtle import *


# function to create koch snowflake or koch curve
def snowflake(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    lengthSide /= 4.0
    snowflake(lengthSide, levels - 1)
    # Taso1:

    left(90)
    snowflake(lengthSide, levels - 1)
    # eteenpäin ja vasemmalle eteenpäin
    right(90)

    snowflake(lengthSide, levels - 1)
    right(90)
    # oikealle eteenpäin ja oikealle
    snowflake(lengthSide, levels - 1)
    right(90)
    snowflake(lengthSide, levels - 1)
    # eteenpäin, oikealle, eteenpäin
    left(90)
    snowflake(lengthSide, levels - 1)
    left(90)
    # vasemmalle eteenpäin ja vasemamlle
    snowflake(lengthSide, levels - 1)
    left(90)
    # eteenpäin vasemmalle
    snowflake(lengthSide, levels - 1)
    right(90)
    snowflake(lengthSide, levels - 1)
    # eteenpäin ja oikealle, eteenpäin


# main function
if __name__ == "__main__":
    # defining the speed of the turtle
    speed(0)
    length = 600.0

    # Pull the pen up – no drawing when moving.
    # Move the turtle backward by distance, opposite
    # to the direction the turtle is headed.
    # Do not change the turtle’s heading.
    penup()
    # turtle aloittaa muuten näytön keskeltä
    backward(length / 2.0)

    # Pull the pen down – drawing when moving.
    pendown()

    snowflake(length, 1)

    # To control the closing windows of the turtle
    mainloop()
