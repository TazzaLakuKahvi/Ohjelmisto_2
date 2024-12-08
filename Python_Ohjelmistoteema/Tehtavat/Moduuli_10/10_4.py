import random
import Auto as Au
import Kilpailu as Ki

autojen_maara = 10
autot = {}
tuntilaskuri = 0
lopetus = 0

for i in range(autojen_maara):
    autot[i] = Au.Auto(rekisteritunnus=f"ABC-{i + 1}", huippunopeus=random.randint(100, 200))

suuri_romuralli = Ki.Kilpailu("Suuri romuralli", 8000, autot)


while lopetus != 1:
    suuri_romuralli.tunti_kuluu()
    tuntilaskuri += 1
    for i in suuri_romuralli.osallistuvat_autot:
        suuri_romuralli.kilpailu_ohi(i)
        if suuri_romuralli.kilpailu_ohi(i):
            lopetus = 1
    if tuntilaskuri == 10:
        suuri_romuralli.tulosta_tilanne()
        tuntilaskuri = 0
print(f"KILPAILU ON OHI\nTULOKSET:")
suuri_romuralli.tulosta_tilanne()