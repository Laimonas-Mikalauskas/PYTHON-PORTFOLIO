class Rytas:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def run(self):
        print(f"{self.name, self.city} runs into fast attack!")

    def throw(self):
        print(f"{self.name, self.citty} throws into basket!")

    def defense(self):
        print(f"{self.name, self.city} returns to defense.")

team = Rytas("Rytas", "Vilnius")

team.throw()


