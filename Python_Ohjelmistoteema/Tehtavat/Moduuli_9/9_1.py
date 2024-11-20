class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka


auto1 = Auto("ABC-123", "142 km/h")

print(f"Auton rekisteritunnus on: {auto1.rekisteritunnus}\nAuton huippunopeus on: {auto1.huippunopeus}")
print(f"Auton kulkema nopeus on: {auto1.nopeus}\nAuton kulkema matka on: {auto1.matka}")
