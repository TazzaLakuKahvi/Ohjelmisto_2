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


auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus on: {auto1.rekisteritunnus}\nAuton huippunopeus on: {kmh(auto1.huippunopeus)}")
print(f"Auton kulkema nopeus on: {kmh(auto1.nopeus)}\nAuton kulkema matka on: {auto1.matka} km")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auto kiihdytti {kmh(30)}, sitten {kmh(70)}, ja lopuksi {kmh(50)}. Auto kulkee nyt {kmh(auto1.nopeus)}.")

auto1.kiihdyta(-200)

print(f"Auto teki hätäjarrutuksen. Auton vauhti on {kmh(auto1.nopeus)}, eli auto on pysähtynyt.")

auto1.kiihdyta(60)
auto1.kulje(1.5)
print(f"Auto on kulkenut {auto1.matka} km")
