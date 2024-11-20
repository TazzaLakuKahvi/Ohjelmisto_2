class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self, numero="", print_boolean=True):
        self.kerros = self.kerros + 1
        if print_boolean:
            print(f"Hissi{numero} on nyt kerroksessa {self.kerros}")

    def kerros_alas(self, numero="", print_boolean=True):
        self.kerros = self.kerros - 1
        if print_boolean:
            print(f"Hissi{numero} on nyt kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kerros, numero="", siirtyma_print_boolean=True, print_boolean=True):
        if print_boolean:
            print(
                f"Hissi{numero} on tällä hetkellä kerroksessa {self.kerros}.\nHissi{numero} siirtyy nyt kerrokseen {kerros}.")
        if kerros < self.alin or kerros > self.ylin:
            print(f"Tässä hississä ei ole kerrosta {kerros}.")
        else:
            if kerros > self.kerros:
                while self.kerros != kerros:
                    self.kerros_ylos(numero, siirtyma_print_boolean)
            elif kerros < self.kerros:
                while self.kerros != kerros:
                    self.kerros_alas(numero, siirtyma_print_boolean)
            elif siirtyma_print_boolean:
                print(f"Hissi on jo kerroksessa {kerros}.")
