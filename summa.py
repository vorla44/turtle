from turtle import *


def summa(luku):
    if luku > 1:
        vastaus = summa(luku - 1) + luku
    else:
        vastaus = 1
    return vastaus


def main():
    print(summa(3))


if __name__ == '__main__':
    main()
    mainloop()