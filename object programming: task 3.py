class LKL:
    def __init__(self):
        self.teams = []

    def is_empty(self):
        return len(self.teams) == 0

    def push(self, team):
        self.teams.append(team)

    def pop(self):
        if not self.is_empty():
            return self.teams.pop()
        raise IndexError("Negalima nuimti komandos – sąrašas tuščias.")

    def size(self):
        return len(self.teams)

    def show(self):
        if self.is_empty():
            print("Sąrašas tuščias. Nėra LKL komandų.")
        else:
            print("LKL komandos išdėstytos stulpeliu:")
            for x in self.teams:
                print(f"– {x}")

lkl = LKL()

# Pridedame 5 komandų

lkl.push("Žalgiris")
lkl.push("Rytas")
lkl.push("Lietkabelis")
lkl.push("Neptūnas")
lkl.push("Šiauliai")

# Parodome komandas

lkl.show()

# Pašaliname 2 komandas

print("Nuimta komanda:", lkl.pop())
print("Nuimta komanda:", lkl.pop())

lkl.push("Wolves")
print(f"Pridėta komanda Wolves ir sąrašas atrodo: {lkl.show()}")

# Komandų kiekis

print("Komandų kiekis:", lkl.size())

# Patikriname komandas

lkl.show()
