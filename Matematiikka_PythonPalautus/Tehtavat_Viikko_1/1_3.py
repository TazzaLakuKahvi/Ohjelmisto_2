import math

asteet = {1:30,2:45,3:60,4:90,5:120,6:135,7:150,8:180,9:270,10:360}

taulukko_rivit = 1

def laskuri(degrees):
    radians = float(degrees) * math.pi / 180
    return radians

print("DEG | RAD")
while taulukko_rivit < 11:
    print(f"{asteet[taulukko_rivit]:<4d}| {laskuri((asteet[taulukko_rivit]))}")
    taulukko_rivit += 1