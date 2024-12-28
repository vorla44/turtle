# d://myweb/w3_python/ou_harjoitukset/osa3_h1_spiraali.py
"""
Opittavat asiat: Tehtävässä opetellaan ennaltamäärätyn toistomäärän
tekeminen silmukalla. Lisäksi
palautellaan mieliin miten funktiolle määritetään valinnaisia argumentteja.

Tavoite: Toteuttaa ohjelma, joka piirtää säännöllisiä spiraaleja,
joiden väriä, sädettä, säteen kasvua sekä viivan leveyttä voidaan säätää.

Toteutettava funktio: piirra_spiraali
Parametrit:
spiraalin väri (väriarvo - merkkijono tai kolmen alkion monikko)
piirrettävien kaarien (neljäsosaympyrä) lukumäärä (kokonaisluku)
spiraalin säde (kokonaisluku)
säteen kasvu (liukuluku)
viivan paksuus (kokonaisluku) - oletusarvo 1

Funktion alussa asetetaan väri ja kynän paksuus.
Loput piirtokomennoista tehdään silmukassa, jossa on kaarien
lukumäärän verran toistoja. Toteutuksessa kannattaa käyttää
for-silmukkaa ja range-funktiota. Jokaisella kierroksella piirretään
90 asteen kaari, jonka jälkeen kasvatetaan sädettä kasvuparametrin verran.
Huomaa, että silmukkamuuttujaa ei varsinaisesti käytetä mihinkään

oteutettava pääohjelma:
Pääohjelmaan voit laittaa esim alla olevat koodirivit:
piirra_spiraali("black", 20, 10, 3)
piirra_spiraali("red", 10, 20, 4, 3)
piirra_spiraali("blue", 10, -20, -4, 3)
done()

Lisäksi circle-komennosta otetaan käyttöön sen ensimmäinen
valinnainen argumentti:
circle(r, a) # piirtää kaaren, jonka säde on r ja sisäkulma a
siis jos säde on > 0 keskipiste on kaaren vasemmallla puolella ja
jos sade < 0 keskipiste on oikealla puolella.
"""
from turtle import *


def piirra_spiraali(vari, kaaret_n, sade, sade_plus, viiva_paksuus=1):
    pensize(viiva_paksuus)
    color(vari)
    down()
    for i in range(kaaret_n):
        circle(sade, 90)
        sade += sade_plus
    up()
    return sade


def main():
    piirra_spiraali("black", 20, 10, 3)
    piirra_spiraali("red", 10, 20, 4, 3)
    piirra_spiraali("blue", 10, -20, -4, 3)


# if __name__ == '__main__':
main()
