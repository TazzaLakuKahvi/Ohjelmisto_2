import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, muutos):

        self.nopeus = self.nopeus + muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka = self.matka + (self.nopeus * tunnit)
        kuljettu = self.nopeus * tunnit
        return kuljettu


def kmh(parametri):
    return str(parametri) + " km/h"


def km(parametri):
    return str(parametri) + " km"


def tulokset(lista):
    print(f"{"":-^57}")
    print(f"|{"rekisteritunnus":^17}|{"huippunopeus":^15}|{"nopeus":^10}|{"matka":^10}|")

    for x in range(len(lista)):
        print(f"{"":-^57}")
        print(
            f"|{lista[x].rekisteritunnus:^17}|{kmh(lista[x].huippunopeus):^15}|{kmh(lista[x].nopeus):^10}|{km(lista[x].matka):^10}|")
    print(f"{"":-^57}")


autot = {}
for i in range(10):
    autot[i] = Auto(rekisteritunnus=f"ABC-{i + 1}", huippunopeus=random.randint(100, 200))

auto_maalissa = False
while not auto_maalissa:

    for i in autot:
        autot[i].kiihdyta(random.randint(-10, 15))
        autot[i].kulje(1)
        if autot[i].matka >= 10000:
            auto_maalissa = True
            break

tulokset(autot)
