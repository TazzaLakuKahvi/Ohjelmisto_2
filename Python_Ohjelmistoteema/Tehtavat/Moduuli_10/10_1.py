class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self):
        self.kerros = self.kerros + 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros = self.kerros - 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def siiry_kerrokseen(self, kerros):
        print(f"Hissi on tällä hetkellä kerroksessa {self.kerros}.\nHissi siirtyy nyt kerrokseen {kerros}.")
        if kerros < self.alin or kerros > self.ylin:
            print(f"Tässä hississä ei ole kerrosta {kerros}.")
        else:
            if kerros > self.kerros:
                while self.kerros != kerros:
                    self.kerros_ylos()
            elif kerros < self.kerros:
                while self.kerros != kerros:
                    self.kerros_alas()
            else:
                print(f"Hissi on jo kerroksessa {kerros}.")


h = Hissi(1, 5)

h.siiry_kerrokseen(5)
