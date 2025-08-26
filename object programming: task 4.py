# Bazinė klasė
class Player:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

# Paveldėta klasė – Žalgiris
class ZalgirisPlayer(Player):
    def __init__(self, name, surname, age, position, team):
        super().__init__(name, surname, age)
        self.position = position
        self.team = team

# Paveldėta klasė – Rytas
class RytasPlayer(Player):
    def __init__(self, name, surname, age, position, team):
        super().__init__(name, surname, age)
        self.position = position
        self.team = team

# Paveldėta klasė – Lietkabelis
class LietkabelisPlayer(Player):
    def __init__(self, name, surname, age, position, team):
        super().__init__(name, surname, age)
        self.position = position
        self.team = team

zalgiris = ZalgirisPlayer("Edgaras", "Ulanovas", 32, "Puolėjas", "Kauno Žalgiris")
rytas = RytasPlayer("Margiris", "Normantas", 27, "Gynėjas", "Vilniaus Rytas")
lietkabelis = LietkabelisPlayer("Vytenis", "Lipkevičius", 36, "Lengvasis krašto puolėjas", "Panevėžio Lietkabelis" )

print(f"{rytas.name} {rytas.surname}, {rytas.age} m., {rytas.team}")
