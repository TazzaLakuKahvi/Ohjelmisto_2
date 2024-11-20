import Hissi as Hi


class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissien_maara = hissien_maara
        self.hissit = []
        for i in range(hissien_maara):
            hissi = Hi.Hissi(self.alin, self.ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros, hissin_numero + 1)

    def palohalytys(self):
        for i in self.hissit:
            i.siirry_kerrokseen(self.alin, "", False, False)
        print("Palohälytys on päällä, ja kaikki hissit ovat siirtyneet alimpaan kerrokseen.")
