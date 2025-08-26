class LKLKomanda:
    def __init__(self, pavadinimas, spalva):
        self.pavadinimas = pavadinimas
        self.spalva = spalva

    def zaisti(self):
        print(f"{self.pavadinimas} žaidžia rungtynes!")

class Zalgiris(LKLKomanda):
    def skanduote(self):
        print(f"{self.pavadinimas}: fanai skanduoja Žalia-balta!")

class Rytas(LKLKomanda):
    def skanduote(self):
        print(f"{self.pavadinimas}: fanai skanduoja Rytas! geriau už vedybas")

class Lietkabelis(LKLKomanda):
    def skanduote(self):
        print(f"{self.pavadinimas}: fanai skanduoja Liet-ka-be-lis!")

zalgiris = Zalgiris("Kauno Žalgiris", "žalia ir balta")
rytas = Rytas("Vilniaus Rytas", "raudona ir juoda")
lietkabelis = Lietkabelis("Panevėžio Lietkabelis", "bordo ir balta")

rytas.zaisti()
rytas.skanduote()
