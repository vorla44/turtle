# Python program to print complete Koch Curve.
from turtle import *


# function to create koch snowflake or koch curve
def snowflake(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)  # 0-taso, Axiom eli millainen kuvio tasolla 0, mahdollisimman yksinkertainen
        return
    # production rule F-F++F-F, - left 60, + right 60
    # jotta kuvio sulkeutuu (kolmio) tehdään 3 silmukkaa
    # voidaan tehdä mikä kuvio vaan
    lengthSide /= 3.0  # pituus 1/3 edellisestä
    snowflake(lengthSide, levels - 1)
    # edellisen tason kuvio, laitetaan siis F:n paikalle edellinen Axiom eli
    # nyt 1-tasolla forward(lengthSide/3)
    left(60)
    snowflake(lengthSide, levels - 1)  # edellisen tason kuvio
    right(60)
    right(60)
    snowflake(lengthSide, levels - 1)  # edellisen tason kuvio
    left(60)
    snowflake(lengthSide, levels - 1)  # edellisen tason kuvio

    # rekursiivisen ohjelman mukaisesti alussa tarkistetaan onko levels==0
    # jos on piirretään viiva ja lopetetaan
    # jos ei suoritetaan if jälkeistä osiota, mitään else lauseita ei tarvita.
    # tapahtumat menevät pinoon ja vasta kun saavutetaan 0-taso, osataan piirtää kun tiedetään lengthSiden arvo.
    # sitten pino suoritetaan ylhäältä alaspäin kokonaan.


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

    backward(length / 2.0)  # kuva keskelle sivua

    # Pull the pen down – drawing when moving.
    pendown()
    for i in range(3):
        snowflake(length, 2)
        right(120)
        # silmukka jotta kuvio on kolmio
    # To control the closing windows of the turtle
    mainloop()