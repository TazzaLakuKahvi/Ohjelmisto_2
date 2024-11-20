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

    #     for i in range(hissien_maara):
    #         self.hissit[f"{HISSI_NIMI}{i+1}"] = Hissi(self.alin, self.ylin)
    #
    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros, hissin_numero + 1)