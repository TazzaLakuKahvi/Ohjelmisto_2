import math

a = 1.6
b = 2.3

def hypotenuusa_laskuri(kateetti1, kateetti2):
    hypotenuusa = math.sqrt(kateetti1**2 + kateetti2**2)
    return hypotenuusa

print(f"Kun kateetit ovat {a} ja {b}, hypotenuusa on {hypotenuusa_laskuri(a,b):.3f}.")