# sukuriam tuščią sąrašą
sarasas = []
print(type(sarasas))  # <class 'list'>
print(sarasas)  # []

# duomenys kuriais pildysim tuščią sąrašą
men1 = "sausis"
men2 = "vasaris"

# .append() prijungia naują elementą į sąrašo pabaigą
sarasas.append(men1)
print(sarasas)  # ['sausis']

sarasas.append(men2)
print(sarasas)  # ['sausis', 'vasaris']

sarasas.append("kovas")
sarasas.append(2024)
print(sarasas)  # ['sausis', 'vasaris', 'kovas', 2024]

# .insert() prijungia naują elementą, indeksu nurodytoj pozicijoj
sarasas.insert(0, "balandis")
sarasas.insert(-1, "balandis")
print(sarasas)  # ['balandis', 'sausis', 'vasaris', 'kovas', 'balandis', 2024]

sarasas.insert(2, "birželis")
print(sarasas)  # ['balandis', 'sausis', 'birželis', 'vasaris', 'kovas', 'balandis', 2024]

# .remove() - pašalinti elementą, pagal reikšmę(šalinamas pirmas pasitaikęs)
sarasas.remove("balandis")
print(sarasas)  # ['sausis', 'birželis', 'vasaris', 'kovas', 'balandis', 2024]

# .pop() - išmesti paskutinį(nenurodžius indekso) arba nurodytą elementą
# šalinamas elementas grąžinamas
sarasas.pop()
print(sarasas)  # ['sausis', 'birželis', 'vasaris', 'kovas', 'balandis']

# gaudom šalinamą elementą, taip pat nurodom jo indeksą
ismestas = sarasas.pop(1)
print(ismestas)  # birželis
print(sarasas)  # ['sausis', 'vasaris', 'kovas', 'balandis']

# del - python komanda trinti
del sarasas[-1]
print(sarasas)  # ['sausis', 'vasaris', 'kovas']

# indeksai listuose
print(sarasas[1])  # vasaris
print(sarasas[1:])  # ['vasaris', 'kovas']

print(sarasas)  # ['sausis', 'vasaris', 'kovas']
sarasas[0] = "lapkritis"
print(sarasas)  # ['lapkritis', 'vasaris', 'kovas']