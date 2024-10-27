import math

a = float(2.493)
b = float(0.911)

def laskuri(radians):
    degrees = radians * 180 / math.pi
    return degrees

print(f"a)  {a} radiaania = {laskuri(a):.4f} astetta")
print(f"b)  {b} radiaania = {laskuri(b):.4f} astetta")