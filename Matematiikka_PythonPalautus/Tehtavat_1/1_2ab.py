import math

a = float(137.7)
b = float(62.3)

def laskuri(degrees):
    radians = degrees * math.pi / 180
    return radians

print(f"a)  {a} astetta = {laskuri(a):.4f} radiaania")
print(f"b)  {b} astetta = {laskuri(b):.4f} radiaania")