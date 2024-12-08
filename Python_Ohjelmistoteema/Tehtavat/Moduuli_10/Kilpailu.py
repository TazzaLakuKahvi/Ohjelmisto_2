import random

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_km, osallistuvat_autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.osallistuvat_autot = osallistuvat_autot

    def tunti_kuluu(self):
            for i in self.osallistuvat_autot:
                self.osallistuvat_autot[i].kiihdyta(random.randint(-10, 15))
                self.osallistuvat_autot[i].kulje(1)

    def tulosta_tilanne(self):
        print(f"{"":-^57}")
        print(f"|{"rekisteritunnus":^17}|{"huippunopeus":^15}|{"nopeus":^10}|{"matka":^10}|")
        for x in range(len(self.osallistuvat_autot)):
            print(f"{"":-^57}")
            print(
                f"|{self.osallistuvat_autot[x].rekisteritunnus:^17}"
                f"|{str(self.osallistuvat_autot[x].huippunopeus) + "km/h":^15}"
                f"|{str(self.osallistuvat_autot[x].nopeus) + "km/h":^10}"
                f"|{str(self.osallistuvat_autot[x].matka) + "km":^10}|")
        print(f"{"":-^57}")

    def kilpailu_ohi(self, auto = None):
        if self.osallistuvat_autot[auto].matka >= self.pituus_km:
            return True
        else:
            return False
