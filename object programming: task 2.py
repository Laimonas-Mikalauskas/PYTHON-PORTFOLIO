class LKLKomanda:
    def __init__(self, title, color):
        self.title = title
        self.color = color

    def zaisti(self):
        print(f"{self.title} plays the match!")

class Zalgiris(LKLTeam):
    def chant(self):
        print(f"{self.title}: fans are chanting Green-white!")

class Rytas(LKLTeam):
    def chant(self):
        print(f"{self.title}: fans are chanting Rytas! geriau už vedybas!")

class Lietkabelis(LKLTeam):
    def skanduote(self):
        print(f"{self.title}: fans are chanting  Liet-ka-be-lis!")

zalgiris = Zalgiris("Kauno Žalgiris", "green and white!")
rytas = Rytas("Vilniaus Rytas", "red and black")
lietkabelis = Lietkabelis("Panevėžys's Lietkabelis", "bordo and white")

rytas.play()
rytas.chant()
