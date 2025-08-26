class Rytas:
    def __init__(self, pavadinimas, miestas):
        self.pavadinimas = pavadinimas
        self.miestas = miestas

    def begti(self):
        print(f"{self.pavadinimas, self.miestas} bėga į greitą puolimą!")

    def mesti(self):
        print(f"{self.pavadinimas, self.miestas} meta į krepšį!")

    def gynyba(self):
        print(f"{self.pavadinimas, self.miestas} grįžta į gynybą.")

komanda = Rytas("Rytas", "Vilnius")

komanda.mesti()


