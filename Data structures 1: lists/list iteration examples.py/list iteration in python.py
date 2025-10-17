menesiai = ['sausis', 'vasaris', 'kovas', 'balandis']

# for sakinyje po for komandos privalom įrašyti
# kintamojo pavadinimą, kuris bus automatiškai
# sukurtas saugoti iteruojamiems elementams
for elem in menesiai:
    print(elem, "mėn.")  # sausis mėn., ..
    print(elem.upper())  # SAUSIS, ..
    print("*****")  # *****, ..

print("---------------")

skaiciai = [10, 7, 50, 111]

for elem in skaiciai:
    print(elem * 100)  # 1000, .., 11100

print("---------------")

# sumavimas, kaupimas iteruojant
suma = 0
for elem in skaiciai:
    suma += elem  # suma = suma + elem

print(suma)  # 178

# susumuojam elementus, kiekvieną padaugintą iš 100
suma = 0
for elem in skaiciai:
    # suma = suma + elem * 100
    suma += elem * 100

print(suma)  # 17800

# sumavimas, kaupimas iteruojant, kas antrą skaičių
suma = 0
for elem in skaiciai[::2]:
    # suma = suma + elem
    suma += elem

print(suma)  # 60