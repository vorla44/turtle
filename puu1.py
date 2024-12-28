from turtle import *

pituus = 100  # aetetaan alkupetäisen haaran pituudeksi 100


def puu_haara(pituus):
    if pituus < 5:  # toisto eli rekursio loppuu, jos haara on < 5
        return
        # piirretään puun haara ilman toistoa
    fd(pituus)
    left(20)

    fd(pituus)
    color("red","white") #viimeinen "puu" jää punaiseksi
    puu_haara(pituus*0.5) # ensin rekursiovaihe jätetään pois, yleensä se kuitenkin tulee alkuperäisen kuvin loppupisteeseen
    penup
    bk(pituus)  # palataan eka haaran alkuun
    pd

    right(45)  # käännytään oikealle ja piirretään pituuden matka
    fd(pituus)
    puu_haara(pituus*0.5) #rekursiohaihe ensin pois, se tulee toisen haaran loppuun
    pu
    bk(pituus)
    left(25)
    bk(pituus)  # piirretään vihreällä runko
    pd  # ollaan lähtökohdassa ja pen down
    color("green", "white")  # rungon väri
    return (pituus)
    #palautetaan pituus, joka on puolet alkuperäisestä, toistetaan kunnes pituus  < 5


def main():
    reset()  # poista kaikki vanhat eli aloita tyhjästä ikkunasta
    pu
    goto(0, -100)  # aloitetaan piitäminen 100 px keskipisteen alupuolehsax
    width(2)  # valitse kynän paksuus
    left(90)
    color("green", "white")  # valitse värit, kynän väri punainen
    puu_haara(pituus)
    ht()  # piilota turtle (hide turtle) eli kursoria ei näy
    return "Done"  # kuvio on valmis eli lopeta


if __name__ == '__main__':
    main()
    mainloop()