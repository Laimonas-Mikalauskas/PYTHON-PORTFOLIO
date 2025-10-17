darbuotojai = [
    ['Valdas', 'programuotojas', 2000],
    ['Adomas', 'direktorius', 3000],
    ['Aldona', 'vadybininkas', 1800],
    ['Jogaila', 'programuotojas', 2500]
]

print(darbuotojai[0])  # ['Valdas', 'programuotojas', 2000]
print(darbuotojai[0][1])  # programuotojas
print(darbuotojai[0][1].upper())  # PROGRAMUOTOJAS

# printinam po 1 vidinį pilną listą
for listas in darbuotojai:
    print(listas)  # ['Valdas', 'programuotojas', 2000], ..

# printinam atskirus elementus iš kiekvieno vidinio listo
# imdami per indeksą
for listas in darbuotojai:
    print(listas[0], listas[2])  # Valdas programuotojas, ..

# python priimta yra išardyti listus for eilutėje
for vardas, pareigos, atlyginimas in darbuotojai:
    print(atlyginimas, vardas, pareigos)  # Valdas 2000 programuotojas, ..

# susumuojam atlyginimus
# variantas 1
suma = 0
for vardas, pareigos, atlyginimas in darbuotojai:
    suma += atlyginimas

print(suma)  # 9300

# variantas 2
atlyginimai = []  # tuščias listas, sukaupti visiems atlyginimams
for vardas, pareigos, atlyginimas in darbuotojai:
    atlyginimai.append(atlyginimas)

print(atlyginimai)  # [2000, 3000, 1800, 2500]
print(sum(atlyginimai))  # 9300

# suskaičiuojam programuotojus
pozicijos = []
for vardas, pareigos, atlyginimas in darbuotojai:
    pozicijos.append(pareigos)

print(pozicijos)  # ['programuotojas', 'direktorius', 'vadybininkas', 'programuotojas']
print("Programuotojų skaičius yra", pozicijos.count("programuotojas"))  # Programuotojų skaičius yra 2

# TODO perdaryti, kad atlyginimų fondas ir programuotojai būtų suskaičiuoti naudojant 1 for ciklą