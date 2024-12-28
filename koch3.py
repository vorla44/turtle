# Python program to print complete Koch Curve.
from turtle import *


# function to create koch snowflake or koch curve
def snowflake(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels - 1)
    # Taso 1
    # eteenpäin,

    left(90)
    snowflake(lengthSide, levels - 1)
    # vasemmalle ja eteenpäin
    right(90)
    snowflake(lengthSide, levels - 1)
    # oikealle ja eteenpäin
    right(90)
    snowflake(lengthSide, levels - 1)
    snowflake(lengthSide, levels - 1)
    # oikealle ja 2x eteenpäin
    left(90)
    snowflake(lengthSide, levels - 1)
    # vasemmalle ja eteenpäin
    left(90)
    snowflake(lengthSide, levels - 1)
    # vasemmalle ja eteenpäin
    right(90)
    snowflake(lengthSide, levels - 1)
    # oikealle ja eteenpäin


# main function
if __name__ == "__main__":
    # defining the speed of the turtle
    speed(0)
    length = 300.0

    # Pull the pen up – no drawing when moving.
    # Move the turtle backward by distance, opposite
    # to the direction the turtle is headed.
    # Do not change the turtle’s heading.
    penup()

    backward(length / 2.0)

    # Pull the pen down – drawing when moving.
    pendown()

    snowflake(length, 2)

    # To control the closing windows of the turtle
    mainloop()
